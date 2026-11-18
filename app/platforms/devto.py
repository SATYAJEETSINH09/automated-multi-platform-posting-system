
import httpx
from app.config import DEVTO_API_KEY


async def post_to_devto(message: str):
    url = "https://dev.to/api/articles"

    headers = {
        "api-key": DEVTO_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "article": {
            "title": "Automated Posting System - Test",
            "body_markdown": message,
            "published": True
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            headers=headers,
            json=payload
        )

        data = response.json()

        if response.status_code != 201:
            raise Exception(
                data.get("error", "DEV.to posting failed")
            )

        return {
            "status": "success",
            "id": data["id"],
            "url": data.get("url"),
            "public": data.get("published", True),
            "visibility": "public",
            "created_at": data.get("published_at")
        }
