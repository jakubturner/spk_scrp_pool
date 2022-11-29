import asyncio
import schedule
import time

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


schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == "__main__":
    main()
