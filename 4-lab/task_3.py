import random


def go(index_now, all_list, visit_list, way_list):
    if index_now[1] == 14:
        return "Путь существует"
    if (index_now[0] - 1) >= 0 and (index_now[0] - 1, index_now[1]) not in visit_list and all_list[
        index_now[0] - 1, index_now[1]] == 0:
        pass
    elif (index_now[1] - 1) >= 0 and (index_now[0], index_now[1] - 1) not in visit_list and all_list[
        index_now[0], index_now[1] - 1] == 0:
        pass
    elif (index_now[0] + 1) <= 14 and (index_now[0], index_now[1] - 1) not in visit_list and all_list[
        index_now[0] + 1, index_now[1]] == 0:
        pass
    elif (index_now[1] + 1) <= 14 and (index_now[0], index_now[1] - 1) not in visit_list and all_list[
        index_now[0], index_now[1] + 1] == 0:
        pass


visit_list = []
x = []
all_list = []
for i in range(15):
    for w in range(15):
        x.append(random.randint(0, 1))
    all_list.append(x)
    x = []
print(all_list)

bad_list = []
lf = (21, 23)
