import copy
import time

lis = [
[4, 2, 4, 3, 4, 1, 4, 1, 1, 5],
[5, 2, 1, 2, 3, 3, 5, 3, 1, 2],
[1, 3, 5, 2, 1, 1, 3, 4, 3, 1],
[1, 4, 5, 1, 6, 5, 4, 5, 3, 1],
[2, 4, 5, 4, 5, 3, 5, 2, 2, 3],
[1, 2, 5, 5, 1, 5, 5, 3, 3, 3],
[2, 2, 2, 2, 1, 3, 5, 5, 6, 6],
[5, 5, 1, 4, 1, 2, 5, 3, 2, 2],
[4, 1, 3, 5, 2, 3, 4, 3, 3, 2],
[1, 1, 4, 4, 2, 3, 4, 4, 5, 2],
]
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


def show(map):
    for i in range(col):
        for j in range(row):
            print(map[i][j].num, end=' ')
        print("\n")


def find(x, y, num, lis):
    need_to_clear_ = []
    for i in range(col):
        for j in range(row):
            lis[i][j].if_checked = False
    list_1 = find_point(x, y, num, lis, need_to_clear_)
    if len(list_1) > 0:
        return list_1
    return []


# def sum_lis(lis_1):
#     sum = 0
#     for i in range(col):
#         for j in range(row):
#             if (lis_1[i][j].num != 0):
#                 sum += 1
#     return sum


def sum_lis(lis_1, lis_2):
    # get no 0 in lis_1
    sum_1 = 0
    sum_2 = 0
    for i in range(col):
        for j in range(row):
            if lis_1[i][j].num != 0:
                sum_1 += 1
            if lis_2[i][j].num != 0:
                sum_2 += 1
    sum = abs(sum_1 - sum_2)
    if sum == 0:
        return 0
    if sum == 2:
        return 20
    if sum == 3:
        return 45
    if sum > 3:
        return sum ** 2 * 5
    return sum


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

    for j in range(col):
        a = 0
        for i in range(row):
            if (lis[i][j].num == 0):
                a += 1
        if a == row:
            # 找到全为0的列
            found_zero_column = j
            # 检查右边是否还有列
            if found_zero_column < col - 1:
                for start in range(found_zero_column, col - 1):
                    for k in range(row):
                        lis[k][start].num = lis[k][start + 1].num
                # 将最右边的列设置为0
                for k in range(row):
                    lis[k][col - 1].num = 0
    return lis


import pyautogui

a = 0

start_x = 35
start_y = 248
step = 36
col = 10
row = 10
move_str = input("请输入移动的坐标，用->隔开，例如：0,0->1,0->2,0")
move_lis = move_str.split("->")
move_lis = [eval(i) for i in move_lis]
for i in range(len(move_lis)):
    pyautogui.moveTo(start_x + move_lis[i][1] * step, start_y + move_lis[i][0] * step)
    time.sleep(2)
    pyautogui.click()
#     copy_lis_ = copy.deepcopy(copy_lis)
#     copy_lis = update(copy_lis, move_lis[i][0], move_lis[i][1])
#     show(copy_lis)
#     print("------------------------")
#     a += sum_lis(copy_lis, copy_lis_)
# show(copy_lis)
# print(a)
