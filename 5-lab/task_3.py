list_x = [int(x) for x in input().split()]
count = 1
max_count = 1

for i in range(1, len(list_x)):
    if list_x[i] <= list_x[i - 1]:
        if count > max_count:
            max_count = count
        count = 1
    else:
        count += 1
if count > max_count:
    max_count = count
print(max_count)
