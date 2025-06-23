from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSizePolicy,
QGraphicsDropShadowEffect)
from  PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from style.colors import Colors

class IntegralTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet(f"background-color: {Colors.LIGHTGRAY};")
        self.init_ui()

    def init_ui(self):
        
        # === Integral Tab === # Start
        self.intLayout = QHBoxLayout(self)
        self.setLayout(self.intLayout)
        self.intLayout.setContentsMargins(0, 0, 0, 0)
        self.intLayout.setSpacing(0)

        # --- Container One --- # Start
        self.intCont1 = QWidget()
        self.intCont1Layout = QVBoxLayout(self.intCont1)
        self.intLayout.addWidget(self.intCont1, stretch=55)
        self.intCont1Layout.setContentsMargins(0, 0, 0, 0)
        self.intCont1Layout.setSpacing(0)
        # self.intCont1.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)

        self.intCont1Space0 = QWidget()
        self.intCont1Layout.addWidget(self.intCont1Space0, stretch=41)

        ## --- Heading Container --- ## Start
        self.intCont1Head = QWidget()
        self.intCont1HeadLayout = QHBoxLayout(self.intCont1Head)
        self.intCont1Layout.addWidget(self.intCont1Head, stretch=97)
        self.intCont1HeadLayout.setContentsMargins(0, 0, 0, 0)
        self.intCont1HeadLayout.setSpacing(0)

        self.intCont1Space1 = QWidget()
        self.intCont1HeadLayout.addWidget(self.intCont1Space1, stretch=2)
        self.intCont1Space1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        ### --- Content in Heading Container --- ### Start
        self.intCont1Head1 = QWidget()
        self.intCont1Head1Layout = QVBoxLayout(self.intCont1Head1)
        self.intCont1HeadLayout.addWidget(self.intCont1Head1, stretch=2)
        self.intCont1Head1Layout.setContentsMargins(0, 0, 0, 0)
        self.intCont1Head1Layout.setSpacing(0)

        self.intTitle = QLabel("CALCSTUDIO")
        self.intCont1Head1Layout.addWidget(self.intTitle)
        self.intTitle.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 80px;
            color: #595959;
            font-weight: bold;
        """)
        self.intTitle.setAlignment(Qt.AlignLeft | Qt. AlignVCenter)
        self.intTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.intSubTitle = QLabel("Integrals: Area Under a Curve")
        self.intCont1Head1Layout.addWidget(self.intSubTitle)
        self.intSubTitle.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.intTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        ### --- Content in Heading Container --- ### End

        self.intCont1Space2 = QWidget()
        self.intCont1HeadLayout.addWidget(self.intCont1Space2, stretch=2)
        self.intSubTitle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.intCont1Space2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        
        ## --- Heading Container --- ## End

        self.intSpace20 = QWidget()
        self.intCont1Layout.addWidget(self.intSpace20, stretch=25)

        ## --- Info Container --- ## Start
        self.intCont1Info = QWidget()
        self.intCont1Layout.addWidget(self.intCont1Info, stretch=267)
        self.intInfoContLayout = QHBoxLayout(self.intCont1Info)
        self.intInfoContLayout.setContentsMargins(0, 0, 0, 0)
        self.intInfoContLayout.setSpacing(0)

        self.intCont1Space3 = QWidget()
        self.intInfoContLayout.addWidget(self.intCont1Space3, stretch=1)

        ### --- Content in Info Container --- ### Start
        self.intCont1Info1 = QWidget()
        self.intInfoContLayout.addWidget(self.intCont1Info1, stretch=14)
        self.intInfoContLayout1 = QVBoxLayout(self.intCont1Info1)
        self.intInfoContLayout1.setContentsMargins(0, 0, 0, 0)
        self.intInfoContLayout1.setSpacing(20)

        self.intFunction = QLineEdit()
        self.intInfoContLayout1.addWidget(self.intFunction, stretch=1)
        self.intFunction.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.intFunction.setAlignment(Qt.AlignLeft)
        self.intFunction.setPlaceholderText("  Function Input: ")
        self.intFunction.setStyleSheet("""
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
        self.intFunction.setFixedHeight(50)

        self.intfirstValue = QLineEdit()
        self.intInfoContLayout1.addWidget(self.intfirstValue, stretch=1)
        self.intfirstValue.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.intfirstValue.setAlignment(Qt.AlignLeft)
        self.intfirstValue.setPlaceholderText("  First Value: ")
        self.intfirstValue.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 3px solid #A9A8A8;
                border-radius: 10px;
                font-size: 25px;
                padding-top: 4px;
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
        self.intfirstValue.setFixedHeight(50)

        self.intsecondValue = QLineEdit()
        self.intInfoContLayout1.addWidget(self.intsecondValue, stretch=1)
        self.intsecondValue.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.intsecondValue.setAlignment(Qt.AlignLeft)
        self.intsecondValue.setPlaceholderText("  Last Value: ")
        self.intsecondValue.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 3px solid #A9A8A8;
                border-radius: 10px;
                font-size: 25px;
                padding-top: 4px;
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
        self.intsecondValue.setFixedHeight(50)


        self.intLabel = QLabel("Area Under the Curve: ")
        self.intInfoContLayout1.addWidget(self.intLabel)
        self.intLabel.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.intLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        ### --- Content in Info Container --- ### End

        self.intCont1Space8 = QWidget()
        self.intInfoContLayout.addWidget(self.intCont1Space8, stretch=1)

        ## --- Info Container --- ## End

        self.intCont1Space9 = QWidget()
        self.intCont1Layout.addWidget(self.intCont1Space9, stretch=39)

        ## --- Button Container --- ## Start
        self.intCont1Button = QWidget()
        self.intCont1Layout.addWidget(self.intCont1Button, stretch=40)
        self.intCont1ButtonLayout = QHBoxLayout(self.intCont1Button)
        self.intCont1ButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.intCont1ButtonLayout.setSpacing(0)

        self.intCont1Space10 = QWidget()
        self.intCont1ButtonLayout.addWidget(self.intCont1Space10, stretch=1)

        self.intButton = QPushButton("INTEGRATE")
        self.intButton.clicked.connect(self.integration)
        self.intCont1ButtonLayout.addWidget(self.intButton, stretch=6)
        self.intButton.setStyleSheet("""
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

        self.intCont1Space11 = QWidget()
        self.intCont1ButtonLayout.addWidget(self.intCont1Space11, stretch=1)

        ## --- Button Container --- ## End

        self.intSpace = QWidget()
        self.intCont1Layout.addWidget(self.intSpace, stretch=93)

        # --- Container One --- # End

        # --- Container Two --- # Start
        self.intCont2 = QWidget()
        self.intCont2Layout = QVBoxLayout(self.intCont2)
        self.intCont2Layout.setContentsMargins(10, 10, 10, 10)
        self.intCont2Layout.setSpacing(0)
        self.intLayout.addWidget(self.intCont2, stretch=45)
        # self.intCont2.setStyleSheet("""
        # border: 2px solid black;
        # background-color: {Colors.PRIMARY};
        # border-radius: 5px;
        # """)

        self.intCanvas = FigureCanvas(plt.Figure(figsize=(6, 7)))
        self.intCanvas.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.intCont2Layout.addWidget(self.intCanvas)
        self.intInsert_ax()

        # --- Container Two --- # End

        # === Integral Tab === # End

    # Function that integrates and plots it on the graph
    def integration(self):
        x = symbols("x")

        # Step 1: Parse Inputs
        try: 
            intfirst = float(self.intfirstValue.text())
            intsecond = float(self.intsecondValue.text())
            intfunc = sympify(self.intFunction.text())
        except Exception as e:
            print(f"Input Error: {e}")
            self.intLabel.setText("Invalid input.")
            return
        
        # Step 2: Integration
        try:
            intValue = integrate(intfunc, (x, intfirst, intsecond))
        except Exception as e:
            print(f"Integration Error: {e}")
            self.intLabel.setText("Error Calculating Integral.")
            return
        
        self.intLabel.setText(f"Area Under the Curve: {intValue}")

        # Step 3: x Range Calculation
        self.axInt.figure.clf()
        self.axInt = self.intCanvas.figure.subplots()

        try:
            center = (intfirst + intsecond) / 2
            range_width = 1.5*abs(intsecond - intfirst)
            x_min = center - range_width
            x_max = center + range_width
            x_points = np.linspace(x_min, x_max, 200)
        except Exception as e:
            print(f"x Range Error: {e}")
            self.intLabel.setText(f"Error Calculating x Range.")
            return

        # Step 4: Numeric Evaluation and y Range Calculation
        try:
            intfunc_np = lambdify(x, intfunc, 'numpy')
            y_intfunc_np = intfunc_np(x_points)

            x_fill = np.linspace(intfirst, intsecond, 200)
            y_fill = intfunc_np(x_fill)

            finite_y = y_fill[np.isfinite(y_fill)]

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
            print(f"Evaluation Error: {e}")
            self.intLabel.setText("Error Evaluating Function or y Range.")
            return
        
        # Step 5: Plotting
        try:
            self.axInt.set_xlim([x_min, x_max])
            self.axInt.set_ylim([y_min - y_margin, y_max + y_margin])
            self.axInt.plot(x_points, y_intfunc_np, label="Function", color='black')
            self.axInt.axhline(0, color='black', linestyle=':')
            self.axInt.axvline(0, color='black', linestyle=':')
            self.axInt.fill_between(x_fill, y_fill, color='#FF6A6A', alpha = 0.4, label='Area Under Curve')

            self.axInt.legend()
            self.intCanvas.draw()
        except Exception as e:
            print(f"Plotting Error: {e}")
            self.intLabel.setText("Error Plotting Function.")

    def intInsert_ax(self):
        self.axInt = self.intCanvas.figure.subplots()
        self.bar = None