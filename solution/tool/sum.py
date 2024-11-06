import cv2
from PIL import ImageGrab
import pyautogui
import numpy as np
import time

def get_color(x, y):
    # 截图
    screen = ImageGrab.grab()
    # 获取颜色
    color = screen.getpixel((x, y))
    return color


def color_distance(color1, color2):
    color1 = np.array(color1)
    color2 = np.array(color2)
    return np.sqrt(((color1 - color2) ** 2).sum())


color_lis = [(237, 108, 137), (115, 211, 254), (209, 113, 255), (134, 233, 93), (250, 203, 93)]
color_lis_np = np.array(color_lis)


def get_num(color):
    min_distance = float('inf')
    min_index = - 1
    for i, ref_color in enumerate(color_lis_np):
        dist = color_distance(color, ref_color)
        if dist < min_distance:
            min_distance = dist
            min_index = i
    if min_distance < 50:
        return min_index + 1
    return 6


start_x = 30
start_y = 260
step = 38
col = 10
row = 10
lis = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        color = get_color(start_x + j * step, start_y + i * step)
        # pyautogui.moveTo(start_x + j * step, start_y + i * step)
        num = get_num(color)
        lis[i][j] = num
        # time.sleep(0.1)

print("[")
for i in lis:
    print(i, end=",\n")
print("]")