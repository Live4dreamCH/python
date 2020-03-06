import numpy as np
import matplotlib.pyplot as plt
import random
import math

# 1:
    # M = np.array([[1, 1 / 2], [0, 1 / 2]])
    # print("矩阵:\n", M)
    # e, P = np.linalg.eig(M)
    # print("特征值：\n", e)
    # print("特征矩阵：\n", P)
    # Pdiv = np.linalg.inv(P)
    # print("特征矩阵的逆：\n", P)

# 2:
    # x0 = np.array([[0.2], [0.3], [0.5]])
    # M = np.array([[1, 1 / 2, 0], [0, 1 / 2, 1], [0, 0, 0]])
    # print(M)
    # t, P = np.linalg.eig(M)
    # print(t)
    # print(P)
    # Pinv = np.linalg.inv(P)
    # print(Pinv)

    # D = np.zeros((3, 3))
    # for i, n in enumerate(t):
    #     D[i][i] = n ** 1000
    # print(D)

    # xn = P @ D @ Pinv @ x0
    # np.set_printoptions(precision=3)  # 设置输出的精度
    # np.set_printoptions(suppress=True)  # 抑制使用对小数的科学记数法
    # print(xn)

    # print(P @ D @ Pinv)

# 3:
    # M = np.array([[1, 1 / 2], [0, 1 / 2]])
    # D = np.array([[1, 0], [0, 0.5]])
    # e, P = np.linalg.eig(M)
    # Pinv = np.linalg.inv(P)
    # M = P @ D @ Pinv
    # print(M)

# 4:
    # a_0 = 0.33
    # b_0 = 0.33
    # c_0 = 0.34
    # N = []
    # A = []
    # B = []
    # C = [c_0]
    # for n in range(0, 100):
    #     N.append(n/10)
    #     A.append((a_0 + (1 - 0.5 ** (n/10)) * b_0) / (a_0 + b_0))
    #     B.append((0.5 ** (n/10) * b_0) / (a_0 + b_0))
    #     if n > 0:
    #         C.append(0)
    # plt.plot(N, A)
    # plt.plot(N, B)
    # plt.plot(N, C)
    # plt.legend(['AA','Aa',"aa"])
    # plt.show()
    # # a_0+(1-1/2^n )b_0 1/2^n  b_0

# 5:
    # # 1 3 2 4   44  0 2 1 3
    # M = [[12, 15, 8, 8], [20, 19, 10, 7], [15, 13, 9, 6], [18, 16, 12, 9]]
    # hour = 10000
    # which = [4, 4, 4, 4]
    # for i in range(0, 4):
    #     for j in range(0, 4):
    #         for k in range(0, 4):
    #             for l in range(0, 4):
    #                 if i + j + k + l != 6:
    #                     continue
    #                 if i == j or i == k or i == l or k == j:
    #                     continue
    #                 if i == 0 and j == 2 and k == 1 and l == 3:
    #                     print('wozai!')
    #                 t = M[0][i] + M[1][j] + M[2][k] + M[3][l]
    #                 if t < hour:
    #                     which = [i, j, k, l]
    #                     hour = t
    # print('hour=',hour,'which=',which)

# 6:
M =\
[[(4, 0, 0), (2, 2, 0), (0, 4, 0)],
[(2, 2, 0), (1, 2, 1), (0, 2, 2)],
[(0, 4, 0), (0, 2, 2), (0, 0, 4)]]
AA, Aa, aa = 60, 10, 30
an = [AA]
bn = [Aa]
cn = [aa]
people = [AA, AA + Aa, AA + Aa + aa]
print('generation=', 0, 'AA=', AA, 'Aa=', Aa, 'aa=', aa)
print('predict:AA=', round((AA + Aa / 2)** 2 / 100), 'Aa=', round(2*(AA + Aa / 2)*(Aa / 2 + aa) / 100), 'aa=', round((Aa / 2 + aa)** 2 / 100))
g=101
for generation in range(1, g):
    l = people[2]
    AA, Aa, aa = 0, 0, 0
    for i in np.linspace(0,l,100):
        if i <= people[0]:
            x = 0
        elif i <= people[1]:
            x = 1
        else:
            x = 2
        r = random.uniform(0, l)
        if r <= people[0]:
            y = 0
        elif r <= people[1]:
            y = 1
        else:
            y = 2
        for j in range(M[x][y][0]):
            AA += 1
        for j in range(M[x][y][1]):
            Aa += 1
        for j in range(M[x][y][2]):
            aa += 1
    AA = AA / 4
    Aa = Aa / 4
    aa = aa / 4
    people = [AA, AA + Aa, AA + Aa + aa]
    an.append(AA)
    bn.append(Aa)
    cn.append(aa)
    print('generation=', generation, 'AA=', AA, 'Aa=', Aa, 'aa=', aa)

x = np.arange(g)
plt.plot(x, an)
plt.plot(x, bn)
plt.plot(x, cn)
plt.show()
