from sympy import solve, symbols


def N_JFET(R_S, I_DSS, U_GSOFF, R_D, E, R_L, R_Glow, R_Ghigh = 1e12):
    # N-JFET
    # R_S = 120
    # I_DSS = 19.7e-3
    # U_GSOFF = -1.45

    # R_D = 1e3
    # E = 12

    U_G = E * R_Glow / (R_Glow + R_Ghigh)

    x, y = symbols("U_GSQ, I_DSQ")  # x=U_GSQ, y=I_DSQ
    a = solve([x + R_S * y - U_G, y - I_DSS * (1 - x / U_GSOFF) ** 2], [x, y])
    print(a)
    if a[0][1] < a[1][1]:
        U_GSQ = a[0][0]
        I_DSQ = a[0][1]
    else:
        U_GSQ = a[1][0]
        I_DSQ = a[1][1]
    print("U_GSQ=", U_GSQ, "I_DSQ=", I_DSQ)

    U_DSQ = E - I_DSQ * (R_D + R_S)
    if U_DSQ > U_GSQ - U_GSOFF:
        print("假设成立,U_DSQ=", U_DSQ)

        g_m = I_DSS * 2 / U_GSOFF * (U_GSQ / U_GSOFF - 1)
        print("g_m=", g_m)

        Au_共S极 = -1 * g_m * R_D * R_L / (R_D + R_L)
        print("Au_共S极(短接R_S)=", Au_共S极)
        print("r_i=", R_Ghigh * R_Glow / (R_Ghigh + R_Glow), "\tr_o=", R_D)

        # Au_共D极 = g_m * R_S
        # print("Au_共D极=", Au_共D极)
        Au_共D极 = g_m / (g_m + 1 / R_S + 1 / R_L)
        print("Au_共D极", Au_共D极)
        print(
            "r_i=", R_Ghigh * R_Glow / (R_Ghigh + R_Glow), "\tr_o=", 1 / (1 / R_S + g_m)
        )

        Au_共G极 = g_m * R_D * R_L / (R_D + R_L)
        print("Au_共G极", Au_共G极)
        print("r_i=", 1 / (1 / R_S + g_m), "\tr_o=", R_D)
    else:
        print("假设不成立,以上无效")


def N_MOSFET(R_S, R_Ghigh, R_Glow, K, U_GSTH, R_D, E, R_L):
    # N-MOSFET
    U_G = E * R_Glow / (R_Glow + R_Ghigh)

    x, y = symbols("U_GSQ, I_DSQ")  # x=U_GSQ, y=I_DSQ
    a = solve([x + R_S * y - U_G, y - K * (x - U_GSTH) ** 2], [x, y])
    print(a)
    if a[0][1] < a[1][1]:
        U_GSQ = a[0][0]
        I_DSQ = a[0][1]
    else:
        U_GSQ = a[1][0]
        I_DSQ = a[1][1]
    print("U_GSQ=", U_GSQ, "I_DSQ=", I_DSQ)

    U_DSQ = E - I_DSQ * (R_D + R_S)
    if U_DSQ > U_GSQ - U_GSTH:
        print("假设成立,U_DSQ=", U_DSQ)

        g_m = 2 * K * (U_GSQ - U_GSTH)
        print("g_m=", g_m)

        # Au_共S极 = -1 * g_m * R_D
        # print("Au_共S极", Au_共S极)
        Au_共S极 = -1 * g_m * R_D * R_L / (R_D + R_L)
        print("Au_共S极(短接R_S)=", Au_共S极)
        print("r_i=", R_Ghigh * R_Glow / (R_Ghigh + R_Glow), "\tr_o=", R_D)

        Au_共D极 = g_m / (g_m + 1 / R_S + 1 / R_L)
        print("Au_共D极", Au_共D极)
        print(
            "r_i=", R_Ghigh * R_Glow / (R_Ghigh + R_Glow), "\tr_o=", 1 / (1 / R_S + g_m)
        )

        Au_共G极 = g_m * R_D * R_L / (R_D + R_L)
        print("Au_共G极", Au_共G极)
        print("r_i=", 1 / (1 / R_S + g_m), "\tr_o=", R_D)
    else:
        print("假设不成立,以上无效")


# N_JFET(120, 19.7e-3, -1.45, 1e3, 12, 1e3, 1e6)  # S
# N_JFET(20e3, 1.6e-3, -2.0712, 0, 10, 100e3, 1e6, 1.2e6)  # D
# N_JFET()
# for i in range(1000):
#     R_S = 500 + 0.1 * i
# N_MOSFET(500, 3e6, 2e6, 0.0502, 2, 1.5e3, 10)
# N_MOSFET(1e3, 430e3, 1e6, 0.0502, 2, 0, 12, 1e3)  # D
# N_MOSFET(0.5e3, 400e3, 200e3, 0.0502, 2, 2e3, 12, 20e3)  # G
# N_MOSFET(225, 100e3, 100e3, 2.2, 3.695, 1e3, 10, 1e3)  # S,P-MOSFET
