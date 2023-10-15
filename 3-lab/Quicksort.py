a = list(map(int, input('Введите неотсортированный список чисел, разделенных пробелом \n').split()))

def quick_sort(a):
    if len(a)<=1:
        return a
    else:
        pivot = a.pop()
    lower = [x for x in a if x < pivot]
    higher = [x for x in a if x >= pivot]
    return quick_sort(lower) + [pivot] + quick_sort(higher)

print(f'Ваш список в отсортированном виде: {quick_sort(a)}')
