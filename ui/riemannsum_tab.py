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
        
        # === Riemann Sum === # Start
        self.remLayout = QHBoxLayout(self)
        self.setLayout(self.remLayout)
        self.remLayout.setContentsMargins(0, 0, 0, 0)
        self.remLayout.setSpacing(0)

        # --- Container One --- # Start
        self.remCont1 = QWidget()
        self.remCont1Layout = QVBoxLayout(self.remCont1)
        self.remLayout.addWidget(self.remCont1, stretch=55)
        self.remCont1Layout.setContentsMargins(0, 0, 0, 0)
        self.remCont1Layout.setSpacing(0)
        # self.remCont1.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)

        self.remCont1Space0 = QWidget()
        self.remCont1Layout.addWidget(self.remCont1Space0, stretch=40)

        ## --- Heading Container --- ## Start
        self.remCont1Head = QWidget()
        self.remCont1HeadLayout = QHBoxLayout(self.remCont1Head)
        self.remCont1Layout.addWidget(self.remCont1Head, stretch=89)
        self.remCont1HeadLayout.setContentsMargins(0, 0, 0, 0)
        self.remCont1HeadLayout.setSpacing(0)

        self.remCont1Space1 = QWidget()
        self.remCont1HeadLayout.addWidget(self.remCont1Space1, stretch=2)
        self.remCont1Space1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        ### --- Content in Heading Container --- ### Start
        self.remCont1Head1 = QWidget()
        self.remCont1Head1Layout = QVBoxLayout(self.remCont1Head1)
        self.remCont1HeadLayout.addWidget(self.remCont1Head1, stretch=2)
        self.remCont1Head1Layout.setContentsMargins(0, 0, 0, 0)
        self.remCont1Head1Layout.setSpacing(0)

        self.remTitle = QLabel("CALCSTUDIO")
        self.remCont1Head1Layout.addWidget(self.remTitle)
        self.remTitle.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 80px;
            color: #595959;
            font-weight: bold;
        """)
        self.remTitle.setAlignment(Qt.AlignLeft | Qt. AlignVCenter)
        self.remTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remSubTitle = QLabel("Integrals: Riemann Sum")
        self.remCont1Head1Layout.addWidget(self.remSubTitle)
        self.remSubTitle.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.remSubTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        ### --- Content in Heading Container --- ### End

        self.remCont1Space2 = QWidget()
        self.remCont1HeadLayout.addWidget(self.remCont1Space2, stretch=2)
        self.remSubTitle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.remCont1Space2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        ## --- Heading Container --- ## End

        self.remSpace20 = QWidget()
        self.remCont1Layout.addWidget(self.remSpace20, stretch=30)

        ## --- Info Container --- ## Start
        self.remCont1Info = QWidget()
        self.remCont1Layout.addWidget(self.remCont1Info, stretch=229)
        self.remInfoContLayout = QHBoxLayout(self.remCont1Info)
        self.remInfoContLayout.setContentsMargins(0, 0, 0, 0)
        self.remInfoContLayout.setSpacing(0)

        self.remCont1Space3 = QWidget()
        self.remInfoContLayout.addWidget(self.remCont1Space3, stretch=1)

        ### --- Content in Info Container --- ### Start
        self.remCont1Info1 = QWidget()
        self.remInfoContLayout.addWidget(self.remCont1Info1, stretch=14)
        self.remInfoContLayout1 = QVBoxLayout(self.remCont1Info1)
        self.remInfoContLayout1.setContentsMargins(0, 0, 0, 0)
        self.remInfoContLayout1.setSpacing(20)

        self.remFuncInput = QLineEdit()
        self.remInfoContLayout1.addWidget(self.remFuncInput)
        self.remFuncInput.setPlaceholderText("  Function Input: ")
        self.remFuncInput.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 3px solid #A9A8A8;
                border-radius: 10px;
                padding-top: 4px;
                font-size: 25px;
                font-family: "Helvetica";
            }
                                         
            QLineEdit:focus {
                border: 3px solid #FF6A6A;
                background-color: #ffffff;
            }
                                       
            QLineEdit::placeholder{
                font-family: "Helvetica";
            }
        """)
        self.remFuncInput.setFixedHeight(50)

        self.remNumRect = QLineEdit()
        self.remInfoContLayout1.addWidget(self.remNumRect)
        self.remNumRect.setPlaceholderText("  Number of Rectangles: ")
        self.remNumRect.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 3px solid #A9A8A8;
                border-radius: 10px;
                padding-top: 4px;
                font-size: 25px;
                font-family: "Helvetica";
            }
                                         
            QLineEdit:focus {
                border: 3px solid #FF6A6A;
                background-color: #ffffff;
            }
                                       
            QLineEdit::placeholder{
                font-family: "Helvetica";
            }
        """)
        self.remNumRect.setFixedHeight(50)

        self.remTypeApprox = QLineEdit()
        self.remInfoContLayout1.addWidget(self.remTypeApprox)
        self.remTypeApprox.setPlaceholderText("  Type of Approx: ")
        self.remTypeApprox.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 3px solid #A9A8A8;
                border-radius: 10px;
                padding-top: 4px;
                font-size: 25px;
                font-family: "Helvetica";
            }
                                         
            QLineEdit:focus {
                border: 3px solid #FF6A6A;
                background-color: #ffffff;
            }
                                       
            QLineEdit::placeholder{
                font-family: "Helvetica";
            }
        """)
        self.remTypeApprox.setFixedHeight(50)

        self.remValueBox = QWidget()
        self.remInfoContLayout1.addWidget(self.remValueBox, stretch=52)
        self.remValueBoxLayout = QHBoxLayout(self.remValueBox)
        self.remValueBox.setLayout(self.remValueBoxLayout)
        self.remValueBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.remValueBoxLayout.setSpacing(0)

        self.remFirstVal = QLineEdit()
        self.remValueBoxLayout.addWidget(self.remFirstVal, stretch=15)
        self.remFirstVal.setPlaceholderText("  First Value: ")
        self.remFirstVal.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 3px solid #A9A8A8;
                border-radius: 10px;
                padding-top: 4px;
                font-size: 25px;
                font-family: "Helvetica";
            }
                                         
            QLineEdit:focus {
                border: 3px solid #FF6A6A;
                background-color: #ffffff;
            }
                                       
            QLineEdit::placeholder{
                font-family: "Helvetica";
            }
        """)
        self.remFirstVal.setFixedHeight(50)

        self.ValueSpace = QWidget()
        self.remValueBoxLayout.addWidget(self.ValueSpace, stretch=1)

        self.remLastVal = QLineEdit()
        self.remValueBoxLayout.addWidget(self.remLastVal, stretch=15)
        self.remLastVal.setPlaceholderText("  Last Value: ")
        self.remLastVal.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 3px solid #A9A8A8;
                border-radius: 10px;
                padding-top: 4px;
                font-size: 25px;
                font-family: "Helvetica";
            }
                                         
            QLineEdit:focus {
                border: 3px solid #FF6A6A;
                background-color: #ffffff;
            }
                                       
            QLineEdit::placeholder{
                font-family: "Helvetica";
            }
        """)
        self.remLastVal.setFixedHeight(50)

        ### --- Content in Info Container --- ### End

        self.remCont1Space8 = QWidget()
        self.remInfoContLayout.addWidget(self.remCont1Space8, stretch=1)

        ## --- Info Container --- ## End

        self.remBox6 = QWidget()
        self.remBox6Layout = QVBoxLayout(self.remBox6)
        self.remInfoContLayout1.addWidget(self.remBox6, stretch=52)
        self.remBox6Layout.setContentsMargins(0, 0, 0, 0)
        self.remBox6Layout.setSpacing(10)

        self.remApproxAreaLabel = QLabel("Approx. Area: ")
        self.remBox6Layout.addWidget(self.remApproxAreaLabel)
        self.remApproxAreaLabel.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.remApproxAreaLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remPercErrorLabel = QLabel("Percent Error: ")
        self.remBox6Layout.addWidget(self.remPercErrorLabel)
        self.remPercErrorLabel.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.remPercErrorLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.remCont1Space16 = QWidget()
        self.remCont1Layout.addWidget(self.remCont1Space16, stretch=29)

        ## --- Button Container --- ## Start
        self.remCont1Button = QWidget()
        self.remCont1Layout.addWidget(self.remCont1Button, stretch=46)
        self.remCont1ButtonLayout = QHBoxLayout(self.remCont1Button)
        self.remCont1ButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.remCont1ButtonLayout.setSpacing(0)

        self.remCont1Space10 = QWidget()
        self.remCont1ButtonLayout.addWidget(self.remCont1Space10, stretch=1)

        self.remSubmit = QPushButton("APPROXIMATE")
        self.remSubmit.clicked.connect(self.riemannSummation)
        self.remCont1ButtonLayout.addWidget(self.remSubmit, stretch=6)
        self.remSubmit.setStyleSheet("""
            QPushButton {
                background-color: #FF6A6A;
                padding: 22px, 16px;
                font-size: 35px;
                border-radius: 10px;
                font-weight: bold;
                font-family: "Helvetica";
            }
                                   
            QPushButton:pressed {
                background-color: #FF6A6A;
            }
        """)

        self.remCont1Space11 = QWidget()
        self.remCont1ButtonLayout.addWidget(self.remCont1Space11, stretch=1)

        ## --- Button Container --- ## End

        self.remSpace = QWidget()
        self.remCont1Layout.addWidget(self.remSpace, stretch=71)

        # --- Container Two --- # Start
        self.remCont2 = QWidget()
        self.remCont2Layout = QVBoxLayout(self.remCont2)
        self.remCont2Layout.setContentsMargins(10, 10, 10, 10)
        self.remCont2Layout.setSpacing(0)
        self.remLayout.addWidget(self.remCont2, stretch=45)
        # self.remCont2.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)

        self.remCanvas = FigureCanvas(plt.Figure(figsize=(6, 7)))
        self.remCanvas.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.remCont2Layout.addWidget(self.remCanvas)
        self.remInsert_ax()

        # --- Container Two --- # End

        # === Riemann Sum Tab === # End

    def riemannSummation(self):
        x, i = symbols("x i")

        # Step 1: Parse Inputs
        try:
            func = sympify(self.remFuncInput.text())
            numRect = int(self.remNumRect.text())
            type = self.remTypeApprox.text()
            firstVal = float(self.remFirstVal.text())
            lastVal = float(self.remLastVal.text())
            delta = (lastVal - firstVal) / numRect
        except Exception as e:
            print(f"Input Error: {e}")
            self.remApproxAreaLabel.setText("Invalid Input.")
            self.remPercErrorLabel.setText("Null")
            return

        # Step 2: x Range Calculation
        self.axRem.clear()

        try:
            center = (lastVal - firstVal) / 2
            range_width = 1.5*abs(lastVal - firstVal)
            x_min = center - range_width
            x_max = center + range_width
            x_points = np.linspace(firstVal - 1, lastVal + 1, 200)
        except Exception as e:
            print(f"x Range Calculation Error: {e}")
            self.remApproxAreaLabel.setText("Error Calculating x Range.")
            self.remPercErrorLabel.setText("Null")
            return

        # Step 3: y Range Calculation
        try:
            func_np = lambdify(x, func, 'numpy')
            y_func_np = func_np(x_points)

            x_values = np.linspace(firstVal, lastVal, 200)
            y_values = func_np(x_values)

            finite_y = y_values[np.isfinite(y_values)]

            if finite_y.size == 0:
                y_min, y_max = -1, 1
            else:
                y_min = np.min(finite_y)
                y_max = np.max(finite_y)

            if y_max == y_min:
                y_min -= 1
                y_max += 1
            else:
                y_margin = 0.1 * (y_max - y_min)
                y_min -= y_margin
                y_max += y_margin
        except Exception as e:
            print(f"y Range Calculation Error: {e}")
            self.remApproxAreaLabel.setText("Error Evaluation Function or y Range.")
            self.remPercErrorLabel.setText("Null")
            return

        # Step 4: Plotting
        try:
            self.axRem.set_xlim([x_min, x_max])
            self.axRem.set_ylim([y_min, y_max])
            self.axRem.plot(x_points, y_func_np, label='Function', color='black')
            self.axRem.axhline(0, color='black', linestyle=':')
            self.axRem.axvline(0, color='black', linestyle=':')

            if type == 'left':
                approx_sum = summation(func.subs(x, firstVal + i*delta) * delta, (i, 0, numRect-1))
                x_left = np.linspace(firstVal, lastVal - delta, numRect)
                y_left = func_np(x_left)

                self.axRem.bar(x_left, y_left, width=delta, align='edge', label='left sum', alpha=0.5, color = '#FF6A6A')

            elif type == 'right':
                approx_sum = summation(func.subs(x, firstVal + i*delta) * delta, (i, 1, numRect))
                x_right = np.linspace(firstVal + delta, lastVal, numRect)
                y_right = func_np(x_right)

                self.axRem.bar(x_right - delta, y_right, width=delta, align = 'edge', label='right sum',  alpha=0.5, color = '#FF6A6A')

            area = integrate(func, (x, firstVal, lastVal))

            perc_error = ((approx_sum - area) / area) * 100

            self.remApproxAreaLabel.setText(f"Approx Area: {approx_sum: .4f}")
            self.remPercErrorLabel.setText(f"Percent Error: {perc_error: .4f}%")

            self.axRem.legend()
            self.remCanvas.draw()
        except Exception as e:
            print(f"Plotting Error: {e}")
            self.remApproxAreaLabel.setText("Error Plotting Function.")
            self.remPercErrorLabel.setText("Null")
            return

    def remInsert_ax(self):
        self.axRem = self.remCanvas.figure.subplots()
        self.bar = None