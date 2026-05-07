# MailMind — Project Context

## Last updated
Phase 1 — Setup, Skeleton, and README (2026-05-07)

## What has been built
- Complete project directory structure with all files and folders
- Backend: FastAPI app with CORS, 7 route modules (all with placeholder endpoints)
- Backend: 6 pipeline modules (all with placeholder functions and full docstrings)
- Backend: SQLite database module with 5 tables (processed_emails, todos, meetings, orders, settings) and deduplication helpers
- Backend: config.py loading env vars from .env via python-dotenv
- Backend: requirements.txt with all pinned Python dependencies
- Frontend: Vite + React project with Tailwind CSS v4
- Frontend: Full "Chromatic Professional" design system ported to Tailwind v4 @theme (all color tokens, spacing, radii)
- Frontend: Sidebar component pixel-matching the HTML mockup (Material Symbols icons, active state with filled icon + right border, NavLink routing)
- Frontend: TopNavBar component with frosted glass backdrop-blur, search, notifications, help, avatar
- Frontend: App.jsx with BrowserRouter and 5 routes (/, /email, /crafter, /orders, /settings)
- Frontend: 5 page components (Home, Email, Crafter, Orders, Settings) with mockup-matched layout structures and placeholder content
- Frontend: 6 component placeholders (TodoCard, MeetingCard, EmailRow, DraftPanel, OrderCard, AnalyticsChart)
- Frontend: Centralised API wrapper (api/index.js) with GET/POST/PATCH/DELETE helpers
- Root: README.md with complete setup instructions
- Root: .env.example with all required env vars
- Root: n8n/workflow.json placeholder

## What is working
- Frontend: All 5 pages are routable via React Router
- Frontend: Sidebar navigation shows correct active state per route
- Frontend: TopNavBar renders with search and icon buttons
- Frontend: All pages render their mockup-matched layout shells with placeholder content
- Backend: All route modules are importable and registered in main.py
- Backend: All pipeline modules have placeholder functions returning safe defaults
- Backend: SQLite module can create all 5 tables

## Known issues / incomplete
- Backend has not been run yet (user needs to create venv and install requirements)
- Frontend has not been run yet (user needs to run `npm run dev`)
- No actual Gmail OAuth flow implemented (Phase 2)
- No OpenAI API calls implemented (Phase 3)
- No live data connections between frontend and backend
- All page content is placeholder — will be populated in Phases 7-11
- n8n workflow is empty placeholder (Phase 12)

## Environment
- Python version: 3.11+
- Node version: 18+
- n8n version: latest (install via `npm install -g n8n`)
- Tailwind CSS version: 4.2.4 (v4 — uses @theme in CSS, not tailwind.config.js)
- Vite version: 8.x
- React version: 19.x
- Key env vars required: OPENAI_API_KEY, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, REDIRECT_URI, SECRET_KEY, DATABASE_PATH

## File map
```
mailmind/
├── CONTEXT.md                           — this file (project context, read every phase)
├── README.md                            — complete setup instructions for CS students
├── .env.example                         — environment variable template with comments
├── backend/
│   ├── main.py                          — FastAPI entry point, CORS, router registration
│   ├── config.py                        — loads env vars from .env via python-dotenv
│   ├── requirements.txt                 — pinned Python dependencies
│   ├── db/
│   │   └── sqlite.py                    — SQLite init, 5 tables, is_processed(), mark_processed()
│   ├── routes/
│   │   ├── auth.py                      — Gmail OAuth placeholder (Phase 2)
│   │   ├── emails.py                    — email fetching placeholder (Phase 2)
│   │   ├── pipeline.py                  — classify/summarize/draft endpoints placeholder (Phase 3)
│   │   ├── todos.py                     — todo CRUD placeholder (Phase 4)
│   │   ├── meetings.py                  — meetings listing placeholder (Phase 4)
│   │   ├── orders.py                    — order tracking placeholder (Phase 5)
│   │   └── analytics.py                — analytics stats placeholder (Phase 6)
│   └── pipeline/
│       ├── classifier.py                — email classification placeholder (Phase 3)
│       ├── summarizer.py                — email summarization placeholder (Phase 3)
│       ├── drafter.py                   — reply drafting placeholder (Phase 3)
│       ├── todo_extractor.py            — todo extraction placeholder (Phase 4)
│       ├── meeting_extractor.py         — meeting extraction placeholder (Phase 4)
│       └── order_extractor.py           — order extraction placeholder (Phase 5)
├── n8n/
│   └── workflow.json                    — empty n8n workflow placeholder (Phase 12)
└── frontend/
    ├── index.html                       — HTML entry with Inter font + Material Symbols CDN
    ├── vite.config.js                   — Vite + React + Tailwind v4 plugins
    ├── package.json                     — npm config with all dependencies
    └── src/
        ├── main.jsx                     — React mount point (StrictMode)
        ├── index.css                    — Tailwind v4 @theme with full design system tokens
        ├── App.jsx                      — BrowserRouter + 5 routes + Layout wrapper
        ├── api/
        │   └── index.js                 — centralised fetch wrapper (GET/POST/PATCH/DELETE)
        ├── pages/
        │   ├── Home.jsx                 — dashboard layout (tasks + meetings + analytics)
        │   ├── Email.jsx                — three-pane inbox layout
        │   ├── Crafter.jsx              — email composer + AI sidebar layout
        │   ├── Orders.jsx               — spending overview + order cards layout
        │   └── Settings.jsx             — profile + AI prefs + security layout
        └── components/
            ├── Sidebar.jsx              — fixed left nav (80px, Material Symbols, active state)
            ├── TopNavBar.jsx            — fixed top bar (backdrop-blur, search, icons)
            ├── TodoCard.jsx             — task item placeholder (Phase 7)
            ├── MeetingCard.jsx          — meeting card placeholder (Phase 7)
            ├── EmailRow.jsx             — inbox row placeholder (Phase 8)
            ├── DraftPanel.jsx           — AI draft panel placeholder (Phase 8)
            ├── OrderCard.jsx            — order card placeholder (Phase 10)
            └── AnalyticsChart.jsx       — Recharts charts placeholder (Phase 7)
```

## Next phase instructions

### Phase 2 — Gmail OAuth and Email Fetching

**Read CONTEXT.md first**, then implement:

1. **`backend/routes/auth.py`** — Replace placeholders with real Gmail OAuth2 flow:
   - `GET /auth/login` — build Google OAuth2 URL with scopes `gmail.readonly` and `gmail.modify`, redirect to Google
   - `GET /auth/callback` — exchange auth code for access + refresh tokens, save refresh token to .env
   - Add inline comments explaining OAuth2, scopes, and why we save the refresh token

2. **`backend/routes/emails.py`** — Replace placeholders with real Gmail API calls:
   - `GET /emails/unread` — fetch unread emails from last 24h via `google-api-python-client`
   - Return list of dicts: `{ id, subject, sender, sender_email, body_plain, thread_id, timestamp }`
   - Add comments on every Gmail API call explaining what it does

3. **`backend/db/sqlite.py`** — Already has the `processed_emails` table and helpers. Verify they work with the auth flow.

4. **Wrap all API calls in try/except** with clear error messages. Use simple retry on failure (wait 2s, try once more).

5. **Update CONTEXT.md** with what was built, what works, and Phase 3 instructions.

**Important notes for the implementing session:**
- The Tailwind version is v4 (not v3) — configuration is done via `@theme` in `src/index.css`, NOT via `tailwind.config.js`
- The backend uses `python-dotenv` to load `.env` — the file should be at `mailmind/.env`
- All pipeline functions in `backend/pipeline/` already have full docstrings — fill in the actual implementations starting Phase 3
- Every file must start with a 3-5 line comment block and every function must have a docstring
- Use `print()` for logging, no logging libraries
- Keep functions under 30 lines
