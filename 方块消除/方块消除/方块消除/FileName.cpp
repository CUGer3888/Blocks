#include<stdio.h>
#include<graphics.h>
#include<time.h>
#include<math.h>
#include<stack>
#include "tools.h"
#include <mmsystem.h>//���ű������ֵ�ͷ�ļ�
#pragma comment(lib,"winmm.lib")//����������Ҫ�Ŀ��ļ�
#define WIDTH 580
#define HEIGHT 580
/// <summary>
/// 1.��ʼ������
/// 2.������ɷ���
/// 3.���
/// 4.�ж��Ƿ��������
/// 5.����
/// 6.��������
/// 7.���´���
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
			blocks[i][j].row = i;
			blocks[i][j].col = j;
			blocks[i][j].x = 44 + j * (Step_size - 1);
			blocks[i][j].y = 39 + i * (Step_size - 1);
			blocks[i][j].isChecked = false;
			blocks[i][j].tmd = 255;
		}
	}
}
void updateWindow() {
	BeginBatchDraw();
	putimage(0, 0, &bg);
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			if (blocks[i][j].type > 0 && !blocks[i][j].isChecked) {
				putimagePNG(44 + blocks[i][j].col * (Step_size - 1), 39 + blocks[i][j].row * (Step_size - 1), &block_[blocks[i][j].type - 1]);
			}
		}
	}
	EndBatchDraw();
}
void check(int x, int y, int type) {
	// ���߽�
	if (blocks[x][y].isChecked) return;
	if (x < 0 || x >= 10 || y < 0 || y >= 10) {
		return;
	}
	if (blocks[x][y].type == type && !blocks[x][y].isChecked) {
		blocks[x][y].isChecked = true;  // ���Ϊ�Ѽ��

		// �ݹ�ؼ���ϡ��¡������ĸ���������ڵ�
		check(x - 1, y, type);  // ��
		check(x + 1, y, type);  // ��
		check(x, y - 1, type);  // ��
		check(x, y + 1, type);  // ��
	}
}
void userClick() {
	ExMessage msg;
	if (peekmessage(&msg) && msg.message == WM_LBUTTONDOWN) {
		if (msg.x < off_x || msg.y < off_y) return;
		int col = (msg.x - off_x) / Step_size;
		int row = (msg.y - off_y) / Step_size;
		if (col < 0 || row < 0 || col > 10 || row > 10) return;
		printf("(%d,%d)\n", row, col);
		check(row, col, blocks[row][col].type);
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
	//����
	for (int i = 9; i >= 1; i--) {
		for (int j = 1; j <= 9; j++) {
			if (blocks[i][j].isChecked) {
				printf("������(%d,%d)", i, j);
			}
		}
	}
	for (int i = 9; i >= 1; i--) {
		for (int j = 1; j <= 9; j++) {
			if (blocks[i][j].isChecked) {
				for (int k = i - 1; k >= 1; k--) {
					if (!blocks[k][j].isChecked) {
						exchange(k, j, i, j);
						break;
					}

				}
			}
		}
	}
	//�����µķ�����и���
	int n = 0;
	for (int j = 1; j <= 9; j++) {

		for (int i = 9; i >= 1; i--) {
			if (blocks[i][j].isChecked) {
				blocks[i][j].type = 1 + rand() % 4;
				blocks[i][j].y = 39 + i * (Step_size - 1);
				n++;
				blocks[i][j].isChecked = false;
			}
		}
	}
}
int main(void) {
	init();
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			printf("%d,", blocks[i][j].type);
		}
		printf("\n");
	}
	updateWindow();
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