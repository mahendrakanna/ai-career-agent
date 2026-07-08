from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.db.database import SessionLocal

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@app.get("/health")
def health():
    try:
        db = SessionLocal()

        db.execute(text("SELECT 1"))

        db.close()

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": str(e),
        }