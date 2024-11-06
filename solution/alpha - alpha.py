import time
import random
lis = [[2, 4, 1, 3, 2, 1, 4, 3, 2, 1, 3, 3, 4, 1, 1, 3, 4, 3, 3, 3],
       [1, 2, 3, 3, 1, 1, 2, 1, 4, 1, 4, 4, 4, 2, 2, 4, 3, 3, 2, 4],
       [1, 2, 1, 1, 4, 1, 3, 3, 3, 4, 4, 3, 1, 1, 1, 1, 3, 1, 1, 1],
       [3, 1, 3, 1, 2, 2, 4, 2, 3, 1, 4, 3, 4, 3, 2, 2, 3, 2, 1, 3],
       [1, 3, 1, 1, 3, 3, 4, 3, 3, 1, 4, 2, 1, 4, 1, 2, 2, 1, 1, 1],
       [4, 3, 4, 2, 3, 1, 1, 4, 4, 2, 2, 2, 4, 3, 4, 4, 3, 2, 2, 2],
       [4, 3, 2, 2, 3, 2, 2, 4, 4, 4, 4, 1, 4, 4, 4, 1, 2, 3, 1, 2],
       [4, 1, 2, 1, 1, 4, 2, 1, 1, 4, 3, 1, 2, 3, 4, 3, 1, 3, 4, 1],
       [4, 2, 4, 3, 3, 4, 2, 1, 1, 3, 2, 3, 3, 2, 2, 4, 2, 3, 1, 1],
       [4, 1, 2, 2, 1, 2, 1, 3, 3, 1, 2, 4, 1, 2, 4, 4, 2, 1, 4, 3],
       [3, 4, 3, 1, 3, 3, 3, 2, 1, 3, 3, 2, 2, 4, 2, 2, 4, 4, 2, 2],
       [1, 2, 1, 2, 4, 4, 1, 3, 1, 3, 1, 3, 3, 2, 1, 2, 3, 2, 4, 3],
       [1, 2, 1, 3, 3, 1, 2, 4, 2, 1, 3, 2, 3, 4, 4, 2, 4, 4, 1, 2],
       [4, 1, 3, 3, 2, 2, 3, 3, 3, 4, 3, 1, 4, 4, 1, 2, 2, 3, 1, 3],
       [4, 3, 4, 2, 3, 2, 2, 1, 2, 4, 1, 3, 4, 1, 1, 2, 3, 3, 1, 3],
       [1, 3, 4, 1, 3, 3, 2, 2, 3, 2, 3, 1, 2, 2, 1, 1, 3, 1, 1, 4],
       [2, 3, 2, 2, 2, 3, 2, 2, 2, 4, 2, 3, 4, 1, 3, 3, 3, 3, 2, 4],
       [3, 3, 4, 1, 3, 4, 4, 3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 1, 4, 2],
       [4, 1, 4, 3, 2, 4, 2, 1, 2, 2, 3, 3, 1, 4, 1, 3, 2, 1, 3, 3],
       [4, 3, 2, 3, 2, 2, 2, 1, 3, 1, 1, 1, 1, 1, 4, 3, 2, 1, 4, 2]]
col, row = len(lis), len(lis[0])
copy_lis = [[0 for i in range(col)] for j in range(row)]


class blocks:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.if_checked = False


for i in range(col):
    for j in range(row):
        block = blocks(i, j, lis[i][j])
        copy_lis[i][j] = block


def find_point(x, y, num, lis_0, need_to_clear):
    if x < 0 or x > (col - 1) or y < 0 or y > (row - 1):
        return
    if lis_0[x][y].if_checked == True:
        return
    if lis_0[x][y].num == 0:
        return need_to_clear
    if lis_0[x][y].num == num and lis_0[x][y].if_checked == False:
        lis_0[x][y].if_checked = True
        need_to_clear.append((x, y))
        find_point(x + 1, y, num, lis_0, need_to_clear)
        find_point(x - 1, y, num, lis_0, need_to_clear)
        find_point(x, y + 1, num, lis_0, need_to_clear)
        find_point(x, y - 1, num, lis_0, need_to_clear)
    return need_to_clear


def find(x, y, num, lis):
    need_to_clear_ = []
    for i in range(col):
        for j in range(row):
            lis[i][j].if_checked = False
    list_1 = find_point(x, y, num, lis, need_to_clear_)
    if len(list_1) > 0:
        return list_1
    return []


def update(lis, x, y):
    need_to_clear = find(x, y, lis[x][y].num, lis)
    # print(need_to_clear)
    if (len(need_to_clear) == 1):
        return lis
    for i in range(col):
        for j in range(row):
            if (i, j) in need_to_clear:
                lis[i][j].num = 0
                lis[i][j].if_checked = False
    for i in range(col - 1, -1, -1):
        for j in range(row):
            if (lis[i][j].num == 0):  # 如果为0，则开始下降
                for k in range(i - 1, -1, -1):
                    if (lis[k][j].num != 0):
                        lis[i][j], lis[k][j] = lis[k][j], lis[i][j]
                        break
    return lis


def sum_lis(lis_1):
    sum = 0
    for i in range(col):
        for j in range(row):
            if (lis_1[i][j].num != 0):
                sum += 1
    return sum


def find_all_point(lis):
    dir = {}
    k = 0
    need_to_clear_list_ = []
    for i in range(col):
        for j in range(row):
            if (lis[i][j].x, lis[i][j].y) not in need_to_clear_list_:
                clear_list = find(i, j, lis[i][j].num, lis)
                if len(clear_list) == 0:
                    continue
                if len(clear_list) == 1:
                    clear_list.clear()
                    continue
                for j in clear_list:
                    need_to_clear_list_.append(j)
                dir[str(k)] = clear_list[0]
                k += 1
                clear_list.clear()
    # 随机打乱
    dir = dict(sorted(dir.items(), key=lambda x: random.random()))
    return dir


def alpha(map, map_sum, points, click_points):
    minValue = map_sum
    best_click_points = click_points[:]
    for point in points:
        x, y = points[point][0], points[point][1]
        new_click_points = click_points + [(x, y)]
        update_map = update(map, x, y)
        next_points = find_all_point(update_map)
        next_map_sum = sum_lis(update_map)
        childValue, next_click_points = alpha(update_map, next_map_sum, next_points, new_click_points)
        if childValue < minValue:
            minValue = childValue
            best_click_points = next_click_points
        if childValue >= minValue:
            break
    return minValue, best_click_points


click_points = []
start_time = time.time()
mix_V, mix_m = alpha(copy_lis, sum_lis(copy_lis), find_all_point(copy_lis), click_points)
print(f"地图大小:{col}×{row}")
print("最优值:", mix_V)
print("最优解:", mix_m)
