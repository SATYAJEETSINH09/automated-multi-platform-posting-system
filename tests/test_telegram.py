
import asyncio
from app.platforms.telegram import post_to_telegram


async def main():
    result = await post_to_telegram(
        "Hello! This is my first automated Telegram post using Python."
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
