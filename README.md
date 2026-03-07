# AI Resume Screening and Analysis System

A tech-role focused AI screening system that ranks candidates against job descriptions using explainable scoring.

## Why this project stands out

- Built for real recruiter workflows, not a toy demo.
- Explainable ranking: each score includes matched skills, missing skills, strengths, and concerns.
- Tunable scoring for different hiring styles.
- API-first design, ready to pair with a modern frontend dashboard.

## Current MVP capabilities

- Accepts a job description and multiple candidate resumes.
- Extracts required technical skills from the job description.
- Uses role-family weighted scoring for tech roles (`backend`, `frontend`, `data_ai`, `devops`, `fullstack`).
- Supports `must_have_skills` and `nice_to_have_skills` for stronger shortlist quality.
- Parses resume files from `PDF`, `DOCX`, and `TXT`.
- Adds semantic skill adjacency matching so related stack experience gets partial credit.
- Returns ranked candidates with transparent reasoning and hard-constraint flags.

## Tech stack

- Python 3.11+
- FastAPI
- Pytest

## Project structure

```text
src/app/
  api/routes.py            # REST endpoints
  services/scoring.py      # Ranking and scoring logic
  services/skill_taxonomy.py
  schemas.py               # Request/response models
  main.py                  # FastAPI app entry
tests/
  test_scoring.py
```

## Local setup (Windows PowerShell, using venv)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
$env:PYTHONPATH = "src"
uvicorn app.main:app --reload
```

API docs: `http://127.0.0.1:8000/docs`
Recruiter dashboard: `http://127.0.0.1:8000/`

If port `8000` is occupied, run on another port:

```powershell
uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
```

If you open the frontend from a different origin (for example VS Code Live Server), set API base in browser console:

```javascript
localStorage.setItem("talentrank_api_base", "http://127.0.0.1:8001");
```

## Run tests

```powershell
$env:PYTHONPATH = "src"
pytest -q
```

## Example API payload

```json
{
  "job_title": "Backend Python Engineer",
  "job_description": "Looking for Python, FastAPI, Docker, PostgreSQL, and AWS experience.",
  "role_family": "backend",
  "must_have_skills": ["python", "fastapi"],
  "nice_to_have_skills": ["aws"],
  "candidates": [
    {
      "name": "Alex",
      "resume_text": "Built Python APIs with FastAPI and Docker, deployed on AWS with PostgreSQL.",
      "years_experience": 4
    }
  ]
}
```

## Endpoints

- `POST /v1/analyze`:
JSON payload-based analysis using extracted and explicit skills.
- `POST /v1/analyze-files`:
Multipart form-based analysis for real resume uploads (`resumes`) with automatic candidate name and experience extraction.

## Dashboard demo flow

1. Open `/` and update the role profile and JD.
2. Choose `Paste Resume Text` or `Upload Resume Files` mode.
3. In file mode, upload PDF/DOCX/TXT resumes.
4. Candidate names and years of experience are inferred automatically from resume content (with filename fallback for name).
5. Run screening to generate leaderboard cards.
6. Use Candidate Comparison to compare score components and semantic evidence.

## Flagship roadmap (next milestones)

1. Embeddings-based semantic matching for skill adjacency.
2. Frontend recruiter dashboard with candidate comparison UI.
3. Exportable shortlist reports (PDF/CSV).
4. Authentication, persistence, and audit trails.
5. Benchmark dataset and quality metrics for portfolio proof.
