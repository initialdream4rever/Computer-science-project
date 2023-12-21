from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(252, 631)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.M = QtWidgets.QLineEdit(self.centralwidget)
        self.M.setGeometry(QtCore.QRect(10, 70, 171, 31))
        self.M.setObjectName("Mass")
        self.R = QtWidgets.QLineEdit(self.centralwidget)
        self.R.setGeometry(QtCore.QRect(10, 110, 171, 31))
        self.R.setObjectName("R")
        self.r = QtWidgets.QLineEdit(self.centralwidget)
        self.r.setGeometry(QtCore.QRect(10, 150, 171, 31))
        self.r.setObjectName("r")
        self.m = QtWidgets.QLineEdit(self.centralwidget)
        self.m.setGeometry(QtCore.QRect(10, 190, 171, 31))
        self.m.setObjectName("m")
        self.I = QtWidgets.QLineEdit(self.centralwidget)
        self.I.setGeometry(QtCore.QRect(10, 230, 171, 31))
        self.I.setObjectName("I")
        self.g = QtWidgets.QLineEdit(self.centralwidget)
        self.g.setGeometry(QtCore.QRect(10, 270, 171, 31))
        self.g.setObjectName("g")
        self.y0 = QtWidgets.QLineEdit(self.centralwidget)
        self.y0.setGeometry(QtCore.QRect(10, 310, 171, 31))
        self.y0.setObjectName("y0")
        self.u = QtWidgets.QLineEdit(self.centralwidget)
        self.u.setGeometry(QtCore.QRect(10, 350, 171, 31))
        self.u.setObjectName("u")
        self.w = QtWidgets.QLineEdit(self.centralwidget)
        self.w.setGeometry(QtCore.QRect(10, 390, 171, 31))
        self.w.setObjectName("w")
        self.fi0 = QtWidgets.QLineEdit(self.centralwidget)
        self.fi0.setGeometry(QtCore.QRect(10, 430, 171, 31))
        self.fi0.setObjectName("fi0")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 41, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 110, 41, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 150, 41, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 190, 41, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 230, 61, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 270, 51, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 310, 41, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 350, 41, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(190, 390, 41, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 430, 51, 31))
        self.label_11.setObjectName("label_11")
        self.push1 = QtWidgets.QPushButton(self.centralwidget)
        self.push1.setGeometry(QtCore.QRect(10, 480, 111, 41))
        self.push1.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.push1.setObjectName("push1")
        self.push2 = QtWidgets.QPushButton(self.centralwidget)
        self.push2.setGeometry(QtCore.QRect(130, 480, 111, 41))
        self.push2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.push2.setObjectName("push2")
        self.push3 = QtWidgets.QPushButton(self.centralwidget)
        self.push3.setGeometry(QtCore.QRect(10, 530, 111, 41))
        self.push3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.push3.setObjectName("push3")
        self.push4 = QtWidgets.QPushButton(self.centralwidget)
        self.push4.setGeometry(QtCore.QRect(130, 530, 111, 41))
        self.push4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.push4.setObjectName("push4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 51))
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 252, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rolling"))
        self.label_2.setText(_translate("MainWindow", "M, кг"))
        self.label_3.setText(_translate("MainWindow", "R, м"))
        self.label_4.setText(_translate("MainWindow", "r, м"))
        self.label_5.setText(_translate("MainWindow", "m, кг"))
        self.label_6.setText(_translate("MainWindow", "I, кг*м^2"))
        self.label_7.setText(_translate("MainWindow", "g, м/с^2"))
        self.label_8.setText(_translate("MainWindow", "y0, м"))
        self.label_9.setText(_translate("MainWindow", "u, м/c"))
        self.label_10.setText(_translate("MainWindow", "w, м/с"))
        self.label_11.setText(_translate("MainWindow", "fi0, рад"))
        self.push1.setText(_translate("MainWindow", "a(phi)"))
        self.push2.setText(_translate("MainWindow", "d(v)"))
        self.push3.setText(_translate("MainWindow", "phase(m,v)"))
        self.push4.setText(_translate("MainWindow", "phase(r,v)"))
        self.label.setText(_translate("MainWindow", "Введите параметры:"))

    def add_functions(self):
        self.push1.clicked.connect(self.first)
        self.push2.clicked.connect(self.second)
        self.push3.clicked.connect(self.third)
        self.push4.clicked.connect(self.fourth)

    def first(self):
        M1 = float(self.M.text())
        R1 = float(self.R.text())
        r1 = float(self.r.text())
        m1 = float(self.m.text())
        I1 = float(self.I.text())
        g1 = float(self.g.text())
        y1 = float(self.y0.text())
        u1 = float(self.u.text())
        w1 = float(self.w.text())
        fi1 = float(self.fi0.text())

        import sympy as sp

        m, g, R, M, I, k, t, VV, E0, r = sp.symbols('m, g, R, M, I, gamma t, omega, E0, r ')

        y0, u, w = sp.symbols('y0, u, w ')  # y0=y center mass0, u-v center wheel0, w-m vel0

        E0 = m * g * y0 + M * u ** 2 / 2 + I * u ** 2 / (2 * R ** 2) + m * w ** 2 / 2

        fi0 = sp.symbols('varphi0')
        fi = sp.Function(r'\varphi')(t)
        ycm = R * (1 + k * sp.cos(fi + fi0))
        xmdot = (R * (fi + fi0) + r * sp.sin(fi + fi0)).diff(t)
        ymdot = (R + r * sp.cos(fi + fi0)).diff(t)

        E1 = m * g * (R + r * sp.cos(fi + fi0))  # Wpm
        E2 = M * (fi.diff() * R) ** 2 / 2  # EM cm
        E3 = I * fi.diff() ** 2 / 2  # EM relat cm
        E4 = m * (xmdot ** 2 + ymdot ** 2) / 2  # Em
        E = E1 + E2 + E3 + E4
        # y0 - initial y-coordinate of center of mass u - initial velocity of center of the wheel w - initial velocity of m point fi0 - initial angle between direction to m and a vertical line
        # substitution
        # factors before w: the third hole 0.21333, the second 0.5133

        p = (R1 - r1) / R1
        arr = [(M, M1), (R, R1), (r, r1), (m, m1), (I, I1), (g, g1),  # system patameters
               (y0, R1 - r1), (u, u1), (w, u1 * p), (fi0, fi1)]  # initial parameters
        eq = sp.Eq(E, E0)
        fidotonfi = list(sp.solveset(eq, fi.diff()))[0]
        fidoubledotonfi = fidotonfi.diff(t)
        ycm1 = (ycm.diff(t, 2).subs(sp.diff(fi, t, 2), fidoubledotonfi)).subs(sp.diff(fi, t), fidotonfi)
        # #substitution of gamma on distance between m and center of the wheel
        exprg = m * r / ((M + m) * R)
        ycm1 = ycm1.subs(k, exprg)
        ycm1 = ycm1.subs(arr)
        import numpy as np

        yddonfi = sp.lambdify(fi, ycm1, modules=np)
        # sp.nsolve(foreq, f)
        import matplotlib.pyplot as plt

        fi = np.linspace(0, 5, 1000)
        ydd = yddonfi(3.1416 * fi)
        plt.ylim(-20, 70)
        plt.xticks(np.arange(0, 5, 0.4))
        plt.grid()
        plt.plot(fi, ydd)
        plt.ylabel('y-component of acceleration of the center of mass, m/s^2')
        plt.xlabel('angle of rotation, pi*rad')
        plt.show()
        plt.savefig('a(phi).png')

    def second(self):
        M1 = float(self.M.text())
        R1 = float(self.R.text())
        r1 = float(self.r.text())
        m1 = float(self.m.text())
        I1 = float(self.I.text())
        g1 = float(self.g.text())
        y1 = float(self.y0.text())
        u1 = float(self.u.text())
        w1 = float(self.w.text())
        fi1 = float(self.fi0.text())

        import sympy as sp
        import matplotlib.pyplot as plt

        m, g, R, M, I, k, t, VV, E0, r = sp.symbols('m, g, R, M, I, gamma t, omega, E0, r ')

        y0, u, w = sp.symbols('y0, u, w ')  # y0=y center mass0, u-v center wheel0, w-m vel0

        E0 = m * g * y0 + M * u ** 2 / 2 + I * u ** 2 / (2 * R ** 2) + m * w ** 2 / 2

        fi0 = sp.symbols('varphi0')
        fi = sp.Function(r'\varphi')(t)
        ycm = R * (1 + k * sp.cos(fi + fi0))
        xmdot = (R * (fi + fi0) + r * sp.sin(fi + fi0)).diff(t)
        ymdot = (R + r * sp.cos(fi + fi0)).diff(t)

        E1 = m * g * ycm  # Wpm
        E2 = M * (fi.diff() * R) ** 2 / 2  # EM cm
        E3 = I * fi.diff() ** 2 / 2  # EM relat cm
        E4 = m * (xmdot ** 2 + ymdot ** 2) / 2  # Em
        E = E1 + E2 + E3 + E4

        # calculations
        eq = sp.Eq(E, E0)
        fidotonfi = list(sp.solveset(eq, fi.diff()))[1]
        fidoubledotonfi = fidotonfi.diff(t)
        fidoubledotonfi
        ycm1 = (ycm.diff(t, 2).subs(sp.diff(fi, t, 2), fidoubledotonfi)).subs(sp.diff(fi, t), fidotonfi)
        import matplotlib.pyplot as plt
        import numpy as np

        exprg = m * r / ((M + m) * R)
        ycm1 = ycm1.subs(k, exprg)

        num = 100
        u1 = 2.75
        u2 = 5
        s = 0
        t = 0

        t0 = num * (u2 - u1)
        arrv = [0 for i in range(int(u1 * num), int(u2 * num), 1)]
        arrfic = [0 for i in range(int(u1 * num), int(u2 * num), 1)]

        p = (R1 - r1) / R1
        for un in range(int(u1 * num), int(u2 * num), 1):
            arrv[s] = un / num
            arr = [(M, M1), (R, R1), (r, r1), (m, m1), (I, I1), (g, g1),  # system patameters
                   (y0, R1 - r1), (u, un / num), (w, p * un / num), (fi0, fi1)]  # initial parameters
            # substitution of gamma on distance between m and center of the wheel
            ycmalternating = ycm1.subs(arr)

            yddonfi = sp.lambdify(fi, ycmalternating, modules=np)
            # acquiring fi angle of jump
            fiarr = np.linspace(0, 3.5, 10000)
            for fic in fiarr:
                if -9.81 < yddonfi(fic) < -9.79:
                    arrfic[s] = fic
                    break
            s += 1
            t += 1
            if t % 10 == 0:
                print(t, '/', t0)

        # data1 = pd.read_csv('d(v) 600 third hole v2.txt', sep='\t')
        # data1['errd'] = 1.5
        # data1['errv'] = 0.2
        # plotting graph of displacement on initial velocity dependence
        import matplotlib.pyplot as plt

        plt.grid()
        # plt.title('displacement before jump on initial velocity of the center of the disk')
        plt.ylabel('displacement, cm')
        plt.xlabel('initial velocity, m/s')
        plt.ylim(8, 18)
        plt.xlim(2.5, 5)
        plt.plot(arrv, [i * 0.075 * 100 for i in arrfic])
        plt.show()
        plt.savefig('d(v).png')
        # data1 = pd.read_csv('d(v) 600 third hole v2.txt', sep='\t')
        # plt.scatter(data1['v'], data1['d'])
        # plt.errorbar(data1['v'], data1['d'], xerr=0.1, yerr=2, ls='none')

    def third(self):
        M1 = float(self.M.text())
        R1 = float(self.R.text())
        r1 = float(self.r.text())
        m1 = float(self.m.text())
        I1 = float(self.I.text())
        g1 = float(self.g.text())
        y1 = float(self.y0.text())
        u1 = float(self.u.text())
        w1 = float(self.w.text())
        fi1 = float(self.fi0.text())

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
        p = (R1 - r1) / R1
        t0 = num1 * (u2 - u1) * num2 * (m2 - m1)
        arrv = [0 for i in
                range(len(range(int(u1 * num1), int(u2 * num1), 1)) * len(range(int(m1 * num2), int(m2 * num2), 1)))]
        arrm = [0 for i in
                range(len(range(int(u1 * num1), int(u2 * num1), 1)) * len(range(int(m1 * num2), int(m2 * num2), 1)))]
        for un in range(int(u1 * num1), int(u2 * num1), 1):
            for mi in range(int(m1 * num2), int(m2 * num2), 1):  # numbers are boundaries in grams
                arr = [(M, M1), (R, R1), (r, r1), (m, (mi / num2) / 1000), (I, I1), (g, g1),
                       # system patameters
                       (y0, R1 - r1), (u, un / num1), (w, 0.21333 * un / num1), (fi0, fi1)]  # initial parameters
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
        plt.savefig('phase(m,v).png')

    def fourth(self):
        M1 = float(self.M.text())
        R1 = float(self.R.text())
        r1 = float(self.r.text())
        m1 = float(self.m.text())
        I1 = float(self.I.text())
        g1 = float(self.g.text())
        y1 = float(self.y0.text())
        u1 = float(self.u.text())
        w1 = float(self.w.text())
        fi1 = float(self.fi0.text())

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
        rstart = 1
        rfin = 7
        s = 0
        t = 0

        t0 = num1 * (u2 - u1) * num2 * (rfin - rstart)
        arrv = [0 for i in
                range(len(range(int(u1 * num1), int(u2 * num1), 1)) * len(
                    range(int(rstart * num2), int(rfin * num2), 1)))]
        arrr = [0 for i in
                range(len(range(int(u1 * num1), int(u2 * num1), 1)) * len(
                    range(int(rstart * num2), int(rfin * num2), 1)))]
        for ui in range(int(u1 * num1), int(u2 * num1), 1):
            for ri in range(int(rstart * num2), int(rfin * num2), 1):
                p = (R1 - (ri / num2) / 100) / R1
                arr = [(M, M1), (R, R1), (r, (ri / num2) / 100), (m, m1), (I, I1), (g, g1),
                       # system patameters
                       (y0, R1 - (ri / num2) / 100), (u, ui / num1), (w, (ui / num1) * p),
                       (fi0, 3.1415)]  # initial parameters
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
        plt.plot([i for i in arrv if i != 0], [i for i in arrr if i != 0])
        plt.show()
        plt.savefig('phase(r,v).png')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
