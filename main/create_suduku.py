import imp
from tkinter.messagebox import NO
import numpy as np
import random
import math

from sqlalchemy import null

def create_sudu(difficulty):  # 用于产生数独答案
    shudu = np.zeros((9, 9), dtype=int)  # 产生全0数组备用
    while (sum(sum(shudu[:, :])) != 405):  # 判断数独答案是否正确，简单了点，但很实用
        n = 1
        A = np.zeros((9, 9), dtype=int)
        a = [x for x in range(1, 10)]  # 产生1-9数组备用
        b = [x for x in range(1, 10)]
        random.shuffle(b)  # 产生随机1-9数组，作为数独第一行
        A[0, :] = b  # 赋值
        for i in range(1, 9):  # 开始填数
            for j in range(0, 9):
                x = A[i, :]  # 取出所在行
                y = A[:, j]  # 取出所在列
                if 0 <= j and j < 3:
                    z = A[:, 0:3]
                elif 3 <= j and j < 6:
                    z = A[:, 3:6]
                else:
                    z = A[:, 6:9]
                if 0 <= i and i < 3:
                    z = z[0:3, :]
                elif 3 <= i and i < 6:
                    z = z[3:6, :]
                else:
                    z = z[6:9, :]  # 取出所在宫

                x_pos = np.nonzero(x)[0]  # 取出行，列，宫的所有非零值
                X = np.zeros((len(x_pos)), dtype=int)
                for p in range(0, len(x_pos)):
                    X[p] = x[x_pos[p]]

                y_pos = np.nonzero(y)[0]
                Y = np.zeros((len(y_pos)), dtype=int)
                for p in range(0, len(y_pos)):
                    Y[p] = y[y_pos[p]]

                z_pos = np.transpose(np.nonzero(z))
                Z = np.zeros((len(z_pos)), dtype=int)
                for p in range(0, len(z_pos)):
                    m = z_pos[p, 0]
                    n = z_pos[p, 1]
                    Z[p] = z[m, n]

                t = list(set(X).union(set(Y)))
                t = list(set(t).union(set(Z)))  # 所有非零值取并集，

                n = list(set(a).difference(set(t)))  # 并集和a取差集，判断哪些数还可以填

                try:
                    L = len(n)  # 判断是否还有备选数
                except BaseException as e:
                    L = 0
                r = random.random()
                h = math.ceil(r * L)  # 备选数中随机选择一个
                try:
                    A[i, j] = n[h - 1]  # 进行赋值
                except BaseException as e:
                    n = 2  # 报错则说明之前的填数有误
                    break
            if n == 2:
                break
        if n == 2:
            continue  # 重新开始循环
        shudu = A  # 81个数全部正确，则赋值
        
    # print(shudu)

    for k in range(0, 9):
        b = [x for x in range(0, 9)]
        random.shuffle(b)
        for m in range(0, difficulty):
            shudu[k, b[m]] = 0

    shudu = np.squeeze(shudu.reshape((1, -1))).tolist()

    for i in range(81):
        if(shudu[i] == 0):
            shudu[i] = ""

    # print(shudu)

    return shudu

if __name__ == "__main__":
    print(create_sudu(4))
    

