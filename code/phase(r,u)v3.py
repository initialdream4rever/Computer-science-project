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
u1 = 2
u2 = 5
r1 = 1
r2 = 7
s = 0
t = 0
Rin = 0.075
t0 = num1 * (u2 - u1) * num2 * (r2 - r1)
arrv = [0 for i in range(len(range(int(u1 * num1), int(u2 * num1), 1)) * len(range(int(r1 * num2), int(r2 * num2), 1)))]
arrr = [0 for i in range(len(range(int(u1 * num1), int(u2 * num1), 1)) * len(range(int(r1 * num2), int(r2 * num2), 1)))]
for ui in range(int(u1 * num1), int(u2 * num1), 1):
    for ri in range(int(r1 * num2), int(r2 * num2), 1):
        p = (Rin - (ri / num2) / 100) / Rin
        arr = [(M, 0.070), (R, Rin), (r, (ri / num2) / 100), (m, 0.022), (I, 2.15 * 10 ** -4), (g, 9.8),
               # system patameters
               (y0, Rin - (ri / num2) / 100), (u, ui / num1), (w, (ui / num1) * p), (fi0, 3.1415)]  # initial parameters
        # substitution
        t += 1
        if t % 1000 == 0:
            print(t, '/', t0)
        if 9.79 < an.subs(arr) < 9.81:
            arrv[s] = ui / num1
            arrr[s] = (ri / num2) / 100
            s += 1

import matplotlib.pyplot as plt

plt.grid()
# plt.ylim(10, 30)
# plt.xlim(2.5,3)
# plt.title('phase diagram')
plt.ylabel('r, m')
plt.xlabel('initial velocity, m/s')
plt.plot([i for i in arrv if i !=0], [i for i in arrr if i !=0])
plt.show()