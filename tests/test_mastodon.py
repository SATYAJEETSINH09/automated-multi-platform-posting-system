
import asyncio
from app.platforms.mastodon import post_to_mastodon


async def main():
    result = await post_to_mastodon(
        "Hello! This is my first automated Mastodon post using Python."
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
