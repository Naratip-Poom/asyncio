#example of gather for many coroutines in a list
import asyncio
import time

#coroutune for a task
async def task_coro(value):
    #report a massege
    print(f'{time.ctime()} task {value} executing')
    #block for a moment
    await asyncio.sleep(1)

#define a coroutine
async def main():
    #report a message
    print(f'{time.ctime()} main starting.') 
    #create many coroutines
    coros = [task_coro(i) for i in range(10000)]
    #run the tasks
    await asyncio.gather(*coros)
    #report a message
    print(f'{time.ctime()} main done')
    
   
# start the asyncio programs
asyncio.run(main())