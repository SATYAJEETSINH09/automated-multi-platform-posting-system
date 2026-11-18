
import asyncio
from app.platforms.github import post_to_github


async def main():
    result = await post_to_github(
        "Testing my Automated Multi-Platform Posting System"
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
