howm = 6
w = [1, 55, 4, 3, 2, 1]
v = [1, 100, 10, 35, 4, 10]
runs = 3
scap = 10

def delist(l, id_to_del):
    for i in sorted(id_to_del, reverse=True):
        l[i] = 99999
        
def knapsack(n, c):
    if n == 0 or c == 0:
        return 0
    if w[n-1] > c:
        return knapsack(n-1, c)
    if w[n-1] <= c:
        a1 = knapsack(n-1, c)
        a2 = v[n-1] + knapsack(n-1, c - w[n-1])
        if a1 > a2:
            return a1
        if a2 > a1:
            return a2

for x in range(0, runs):
    if howm <= 0:
        print('Вы украли желаемое число предметов')
        break
    if len(w) == 0:
        print('Вы украли все предметы')
        break
    print(f'Заход №{x+1}')
    cap = scap        
    res = knapsack(len(w), cap)
    taken = []
    for i in range(len(w)-1, -1, -1):

        if knapsack(i+1, cap) == (knapsack(i, cap - w[i]) + v[i]):
            taken.append(i)
            res = res - v[i]
            cap = cap - w[i]
        else:
            continue
    if len(taken) == 0:
        print(' \t Вы ничего не смогли украсть. Пора уходить..')
        break

    print('\t Индексы взятых предметов - ', taken)
    delist(w, taken)
    delist(v, taken)
    howm = howm - len(taken)

if howm > 0:
    print('\n Вы не смогли украсть желаемое число предметов за данное количество заходов. Надо тренироваться!')
