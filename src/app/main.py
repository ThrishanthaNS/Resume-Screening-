from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes import router
from app.web.routes import router as web_router

app = FastAPI(
    title="AI Resume Screening and Analysis System",
    version="0.1.0",
    description="Tech-role focused candidate screening API with explainable ranking.",
)

# Allow dashboard access from any origin.
# The dashboard is served from the same FastAPI instance, so same-origin
# requests work by default.  Wildcard is needed for local dev variants
# (VS Code Live Server, different ports) and the Render deployment URL.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

_static_dir = Path(__file__).resolve().parent / "web" / "static"
app.mount("/static", StaticFiles(directory=str(_static_dir)), name="static")

app.include_router(web_router)
app.include_router(router)
