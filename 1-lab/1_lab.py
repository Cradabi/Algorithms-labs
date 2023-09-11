def first_task(num):
    counter = 0
    while 2 ** counter < num:
        counter += 1
    return counter

def second_task(dict, list_with_questions):  #на вход подается словарь людей с ответами через / в нижнем регистре и список вопросов
    for i in range(len(list_with_questions)):
        print(list_with_questions[i])
        ans = input().lower()
        dict_to_change = {}
        for key in dict:
            if dict[key].split('/')[i] == ans:
                dict_to_change.update({key: dict[key]})
        dict = dict_to_change
        if len(dict) == 1:
            for key in dict:
                return key

dict = {'s': 'yes/yes/yes', 'a': 'yes/yes/no'}
list_with_question = ["Человек блондин", "Человек дурак", "Человек красивый"]
print(second_task(dict, list_with_question))
