#include<stdio.h>
#include<graphics.h>
#include<time.h>
#include<math.h>
#include<stack>
#include "tools.h"
#include <mmsystem.h>//播放背景音乐的头文件
#pragma comment(lib,"winmm.lib")//播放音乐需要的库文件
#define WIDTH 580
#define HEIGHT 580
/// <summary>
/// 1.初始化窗口
/// 2.随机生成方块
/// 3.点击
/// 4.判断是否可以消除
/// 5.消除
/// 6.方块下落
/// 7.更新窗口
/// </summary>
IMAGE block_[4];
IMAGE bg;
int time_ = 0;
int Step_size = 42;
int off_x = 45;
int off_y = 39;
struct block {
	int row;
	int col;
	int type;
	int x, y;
	bool isChecked;
	int tmd;

};
struct block blocks[10][10];
void init() {
	initgraph(WIDTH, HEIGHT);
	loadimage(&bg, "res/bg_2.png");

	char name[64];
	for (int i = 0; i < 4; i++) {
		sprintf_s(name, "res/%d.png", i + 1);
		loadimage(&block_[i], name, 40, 40, true);
	}

	srand(time(NULL));
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			blocks[i][j].type = 1 + rand() % 4;
			blocks[i][j].row = i;//行
			blocks[i][j].col = j;//列
			blocks[i][j].x = 44 + j * (Step_size - 1);//向左横坐标
			blocks[i][j].y = 39 + i * (Step_size - 1);//向上纵坐标
			blocks[i][j].isChecked = false;//未被点击
			blocks[i][j].tmd = 255;//透明度
		}
	}
}
void updateWindow() {
	BeginBatchDraw();
	putimage(0, 0, &bg);
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			if (blocks[i][j].type > 0 && !blocks[i][j].isChecked) {//类别大于0且未被点击
				putimagePNG(44 + blocks[i][j].col * (Step_size - 1), 39 + blocks[i][j].row * (Step_size - 1), &block_[blocks[i][j].type - 1]);//图片初始化
			}
		}
	}
	EndBatchDraw();
}
void check(int x, int y, int type) {
	// 检查边界
	if (blocks[x][y].isChecked) {
		return;
	}
	else if (x < 0 || x >= 10 || y < 0 || y >= 10) {
		return;
	}
	else if (blocks[x][y].type == type && !blocks[x][y].isChecked) {
		blocks[x][y].isChecked = true;  // 标记为已检查

		// 递归地检查上、下、左、右四个方向的相邻点
		check(x - 1, y, type);  // 上
		check(x + 1, y, type);  // 下
		check(x, y - 1, type);  // 左
		check(x, y + 1, type);  // 右
	}
}
void userClick() {
	//用户点击操作
	ExMessage msg;
	if (peekmessage(&msg) && msg.message == WM_LBUTTONDOWN) {
		if (msg.x < off_x || msg.y < off_y) return;
		int col = (msg.x - off_x) / Step_size;
		int row = (msg.y - off_y) / Step_size;
		if (col < 0 || row < 0 || col > 10 || row > 10) return;
		printf("点击坐标：(%d,%d)\n", row, col);
		//检查该点，传入坐标和点的类型
		check(row, col, blocks[row][col].type);
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				if (blocks[i][j].isChecked) {
					printf("经过检查，被遍历的点：（%d,%d）", i, j);
				}
			}
			printf("\n");
		}
	}
}
void exchange(int row1, int col1, int row2, int col2) {
	struct block tmp = blocks[row1][col1];
	blocks[row1][col1] = blocks[row2][col2];
	blocks[row2][col2] = tmp;
	blocks[row1][col1].row = row1;
	blocks[row1][col1].col = col1;
	blocks[row2][col2].row = row2;
	blocks[row2][col2].col = col2;
}
void updateGame() {
	//降落
	for (int i = 9; i >= 0; i--) {
		for (int j = 0; j <= 9; j++) {
			if (blocks[i][j].isChecked) {
				for (int k = i - 1; k >= 0; k--) {
					if (!blocks[k][j].isChecked) {
						exchange(k, j, i, j);
						break;
					}

				}
			}
		}
	}

	////生成新的方块进行更新
	//int n = 0;
	//for (int j = 1; j <= 9; j++) {

	//	for (int i = 9; i >= 1; i--) {
	//		if (blocks[i][j].isChecked) {
	//			blocks[i][j].type = 1 + rand() % 4;
	//			blocks[i][j].y = 39 + i * (Step_size - 1);
	//			n++;
	//			blocks[i][j].isChecked = false;
	//		}
	//	}
	//}
}
int main(void) {
	//初始化
	init();
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			printf("%d,", blocks[i][j].type);
		}
		printf("\n");
	}
	//更新窗口
	updateWindow();
	//循环
	while (time_ < 100000) {
		userClick();

		updateGame();
		updateWindow();
		Sleep(10);
		time_++;
	}
	system("pause");
	return 0;
}
