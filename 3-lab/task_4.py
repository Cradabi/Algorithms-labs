def insertion_sort(list_n):
    for i in range(1, len(list_n)):
        j = i - 1
        num_n = list_n[i]
        while list_n[j] > num_n and j >= 0:
            list_n[j + 1] = list_n[j]
            j -= 1
        list_n[j + 1] = num_n
    return list_n


a = result = list(map(int, input("Введите числа: ").split()))
print(insertion_sort(a))
