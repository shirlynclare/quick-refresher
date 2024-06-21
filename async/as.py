import asyncio

async def delayed_hi(seconds: int):
    await asyncio.sleep(seconds)
    print(f"Hi after {seconds}")
async def bye(bye):
    print("bye")

async def main():
    await asyncio.gather(
        delayed_hi(1),
        delayed_hi(5),
        delayed_hi(3),
        bye,
    )

asyncio.run(main())