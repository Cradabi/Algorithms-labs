import csv


def second_task(dict,
                list_with_questions):  # на вход подается словарь людей с ответами через / в нижнем регистре и список вопросов
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


list_csv = []
list_with_question = []
dict = {}
with open("answers_2.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    for row in file_reader:
        list_csv.append(row)
for i in range(len(list_csv)):
    if i == 0:
        for w in range(2, len(list_csv[i])):
            list_with_question.append(list_csv[i][w])
    else:
        name_l = ''
        str_answers = []
        for w in range(1, len(list_csv[i])):
            if w == 1:
                name_l = list_csv[i][w]
            else:
                str_answers.append(list_csv[i][w].lower())
        dict.update({name_l: "/".join(str_answers)})
print(second_task(dict, list_with_question))
