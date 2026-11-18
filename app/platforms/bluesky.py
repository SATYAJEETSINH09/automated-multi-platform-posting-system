
from atproto import Client
from app.config import BLUESKY_HANDLE, BLUESKY_APP_PASSWORD
from datetime import datetime, timezone


async def post_to_bluesky(message: str):
    client = Client()
    client.login(BLUESKY_HANDLE, BLUESKY_APP_PASSWORD)

    response = client.send_post(text=message)

    post_id = response.uri.split("/")[-1]

    return {
        "status": "success",
        "id": post_id,
        "uri": response.uri,
        "cid": response.cid,
        "url": (
            f"https://bsky.app/profile/"
            f"{BLUESKY_HANDLE}/post/{post_id}"
        ),
        "public": True,
        "visibility": "public",
        "created_at": datetime.now(timezone.utc).isoformat()
    }
