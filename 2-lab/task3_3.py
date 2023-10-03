def gp(permutation, remaining, index):
    if index == len(remaining):
        print(permutation)
    else:
        for i in range(index, len(remaining)):
            # Cмена элементов друг с другом
            remaining[index], remaining[i] = remaining[i], remaining[index]

            # Рекурсивный перебор
            gp(permutation + [remaining[index]], remaining, index + 1)


elements = [1, 2, 3]
gp([], elements, 0)
