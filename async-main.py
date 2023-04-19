import asyncio
from watchfiles import awatch

async def main():
    async for changes in awatch('/watch-this', debug=True):
        print(changes)

asyncio.run(main())
