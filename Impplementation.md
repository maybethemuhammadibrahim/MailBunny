# MailMind — Full Project Implementation Plan

## Overview

Building **MailMind**, an AI-powered email assistant web application as a semester project. The project spans 12 phases and involves a FastAPI backend, React frontend (with Vite), n8n automation workflows, and OpenAI GPT integration. All UI must pixel-match the provided HTML mockup files.

## Key Design Observations from Mockups

The HTML mockups use **Tailwind CSS** with a custom design system called "Chromatic Professional":
- **Sidebar**: Fixed 80px wide left sidebar with icon-only nav (Home, Email, Crafter, Orders, Settings), active state uses `border-r-4 border-primary` and filled icons
- **Top navbar**: Fixed header with `backdrop-blur-md`, search bar, notifications, help, and user avatar
- **Color palette**: Neutral-anchored with `#010203` primary, `#006783` secondary, `#030012` tertiary. Vibrant accents for data viz
- **Cards**: White backgrounds (`surface-container-lowest`), `rounded-xl`, subtle shadows `0px 4px 20px rgba(0,0,0,0.03)`, borders
- **Icons**: Material Symbols Outlined with FILL variation settings
- **Font**: Inter throughout, custom type scale (h1: 32px, h2: 20px, body-lg: 16px, body-md: 14px, label-md: 13px, label-sm: 11px)

> [!IMPORTANT]
> The mockups use **TailwindCSS** with a custom config. The user's spec says "React + simple CSS" but the mockups are entirely Tailwind-based. I recommend using **TailwindCSS** in the React project to faithfully replicate the mockups, since re-implementing all these utility classes in vanilla CSS would be impractical and error-prone. The tailwind config from the mockups will be directly ported.

> [!IMPORTANT]  
> The user spec mentions `tailwind.config.js` in the folder structure, confirming Tailwind should be used.

## Open Questions

1. **Tailwind vs. Vanilla CSS**: The spec says "simple CSS" but mockups use Tailwind and the folder structure includes `tailwind.config.js`. **I'll proceed with Tailwind** since the mockups are the ground truth. Please confirm this is acceptable.

2. **Phase scope**: Should I implement all 12 phases in this session, or start with Phase 1 and get your approval before continuing? Given the massive scope, I recommend **doing Phase 1 now** and progressing through subsequent phases with your approval.

3. **Previous conversation**: You have a prior conversation (eee98056) about "Building AI Email Responder" with similar scope. Should I incorporate anything from that session, or start fresh?

---

## Phase 1 — Setup, Skeleton, and README

### Backend Setup

#### [NEW] [main.py](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/backend/main.py)
- FastAPI app with CORS (allow `localhost:5173`)
- Register all route files as empty routers
- Comment blocks explaining each section

#### [NEW] [config.py](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/backend/config.py)
- Load env vars from `.env` using `python-dotenv`
- All config values as module-level variables

#### [NEW] [requirements.txt](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/backend/requirements.txt)
- FastAPI, uvicorn, python-dotenv, openai, google-api-python-client, google-auth-oauthlib, pydantic

#### [NEW] Empty route files
- `routes/auth.py` — empty router with placeholder
- `routes/emails.py` — empty router
- `routes/pipeline.py` — empty router
- `routes/todos.py` — empty router
- `routes/meetings.py` — empty router
- `routes/orders.py` — empty router
- `routes/analytics.py` — empty router

#### [NEW] [sqlite.py](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/backend/db/sqlite.py)
- Placeholder with init function

#### [NEW] Empty pipeline files
- `pipeline/classifier.py`, `summarizer.py`, `drafter.py`, `todo_extractor.py`, `meeting_extractor.py`, `order_extractor.py`

---

### Frontend Setup

#### [NEW] Vite + React project in `frontend/`
- Initialize with `npx create-vite` (React template)
- Install dependencies: `react-router-dom`, `lucide-react`, `recharts`
- TailwindCSS v3 setup with the design system config ported from the mockups

#### [NEW] [App.jsx](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/src/App.jsx)
- React Router with 5 routes: `/`, `/email`, `/crafter`, `/orders`, `/settings`
- Layout wrapper with Sidebar + TopNavBar

#### [NEW] [Sidebar.jsx](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/src/components/Sidebar.jsx)
- Pixel-match the sidebar from mockups
- Material Symbols icons (Home, Email, Crafter/auto_awesome, Orders/shopping_cart, Settings)
- Active state with right border + filled icon
- NavLink integration with React Router

#### [NEW] Page placeholders
- `pages/Home.jsx`, `Email.jsx`, `Crafter.jsx`, `Orders.jsx`, `Settings.jsx`
- Each with simple placeholder content

#### [NEW] [api/index.js](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/frontend/src/api/index.js)
- Base fetch wrapper pointing to `http://localhost:8000`

#### [NEW] Component placeholders
- `TodoCard.jsx`, `MeetingCard.jsx`, `EmailRow.jsx`, `DraftPanel.jsx`, `OrderCard.jsx`, `AnalyticsChart.jsx`

---

### Project Root Files

#### [NEW] [README.md](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/README.md)
- Complete setup instructions for a CS student
- Prerequisites, environment setup, running instructions

#### [NEW] [.env.example](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/.env.example)
- All env var templates with comments

#### [NEW] [CONTEXT.md](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/CONTEXT.md)
- Initial project context

#### [NEW] [n8n/workflow.json](file:///c:/Users/Muhammad%20Ibrahim/Desktop/Projects/AI/mailmind/n8n/workflow.json)
- Empty placeholder

---

## Verification Plan

### Automated Tests
- Run `uvicorn main:app --reload` from backend — should start without errors
- Run `npm run dev` from frontend — should start and show sidebar navigation
- Click all 5 nav items — each should render its page component
- Sidebar active state should highlight correctly per route

### Manual Verification
- Open browser to `localhost:5173`, verify all pages load
- Verify sidebar matches mockup styling
- Verify top navbar appears correctly

---

## Phases 2-12 Summary (Future Work)

| Phase | Goal | Key Deliverables |
|-------|------|-----------------|
| 2 | Gmail OAuth + Email Fetching | `auth.py`, `emails.py`, SQLite `processed_emails` table |
| 3 | AI Pipeline | `classifier.py`, `summarizer.py`, `drafter.py`, pipeline endpoints |
| 4 | Todo + Meeting Extraction | `todo_extractor.py`, `meeting_extractor.py`, SQLite tables |
| 5 | Order Tracking | `order_extractor.py`, orders endpoints, SQLite table |
| 6 | Analytics | `analytics.py` with overview + security stats |
| 7 | Frontend: Home Page | TodoCard, MeetingCard, AnalyticsChart with Recharts |
| 8 | Frontend: Email Page | Three-pane inbox, EmailRow, DraftPanel |
| 9 | Frontend: Crafter | New email composer with AI generation |
| 10 | Frontend: Orders | Order cards grid with filtering |
| 11 | Frontend: Settings | AI personality, account, security settings |
| 12 | n8n Workflow | Full automation pipeline JSON |
