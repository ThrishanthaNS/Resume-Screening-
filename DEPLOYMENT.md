# Deploying TalentRank Studio on Render

## Prerequisites

- A [Render](https://render.com) account (free tier works).
- The project pushed to a GitHub or GitLab repository.

---

## Option A — Blueprint Deploy (Recommended)

This project includes a `render.yaml` blueprint that pre-configures everything.

1. Push all changes to your GitHub repository.
2. Go to [https://render.com/deploy](https://render.com/deploy).
3. Connect your repository.
4. Render reads `render.yaml` and creates the service automatically.
5. Click **Apply** to deploy.

---

## Option B — Manual Dashboard Setup

1. Sign in to [Render](https://render.com).
2. Click **New → Web Service**.
3. Connect your GitHub repository.
4. Configure the service:

| Setting            | Value                                                          |
| ------------------ | -------------------------------------------------------------- |
| **Name**           | `talentrank-studio` (or any name you prefer)                   |
| **Runtime**        | Python                                                         |
| **Build Command**  | `pip install -r requirements.txt`                              |
| **Start Command**  | `PYTHONPATH=src uvicorn app.main:app --host 0.0.0.0 --port $PORT` |

5. Add environment variables:

| Key                     | Value        |
| ----------------------- | ------------ |
| `APP_ENV`               | `production` |
| `APP_HOST`              | `0.0.0.0`   |
| `TOP_CANDIDATES_LIMIT`  | `5`          |
| `PYTHON_VERSION`        | `3.11.11`    |

6. Click **Deploy**.

---

## Python Version

Render defaults to the latest Python, which may not have pre-built wheels for
all dependencies (e.g., `pydantic-core`). The `runtime.txt` file in the
repository root pins Python to `3.11.11` to avoid this issue.

If you need a different version, update both:
- `runtime.txt` (Render reads this during build)
- `PYTHON_VERSION` environment variable in `render.yaml` or the dashboard

---

## How the Dashboard Works in Production

The dashboard frontend (`src/app/web/static/`) is served by FastAPI itself.
The JavaScript automatically detects whether it's running on `localhost` or a
deployed origin and adjusts API calls accordingly — no manual URL configuration
is needed.

---

## Verifying the Deployment

Once deployed, Render provides a URL like `https://talentrank-studio.onrender.com`.

- **Dashboard:** `https://talentrank-studio.onrender.com/`
- **API Docs:** `https://talentrank-studio.onrender.com/docs`
- **Health Check:** `https://talentrank-studio.onrender.com/v1/health`

---

## Troubleshooting

### Build fails with pydantic-core error
→ Make sure `runtime.txt` contains `python-3.11.11` and is committed to the repo.

### Dashboard shows "Failed to fetch"
→ The API and dashboard are served from the same origin, so this should not
   happen on Render. If it does, check the Render logs for startup errors.

### Application crashes on startup
→ Check that the start command includes `PYTHONPATH=src`. Without it, Python
   cannot find the `app` package inside the `src/` directory.

### Free tier cold starts
→ Render's free tier spins down after 15 minutes of inactivity. The first
   request after idle may take 30-60 seconds. This is normal.
