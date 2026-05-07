# MailMind — AI-Powered Email Assistant

MailMind is a semester project that uses AI (OpenAI GPT-4o) to automatically classify,
summarise, and draft replies to your Gmail inbox. It also extracts to-do items, meeting
events, and order/purchase data from emails, presenting everything in a clean dashboard.

---

## Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Python | 3.11+ | [python.org](https://www.python.org/downloads/) |
| Node.js | 18+ | [nodejs.org](https://nodejs.org/) |
| n8n | latest | `npm install -g n8n` |

---

## 1. Google Cloud Setup (Gmail API)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a **new project** (e.g. "MailMind")
3. Enable the **Gmail API**: APIs & Services → Library → search "Gmail API" → Enable
4. Create **OAuth 2.0 credentials**:
   - APIs & Services → Credentials → Create Credentials → OAuth client ID
   - Application type: **Web application**
   - Authorised redirect URIs: `http://localhost:8000/auth/callback`
   - Download the JSON file — you'll need `client_id` and `client_secret`
5. Configure the **OAuth consent screen**:
   - User type: External (or Internal if using a Workspace account)
   - Add scopes: `gmail.readonly`, `gmail.modify`
   - Add your email as a test user

---

## 2. OpenAI API Key

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Go to API Keys → Create new secret key
4. Copy the key — you'll paste it into `.env`

---

## 3. Environment Setup

```bash
# Clone or navigate to the project folder
cd mailmind

# ----- Backend -----
# Create a Python virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r backend/requirements.txt

# ----- Frontend -----
cd frontend
npm install
cd ..
```

---

## 4. Configure Environment Variables

```bash
# Copy the example env file
cp .env.example .env

# Open .env in your editor and fill in:
#   OPENAI_API_KEY       — from step 2
#   GOOGLE_CLIENT_ID     — from step 1
#   GOOGLE_CLIENT_SECRET — from step 1
#   SECRET_KEY           — any random string (run: python -c "import secrets; print(secrets.token_hex(32))")
```

---

## 5. Running the App

### Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload
# Server starts at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### Frontend (React + Vite)

```bash
cd frontend
npm run dev
# App opens at http://localhost:5173
```

### n8n (Workflow Automation)

```bash
n8n start
# Opens at http://localhost:5678
# Go to Workflows → Import → select n8n/workflow.json
```

---

## Project Structure

```
mailmind/
├── CONTEXT.md                  ← project context (read/update every phase)
├── README.md                   ← this file
├── .env.example                ← env var template
├── backend/
│   ├── main.py                 ← FastAPI entry point
│   ├── config.py               ← env var loading
│   ├── requirements.txt        ← Python dependencies
│   ├── db/
│   │   └── sqlite.py           ← database init + helpers
│   ├── routes/
│   │   ├── auth.py             ← Gmail OAuth
│   │   ├── emails.py           ← fetch + classify + deduplicate
│   │   ├── pipeline.py         ← classify / summarize / draft endpoints
│   │   ├── todos.py            ← to-do item endpoints
│   │   ├── meetings.py         ← meeting event endpoints
│   │   ├── orders.py           ← order/purchase tracking
│   │   └── analytics.py        ← spam/source/security stats
│   └── pipeline/
│       ├── classifier.py       ← email classification (GPT-4o-mini)
│       ├── summarizer.py       ← email summarisation (GPT-4o-mini)
│       ├── drafter.py          ← reply drafting (GPT-4o)
│       ├── todo_extractor.py   ← to-do extraction (GPT-4o-mini)
│       ├── meeting_extractor.py← meeting extraction (GPT-4o-mini)
│       └── order_extractor.py  ← order extraction (GPT-4o-mini)
├── n8n/
│   └── workflow.json           ← n8n automation workflow
└── frontend/
    ├── index.html
    ├── vite.config.js
    ├── tailwind.config.js
    └── src/
        ├── main.jsx
        ├── App.jsx             ← React Router + layout
        ├── index.css           ← Tailwind directives + global styles
        ├── api/
        │   └── index.js        ← fetch wrapper for backend API
        ├── pages/
        │   ├── Home.jsx        ← dashboard (tasks, meetings, analytics)
        │   ├── Email.jsx       ← smart inbox (3-pane)
        │   ├── Crafter.jsx     ← new email composer
        │   ├── Orders.jsx      ← order tracking
        │   └── Settings.jsx    ← settings
        └── components/
            ├── Sidebar.jsx     ← side navigation
            ├── TopNavBar.jsx   ← top header bar
            ├── TodoCard.jsx    ← task item component
            ├── MeetingCard.jsx ← meeting card component
            ├── EmailRow.jsx    ← inbox email row
            ├── DraftPanel.jsx  ← AI draft panel
            ├── OrderCard.jsx   ← order card component
            └── AnalyticsChart.jsx ← charts (Recharts)
```

---

## Phase Checklist

```
Phase 1  - [ ] Project runs, sidebar navigation works, all pages load
Phase 2  - [ ] Gmail OAuth login works, unread emails fetched
Phase 3  - [ ] Classify / summarize / draft pipeline returns correct JSON
Phase 4  - [ ] Todos and meetings extracted and stored in SQLite
Phase 5  - [ ] Order emails detected and structured data stored
Phase 6  - [ ] Analytics endpoint returns correct stats
Phase 7  - [ ] Home page renders todos, meetings, charts from live data
Phase 8  - [ ] Email page shows inbox, clicking email shows AI draft
Phase 9  - [ ] Crafter generates full email from tone + prompt
Phase 10 - [ ] Orders page shows all orders with correct status badges
Phase 11 - [ ] Settings saved to DB, Gmail connected/disconnected works
Phase 12 - [ ] n8n workflow runs end-to-end, Gmail Draft appears in inbox
```

# Phase 1 Walkthrough — Setup, Skeleton, and README

## Summary

Phase 1 of MailMind is complete. **42 files** were created across the full project structure, establishing the backend (FastAPI), frontend (React + Vite + Tailwind v4), and all skeleton files for upcoming phases.

---

## What Was Built

### Project Root (4 files)
| File | Purpose |
|------|---------|
| [README.md](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/README.md) | Complete setup guide for CS students |
| [.env.example](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/.env.example) | Env var template (OPENAI, Google, etc.) |
| [CONTEXT.md](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/CONTEXT.md) | Project context — single source of truth |
| [n8n/workflow.json](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/n8n/workflow.json) | Empty n8n placeholder (Phase 12) |

### Backend (16 files)

| File | Purpose |
|------|---------|
| [main.py](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/backend/main.py) | FastAPI app with CORS + 7 routers |
| [config.py](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/backend/config.py) | Env var loading via python-dotenv |
| [requirements.txt](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/backend/requirements.txt) | Pinned Python dependencies |
| [db/sqlite.py](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/backend/db/sqlite.py) | 5 SQLite tables + deduplication helpers |
| routes/auth.py | Gmail OAuth placeholders |
| routes/emails.py | Email fetching placeholders |
| routes/pipeline.py | Classify/summarize/draft placeholders |
| routes/todos.py | Todo CRUD placeholders |
| routes/meetings.py | Meetings listing placeholders |
| routes/orders.py | Order tracking placeholders |
| routes/analytics.py | Analytics stats placeholders |
| pipeline/classifier.py | Email classification skeleton |
| pipeline/summarizer.py | Email summarization skeleton |
| pipeline/drafter.py | Reply drafting skeleton |
| pipeline/todo_extractor.py | Todo extraction skeleton |
| pipeline/meeting_extractor.py | Meeting extraction skeleton |
| pipeline/order_extractor.py | Order extraction skeleton |

### Frontend (18 files)

| File | Purpose |
|------|---------|
| [vite.config.js](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/vite.config.js) | Vite + React + Tailwind v4 plugins |
| [index.html](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/index.html) | HTML entry with Inter font + Material Symbols |
| [src/index.css](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/src/index.css) | Tailwind v4 @theme with full design system |
| [src/main.jsx](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/src/main.jsx) | React mount point |
| [src/App.jsx](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/src/App.jsx) | BrowserRouter + 5 routes + Layout |
| [src/components/Sidebar.jsx](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/src/components/Sidebar.jsx) | Fixed 80px sidebar with Material Symbols |
| [src/components/TopNavBar.jsx](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/src/components/TopNavBar.jsx) | Fixed top bar with backdrop-blur |
| src/pages/Home.jsx | Dashboard layout (tasks + meetings + analytics) |
| src/pages/Email.jsx | Three-pane inbox layout |
| src/pages/Crafter.jsx | Email composer + AI sidebar |
| src/pages/Orders.jsx | Spending overview + order cards |
| src/pages/Settings.jsx | Profile + AI prefs + security |
| src/components/TodoCard.jsx | Task item (Phase 7) |
| src/components/MeetingCard.jsx | Meeting card (Phase 7) |
| src/components/EmailRow.jsx | Inbox row (Phase 8) |
| src/components/DraftPanel.jsx | AI draft panel (Phase 8) |
| src/components/OrderCard.jsx | Order card (Phase 10) |
| src/components/AnalyticsChart.jsx | Recharts charts (Phase 7) |
| [src/api/index.js](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/src/api/index.js) | Centralised API wrapper |

---

## Key Technical Decisions

1. **Tailwind v4** was installed (not v3). Configuration uses `@theme` in `src/index.css` rather than `tailwind.config.js`. All design tokens from the HTML mockups are ported.

2. **Material Symbols** are loaded via CDN in `index.html` — same approach as the mockups. The Sidebar uses `fontVariationSettings` to toggle between outlined (FILL 0) and filled (FILL 1) icons for active state.

3. **React Router v7** handles all navigation. The `Layout` component wraps every route with Sidebar + TopNavBar.

4. **Every backend file** has a 3-5 line comment block and every function has a docstring, per the coding rules.

5. **SQLite tables** for all 5 entities (processed_emails, todos, meetings, orders, settings) are pre-defined in `db/sqlite.py` so future phases just need to use them.

---

## Manual Verification Steps

### Backend
```bash
cd mailmind
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r backend/requirements.txt
cd backend
uvicorn main:app --reload
# Visit http://localhost:8000 → should show {"message":"MailMind API is running","status":"ok"}
# Visit http://localhost:8000/docs → should show Swagger API docs with all placeholder endpoints
```

### Frontend
```bash
cd mailmind/frontend
npm install     # (already done, but safe to re-run)
npm run dev
# Visit http://localhost:5173 → should show:
#   - Left sidebar with 5 nav icons (Home, Email, Crafter, Orders, Settings)
#   - Top bar with "Dashboard" title, search, notification/help icons
#   - Home page content with "Good evening, Alex" greeting
#   - Click each nav item → page changes, sidebar active state updates
```
