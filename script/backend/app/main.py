
from fastapi import FastAPI

app = FastAPI(
    title="EON AI",
    description="Personal Artificial Intelligence System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "EON is online!",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "assistant": "EON"
    }
