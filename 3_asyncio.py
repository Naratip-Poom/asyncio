#example of starting many tasks and getting access to all tasks
import asyncio
import time

#coroutune for a task
async def task_coroutine(value):
    #report a massege
    print(f'{time.ctime()} task {value} is runing')
    #block for a moment
    await asyncio.sleep(1)


#define a coroutine
async def main():
    #report a message
    print(f'{time.ctime()} main coroutine started') 
    #start many tasks
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    #allow some of the tasks time to start
    await asyncio.sleep(0.1)
    #get all tasks
    tasks = asyncio.all_tasks()
    #report its details
    for task in tasks:
        print(f'{time.ctime()}>{task.get_name()}, {task.get_coro()}')
    #wait for all tasks to compleate
    for task in started_tasks:
        await task
    
   
# start the coroutine programs
asyncio.run(main())
