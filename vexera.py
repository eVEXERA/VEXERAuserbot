import asyncio

from pytgcalls import idle

from config import call_py


async def vexera():
    await call_py.start()
    print(
        """
      ------------------
|𝙑𝙀𝙓𝙀𝙍𝘼 𝙑𝘾 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𝙎𝙏𝘼𝙍𝙏𝙀𝘿|
      ------------------
"""
    )
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(vexera())
