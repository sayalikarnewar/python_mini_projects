import asyncio
import time
import schedule

async def webapp():
    print(1)
    await asyncio.sleep(1)

async def scheduler():
    def job():
        func()

    schedule.every(3).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

async def main():
    task1 = asyncio.create_task(webapp())
    task2 = asyncio.create_task(scheduler())

    await task1
    await task2

asyncio.run(main())