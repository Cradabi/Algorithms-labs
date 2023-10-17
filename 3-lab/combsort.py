import random

a = list(random.randint(1, 1000) for x in range (1, 10))

print(a)

def comb_sort(a):
    gap = len(a) - 1
    while gap >= 1:
        for x in range(0, len(a) - gap):
            if a[x] > a[x+gap]:
                a[x], a[x+gap] = a[x+gap], a[x]
                changed = True
        gap = int(gap/1.3)
    return a

print(f'Ваш список в отсортированном виде: {comb_sort(a)}')
    


