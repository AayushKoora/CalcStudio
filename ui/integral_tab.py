from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSizePolicy
from  PyQt5.QtCore import Qt
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
        
        # === Integral Tab ===
        self.intLayout = QHBoxLayout(self)
        self.setLayout(self.intLayout)

        # --- Container One --- 
        self.intCont1 = QWidget()
        self.intCont1Layout = QVBoxLayout(self.intCont1)
        self.intLayout.addWidget(self.intCont1, stretch=4)
        # self.intCont1.setStyleSheet("""
        #     border: 2px solid black;
        #     border-radius: 5px;        
        # """)

        self.intTitle = QLabel("CALCSTUDIO")
        self.intCont1Layout.addWidget(self.intTitle)
        self.intTitle.setStyleSheet("""
            font-family: 'Arial';
            font-size: 80px;
            color: #595959;
        """)
        self.intTitle.setAlignment(Qt.AlignLeft | Qt. AlignVCenter)
        self.intTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.intSubTitle = QLabel("Integrals: Area Under a Curve")
        self.intCont1Layout.addWidget(self.intSubTitle)
        self.intSubTitle.setStyleSheet("""
            font-family: 'Arial';
            font-size: 50px;
            color: #595959;
        """)
        self.intTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.intFunctionLabel = QLabel("Function Input: ")
        self.intCont1Layout.addWidget(self.intFunctionLabel)
        self.intFunctionLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.intTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.intFunction = QLineEdit()
        self.intCont1Layout.addWidget(self.intFunction)
        self.intFunction.setStyleSheet("""
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
        self.intFunction.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.intFirstValueLabel = QLabel("First Value:")
        self.intCont1Layout.addWidget(self.intFirstValueLabel)
        self.intFirstValueLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.intTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.intfirstValue = QLineEdit()
        self.intCont1Layout.addWidget(self.intfirstValue)
        self.intfirstValue.setStyleSheet("""
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
        self.intfirstValue.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.intSecondValueLabel = QLabel("Second Value: ")
        self.intCont1Layout.addWidget(self.intSecondValueLabel)
        self.intSecondValueLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.intTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.intsecondValue = QLineEdit()
        self.intCont1Layout.addWidget(self.intsecondValue)
        self.intsecondValue.setStyleSheet("""
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
        self.intsecondValue.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.intButton = QPushButton("Integrate")
        self.intButton.clicked.connect(self.integration)
        self.intCont1Layout.addWidget(self.intButton)
        self.intButton.setStyleSheet("""
            QPushButton {
                background-color: #999999;
                padding: 16px, 16px;
                font-size: 16px;
            }
                                   
            QPushButton:pressed {
                background-color: #88cc88;
            }
        """)

        self.intLabel = QLabel("Area Under the Curve: ")
        self.intCont1Layout.addWidget(self.intLabel)
        self.intLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.intTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.intSpace = QWidget()
        self.intCont1Layout.addWidget(self.intSpace, stretch=1)

        # --- Container Two ---
        self.intCont2 = QWidget()
        self.intCont2Layout = QVBoxLayout(self.intCont2)
        self.intLayout.addWidget(self.intCont2, stretch=6)
        # self.intCont2.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)

        self.intCanvas = FigureCanvas(plt.Figure(figsize=(10, 10)))
        self.intCont2Layout.addWidget(self.intCanvas)
        self.intInsert_ax()

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
            self.axInt.plot(x_points, y_intfunc_np, label="Function")
            self.axInt.axhline(0, color='black', linestyle=':')
            self.axInt.axvline(0, color='black', linestyle=':')
            self.axInt.fill_between(x_fill, y_fill, color='blue', alpha = 0.4, label='Area under curve')

            self.axInt.legend()
            self.intCanvas.draw()
        except Exception as e:
            print(f"Plotting Error: {e}")
            self.intLabel.setText("Error Plotting Function.")

    def intInsert_ax(self):
        self.axInt = self.intCanvas.figure.subplots()
        self.bar = None