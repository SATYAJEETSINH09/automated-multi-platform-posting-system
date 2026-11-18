
import httpx
from datetime import datetime, timezone

from app.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID


async def post_to_telegram(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHANNEL_ID,
        "text": message
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        data = response.json()

        if response.status_code != 200 or not data.get("ok"):
            raise Exception(
                data.get("description", "Telegram posting failed")
            )

        result = data["result"]
        message_id = result["message_id"]

        channel_username = TELEGRAM_CHANNEL_ID.lstrip("@")

        return {
            "status": "success",
            "message_id": message_id,
            "chat_id": result["chat"]["id"],
            "url": f"https://t.me/{channel_username}/{message_id}",
            "public": True,
            "created_at": datetime.fromtimestamp(
                result["date"], timezone.utc
            ).isoformat()
        }
