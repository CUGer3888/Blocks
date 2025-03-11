import copy
from collections import deque

# 全局配置
NUM = 5  # 数值种类数


def calculate_click_reward(count):
    """计算点击区域的得分"""
    return {2: 20, 3: 45}.get(count, count ** 2 * 5) if count >= 2 else 0


def calculate_remain_reward(grid):
    """计算剩余区域的预期得分"""
    counts = [0]*(NUM + 1)  # 索引0保留，统计1-NUM的数值
    for row in grid:
        for val in row:
            if 1 <= val <= NUM:
                counts[val] += 1
    return sum(v ** 2 * 5 for v in counts)


def update_grid(grid, point):
    """更新网格并返回新状态和得分"""
    x, y = point
    n = len(grid)
    if not (0 <= x < n and 0 <= y < n) or grid[x][y] == 0:
        return 0, copy.deepcopy(grid)

    target = grid[x][y]
    new_grid = copy.deepcopy(grid)
    q = deque([(x, y)])
    new_grid[x][y] = 0
    count = 1

    # BFS处理连通区域
    while q:
        cx, cy = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and new_grid[nx][ny] == target:
                new_grid[nx][ny] = 0
                count += 1
                q.append((nx, ny))

    if count == 1:
        return 0, grid

    # 对地图进行下降
    for j in range(n):
        for i in range(n - 1, 0, -1):
            if new_grid[i][j] == 0:
                for k in range(i - 1, -1, -1):
                    if new_grid[k][j] != 0:
                        new_grid[i][j], new_grid[k][j] = new_grid[k][j], new_grid[i][j]
                        break

    # 检查最后一行，如果是0，则将其与右边的所有列整体交换，移到最后一列
    for i in range(n):
        if new_grid[n - 1][i] == 0:
            for j in range(i + 1, n):
                if new_grid[n - 1][j] != 0:
                    new_grid[n - 1][i], new_grid[n - 1][j] = new_grid[n - 1][j], new_grid[n - 1][i]
                    break


    return count, new_grid


def find_valid_blocks(grid):
    """查找所有有效可点击区域"""
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    valid_points = []

    def bfs(start_x, start_y):
        """BFS检测连通区域"""
        q = deque([(start_x, start_y)])
        visited[start_x][start_y] = True
        size = 1
        target = grid[start_x][start_y]

        while q:
            x, y = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == target:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    size += 1
        return size

    # 遍历所有可能的数值
    for val in range(1, NUM + 1):
        for i in range(n):
            for j in range(n):
                if grid[i][j] == val and not visited[i][j]:
                    if bfs(i, j) >= 2:
                        valid_points.append((i, j))

    return valid_points


def optimize_clicks(initial_grid):
    """主优化函数，返回 (总得分, 点击步骤)"""
    current_grid = copy.deepcopy(initial_grid)
    total_score = 0
    click_steps = []

    while True:
        candidates = find_valid_blocks(current_grid)
        if not candidates:
            break

        best_score = -1
        best_reward = 0
        best_next_grid = current_grid
        best_point = None

        for point in candidates:
            count, new_grid = update_grid(current_grid, point)
            current_reward = calculate_click_reward(count)
            future_reward = calculate_remain_reward(new_grid)

            total_evaluation = current_reward + future_reward

            if total_evaluation > best_score:
                best_score = total_evaluation
                best_reward = current_reward
                best_next_grid = new_grid
                best_point = point

        if best_point is None:
            break

        total_score += best_reward
        click_steps.append(best_point)
        current_grid = best_next_grid

    return total_score, click_steps
from sum import one
# 使用示例
import time
while True:
    grid_example = one()


    score, steps = optimize_clicks(grid_example)
    if 100<score and score<500:
        print("分数过低，重新生成")
        time.sleep(5)
        continue
    print(f"总得分: {score}")
    print("最优点击路径:")
    for step, (x, y) in enumerate(steps, 1):
        print(f"步骤{step}: 点击 ({x}, {y})")
    map_ = grid_example
    for s in steps:
        map_ = update_grid(map_, s)[1]
    print(map_)

    start_x = 32
    start_y = 302
    step = 57
    import time
    import pyautogui
    for step, (x, y) in enumerate(steps, 1):
        pyautogui.moveTo(start_x + y * 57, start_y + x * 57)
        pyautogui.click()
        time.sleep(1.8)
    time.sleep(10)
""" 8个，奖励720，7个1020
测试，玩十局，看能不能到20000分，添加函数，统计最优地图，若
"""