
#include<stdio.h>
#include<graphics.h>
#include<time.h>
#include<math.h>
#include<stack>
#include "tools.h"
#include <mmsystem.h>//播放背景音乐的头文件
#pragma comment(lib,"winmm.lib")//播放音乐需要的库文件
#include <graphics.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define WIDTH 800
#define HEIGHT 600
#define NUM_BLOCKS 10
#define BLOCK_TYPES 4
#define BLOCK_SIZE 40
#define BLOCK_STEP 42
#define OFFSET_X 45
#define OFFSET_Y 39

typedef struct {
	int type;
	int row, col;
	int x, y;
	bool isChecked;
} Block;

Block blocks[NUM_BLOCKS][NUM_BLOCKS];
IMAGE bg, blockImages[BLOCK_TYPES];

void loadResources() {
	initgraph(WIDTH, HEIGHT);
	loadimage(&bg, "res/bg_2.png");

	char name[64];
	for (int i = 0; i < BLOCK_TYPES; i++) {
		sprintf_s(name, "res/%d.png", i + 1);
		loadimage(&blockImages[i], name, BLOCK_SIZE, BLOCK_SIZE, true);
	}
}

void initBlocks() {
	srand(time(NULL));
	for (int i = 0; i < NUM_BLOCKS; i++) {
		for (int j = 0; j < NUM_BLOCKS; j++) {
			blocks[i][j].type = 1 + rand() % BLOCK_TYPES;
			blocks[i][j].row = i;
			blocks[i][j].col = j;
			blocks[i][j].x = OFFSET_X + j * (BLOCK_STEP - 1);
			blocks[i][j].y = OFFSET_Y + i * (BLOCK_STEP - 1);
			blocks[i][j].isChecked = false;
		}
	}
}

void drawBackground() {
	putimage(0, 0, &bg);
}

void drawBlocks() {
	for (int i = 0; i < NUM_BLOCKS; i++) {
		for (int j = 0; j < NUM_BLOCKS; j++) {
			if (blocks[i][j].type > 0 && !blocks[i][j].isChecked) {
				putimagePNG(blocks[i][j].x, blocks[i][j].y, &blockImages[blocks[i][j].type - 1]);
			}
		}
	}
}

void moveBlocks() {
	for (int i = 0; i < NUM_BLOCKS; i++) {
		for (int j = 0; j < NUM_BLOCKS; j++) {
			if (blocks[i][j].isChecked) {
				continue;
			}
			int x = OFFSET_X + blocks[i][j].col * (BLOCK_STEP - 1);
			int y = OFFSET_Y + blocks[i][j].row * (BLOCK_STEP - 1);

			blocks[i][j].x = x;
			blocks[i][j].y = y;
		}
	}
}

void checkForMatch(int x, int y, int type) {
	if (blocks[x][y].isChecked || x < 0 || y < 0 || x >= NUM_BLOCKS || y >= NUM_BLOCKS) {
		return;
	}
	if (blocks[x][y].type == type) {
		blocks[x][y].isChecked = true;
		checkForMatch(x - 1, y, type);
		checkForMatch(x + 1, y, type);
		checkForMatch(x, y - 1, type);
		checkForMatch(x, y + 1, type);
	}
}
void handleUserClick(ExMessage* msg) {
	int col = (msg->x - OFFSET_X) / BLOCK_STEP;
	int row = (msg->y - OFFSET_Y) / BLOCK_STEP;
	checkForMatch(row, col, blocks[row][col].type);
}
int* blockToIntPtr(Block* block) {
	return (int*)block;
}
void swap(Block& a, Block& b) {
	Block temp = a;
	int row = a.row;
	int row_1 = b.row;
	a = b;
	b = temp;
	a.row = row;
	b.row = row_1;
}
void updateGame() {
	// Drop blocks down
	for (int col = 0; col < NUM_BLOCKS; col++) {
		for (int row = NUM_BLOCKS - 1; row >= 0; row--) {
			if (blocks[row][col].isChecked) {
				int newRow = row;
				while (newRow > 0 && blocks[newRow - 1][col].type == 0) {
					swap(blocks[newRow][col], blocks[newRow - 1][col]);
					newRow--;
				}
			}
		}
	}
	// Generate new blocks
	for (int col = 0; col < NUM_BLOCKS; col++) {
		for (int row = 0; row < NUM_BLOCKS; row++) {
			if (blocks[row][col].type == 0) {
				blocks[row][col].type = 1 + rand() % BLOCK_TYPES;
				blocks[row][col].isChecked = false;
			}
		}
	}
}

int main() {
	loadResources();
	initBlocks();

	ExMessage msg;
	while (true) {
		if (peekmessage(&msg)) {
			if (msg.message == WM_LBUTTONDOWN) {
				handleUserClick(&msg);
			}
		}
		BeginBatchDraw();
		drawBackground();
		drawBlocks();
		updateGame();
		EndBatchDraw();
		Sleep(10);
	}

	system("pause");
	return 0;
}