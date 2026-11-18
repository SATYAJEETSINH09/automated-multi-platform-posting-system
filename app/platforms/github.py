
import httpx
from app.config import GITHUB_TOKEN


async def post_to_github(message: str):
    url = "https://api.github.com/gists"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    payload = {
        "description": "Automated Posting System",
        "public": True,
        "files": {
            "automated-post.txt": {
                "content": message
            }
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
                data.get("message", "GitHub Gist posting failed")
            )

        return {
    "status": "success",
    "id": data["id"],
    "url": data["html_url"],
    "public": data["public"],
    "visibility": "public" if data["public"] else "private",
    "created_at": data["created_at"]
}
