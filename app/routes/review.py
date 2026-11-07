from fastapi import APIRouter, status
from pydantic import BaseModel, HttpUrl

router = APIRouter()


class ReviewRequest(BaseModel):
    github_url: HttpUrl


@router.post("/api/reviews", status_code=status.HTTP_201_CREATED)
def create_review(request: ReviewRequest):
    return {
        "message": "Review request received successfully",
        "github_url": str(request.github_url)
    }