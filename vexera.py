import asyncio

from pytgcalls import idle

from config import call_py


async def vexera():
    await call_py.start()
    print(
        """
      ------------------
|ππππππΌ ππΎ πππππ½ππ πππΌππππΏ|
      ------------------
"""
    )
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(vexera())
