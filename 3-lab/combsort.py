a = list(map(int, input('Введите неотсортированный список чисел, разделенных пробелом \n').split()))

def comb_sort(a):
    gap = len(a) - 1
    changed = True
    while changed == True:
        changed = False
        for x in range(0, len(a) - gap):
            if a[x] > a[x+gap]:
                a[x], a[x+gap] = a[x+gap], a[x]
                changed = True
        gap = int(gap/1.3)
    return a

print(f'Ваш список в отсортированном виде: {comb_sort(a)}')
    


