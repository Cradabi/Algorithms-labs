inp = input('Введите отсортированный список чисел, разделенных пробелом \n')
arr = list(int(x) for x in inp.split())
num1 = int(input('Введите первое число из списка для поиска \n'))
num2 = int(input('Введите второе число из списка для поиска \n'))
num3 = int(input('Введите третье число из списка для поиска \n'))
arr1=arr
minborder = 0
maxborder = len(arr1) - 1
mid = len(arr1) // 2
while maxborder - minborder >= 0 and arr1[mid] != num1:
    if num1 > arr1[mid]:
        minborder = mid + 1
        mid = (minborder + maxborder) // 2
    else:
        maxborder = mid - 1
        mid = (minborder + maxborder) // 2
if arr1[mid] == num1:
    print(f'Номер числа в списке - {mid + 1}')
else:
    print('Заданного числа нет в списке')
arr1=arr
minborder = 0
maxborder = len(arr1) - 1
mid = len(arr1) // 2
while maxborder - minborder >= 0 and arr1[mid] != num2:
    if num2 > arr1[mid]:
        minborder = mid + 1
        mid = (minborder + maxborder) // 2
    else:
        maxborder = mid - 1
        mid = (minborder + maxborder) // 2
if arr1[mid] == num2:
    print(f'Номер числа в списке - {mid + 1}')
else:
    print('Заданного числа нет в списке')
arr1=arr
minborder = 0
maxborder = len(arr1) - 1
mid = len(arr1) // 2
while maxborder - minborder >= 0 and arr1[mid] != num3:
    if num3 > arr1[mid]:
        minborder = mid + 1
        mid = (minborder + maxborder) // 2
    else:
        maxborder = mid - 1
        mid = (minborder + maxborder) // 2
if arr1[mid] == num3:
    print(f'Номер числа в списке - {mid + 1}')
else:
    print('Заданного числа нет в списке')
