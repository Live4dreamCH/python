import numpy as np
import matplotlib.pyplot as plt

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
a_0 = 0.33
b_0 = 0.33
c_0 = 0.34
N = []
A = []
B = []
C = [c_0]
for n in range(0, 100):
    N.append(n/10)
    A.append((a_0 + (1 - 0.5 ** (n/10)) * b_0) / (a_0 + b_0))
    B.append((0.5 ** (n/10) * b_0) / (a_0 + b_0))
    if n > 0:
        C.append(0)
plt.plot(N, A)
plt.plot(N, B)
plt.plot(N, C)
plt.legend(['AA','Aa',"aa"])
plt.show()
# a_0+(1-1/2^n )b_0 1/2^n  b_0