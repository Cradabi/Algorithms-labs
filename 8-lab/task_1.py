import asyncio
import time
import requests


async def fun1():
    url = 'https://www.google.com'
    response = requests.get(url)
    print(response.text)
    print('\n')


async def fun2():
    url = 'https://vk.company/ru/'
    response = requests.get(url)
    print(response.text)
    print('\n')


async def fun3():
    url = 'https://www.youtube.com'
    response = requests.get(url)
    print(response.text)
    print('\n')


async def main():
    task1 = asyncio.create_task(fun1())
    task2 = asyncio.create_task(fun2())
    task3 = asyncio.create_task(fun3())

    await task1
    await task2
    await task3
    print("That's all")


asyncio.run(main())
