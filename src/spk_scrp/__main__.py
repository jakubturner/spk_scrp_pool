import asyncio

from src.spk_scrp.app import App


async def run() -> None:
    app = App()
    await app.setup()

    try:
        await app.scrapper()
    except KeyboardInterrupt:
        pass


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()
