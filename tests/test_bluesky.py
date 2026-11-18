
import asyncio
from app.platforms.bluesky import post_to_bluesky


async def main():
    result = await post_to_bluesky(
        "Hello! This is my first automated Bluesky post using Python."
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())

