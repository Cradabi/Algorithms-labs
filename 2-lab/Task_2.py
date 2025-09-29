import random

def bubble_sort(arr):
    arrlen = len(arr)
    sortcnt = 1
    while sortcnt > 0:
        sortcnt = 0
        for x in range(arrlen - 1):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
                sortcnt += 1
    return arr



