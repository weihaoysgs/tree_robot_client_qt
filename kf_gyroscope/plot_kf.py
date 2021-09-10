# -*- coding:utf-8 -*-
'''
file    : plot_kf
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-09-06 23:39
IDE     : PyCharm
'''
import matplotlib.pyplot as plt
import numpy as np

# 创建噪声
NUM = 300
np.random.seed(4)
Noise = np.random.randn(NUM)  # 高斯分布随机噪声,服从 (0,1) 标准正态分布
Noise_std = np.random.randn(NUM)  # 测量噪声

X = [0] * NUM
Y = [0] * NUM

# 创建数据集
for i in range(1, NUM):
    X[i] = np.sin(0.2 * i)

Noise_std_ = np.square(np.var(Noise_std))     # 求噪声的方差
Noise_ = np.square(np.var(Noise))           # 测量噪声

P = [0] * NUM  # 每次的最优偏差
K = [0] * NUM  # 卡尔曼增益

S = X + Noise_std  # 测量值

for i in range(1, NUM):
    P[i] = np.square(P[i - 1]) + 0.1 * Noise_

    K[i] = 0.1 * np.sqrt(P[i] / (Noise_std_ + P[i]))

    Y[i] = Y[i - 1] + K[i] * (S[i] - Y[i - 1]) # 测量值减去上一个时刻的过滤后的数据

    P[i] = np.sqrt((1 - K[i]) * P[i])
    print(P[i])

plt.plot(X, color='r', label='数据集')
plt.plot(S, color='g', label='数据测量获取值（带噪声）')
plt.plot(Y, color='b', label='过滤后的数据')

plt.show()