from fastapi import FastAPI
from app.routes import review

app = FastAPI(
    title="GitHub AI Code Reviewer",
    description="An AI-powered code review platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to GitHub AI Code Reviewer!",
        "status": "Application is running"
    }


app.include_router(review.router)