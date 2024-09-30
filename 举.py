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

    def copy(lis_0, lis_1):
        lis_1 = [[0 for i in range(col)] for j in range(row)]
        for i in range(col):
            for j in range(row):
                block = blocks(i, j, lis_0[i][j])
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

    def sum_lis(lis_1):
        sum = 0
        for i in range(col):
            for j in range(row):
                if (lis_1[i][j].num != 0):
                    sum += 1
        return sum

    def data(list, x, y):
        clear_list = find(x, y, list[x][y].num, list)
        update(list, clear_list)
        return list, sum_lis(list)

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
        return dir

    dir_1 = find_all_point(lis_1)

    def deep_copy(lis_0):
        return [[blocks(i, j, lis_0[i][j]) for j in range(col)] for i in range(row)]

    # sum_dir = {}

    def one_update(lis_1, dir_1, name):
        list_ = [[lis_1[i][j].num for j in range(col)] for i in range(row)]
        global start
        for i in dir_1:
            x, y = dir_1[i][0], dir_1[i][1]
            lis_1 = deep_copy(list_)
            tmp_lis, tmp_sum = data(lis_1, x, y)
            tmp_list = [[tmp_lis[i][j].num for j in range(col)] for i in range(row)]
            tmp_lis = deep_copy(tmp_list)
            dir = find_all_point(tmp_lis)
            string_ = str(name) + "(" + str(dir_1[i][0]) + "," + str(dir_1[i][1]) + ")" + "->"
            f.write(string_ + "^" + str(tmp_sum) + "\n")
            # sum_dir[string_] = tmp_sum
            tim = time.time()

            # 每隔10秒输出一个数字
            if tim - start > 1:
                print("3s")
                f.close()
                print_1()
                exit()

            if len(dir) == 0:
                pass
            else:
                one_update(tmp_lis, dir, string_)

    one_update(lis_1, dir_1, "0")
    # sorted(sum_dir.items(), key=lambda x: x[1], reverse=True)
    # min_key = min(sum_dir, key=sum_dir.get)
    # print(min_key, sum_dir[min_key])

# lis =[[1,1,1,4,3,2,2,4,1,1],
# [1,2,3,2,2,3,3,4,3,4],
# [2,4,4,4,4,1,3,4,3,2],
# [1,3,3,2,1,4,3,2,4,2],
# [4,4,4,3,4,3,1,2,4,3],
# [4,3,1,2,2,2,2,3,4,2],
# [2,2,1,3,2,4,1,4,2,1],
# [3,2,1,3,2,3,4,1,3,2],
# [2,4,2,3,1,4,1,1,4,2],
# [1,3,1,4,4,4,1,1,3,2]
# ]
lis = [[1,2,3],
       [2,1,1],
       [2,3,1]]

# lis = [[3, 1, 2, 2, 1, 4, 1, 1, 4, 2],
#        [2, 1, 1, 1, 4, 4, 2, 4, 4, 3],
#        [2, 1, 1, 2, 4, 1, 2, 2, 4, 1],
#        [3, 3, 2, 3, 3, 3, 1, 1, 1, 2],
#        [3, 1, 4, 2, 1, 2, 3, 2, 1, 2],
#        [1, 2, 2, 4, 4, 4, 4, 4, 1, 2],
#        [1, 1, 3, 3, 4, 3, 1, 3, 3, 1],
#        [2, 3, 2, 4, 1, 4, 2, 4, 2, 2],
#        [3, 3, 1, 4, 1, 4, 1, 3, 4, 1],
#        [2, 4, 3, 4, 3, 1, 3, 2, 3, 2]]
# 9
# lis = [[3, 1, 2, 2, 1, 4, 1, 1, 4],
#        [2, 1, 1, 1, 4, 4, 2, 4, 4],
#        [2, 1, 1, 2, 4, 1, 2, 2, 4],
#        [3, 3, 2, 3, 3, 3, 1, 1, 1],
#        [3, 1, 4, 2, 1, 2, 3, 2, 1],
#        [1, 2, 2, 4, 4, 4, 4, 4, 1],
#        [1, 1, 3, 3, 4, 3, 1, 3, 3],
#        [2, 3, 2, 4, 1, 4, 2, 4, 2],
#        [3, 3, 1, 4, 1, 4, 1, 3, 4]]
# 8
# lis = [[3,4,4,2,3,3,4,4,3,2],
# [2,1,1,3,4,1,1,2,1,3],
# [3,2,3,4,1,3,2,2,2,1],
# [1,3,4,2,3,2,4,3,1,4],
# [4,2,2,4,4,4,2,4,3,1],
# [4,2,3,4,1,3,4,2,2,1],
# [2,1,2,3,2,1,3,1,2,1],
# [3,1,2,2,4,1,2,1,4,2],
# [1,2,2,1,4,1,1,3,4,4],
# [4,2,4,1,2,2,2,1,3,1],
# ]

# 7
# lis = [[3, 1, 2, 2, 1, 4, 1],
#        [2, 1, 1, 1, 4, 4, 2],
#        [2, 1, 1, 2, 4, 1, 2],
#        [3, 3, 2, 3, 3, 3, 1],
#        [3, 1, 4, 2, 1, 2, 3],
#        [1, 2, 2, 4, 4, 4, 4],
#        [1, 1, 3, 3, 4, 3, 1]]
# 6
# lis = [[3, 1, 2, 2, 1, 4],
#        [2, 1, 1, 1, 4, 4],
#        [2, 1, 1, 2, 4, 1],
#        [3, 3, 2, 3, 3, 3],
#        [3, 1, 4, 2, 1, 2],
#        [1, 2, 2, 4, 4, 4]]
# 5
# lis = [[3, 1, 2, 2, 1],
#        [2, 1, 1, 1, 4],
#        [2, 1, 1, 2, 4],
#        [3, 3, 2, 3, 3],
#        [3, 1, 4, 2, 1]]
# lis = [[3, 1, 2, 2],
#        [2, 1, 1, 1],
#        [2, 1, 1, 2],
#        [3, 3, 2, 3]]
# lis = [[3, 1, 2],
#        [2, 1, 1],
#        [2, 1, 1]]
# lis = [[3, 1],
#        [2, 1]]
# lis = [[3]]

def print_1():
    with open("10.txt", "r") as f:
        lines = f.readlines()
    start_j = 0
    for i in range(len(lines)):
        x, y = lines[i].split("^")[0], lines[i].split("^")[1]
        if len(x) >= start_j:
            start_j = len(x)
            start_i = lines[i]
        if len(x) < start_j:
            break
    print("步骤：", start_i.split("->^")[0])
    print("结果", start_i.split("->^")[1])


def main(lis):
    qiongju(lis)


f = open("10.txt", "w")
# 添加一个计时功能
import time

start = time.time()
if __name__ == '__main__':
    start_time = time.time()
    main(lis)
    end_time = time.time()
    print("程序运行时间：", end_time - start_time, "秒")
f.close()
