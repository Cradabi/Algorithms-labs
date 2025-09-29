''' На какой-то планете находится x городов. Матрица x*x с 0 и 1, где 1 - там дорога.
Если нет дорог, то города в других странах. Посчитать, сколько стран на планете.
'''

import random

scale = 4

matrix = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]

borders = {x: set() for x in range(scale)}


for i in range(scale):
    matrix[i][i] = 1
    
for x in range(scale):
    for y in range(scale):
        if matrix[x][y] == 1 and x!= y:
            borders[x].add(y)

print(matrix)

countries = {x: set() for x in range(scale)}

for y in range(scale):
    z = borders[y]
    for i in z:
        countries[y].add(i)
    countries[y].add(y)

for x in range(scale):
    for y in range(scale):
        if x in countries and y in countries and x!=y:
            k = countries[x]
            l = countries[y]
            if len(k.intersection(l)) > 0:
                countries[x].update(l)
                del countries[y]

print(countries)
bob = len(countries)
print(f'Количество стран на планете - {bob}')
 
            
