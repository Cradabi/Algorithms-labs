import anyio
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(1)

def long_word(x):
    b = x.split()
    print(max(len(a) for a in b))

async def max_len(x):
    async with await anyio.open_file(x) as f:
        contents = await f.read()
        await loop.run_in_executor(_executor, long_word, contents)
    await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(max_len("file1.txt"))
    task2 = asyncio.create_task(max_len("file2.txt"))
    task3 = asyncio.create_task(max_len("file3.txt"))
    await asyncio.gather(task1, task2, task3)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
t2 = time.time()
print(f"Time taken - {t2 - t1} seconds")
