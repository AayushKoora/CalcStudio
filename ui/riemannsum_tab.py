from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSizePolicy
from  PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sympy import *
from style.colors import Colors

class RiemannSumTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet(f"background-color: {Colors.LIGHTGRAY};")
        self.init_ui()
    
    def init_ui(self):
        
        # === Riemann Sum ===
        self.remLayout = QHBoxLayout(self)
        self.setLayout(self.remLayout)

        # --- Container One ---
        self.remCont1 = QWidget()
        self.remCont1Layout = QVBoxLayout(self.remCont1)
        self.remLayout.addWidget(self.remCont1, stretch=4)
        # self.remCont1.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)

        self.remTitle = QLabel("CALCSTUDIO")
        self.remCont1Layout.addWidget(self.remTitle)
        self.remTitle.setStyleSheet("""
            font-family: 'Arial';
            font-size: 80px;
            color: #595959;
        """)
        self.remTitle.setAlignment(Qt.AlignLeft | Qt. AlignVCenter)
        self.remTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remSubTitle = QLabel("Riemann Sum")
        self.remCont1Layout.addWidget(self.remSubTitle)
        self.remSubTitle.setStyleSheet("""
            font-family: 'Arial';
            font-size: 50px;
            color: #595959;
        """)
        self.remSubTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remFuncInputLabel = QLabel("Function Input: ")
        self.remCont1Layout.addWidget(self.remFuncInputLabel)
        self.remFuncInputLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.remFuncInputLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remBox1 = QWidget()
        self.remBox1Layout = QHBoxLayout(self.remBox1)
        self.remCont1Layout.addWidget(self.remBox1)

        self.remFuncInput = QLineEdit()
        self.remBox1Layout.addWidget(self.remFuncInput)
        self.remFuncInput.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid black;
            }
                                         
            QLineEdit:focus {
                border: 2px solid #88cc88;
                background-color: #ffffff;
            }
        """)
        self.remFuncInput.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remSubmit = QPushButton()
        self.remSubmit.clicked.connect(self.riemannSummation)
        self.remBox1Layout.addWidget(self.remSubmit)
        self.remSubmit.setStyleSheet("""
            QPushButton {
                background-color: #999999;
                padding: 16px, 16px;
                font-size: 16px;
            }
                                   
            QPushButton:pressed {
                background-color: #88cc88;
            }
        """)

        self.remBox2 = QWidget()
        self.remBox2Layout = QHBoxLayout(self.remBox2)
        self.remCont1Layout.addWidget(self.remBox2)

        self.remNumRectLabel = QLabel("# of Rectangles")
        self.remBox2Layout.addWidget(self.remNumRectLabel)
        self.remNumRectLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.remNumRectLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remTypeApproxLabel = QLabel("Type of Approx")
        self.remBox2Layout.addWidget(self.remTypeApproxLabel)
        self.remTypeApproxLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.remTypeApproxLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remBox3 = QWidget()
        self.remBox3Layout = QHBoxLayout(self.remBox3)
        self.remCont1Layout.addWidget(self.remBox3)

        self.remNumRect = QLineEdit()
        self.remBox3Layout.addWidget(self.remNumRect)
        self.remNumRect.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid black;
            }
                                         
            QLineEdit:focus {
                border: 2px solid #88cc88;
                background-color: #ffffff;
            }
        """)
        self.remNumRect.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remTypeApprox = QLineEdit()
        self.remBox3Layout.addWidget(self.remTypeApprox)
        self.remTypeApprox.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid black;
            }
                                         
            QLineEdit:focus {
                border: 2px solid #88cc88;
                background-color: #ffffff;
            }
        """)
        self.remTypeApprox.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remBox4 = QWidget()
        self.remBox4Layout = QHBoxLayout(self.remBox4)
        self.remCont1Layout.addWidget(self.remBox4)

        self.remFirstValLabel = QLabel("First Value: ")
        self.remBox4Layout.addWidget(self.remFirstValLabel)
        self.remFirstValLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.remFirstValLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remLastValLabel = QLabel("Last Value: ")
        self.remBox4Layout.addWidget(self.remLastValLabel)
        self.remLastValLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.remLastValLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remBox5 = QWidget()
        self.remBox5Layout = QHBoxLayout(self.remBox5)
        self.remCont1Layout.addWidget(self.remBox5)

        self.remFirstVal = QLineEdit()
        self.remBox5Layout.addWidget(self.remFirstVal)
        self.remFirstVal.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid black;
            }
                                         
            QLineEdit:focus {
                border: 2px solid #88cc88;
                background-color: #ffffff;
            }
        """)
        self.remFirstVal.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remLastVal = QLineEdit()
        self.remBox5Layout.addWidget(self.remLastVal)
        self.remLastVal.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid black;
            }
                                         
            QLineEdit:focus {
                border: 2px solid #88cc88;
                background-color: #ffffff;
            }
        """)
        self.remLastVal.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remBox6 = QWidget()
        self.remBox6Layout = QHBoxLayout(self.remBox6)
        self.remCont1Layout.addWidget(self.remBox6)

        self.remApproxAreaLabel = QLabel("Approx. Area")
        self.remBox6Layout.addWidget(self.remApproxAreaLabel)
        self.remApproxAreaLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.remApproxAreaLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remPercErrorLabel = QLabel("Percent Error")
        self.remBox6Layout.addWidget(self.remPercErrorLabel)
        self.remPercErrorLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.remPercErrorLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        # --- Container Two ---
        self.remCont2 = QWidget()
        self.remCont2Layout = QVBoxLayout(self.remCont2)
        self.remLayout.addWidget(self.remCont2, stretch=6)
        # self.remCont2.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)

        self.remCanvas = FigureCanvas(plt.Figure(figsize=(10, 10)))
        self.remCont2Layout.addWidget(self.remCanvas)
        self.remInsert_ax()

    def riemannSummation(self):
        x, i = symbols("x i")

        func = sympify(self.remFuncInput.text())
        numRect = int(self.remNumRect.text())
        type = self.remTypeApprox.text()

        firstVal = float(self.remFirstVal.text())
        lastVal = float(self.remLastVal.text())
        delta = (lastVal - firstVal) / numRect

        self.axRem.clear()
        x_points = np.linspace(firstVal - 1, lastVal + 1, 300)
        func_np = lambdify(x, func, 'numpy')
        y_func_np = func_np(x_points)

        self.axRem.plot(x_points, y_func_np, label='Function')

        if type == 'left':
            approx_sum = summation(func.subs(x, firstVal + i*delta) * delta, (i, 0, numRect-1))
            x_left = np.linspace(firstVal, lastVal - delta, numRect)
            y_left = func_np(x_left)

            self.axRem.bar(x_left, y_left, width=delta, align='edge', label='left sum', alpha=0.5, color = 'blue')

        elif type == 'right':
            approx_sum = summation(func.subs(x, firstVal + i*delta) * delta, (i, 1, numRect))
            x_right = np.linspace(firstVal + delta, lastVal, numRect)
            y_right = func_np(x_right)

            self.axRem.bar(x_right - delta, y_right, width=delta, align = 'edge', label='right sum',  alpha=0.5, color = 'blue')

        area = integrate(func, (x, firstVal, lastVal))

        perc_error = ((approx_sum - area) / area) * 100

        self.remApproxAreaLabel.setText(f"Approx Area: {approx_sum}")
        self.remPercErrorLabel.setText(f"Percent Error: {perc_error}%")

        self.axRem.legend()
        self.remCanvas.draw()
        

    def remInsert_ax(self):
        self.axRem = self.remCanvas.figure.subplots()
        self.axRem.set_ylim([-100, 100])
        self.axRem.set_xlim([-100, 100])
        self.bar = None