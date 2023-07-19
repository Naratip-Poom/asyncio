#examole of runing a coroutine
import asyncio
import time


#define a coroutine
async def main():
    #report a message
    print(f'{time.ctime()} main coroutine started') 
    #get the current task
    task = asyncio.current_task()
    #report its details
    print(f'{time.ctime()}{task}')
    
   
# start the coroutine programs
asyncio.run(main())

# Wed Jul 12 14:38:46 2023 main coroutine started
# Wed Jul 12 14:38:46 2023<Task pending name='Task-1' coro=<main() running at D:\IOTAsyncronus\asy\2_asyncio.py:13> cb=[_run_until_complete_cb() at C:\Program Files\Python311\Lib\asyncio\base_events.py:180]>
