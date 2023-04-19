import sys

import asyncio
from watchfiles import awatch

async def main():
    async for changes in awatch(sys.argv[1], debug=True):
        print(changes)

asyncio.run(main())
