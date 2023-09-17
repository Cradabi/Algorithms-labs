import random

itemcnt = int(input('Введите число элементов списка \n'))
maxnumb = int(input('Введите максимально возможное числовое значение элемента списка \n'))
numtofind = int(input('Введите искомое число \n'))
arr = random.sample(range(1, maxnumb+1), itemcnt)
arr.sort()
steps = 0 
minborder = 0
maxborder = len(arr)-1
mid = len(arr)//2
steps = 1
print(arr)
while maxborder - minborder >= 0 and arr[mid] != numtofind:
    if numtofind > arr[mid]:
        minborder = mid  + 1
        mid = (minborder + maxborder) // 2
        steps +=1
    else:
        maxborder = mid - 1
        mid = (minborder + maxborder) // 2
        steps +=1
if arr[mid] == numtofind:
    print(f'Число найдено. Потребовалось шагов - {steps}, индекс искомого числа - {mid}')
else:
    print('Заданного числа нет в списке')
        

