import random

arrlen = int(input('Введите длину массива случайных чисел для сортировки \n'))

arr = [random.randint(0, 100) for x in range(arrlen)]

print(f'Неотсортированный массив: {arr}')

sortcnt = 1

while sortcnt > 0:
    sortcnt = 0
    for x in range(0, arrlen-1):
        if arr[x] > arr[x+1]:
            arr[x], arr[x+1] = arr[x+1], arr[x]
            sortcnt+=1
print(f'Отсортированный массив: {arr}')
