
import httpx

from app.config import MASTODON_BASE_URL, MASTODON_ACCESS_TOKEN


async def post_to_mastodon(message: str):
    url = f"{MASTODON_BASE_URL}/api/v1/statuses"

    headers = {
        "Authorization": f"Bearer {MASTODON_ACCESS_TOKEN}"
    }

    payload = {
        "status": message,
        "visibility": "public"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            headers=headers,
            json=payload
        )

        data = response.json()

        if response.status_code not in (200, 201):
            raise Exception(
                data.get("error", "Mastodon posting failed")
            )

        return {
            "status": "success",
            "id": data["id"],
            "url": data.get("url"),
            "public": data.get("visibility") == "public",
            "visibility": data.get("visibility"),
            "created_at": data.get("created_at")
        }
