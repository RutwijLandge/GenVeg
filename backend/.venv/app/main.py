from fastapi import FastAPI

app = FastAPI(
    title="GenVeg AI",
    description="AI-powered conversational vegetable shopping assistant",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to GenVeg AI",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }