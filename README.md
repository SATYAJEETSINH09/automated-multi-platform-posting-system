# Automated Multi-Platform Posting System

A Python-based automated posting system built using FastAPI. It allows users to publish a single message to multiple platforms through one REST API endpoint.

## Features

- Single API endpoint: `POST /posting`
- Supports five platform integrations:
  - Telegram
  - Mastodon
  - Bluesky
  - DEV.to
  - GitHub Gist
- Message validation (maximum 200 characters)
- Exactly one CTA URL required
- URL validation
- Concurrent posting to multiple platforms
- Independent error handling for each platform
- Platform-wise posting results
- Returns post URL, visibility, date/time and error details

## Technology Stack

- Python 3.11
- FastAPI
- Pydantic
- HTTPX
- AT Protocol (Bluesky)
- Pytest

## Project Structure

```text
automated-posting/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── config.py
│   │
│   ├── platforms/
│   │   ├── telegram.py
│   │   ├── mastodon.py
│   │   ├── bluesky.py
│   │   ├── devto.py
│   │   └── github.py
│   │
│   └── services/
│       └── posting_service.py
│
├── tests/
│   ├── test_posting.py
│   ├── test_telegram.py
│   ├── test_mastodon.py
│   ├── test_bluesky.py
│   ├── test_devto.py
│   └── test_github.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd automated-posting
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate on Windows:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

Add your platform credentials:

```env
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHANNEL_ID=

MASTODON_BASE_URL=
MASTODON_ACCESS_TOKEN=

BLUESKY_HANDLE=
BLUESKY_APP_PASSWORD=

DEVTO_API_KEY=

GITHUB_TOKEN=
```

Never commit your `.env` file or expose API credentials.

### 5. Start the application

```bash
uvicorn app.main:app --reload --port 4000
```

Application URL:

```text
http://127.0.0.1:4000
```

Swagger API documentation:

```text
http://127.0.0.1:4000/docs
```

## API Documentation

### POST /posting

Publishes a message to all configured platforms.

**Request Body**

```json
{
  "message": "Testing automated posting https://example.com"
}
```

### Validation Rules

- Message must not be empty.
- Maximum message length is 200 characters.
- Exactly one CTA URL is required.
- URL must have a valid scheme and domain.

### Response Example

```json
{
  "success": true,
  "total_platforms": 5,
  "successful": 5,
  "failed": 0,
  "platforms": {
    "telegram": {
      "status": "success",
      "posted_url": "https://t.me/channel/123",
      "public_access": true,
      "date_time": "2026-11-18T10:00:00Z",
      "error": null
    }
  }
}
```

The response includes individual results for all five platforms.

## Error Handling

Each platform is executed independently.

If one platform fails, the other platforms continue processing.

The response provides:
- Success or failure status
- Published post URL
- Public access information when available
- Posting date and time
- Error message when posting fails

## Running Tests

Run all automated tests:

```bash
python -m pytest tests/test_posting.py -v
```

Current automated test coverage includes:

- Home endpoint
- Missing CTA URL
- Multiple URLs
- Message length validation
- Empty message validation
- Independent platform failure handling

**Latest test result: 6 passed.**

## Security

- API credentials are stored in environment variables.
- `.env` is excluded from Git.
- Never publish API tokens or passwords in source code.
- Use `.env.example` for configuration documentation.

## Author

Satyajeetsinh Dodiya

Automated Multi-Platform Posting System — Python & FastAPI.
