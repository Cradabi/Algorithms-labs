
def is_correct_parentheses(string):
    parlist = [x for x in string]
    secondpar = []
    goodpar = []
    correct = True

    for x in range(len(parlist) - 1, -1, -1):
        if parlist[x] == '(':
            for y in range(x + 1, len(parlist)):
                if parlist[y] == ')' and y not in secondpar:
                    secondpar.append(y)
                    goodpar.append(x)
                    goodpar.append(y)
                    correct = True
                    break
                correct = False

    if correct and len(secondpar) == parlist.count(")"):
        return True
    else:
        return False

