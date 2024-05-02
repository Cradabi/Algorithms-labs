import requests
import asyncio


async def fun1(id):
    # Замените на ваш access_token
    access_token = 'vk1.a.1Rs5MFNPLyqMafOtS6pUfQ_KV5X8L9-tmCBzjt-laHiE5r6WG2pEoMF-EfFdayi3qeiJbYPc9CILKwFqs2722BNYyxwizrfPOY0-TiR5fzQNeVagvsCirXUsZ67LwYeq8zkIPXerwr24AS_-8WfScI8_GR7YHMsWPg9Jv0wmxUPrc2PMVELs2W6FKWigC4r4'

    # ID пользователя, информацию о котором вы хотите получить
    user_id = str(id)

    # Отправляем запрос к API ВКонтакте
    params = {
        'user_ids': user_id,
        'fields': 'first_name,last_name,bdate,city,country',
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/users.get', params=params)

    # Обрабатываем ответ
    if response.status_code == 200:
        data = response.json()
        if 'response' in data:
            user = data['response'][0]
            print(f"Имя: {user['first_name']}")
            print(f"Фамилия: {user['last_name']}")
            print(f"Дата рождения: {user.get('bdate', 'Не указана')}")
            print(f"Город: {user.get('city', {}).get('title', 'Не указан')}")
            print(f"Страна: {user.get('country', {}).get('title', 'Не указана')}")
        else:
            print('Ошибка при получении данных')
    else:
        print('Ошибка при выполнении запроса')
    print('\n')


async def fun2(id):
    # Замените на ваш access_token
    access_token = 'vk1.a.1Rs5MFNPLyqMafOtS6pUfQ_KV5X8L9-tmCBzjt-laHiE5r6WG2pEoMF-EfFdayi3qeiJbYPc9CILKwFqs2722BNYyxwizrfPOY0-TiR5fzQNeVagvsCirXUsZ67LwYeq8zkIPXerwr24AS_-8WfScI8_GR7YHMsWPg9Jv0wmxUPrc2PMVELs2W6FKWigC4r4'

    # ID пользователя, информацию о котором вы хотите получить
    user_id = str(id)

    # Отправляем запрос к API ВКонтакте
    params = {
        'user_ids': user_id,
        'fields': 'first_name,last_name,bdate,city,country',
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/users.get', params=params)

    # Обрабатываем ответ
    if response.status_code == 200:
        data = response.json()
        if 'response' in data:
            user = data['response'][0]
            print(f"Имя: {user['first_name']}")
            print(f"Фамилия: {user['last_name']}")
            print(f"Дата рождения: {user.get('bdate', 'Не указана')}")
            print(f"Город: {user.get('city', {}).get('title', 'Не указан')}")
            print(f"Страна: {user.get('country', {}).get('title', 'Не указана')}")
        else:
            print('Ошибка при получении данных')
    else:
        print('Ошибка при выполнении запроса')
    print('\n')


async def fun3(id):
    # Замените на ваш access_token
    access_token = 'vk1.a.1Rs5MFNPLyqMafOtS6pUfQ_KV5X8L9-tmCBzjt-laHiE5r6WG2pEoMF-EfFdayi3qeiJbYPc9CILKwFqs2722BNYyxwizrfPOY0-TiR5fzQNeVagvsCirXUsZ67LwYeq8zkIPXerwr24AS_-8WfScI8_GR7YHMsWPg9Jv0wmxUPrc2PMVELs2W6FKWigC4r4'

    # ID пользователя, информацию о котором вы хотите получить
    user_id = str(id)

    # Отправляем запрос к API ВКонтакте
    params = {
        'user_ids': user_id,
        'fields': 'first_name,last_name,bdate,city,country',
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/users.get', params=params)

    # Обрабатываем ответ
    if response.status_code == 200:
        data = response.json()
        if 'response' in data:
            user = data['response'][0]
            print(f"Имя: {user['first_name']}")
            print(f"Фамилия: {user['last_name']}")
            print(f"Дата рождения: {user.get('bdate', 'Не указана')}")
            print(f"Город: {user.get('city', {}).get('title', 'Не указан')}")
            print(f"Страна: {user.get('country', {}).get('title', 'Не указана')}")
        else:
            print('Ошибка при получении данных')
    else:
        print('Ошибка при выполнении запроса')
    print('\n')


async def main():
    id_1 = int(input())
    id_2 = int(input())
    id_3 = int(input())
    task1 = asyncio.create_task(fun1(id_1))
    task2 = asyncio.create_task(fun2(id_2))
    task3 = asyncio.create_task(fun3(id_3))

    await task1
    await task2
    await task3
    print("That's all")


asyncio.run(main())
