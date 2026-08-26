from fastapi import FastAPI

from app.database import check_database_connection
from app.routes.products import router as product_router


app = FastAPI(
    title="GenVeg AI",
    description="AI-powered conversational grocery shopping assistant",
    version="0.1.0",
)


app.include_router(product_router)


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