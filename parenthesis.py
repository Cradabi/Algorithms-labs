string = input('Введите произвольный набор круглых скобок \n')


'''
a = 0


for x in string:
    if x == "(":
        a+=1
    elif x == ")":
        a-=1
    if a < 0:
        break

if a == 0:
    print('Ваш набор - правильная скобочная последовательность')
else:
    print('Ваш набор - неправильная скобочная последовательность')
'''

parlist = [x for x in string]

secondpar = []
goodpar = []
correct = True

for x in range(len(parlist)-1, -1, -1):
    if parlist[x] == '(':
        for y in range(x+1, len(parlist)):
            if parlist[y] == ')' and y not in secondpar:
                secondpar.append(y)
                goodpar.append(x)
                goodpar.append(y)
                correct = True
                break
            correct = False

print(goodpar)

if correct and len(secondpar) == parlist.count(")"):
    print('Ваш набор - правильная скобочная последовательность')
else:
    for x in range(0, len(string)):
        if x not in goodpar:  
            print(f'Ваш набор - неправильная скобочная последовательность. Индекс первой лишней скобки - {x}')
            break
