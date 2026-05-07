# backend/db/sqlite.py
# ---------------------------------------------------------------
# Handles all SQLite database operations for MailMind. Creates
# tables on first run and provides helper functions for CRUD
# operations on processed emails, todos, meetings, and orders.
# ---------------------------------------------------------------

import sqlite3
import os

# Import the database path from our central config
from config import DATABASE_PATH


def get_connection():
    """
    Opens a connection to the SQLite database file.

    Returns:
        sqlite3.Connection: an open database connection with
                            row_factory set to sqlite3.Row so
                            results can be accessed by column name.
    """
    # Connect to the database file specified in .env
    connection = sqlite3.connect(DATABASE_PATH)

    # This lets us access columns by name (e.g. row["subject"])
    # instead of by index (e.g. row[1])
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Creates all required tables if they don't already exist.
    Called once when the app starts up. Each table is created
    with IF NOT EXISTS so it's safe to call multiple times.

    Tables created:
        - processed_emails: tracks which emails have been processed
        - todos: to-do items extracted from emails
        - meetings: meeting events extracted from emails
        - orders: order/purchase data extracted from emails
        - settings: key-value store for user preferences
    """
    connection = get_connection()
    cursor = connection.cursor()

    # --- Processed Emails ---
    # Tracks which emails have already been through the AI pipeline
    # so we don't process the same email twice (deduplication).
    # This is important because n8n polls Gmail every 15 minutes,
    # and the same email could appear in multiple poll results.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS processed_emails (
            email_id TEXT PRIMARY KEY,
            subject TEXT,
            sender TEXT,
            category TEXT,
            priority_score INTEGER,
            is_spam INTEGER DEFAULT 0,
            processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # --- Todos ---
    # Stores actionable to-do items extracted from emails by GPT.
    # is_done tracks whether the user has checked it off.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            due_date TEXT,
            priority TEXT,
            source_email_subject TEXT,
            is_done INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # --- Meetings ---
    # Stores meeting/call/event data extracted from emails.
    # attendees is stored as a comma-separated string for simplicity.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meetings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            date TEXT,
            time TEXT,
            location_or_link TEXT,
            attendees TEXT,
            source_email_subject TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # --- Orders ---
    # Stores order/purchase information extracted from shipping
    # and order confirmation emails.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            retailer TEXT,
            order_number TEXT,
            item_description TEXT,
            order_date TEXT,
            estimated_delivery TEXT,
            status TEXT,
            tracking_number TEXT,
            tracking_url TEXT,
            price TEXT,
            source_email_id TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # --- Settings ---
    # Simple key-value store for user preferences (tone, auto-draft, etc.)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    # Save all table creations to disk
    connection.commit()
    connection.close()

    print("[DB] All tables initialized successfully.")


def is_processed(email_id):
    """
    Checks whether an email has already been processed by the
    AI pipeline. Used for deduplication when polling Gmail.

    Args:
        email_id (str): the unique Gmail message ID

    Returns:
        bool: True if the email is already in the database
    """
    connection = get_connection()
    cursor = connection.cursor()

    # Look for this email_id in the processed_emails table
    cursor.execute(
        "SELECT 1 FROM processed_emails WHERE email_id = ?",
        (email_id,)
    )
    result = cursor.fetchone()
    connection.close()

    # If we found a row, the email has been processed
    return result is not None


def mark_processed(email_id, subject, sender, category, priority_score, is_spam=False):
    """
    Records an email as processed so it won't be run through the
    AI pipeline again on the next poll.

    Args:
        email_id (str): the unique Gmail message ID
        subject (str): the email subject line
        sender (str): the sender's email address
        category (str): the classification category (e.g. "urgent")
        priority_score (int): priority score from 1-10
        is_spam (bool): whether the email was classified as spam
    """
    connection = get_connection()
    cursor = connection.cursor()

    # INSERT OR REPLACE handles the case where the email_id
    # already exists (shouldn't happen, but safe to handle)
    cursor.execute(
        """INSERT OR REPLACE INTO processed_emails
           (email_id, subject, sender, category, priority_score, is_spam)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (email_id, subject, sender, category, priority_score, int(is_spam))
    )

    connection.commit()
    connection.close()
