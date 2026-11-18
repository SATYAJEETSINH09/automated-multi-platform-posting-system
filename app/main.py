
from fastapi import FastAPI
from app.schemas import PostingRequest
from app.services.posting_service import post_to_all_platforms

app = FastAPI(
    title="Automated Multi-Platform Posting System",
    description="Post messages to five platforms using one API.",
    version="1.0.0"
)


@app.get("/")
async def home():
    return {
        "message": "Automated Posting System is running!"
    }


@app.post("/posting")
async def create_post(request: PostingRequest):
    result = await post_to_all_platforms(request.message)

    return result
