from fastapi import FastAPI

from app.database import check_database_connection


app = FastAPI(
    title="GenVeg AI",
    description="AI-powered conversational grocery shopping assistant",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to GenVeg AI",
        "status": "running",
    }


@app.get("/health")
def health():
    database_status = check_database_connection()

    return {
        "status": "healthy" if database_status else "degraded",
        "database": "connected" if database_status else "disconnected",
    }