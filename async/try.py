import asyncio
async def main():
    print("tim")
#create evnt loop by task creating
    #await foo("text")
    task=asyncio.create_task(foo("text"))

async def foo(text):
    print(text)
    #sleep coroutine
    #wait 1 sec to run
    await asyncio.sleep(1)
asyncio.run (main())
#await can only be used in couritine(async function)
#await means wait till that is finished then proceed