''' На какой-то планете находится x городов. Матрица x*x с 0 и 1, где 1 - там дорога.
Если нет дорог, то города в других странах. Посчитать, сколько стран на планете.
'''

import random

scale = 20

rng = [0] * 10 + [1]
matrix = [[random.choice(rng) for x in range(scale)] for x in range(scale)]

borders = {x: set() for x in range(scale)}


for i in range(scale):
    matrix[i][i] = 1
    
for x in range(scale):
    for y in range(scale):
        if matrix[x][y] == 1 and x!= y:
            borders[x].add(y)



countries = {x: set() for x in range(scale)}

for y in range(scale):
    z = borders[y]
    for i in z:
        countries[y].add(i)

for x in range(scale):
    for y in range(scale):
        if x in countries and y in countries and x!=y:
            k = countries[x]
            l = countries[y]
            if len(k.intersection(l)) > 0:
                countries[x].update(l)
                del countries[y]

bob = len(countries)
print(f'Количество стран на планете - {bob}')
 
            
