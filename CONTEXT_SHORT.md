# MailMind — Project Context

## Project Overview
MailMind is an AI-powered email assistant that automates processing, categorizing, summarizing, and drafting replies to emails. It extends basic email functionality by extracting actionable items such as to-dos, meetings, and orders directly from the inbox. Designed as a monolithic full-stack application, it connects to Gmail, runs AI pipelines using Google Gemini models, and provides a centralized dashboard for email analytics and task management.

## Tech Stack
- **Languages:** Python (Backend), JavaScript (Frontend Interactivity), HTML/CSS (UI)
- **Backend Framework:** FastAPI (with Uvicorn as ASGI server)
- **Database:** SQLite
- **AI / LLM:** Google GenAI SDK (`google-genai` for Gemini 2.5 Flash/Pro)
- **Authentication & Email Integration:** Google Gmail API (`google-api-python-client`), OAuth2 (`google-auth-oauthlib`)
- **Frontend / Templating:** Jinja2
- **Styling:** Tailwind CSS v4 (via `@tailwindcss/cli`)
- **Workflow Automation:** n8n (for email polling and processing workflows)

## Architecture & Structure
The project follows a **Monolithic Architecture** where the backend serves both the REST API endpoints and the server-rendered HTML templates.

**Core Directories & Systemic Functions:**
- `backend/main.py`: The root application file that initializes FastAPI, configures CORS, mounts static assets, and registers all routers.
- `backend/routes/`: Contains domain-specific API routing logic (e.g., `emails.py`, `auth.py`, `pipeline.py`, `orders.py`). Separate module `pages.py` is dedicated to returning Jinja2 HTML templates.
- `backend/pipeline/`: Encapsulates all AI logic and integration with Google Gemini. Contains specific modules for classification, summarization, drafting, and data extraction (todos, meetings, orders).
- `backend/db/`: Contains the database wrapper (`sqlite.py`) handling all SQLite connections, table initialization, and CRUD operations.
- `backend/templates/`: Stores Jinja2 HTML views (e.g., `email.html`, `home.html`, `settings.html`) that structure the frontend.
- `backend/static/`: Contains client-side assets including Tailwind CSS definitions (`input.css`, `style.css`) and vanilla JavaScript (`app.js`).
- `n8n/`: Houses workflow configuration files (e.g., `workflow.json`) for automating periodic Gmail polling and API triggering.

## Key Entry Points
- **Execution File:** `backend/main.py` is the primary entry point. The application is run via `uvicorn main:app --reload --port 8000`.
- **Configuration Manifests:**
  - `backend/requirements.txt`: Python package dependencies.
  - `package.json`: Node dependencies, primarily for the Tailwind CSS CLI.
  - `.env` / `.env.example`: Environment variables (e.g., `GEMINI_API_KEY`, `DATABASE_PATH`, OAuth secrets).
  - `backend/config.py`: Centralized Python configuration loader parsing the `.env` file.
- **Routing Logic:** FastAPI uses `APIRouter` in individual modules within `backend/routes/`. These routers are then imported and registered with URL prefixes (e.g., `/api/emails`, `/api/auth`) inside `backend/main.py`.

## Data & State Flow
- **Data Models & Schemas:** Managed via raw SQLite queries encapsulated in `backend/db/sqlite.py`. The application does not use an ORM. Tables include `emails` (caches content and AI results), `processed_emails` (tracks pipeline state to prevent duplicate processing), `todos`, `meetings`, `orders`, and `settings`.
- **State Management:**
  - **Backend State:** The SQLite database acts as the single source of truth for email status, cached pipeline results, and extracted entities.
  - **Frontend State:** Managed locally in the browser via Vanilla JavaScript and DOM manipulation (e.g., tracking active UI tabs, caching selected emails, and displaying dynamic toast notifications). 
  - **Authentication State:** OAuth2 tokens are persisted locally in `token.json` within the project root.
- **Data Flow:**
  1. Emails are fetched via the Gmail API (`routes/emails.py`).
  2. The application passes email content to the AI pipeline (`routes/pipeline.py`), which calls Gemini models to classify, summarize, draft, and extract details.
  3. Extracted data and AI outputs are serialized and saved to SQLite.
  4. Jinja2 templates render the UI, while client-side JS makes asynchronous calls to the API to update views without full page reloads.

## Conventions
- **Coding Standards (Python):** PEP 8 style formatting. Variables and functions are `snake_case`, while classes and Pydantic models use `PascalCase`. Type hinting is used in some endpoints.
- **API Design:** RESTful conventions are followed for API endpoints (e.g., `GET /api/orders`, `POST /api/drafts/save`). Requests and responses are validated using Pydantic models.
- **Frontend Design:** Tailwind CSS utility classes are used exclusively for styling. No heavy frontend frameworks (like React) are used; interactivity relies on lightweight Vanilla JS.
- **Documentation:** Inline docstrings are used for major functions (especially in the DB and Pipeline modules). The API includes auto-generated Swagger documentation at `/docs`.
- **Testing:** No formal testing frameworks (e.g., `pytest`) are currently evident in the structure, but an internal developer dashboard (`dev.html` and `dev.py`) is used for manual sandbox testing and API verification.
