#example of waiting for all tasks to complete
import asyncio
import time
import random

#coroutine to execute in new task
async def task_coro(arg):
    #generate a random vakue between 0 and 1
    value = random.random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'{time.ctime()} >task {arg} done with {value}')

# main coroutine
async def main():
    #create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    #wait for all tasks to complete # All_COMPLETED, FIRST_COMPLETED, FIRST_EXCEPTION
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    # report results
    print(f'{time.ctime()} All done')

#start the asyncio program
asyncio.run(main())
