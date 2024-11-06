# import numpy as np
# import random
#
#
# # 定义迷宫环境
# class Maze:
#     def __init__(self):
#         self.state_space = [(i, j) for i in range(4) for j in range(4)]
#         self.action_space = ['up', 'down', 'left', 'right']
#         self.terminal_states = [(3, 3)]
#         self.reward_map = {(3, 3): 1}
#         self.reset()
#
#     def reset(self):
#         self.current_state = (0, 0)
#         return self.current_state
#
#     def step(self, action):
#         x, y = self.current_state
#         if action == 'up':
#             x = max(0, x - 1)
#         elif action == 'down':
#             x = min(3, x + 1)
#         elif action == 'left':
#             y = max(0, y - 1)
#         elif action == 'right':
#             y = min(3, y + 1)
#         self.current_state = (x, y)
#         reward = self.reward_map.get(self.current_state, -0.1)
#         done = self.current_state in self.terminal_states
#         return self.current_state, reward, done
#
#
# # 定义 Q-Learning 算法
# def q_learning(env, num_episodes=500, alpha=0.1, gamma=0.99, epsilon=0.1):
#     q_table = {(s, a): 0 for s in env.state_space for a in env.action_space}
#     for episode in range(num_episodes):
#         state = env.reset()
#         while True:
#             if random.uniform(0, 1) < epsilon:
#                 action = random.choice(env.action_space)
#             else:
#                 action = max(env.action_space, key=lambda a: q_table[(state, a)])
#
#             next_state, reward, done = env.step(action)
#             best_next_action = max(env.action_space, key=lambda a: q_table[(next_state, a)])
#             td_target = reward + gamma * q_table[(next_state, best_next_action)]
#             q_table[(state, action)] += alpha * (td_target - q_table[(state, action)])
#
#             state = next_state
#
#             if done:
#                 break
#
#     return q_table
#
#
# # 训练 Q-Learning 模型
# env = Maze()
# q_table = q_learning(env)
#
# # 使用训练好的 Q 表进行路径规划
# state = env.reset()
# steps = [state]
# while state != (3, 3):
#     action = max(env.action_space, key=lambda a: q_table[(state, a)])
#     state, _, _ = env.step(action)
#     steps.append(state)
#
# print("Optimal Path:", steps)

import keyboard
while True:
    #如果按下q键，则退出循环
    if keyboard.is_pressed('q'):
        break