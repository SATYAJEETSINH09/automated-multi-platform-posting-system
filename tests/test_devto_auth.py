
import asyncio
import httpx
from app.config import DEVTO_API_KEY


async def main():
    headers = {
        "api-key": DEVTO_API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://dev.to/api/users/me",
            headers=headers
        )

        print("Status code:", response.status_code)
        print("Response:", response.text)


if __name__ == "__main__":
    asyncio.run(main())
