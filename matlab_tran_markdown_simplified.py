import os


Operator = ["+", "-", "*", "/", "(", ")", "^", "_"]  # 仅需要处理的操作符们
# + - 不用操作
# * 变成 ' \times '
# / 变成 \frac {} {}
# ^... 变成 ^{...}

an = input("")  # 输入

# 提取出空格并删除
an = an.replace(" ", "")

# 获取SPLIT数组，按照操作符拆分
tmp = ""
SPLIT = []
for x in an:
    if x in Operator:
        if tmp != "":
            SPLIT.append(tmp)
        SPLIT.append(x)
        tmp = ""
    else:
        tmp = tmp + (x)
if tmp != "":
    SPLIT.append(tmp)
    tmp = ""


def H(ch):
    """优先级"""
    if ch[-1] == "(":
        return 0
    if ch == "+" or ch == "-":
        return 1
    if ch == "*" or ch == "/":
        return 2
    if ch == "^" or ch == "_":
        return 3
    if ch == ")":
        return 4
    return -1


def OPE(Num1, Opt, Num2):
    """运算符转化"""
    if Opt == "*":
        return Num1 + " \\times " + Num2
    if Opt == "/":
        return "{\\frac{" + Num1 + "}{" + Num2 + "}}"
    if Opt == "^":
        if Num2 == "({\\frac{1}{2}})":
            return "\sqrt{" + Num1 + "}"
        else:
            return "{" + Num1 + "}^{" + Num2 + "}"
    if Opt == "_":
        return "{" + Num1 + "}_{" + Num2 + "}"
    return Num1 + Opt + Num2


OptStk = []
NumStk = []


def DO():
    a = NumStk[-1]
    NumStk.pop()
    b = NumStk[-1]
    NumStk.pop()
    c = OptStk[-1]
    OptStk.pop()
    New_Number = OPE(b, c, a)
    NumStk.append(New_Number)


# 将SPLIT数组转换为markdown语言

for x in SPLIT:
    if H(x) == -1:
        NumStk.append(x)
    else:
        if H(x) == 0:
            OptStk.append(x)
            continue
        if H(x) == 4:
            while H(OptStk[-1]) != 0:
                DO()
            NumStk[-1] = OptStk[-1] + NumStk[-1] + ")"
            OptStk.pop()
            continue
        while 1:
            if len(OptStk) == 0:
                break
            if H(OptStk[-1]) < H(x):
                break
            DO()
        OptStk.append(x)

while len(OptStk) != 0:
    DO()
ans = "$$ " + NumStk[-1] + " $$"

print(ans)
