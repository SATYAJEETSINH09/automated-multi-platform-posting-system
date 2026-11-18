
import asyncio

from app.platforms.telegram import post_to_telegram
from app.platforms.mastodon import post_to_mastodon
from app.platforms.bluesky import post_to_bluesky
from app.platforms.devto import post_to_devto
from app.platforms.github import post_to_github


async def post_to_all_platforms(message: str):

    platforms = {
        "telegram": post_to_telegram,
        "mastodon": post_to_mastodon,
        "bluesky": post_to_bluesky,
        "devto": post_to_devto,
        "github": post_to_github,
    }

    async def execute_platform(name, function):
        try:
            data = await function(message)

            return {
                "status": "success",
                "posted_url": data.get("url"),
                # "public_access": data.get("public"),
                "public_access": data.get("public", False),
                "date_time": (
                    data.get("created_at")
                    or data.get("published_at")
                    or data.get("date")
                ),
                "error": None
            }

        except Exception as error:
            return {
                "status": "failed",
                "posted_url": None,
                "public_access": None,
                "date_time": None,
                "error": str(error)
            }

    tasks = [
        execute_platform(name, function)
        for name, function in platforms.items()
    ]

    results = await asyncio.gather(*tasks)

    return {
        "success": any(
            result["status"] == "success"
            for result in results
        ),
        "total_platforms": len(platforms),
        "successful": sum(
            result["status"] == "success"
            for result in results
        ),
        "failed": sum(
            result["status"] == "failed"
            for result in results
        ),
        "platforms": dict(zip(platforms.keys(), results))
    }
