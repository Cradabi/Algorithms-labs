import random
import sys




sys.setrecursionlimit(5000000)


def go(index_now, all_list, visit_list, way_list):
    visit_list.append(index_now)
    if len(way_list) > 0:
        if way_list[-1] != index_now:
            way_list.append(index_now)
    else:
        way_list.append(index_now)
    if index_now[1] == 14:
        print(way_list)
        return way_list
    if (index_now[0] - 1) >= 0 and (index_now[0] - 1, index_now[1]) not in visit_list and all_list[
        index_now[0] - 1][index_now[1]] == 0:
        go((index_now[0] - 1, index_now[1]), all_list, visit_list, way_list)
    elif (index_now[1] - 1) >= 0 and (index_now[0], index_now[1] - 1) not in visit_list and all_list[
        index_now[0]][index_now[1] - 1] == 0:
        go((index_now[0], index_now[1] - 1), all_list, visit_list, way_list)
    elif (index_now[0] + 1) <= 14 and (index_now[0] + 1, index_now[1]) not in visit_list and all_list[
        index_now[0] + 1][index_now[1]] == 0:
        go((index_now[0] + 1, index_now[1]), all_list, visit_list, way_list)
    elif (index_now[1] + 1) <= 14 and (index_now[0], index_now[1] + 1) not in visit_list and all_list[
        index_now[0]][index_now[1] + 1] == 0:
        go((index_now[0], index_now[1] + 1), all_list, visit_list, way_list)
    else:
        way_list.pop(-1)
        if len(way_list) == 0:
            return 0
        else:
            go(way_list[-1], all_list, visit_list, way_list)




visit_list = []
x = []
all_list = []
for i in range(15):
    for w in range(15):
        x.append(random.randint(0, 1))
    print(x)
    all_list.append(x)
    x = []

res = []
for i in range(15):
    if all_list[i][0] == 0:
        go((i, 0), all_list, [], [])
