
import asyncio
from app.platforms.devto import post_to_devto


async def main():
    result = await post_to_devto(
        "Hello! This is my first automated article using Python."
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
