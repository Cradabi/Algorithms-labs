inp = input('Введите отсортированный список чисел, разделенных пробелом \n')
arr = list(int(x) for x in inp.split())
numtofind = int(input('Введите число из списка для поиска \n'))
minborder = 0
maxborder = len(arr) - 1
mid = len(arr) // 2
steps = 1
while maxborder - minborder >= 0 and arr[mid] != numtofind:
    if numtofind > arr[mid]:
        minborder = mid + 1
        mid = (minborder + maxborder) // 2
        steps += 1
    else:
        maxborder = mid - 1
        mid = (minborder + maxborder) // 2
        steps += 1
if arr[mid] == numtofind:
    print(f'Число найдено. Потребовалось шагов - {steps}, номер числа в списке - {mid + 1}')
else:
    print('Заданного числа нет в списке')
