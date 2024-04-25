import asyncio
import time
import requests


async def fun1():
    url = 'https://www.google.com'
    response = requests.get(url)
    print(response.text)


async def fun2():
    url = 'https://www.google.com'
    response = requests.get(url)
    print(response.text)


async def main():
    task1 = asyncio.create_task(fun1())
    task2 = asyncio.create_task(fun2())

    await task1
    await task2


asyncio.run(main())

