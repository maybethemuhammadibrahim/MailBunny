# MailMind Viva Concepts (From Basics to Project Level)

This guide is designed for viva preparation.
It starts from fundamentals and builds up to the exact architecture used in MailMind.
Use this as a quick revision sheet before demo and viva questions.

## 1) Web and API Basics

### What is a web application?
A web application is software that runs through a browser.
It has two main sides:
- Client side: browser UI (HTML, CSS, JavaScript)
- Server side: backend application (here: FastAPI)

### Client-server model
- Client sends a request
- Server processes request
- Server sends a response

In MailMind:
- Browser requests routes like `/settings`, `/email`
- FastAPI renders templates and provides API JSON endpoints like `/api/process-email`

### What is HTTP?
HTTP is a request-response protocol.
Each request has:
- Method (GET, POST, PATCH, etc.)
- URL/path
- Headers
- Optional body

Each response has:
- Status code (200, 404, 500, etc.)
- Headers
- Body (HTML or JSON)

### Important HTTP status codes
- 200 OK: request success
- 201 Created: new resource created
- 400 Bad Request: invalid request format
- 401 Unauthorized: auth missing/invalid
- 403 Forbidden: authenticated but not allowed
- 404 Not Found: endpoint/resource does not exist
- 422 Unprocessable Entity: validation failed (very common in FastAPI)
- 500 Internal Server Error: server-side failure

## 2) HTTP Methods (GET, POST, etc.)

### GET
Purpose: read/fetch data.
Examples in this project:
- `/api/health`
- `/api/auth/status`
- `/api/emails/unread`

Properties:
- Should not modify data
- Usually no request body

### POST
Purpose: create data or trigger processing.
Examples:
- `/api/process-email`
- `/api/draft`
- `/api/emails/mark-processed`

Properties:
- Has request body (usually JSON)
- Can change database state

### PATCH
Purpose: partially update existing data.
Example target use:
- Mark todo as done: `/api/todos/{id}/done`

### PUT
Purpose: full replacement update of resource.
Not heavily used in current phase, but conceptually used for replacing full record content.

### DELETE
Purpose: remove data.
Example future use in settings cleanup APIs.

### OPTIONS
Used by browsers for CORS preflight checks before real requests.
FastAPI + CORS middleware handles this automatically.

## 3) FastAPI Fundamentals

### Why FastAPI?
- Very fast to build APIs
- Automatic input validation with Pydantic
- Auto-generated docs at `/docs`
- Clear route decorators

### Basic route syntax
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}
```

### Route decorators meaning
- `@app.get("/path")` -> HTTP GET endpoint
- `@app.post("/path")` -> HTTP POST endpoint
- `@app.patch("/path")` -> HTTP PATCH endpoint
- `@app.delete("/path")` -> HTTP DELETE endpoint

### APIRouter usage
Large projects split endpoints into modules.
MailMind uses separate files in `backend/routes` and registers them in `backend/main.py`.

Example concept:
```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():
    return {"connected": True}
```

Then mounted in main app with prefix:
```python
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
```

So final path becomes `/api/auth/status`.

### Path, query, and body parameters

Path parameter:
```python
@router.get("/check/{email_id}")
def check(email_id: str):
    ...
```

Query parameter:
```python
@router.get("/emails")
def list_emails(limit: int = 10):
    ...
```

Body parameter using Pydantic:
```python
from pydantic import BaseModel

class DraftRequest(BaseModel):
    subject: str
    body: str

@router.post("/draft")
def draft(req: DraftRequest):
    ...
```

### Why Pydantic is important
- Validates input types automatically
- Rejects malformed JSON with clear 422 errors
- Reduces manual validation code

### Sync vs async in FastAPI
FastAPI supports both `def` and `async def`.
MailMind currently uses regular `def` routes (synchronous style), which is fine for current project complexity.

### Middleware and CORS
CORS allows frontend/browser calls from another origin.
In MailMind, CORS middleware allows localhost frontend origins and methods/headers for dev.

## 4) Gmail OAuth2 and API Flow

### What is OAuth2?
OAuth2 lets users grant app access without sharing password.

MailMind flow:
1. User opens `/api/auth/login`
2. App redirects to Google consent screen
3. User approves scopes (`gmail.readonly`, `gmail.modify`)
4. Google redirects to `/api/auth/callback` with code
5. Backend exchanges code for access and refresh tokens
6. Tokens are saved in `token.json`

### Access token vs refresh token
- Access token: short-lived, used in API calls
- Refresh token: long-lived, used to request new access tokens

MailMind refreshes expired access token automatically.

### Gmail API usage in project
- List messages
- Fetch full message content
- Parse headers/body
- Use results in AI pipeline

## 5) Gemini AI Integration in MailMind

### Why Gemini in this project?
- Official Python SDK (`google-genai`)
- Fast model available for classification/summarization/drafting
- Good free-tier support for student projects

### Where AI is used
- Classification (`classifier.py`): category, urgency, spam flags
- Summarization (`summarizer.py`): concise understanding
- Drafting (`drafter.py`): reply generation
- Shared Gemini wrapper (`gemini.py`) centralizes calls and retry behavior

### AI pipeline sequence
For one email:
1. Classify
2. Summarize
3. Draft reply

Combined endpoint `/api/process-email` executes sequence and stores results.

### JSON-first responses
Prompting asks model to return JSON so backend can parse and store predictable structured output.

## 6) SQLite Concepts (Important for Viva)

### What is SQLite?
SQLite is a lightweight relational database engine.
It stores the entire database in a single file (here: `mailmind.db`).

### Why SQLite was used
- Zero server setup
- Easy local development
- Great for prototypes and semester projects
- Works well with small-to-medium data volumes

### How data is organized
Relational structure:
- Tables
- Rows
- Columns
- Primary keys

In MailMind examples:
- `processed_emails`
- `emails`
- `todos`
- `meetings`
- `orders`
- `settings`

### Primary key meaning
A primary key uniquely identifies a row.
Example: `email_id` in processed emails ensures deduplication.

### How SQLite stores data internally (high-level)
- Stored in pages inside one file
- Uses B-tree structures for tables/indexes
- Supports transactions (ACID)
- Uses journaling/WAL to maintain consistency during writes

### ACID in simple terms
- Atomicity: transaction is all-or-nothing
- Consistency: data stays valid after transaction
- Isolation: concurrent operations do not corrupt each other
- Durability: committed data persists on disk

### SQL operations used in project
- CREATE TABLE IF NOT EXISTS
- INSERT OR REPLACE
- INSERT OR IGNORE
- SELECT with filtering and ordering
- UPDATE for pipeline and status fields

### Why `INSERT OR IGNORE` and `INSERT OR REPLACE` matter
- Ignore prevents duplicate row insertion errors
- Replace updates same primary key row safely

### How Python talks to SQLite
Using built-in `sqlite3` module:
1. Open connection
2. Create cursor
3. Execute SQL with placeholders (`?`)
4. Commit for writes
5. Close connection

Example safe parameterized query:
```python
cursor.execute(
    "SELECT 1 FROM processed_emails WHERE email_id = ?",
    (email_id,)
)
```

Parameterized queries prevent SQL injection and handle escaping safely.

## 7) Project Architecture (MailMind)

### Layers
- Routes layer (`backend/routes`): API endpoints
- Pipeline layer (`backend/pipeline`): AI business logic
- DB layer (`backend/db/sqlite.py`): persistence helpers
- Config layer (`backend/config.py`): env variables
- UI templates (`backend/templates`): Jinja-rendered pages

### End-to-end processing flow
1. Gmail auth completed and token stored
2. Emails fetched from Gmail API
3. Email data saved in SQLite
4. AI pipeline runs for each selected/new email
5. Structured outputs returned to UI and cached in DB

### Why this layered approach is good
- Easier debugging
- Reusable logic
- Clear separation of concerns
- Better maintainability for team projects

## 8) Common Viva Questions and Strong Answers

### Q1: Why FastAPI and not Flask/Django?
FastAPI gives automatic validation, clear type hints, and auto docs, so development is faster and safer for API-heavy projects.

### Q2: Why SQLite and not MySQL/PostgreSQL?
For local-first academic project scope, SQLite is enough, simpler to ship, and requires no database server setup.

### Q3: How do you avoid processing same email twice?
Use `processed_emails` table with `email_id` primary key and an `is_processed` check before/while processing.

### Q4: Why keep AI output in JSON?
JSON makes responses structured and machine-parseable, which simplifies database persistence and frontend rendering.

### Q5: How is security handled for secrets?
Secrets are kept in `.env`, not hardcoded in source files.

### Q6: What happens if external API fails?
Code uses try/except and retry strategy (short backoff, one retry) and returns safe fallback responses.

## 9) Final Revision Checklist Before Viva

- Explain complete OAuth flow without looking at notes
- Explain difference between GET and POST with project examples
- Explain path/query/body params in FastAPI
- Explain why Pydantic gives 422 errors
- Explain deduplication logic in processed_emails
- Explain why SQLite is suitable for this scope
- Explain pipeline order: classify -> summarize -> draft
- Explain where Gemini key and Google credentials are stored

If you can confidently explain each checklist point with one project example, you are viva-ready.
