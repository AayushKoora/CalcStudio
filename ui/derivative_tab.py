from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QSlider, QLabel, QSizePolicy, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, diff, lambdify, zoo
from sympy import (sin, cos, tan, exp, log, sqrt, Pow, Add, Mul, Function)
from style.colors import Colors

class DerivativeTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet(f"background-color: {Colors.LIGHTGRAY};")
        self.init_ui()

    def init_ui(self):

        # === Derivative Tab === # Start
        self.derivLayout = QHBoxLayout(self)
        self.setLayout(self.derivLayout)
        self.derivLayout.setContentsMargins(0, 0, 0, 0)
        self.derivLayout.setSpacing(0)

        # --- Container One --- # Start
        self.derivCont1 = QWidget()
        self.derivCont1Layout = QVBoxLayout(self.derivCont1)
        self.derivLayout.addWidget(self.derivCont1, stretch=55)
        self.derivCont1Layout.setContentsMargins(0, 0, 0, 0)
        self.derivCont1Layout.setSpacing(0)
        # self.derivCont1.setStyleSheet("""
        #     border: 2px solid black;
        #     border-radius: 5px;        
        # """)

        self.derivCont1Space0 = QWidget()
        self.derivCont1Layout.addWidget(self.derivCont1Space0, stretch=41)

        ## --- Heading Container --- ## Start
        self.derivCont1Head = QWidget()
        self.derivCont1HeadLayout = QHBoxLayout(self.derivCont1Head)
        self.derivCont1Layout.addWidget(self.derivCont1Head, stretch=89)
        self.derivCont1HeadLayout.setContentsMargins(0, 0, 0, 0)
        self.derivCont1HeadLayout.setSpacing(0)

        self.derivCont1Space1 = QWidget()
        self.derivCont1HeadLayout.addWidget(self.derivCont1Space1, stretch=2)
        self.derivCont1Space1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        ### --- Content in Heading Container --- ### Start
        self.derivCont1Head1 = QWidget()
        self.derivCont1Head1Layout = QVBoxLayout(self.derivCont1Head1)
        self.derivCont1HeadLayout.addWidget(self.derivCont1Head1, stretch=2)
        self.derivCont1Head1Layout.setContentsMargins(0, 0, 0, 0)
        self.derivCont1Head1Layout.setSpacing(0)        

        self.derivTitle = QLabel("CALCSTUDIO")
        self.derivCont1Head1Layout.addWidget(self.derivTitle)
        self.derivTitle.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 80px;
            color: #595959;
            font-weight: bold;
        """)
        self.derivTitle.setAlignment(Qt.AlignLeft | Qt. AlignVCenter)
        self.derivTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.derivSubTitle = QLabel("Derivatives: Tangent Line")
        self.derivCont1Head1Layout.addWidget(self.derivSubTitle,)
        self.derivSubTitle.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.derivSubTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        ### --- Content in Heading Container --- ### End

        self.derivCont1Space2 = QWidget()
        self.derivCont1HeadLayout.addWidget(self.derivCont1Space2, stretch=2)
        self.derivSubTitle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.derivCont1Space2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        ## --- Heading Container --- ## End

        self.derivSpace20 = QWidget()
        self.derivCont1Layout.addWidget(self.derivSpace20, stretch=41)

        ## --- Info Container -- ## Start
        self.derivCont1Info = QWidget()
        self.derivCont1Layout.addWidget(self.derivCont1Info, stretch=192)
        self.derivInfoContLayout = QHBoxLayout(self.derivCont1Info)
        self.derivInfoContLayout.setContentsMargins(0, 0, 0, 0)
        self.derivInfoContLayout.setSpacing(0)

        self.derivCont1Space3 = QWidget()
        self.derivInfoContLayout.addWidget(self.derivCont1Space3, stretch=1)

        ### --- Content in Info Container --- ### Start
        self.derivCont1Info1 = QWidget()
        self.derivInfoContLayout.addWidget(self.derivCont1Info1, stretch=14)
        self.derivInfoContLayout1 = QVBoxLayout(self.derivCont1Info1)
        self.derivInfoContLayout1.setContentsMargins(0, 0, 0, 0)
        self.derivInfoContLayout1.setSpacing(20)

        self.input = QLineEdit()
        self.input.setPlaceholderText("  Function Input: ")
        self.derivInfoContLayout1.addWidget(self.input, stretch=4)
        self.input.setStyleSheet("""
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
        self.input.setFixedHeight(50)

        self.derivXValue = QLabel("Input X Value:")
        self.derivInfoContLayout1.addWidget(self.derivXValue)
        self.derivXValue.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.derivXValue.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(-100)
        self.slider.setMaximum(100)
        self.slider.setValue(1)
        self.slider.valueChanged.connect(self.derivative)
        self.derivInfoContLayout1.addWidget(self.slider)
        self.slider.setStyleSheet("""
        QSlider::groove:horizontal {
            border: 1px solid #999999;
            height: 8px;
            background: #dddddd;
            border-radius: 4px;
        }

        QSlider::handle:horizontal {
            background: #FF6A6A;
            border: 1px solid #5c5c5c;
            width: 16px;
            height: 16px;
            margin: -4px 0;
            border-radius: 8px;
        }

        QSlider::sub-page:horizontal {
            background: #FF6A6A;
            border-radius: 4px;
        }

        QSlider::add-page:horizontal {
            background: #cccccc;
            border-radius: 4px;
        }
    """)

        self.derLabel = QLabel("Derivative:")
        self.derivInfoContLayout1.addWidget(self.derLabel)
        self.derLabel.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.derivXValue.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.derivTangLine = QLabel("Tangent Line:")
        self.derivInfoContLayout1.addWidget(self.derivTangLine)
        self.derivTangLine.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.derivTangLine.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        ### --- Content in Info Container --- ### End

        self.derivSpace = QWidget()
        self.derivInfoContLayout.addWidget(self.derivSpace, stretch=1)

        ## --- Info Container --- ## End

        self.derivSpace19 = QWidget()
        self.derivCont1Layout.addWidget(self.derivSpace19, stretch=43)

        ## --- Button Container --- ## Start
        self.derivCont1Button = QWidget()
        self.derivCont1Layout.addWidget(self.derivCont1Button, stretch=46)
        self.derivCont1ButtonLayout = QHBoxLayout(self.derivCont1Button)
        self.derivCont1ButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.derivCont1ButtonLayout.setSpacing(0)

        self.derivCont1Space10 = QWidget()
        self.derivCont1ButtonLayout.addWidget(self.derivCont1Space10, stretch=1)
        
        self.derivSubmit = QPushButton("DIFFERENTIATE")
        self.derivSubmit.clicked.connect(self.setfunction)
        self.derivCont1ButtonLayout.addWidget(self.derivSubmit, stretch=6)
        self.derivSubmit.setStyleSheet("""
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

        self.derivCont1Space11 = QWidget()
        self.derivCont1ButtonLayout.addWidget(self.derivCont1Space11, stretch=1)

        ## --- Button Container --- ## End

        self.derivSpace29 = QWidget()
        self.derivCont1Layout.addWidget(self.derivSpace29, stretch=146)

        # --- Container One --- # End

        # --- Container Two --- # Start
        self.derivCont2 = QWidget()
        self.derivCont2Layout = QVBoxLayout(self.derivCont2)
        self.derivCont2Layout.setContentsMargins(10, 10, 10, 10)
        self.derivCont2Layout.setSpacing(0)
        self.derivLayout.addWidget(self.derivCont2, stretch=45)
        # self.derivCont2.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;        
        # """)

        self.canvas = FigureCanvas(plt.Figure(figsize=(6, 7)))
        self.canvas.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.derivCont2Layout.addWidget(self.canvas)
        self.insert_ax()

        # --- Container Two --- # End

    def classifyFunction(self, function):
        x = symbols("x")
        self.funcType = "other"
        numer, denom = function.as_numer_denom()

        if function.is_constant():
            self.funcType = "constant"
            return

        if function.has(log):
            self.funcType = "logarithmic"
            return

        if function.has(sin, cos):
            self.funcType = "trigonometric"
            return

        for p in function.atoms(Pow):
            base, exponent = p.args
            if exponent.has(x) and base.is_number:
                self.funcType = "exponential"
                return
        if function.has(exp):
            self.funcType = "exponential"
            return

        if denom == 1 and function.is_polynomial():
            self.funcType = "polynomial"
            return

        if function.is_rational_function():
            self.funcType = "rational"
            return

        for p in function.atoms(Pow):
            if p.exp.is_Rational and p.exp < 1:
                self.funcType = "root"
                return

        self.funcType = "other"
    
    def setfunction(self):
        self.func_str = self.input.text().strip()
        if not self.func_str:
            self.func_str = "x"
        print(f"Stored input: {self.func_str}")

        x = symbols("x")
        try:
            func = sympify(self.func_str)
        except Exception:
            func = x

        self.classifyFunction(func)
        self.slider.setValue(0)

        if self.funcType == "trigonometric":
            self.slider.setMinimum(-6)
            self.slider.setMaximum(6)
        else:
            self.slider.setMinimum(-100)
            self.slider.setMaximum(100)

    # Function that differentiates input function and plots it on the graph
    def derivative(self, value):
        if not hasattr(self, 'func_str'):
            return
        value = float(value)
        x = symbols("x")

        self.derivXValue.setText("Input X Value:")

        # Step 1: Parse Inputs; Differentiation
        try:
            func = sympify(self.func_str)
            deriv = diff(func, x)
            slope = deriv.subs(x, value).evalf()
            y_val = func.subs(x, value).evalf()
            if slope == zoo or y_val == zoo or slope.is_infinite or y_val.is_infinite:
                self.derivXValue.setText("Error: Value at x is infinite or undefined.")
                self.derLabel.setText("Derivative at x = ? : undefined")
                self.derivTangLine.setText("Tangent Line: undefined")
                self.ax.clear()
                self.canvas.draw()
                return

            if not slope.is_real or not y_val.is_real:
                self.derivXValue.setText("Error: Value at x is complex (non-real).")
                self.derLabel.setText("Derivative at x = ? : complex")
                self.derivTangLine.setText("Tangent Line: complex")
                self.ax.clear()
                self.canvas.draw()
                return
            
        except Exception as e:
            print(f"Input Error: {e}")
            self.derivXValue.setText("Invalid input; Error Calculating Derivative.")
            return
    
        funcType = self.funcType
        print(funcType)

        tangent_line = slope * x - slope * value + y_val
        y_intercept = y_val - slope * value
        self.derLabel.setText(f"Derivative at x = {value}: {slope:.4f}")
        self.derivTangLine.setText(f"Tangent Line: {slope:.4f}x - {y_intercept:.4f} ")

        # Step 2: x Range Calculation
        try:
            
            if funcType == "trigonometric":
                range_width = 7
            else:
                range_width = 100
            x_min = value - range_width
            x_max = value + range_width
            x_points = np.linspace(x_min, x_max, 400)

            func_np = lambdify(x, func, 'numpy')
            tangent_np = lambdify(x, tangent_line, 'numpy')
        except Exception as e:
            print(f"x Range Calculation Error: {e}")
            self.derivXValue.setText("x Range Calculation Error.")
            return

        # Step 3: y Range Calculation
        try:
            y_func_np = func_np(x_points)
            y_tangent_np = tangent_np(x_points)

            if np.ndim(y_func_np) == 0:
                y_func_np = np.full_like(x_points, y_func_np)

            if np.ndim(y_tangent_np) == 0:
               y_tangent_np = np.full_like(x_points, y_tangent_np)

            y_all = np.concatenate([y_func_np, y_tangent_np])
            finite_y = y_all[np.isfinite(y_all)]

            if finite_y.size == 0:
                self.show_error("Function has no finite values in this range")
                return

            y_min = np.min(finite_y)
            y_max = np.max(finite_y)

            y_margin = 0.1 * (y_max - y_min) if y_max != y_min else 1

        except Exception as e:
            print(f"y Range Calculation Error: {e}")
            self.derivXValue.setText("y Range Calculation Error.")
            return

        # Step 4: Plotting
        try:
            self.ax.clear()
            self.ax.set_xlim([x_min, x_max])
            self.ax.set_ylim([y_min - y_margin, y_max + y_margin])

            self.ax.plot(x_points, y_tangent_np, label="Tangent Line", color='black')
            self.ax.plot(x_points, y_func_np, label="Function", color='red')
            self.ax.axhline(0, color='black', linestyle=':')
            self.ax.axvline(0, color='black', linestyle=':')

            self.ax.legend()
            self.canvas.draw()
        except Exception as e:
            print(f" Plotting Error: {e}")
            self.derivXValue.setText("Error Plotting Function")
            return

    def insert_ax(self):
        self.ax = self.canvas.figure.subplots()
        self.bar = None