import copy
import random

def qiongju(lis):
    col, row = len(lis), len(lis[0])
    lis_1 = [[0 for i in range(col)] for j in range(row)]

    class blocks:
        def __init__(self, x, y, num):
            self.x = x
            self.y = y
            self.num = num
            self.is_clear = False

    for i in range(col):
        for j in range(row):
            block = blocks(i, j, lis[i][j])
            lis_1[i][j] = block

    def copy(lis_0):
        lis_0_ = [[lis_0[i][j].num for j in range(col)] for i in range(row)]
        lis_1 = [[0 for i in range(col)] for j in range(row)]
        for i in range(col):
            for j in range(row):
                block = blocks(i, j, lis_0_[i][j])
                lis_1[i][j] = block
        return lis_1

    def find_point(x, y, num, lis_0, need_to_clear):
        if x < 0 or x > (col - 1) or y < 0 or y > (row - 1):
            return
        elif lis_0[x][y].is_clear == True:
            return
        elif lis_0[x][y].num == 0:
            return need_to_clear
        elif lis_0[x][y].num == num and lis_0[x][y].is_clear == False:
            lis_0[x][y].is_clear = True
            need_to_clear.append((x, y))
            find_point(x + 1, y, num, lis_0, need_to_clear)
            find_point(x - 1, y, num, lis_0, need_to_clear)
            find_point(x, y + 1, num, lis_0, need_to_clear)
            find_point(x, y - 1, num, lis_0, need_to_clear)
        return need_to_clear

    def find(x, y, num, lis):
        need_to_clear = []
        list_1 = find_point(x, y, num, lis, need_to_clear)
        if len(list_1) > 0:
            return list_1
        else:
            return []

    def update(lis_1, need_to_clear):
        if (len(need_to_clear) == 1):
            return
        for i in range(col):
            for j in range(row):
                if (i, j) in need_to_clear:
                    lis_1[i][j].num = 0
                    lis_1[i][j].is_clear = False
        for i in range(col - 1, -1, -1):
            for j in range(row):
                if (lis_1[i][j].num == 0):  # 如果为0，则开始下降
                    for k in range(i - 1, -1, -1):
                        if (lis_1[k][j].num != 0):
                            lis_1[i][j], lis_1[k][j] = lis_1[k][j], lis_1[i][j]
                            break

        need_to_clear.clear()

    def show(map):
        for i in range(col):
            for j in range(row):
                print(map[i][j].num, end=' ')
            print("\n")

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

    def deep_copy(lis_0):
        return [[blocks(i, j, lis_0[i][j]) for j in range(col)] for i in range(row)]

    def data(lis, x, y):
        lis_ = copy(lis)

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
        for j in range(row):
            if (lis[col-1][j].num == 6):
                lis[col-1][j].num = 0
                for i in range(col - 1, -1, -1):
                    for j in range(row):
                        if (lis[i][j].num == 0):  # 如果为0，则开始下降
                            for k in range(i - 1, -1, -1):
                                if (lis[k][j].num != 0):
                                    lis[i][j], lis[k][j] = lis[k][j], lis[i][j]
                                    break
        return lis, sum_lis(lis, lis_)

    def find_all_point(lis):
        dir = {}
        k = 0
        need_to_clear_list = []
        for i in range(col):
            for j in range(row):
                if (lis[i][j].x, lis[i][j].y) not in need_to_clear_list:
                    clear_list = find(i, j, lis[i][j].num, lis)
                    if len(clear_list) == 0:
                        continue
                    if len(clear_list) == 1:
                        clear_list.clear()
                        continue
                    for j in clear_list:
                        need_to_clear_list.append(j)
                    dir[str(k)] = clear_list[0]
                    k += 1
                    clear_list.clear()
            # 随机打乱
        dir = dict(sorted(dir.items(), key=lambda x: random.random()))
        return dir

    dir_1 = find_all_point(lis_1)

    # print(dir_1)

    # sum_dir = {}
    sums = 0
    target = 2000
    now_max = 0
    have_lis =[]
    def one_update(lis_1, dir_1, name, target,now_max):
        stack = [(lis_1, dir_1, name, 0)]
        start_time = time.time()
        while stack:

            lis, dir_, name, sums = stack.pop()

            list_ = [[lis[i][j].num for j in range(col)] for i in range(row)]

            for i in dir_:
                x, y = dir_[i][0], dir_[i][1]
                new_lis = deep_copy(list_)
                tmp_lis, tmp_sum = data(new_lis, x, y)
                new_sums = sums + tmp_sum
                end_time = time.time()
                if end_time - start_time > 10:
                    target-=10
                    print("t:",target)
                if new_sums >= target:
                    string_ = str(name) + "(" + str(dir_[i][0]) + "," + str(dir_[i][1]) + ")" + "->"
                    f.write(string_ + str(new_sums) + "\n")
                    print(new_sums)
                    print("over",target)
                    f.close()
                    with open("10.txt", "r") as file:
                        lines = file.readlines()
                    last_line = lines[-1]
                    print(last_line)
                    a = last_line[1:-7]
                    move_lis = a.split("->")
                    move_lis = [eval(i) for i in move_lis]
                    for i in range(len(move_lis)):
                        pyautogui.moveTo(start_x + move_lis[i][1] * step, start_y + move_lis[i][0] * step)
                        time.sleep(2)
                        pyautogui.click()
                    return
                if new_sums < target:
                    now_max = new_sums
                    if now_max not in have_lis:
                        have_lis.append(now_max)
                        a = have_lis
                        a.sort(reverse=True)
                        print("现在最大值是:",a[0])
                    tmp_list = [[tmp_lis[i][j].num for j in range(col)] for i in range(row)]
                    tmp_lis = deep_copy(tmp_list)
                    new_dir = find_all_point(tmp_lis)
                    string_ = str(name) + "(" + str(dir_[i][0]) + "," + str(dir_[i][1]) + ")" + "->"
                    f.write(string_ + str(new_sums) + "\n")
                    if new_dir:
                        stack.append((tmp_lis, new_dir, string_, new_sums))

    one_update(lis_1, dir_1, "0", target,now_max)
n = 0
lis =lis


def main(lis):
    qiongju(lis)


f = open("10.txt", "w")
# 添加一个计时功能
import time

if __name__ == '__main__':
    start_time = time.time()
    main(lis)
    end_time = time.time()
    print("程序运行时间：", end_time - start_time, "秒")