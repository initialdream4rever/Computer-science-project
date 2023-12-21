import sympy as sp

m, g, R, M, I, k, t, VV, E0, r = sp.symbols('m, g, R, M, I, gamma t, omega, E0, r ')

y0, u, w = sp.symbols('y0, u, w ')  # y0=y center mass0, u-v center wheel0, w-m vel0

E0 = m * g * y0 + M * u ** 2 / 2 + I * u ** 2 / (2 * R ** 2) + m * w ** 2 / 2

fi0 = sp.symbols('varphi0')
fi = sp.symbols(r'\varphi')

exprg = m * r / ((M + m) * R)
E1 = m * g * (R + r)  # Wpm
E2 = (M * R ** 2 + I) * VV ** 2 / 2  # EM
E3 = m * (VV * (R + r)) ** 2 / 2  # Em
eqmin = sp.Eq(E1 + E2 + E3, E0).subs(k, exprg)
fidot = list(sp.solveset(eqmin, VV))[0]
an = ((VV ** 2 * k * R).subs(k, exprg)).subs(VV, fidot)
num1 = 25
num2 = 25
u1 = 2.5
u2 = 4
m1 = 5
m2 = 25
s = 0
t = 0
t0 = num1 * (u2 - u1) * num2 * (m2 - m1)
arrv = [0 for i in range(len(range(int(u1 * num1), int(u2 * num1), 1)) * len(range(int(m1 * num2), int(m2 * num2), 1)))]
arrm = [0 for i in range(len(range(int(u1 * num1), int(u2 * num1), 1)) * len(range(int(m1 * num2), int(m2 * num2), 1)))]
for un in range(int(u1 * num1), int(u2 * num1), 1):
    for mi in range(int(m1 * num2), int(m2 * num2), 1):  # numbers are boundaries in grams
        arr = [(M, 0.070), (R, 0.075), (r, 0.059), (m, (mi / num2) / 1000), (I, 2.15 * 10 ** -4), (g, 9.8),
               # system patameters
               (y0, 0.016), (u, un / num1), (w, 0.21333 * un / num1), (fi0, 3.1415)]  # initial parameters
        # substitution
        t += 1
        if t % 1000 == 0:
            print(t, '/', t0)
        if 9.795 < an.subs(arr) < 9.805:
            arrv[s] = un / num1
            arrm[s] = (mi / num2) / 1000
            s += 1
import matplotlib.pyplot as plt

plt.grid()
plt.ylim(5, 25)
plt.xlim(2.5, 4)
# plt.title('phase diagram')
plt.ylabel('attached mass, g')
plt.xlabel('initial velocity, m/s')
plt.plot([i for i in arrv if i != 0], [1000 * i for i in arrm if i != 0])
plt.show()
