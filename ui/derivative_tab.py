import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QSlider, QLabel, QSizePolicy
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sympy import symbols, sympify, diff, lambdify
from style.colors import Colors

class DerivativeTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet(f"background-color: {Colors.LIGHTGRAY};")
        self.init_ui()

    def init_ui(self):
        
        # === Derivative Tab ===
        self.derivLayout = QHBoxLayout(self)
        self.setLayout(self.derivLayout)

        # --- Container One ---
        self.derivCont1 = QWidget()
        self.derivCont1Layout = QVBoxLayout(self.derivCont1)
        self.derivCont1Layout.setContentsMargins(0, 0, 0, 0)
        self.derivCont1Layout.setSpacing(0)
        self.derivLayout.addWidget(self.derivCont1, stretch=4)
        # self.derivCont1.setStyleSheet("""
        #     border: 2px solid black;
        #     border-radius: 5px;        
        # """)

        self.derivTitle = QLabel("CALCSTUDIO")
        self.derivCont1Layout.addWidget(self.derivTitle)
        self.derivTitle.setStyleSheet("""
            font-family: 'Arial';
            font-size: 80px;
            color: #595959;
        """)
        self.derivTitle.setAlignment(Qt.AlignLeft | Qt. AlignVCenter)
        self.derivTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.derivSubTitle = QLabel("Derivatives: Tangent Line")
        self.derivCont1Layout.addWidget(self.derivSubTitle,)
        self.derivSubTitle.setStyleSheet("""
            font-family: 'Arial';
            font-size: 50px;
            color: #595959;
        """)
        self.derivSubTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.derivFunc = QLabel("Function Input")
        self.derivCont1Layout.addWidget(self.derivFunc)
        self.derivFunc.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.derivFunc.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.input = QLineEdit()
        self.input.returnPressed.connect(self.setfunction)
        self.derivCont1Layout.addWidget(self.input)
        self.input.setStyleSheet("""
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
        self.input.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.derivXValue = QLabel("X Value:")
        self.derivCont1Layout.addWidget(self.derivXValue)
        self.derivXValue.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.derivXValue.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(1)
        self.slider.valueChanged.connect(self.derivative)
        self.derivCont1Layout.addWidget(self.slider)
        self.slider.setStyleSheet("""
        QSlider::groove:horizontal {
            border: 1px solid #999999;
            height: 8px;
            background: #dddddd;
            border-radius: 4px;
        }

        QSlider::handle:horizontal {
            background: #88cc88;
            border: 1px solid #5c5c5c;
            width: 16px;
            height: 16px;
            margin: -4px 0;
            border-radius: 8px;
        }

        QSlider::sub-page:horizontal {
            background: #88cc88;
            border-radius: 4px;
        }

        QSlider::add-page:horizontal {
            background: #cccccc;
            border-radius: 4px;
        }
    """)
        
        self.label = QLabel("Value: 1")
        self.derivCont1Layout.addWidget(self.label)
        self.label.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.derivSpace = QWidget()
        self.derivCont1Layout.addWidget(self.derivSpace, stretch=1)

        # --- Container Two ---
        self.derivCont2 = QWidget()
        self.derivCont2Layout = QVBoxLayout(self.derivCont2)
        self.derivLayout.addWidget(self.derivCont2, stretch=6)

        self.canvas = FigureCanvas(plt.Figure(figsize=(10, 10)))
        self.derivCont2Layout.addWidget(self.canvas)
        self.insert_ax()

        self.derivCont2.setStyleSheet("""

        border: 2px solid black;
        border-radius: 5px;        

        """)
        
    def setfunction(self):
        self.func_str = self.input.text().strip()
        if not self.func_str:
            self.func_str = "x"
        print(f"Stored input: {self.func_str}")

    def derivative(self, value):
        if not hasattr(self, 'func_str'):
            return

        x = symbols("x")
        func = sympify(self.func_str)
        deriv = diff(func, x)
        slope = deriv.subs(x, value)
        y_val = func.subs(x, value)

        tangent_line = slope * x - slope * value + y_val

        print(f"Tangent Line: {tangent_line}")
        self.label.setText(f"Derivative at x = {value}: {slope}")

        self.ax.clear()
        self.ax.set_ylim([-100, 100])
        self.ax.set_xlim([-100, 100])

        x_points = np.linspace(-100, 100, 200)
        func_np = lambdify(x, func, 'numpy')
        tangent_np = lambdify(x, tangent_line, 'numpy')

        y_func_np = func_np(x_points)
        y_tangent_np = tangent_np(x_points)

        self.ax.plot(x_points, y_tangent_np, label="Tangent Line")
        self.ax.plot(x_points, y_func_np, label="Function")

        self.ax.legend()
        self.canvas.draw()

    def insert_ax(self):
        self.ax = self.canvas.figure.subplots()
        self.ax.set_ylim([-100, 100])
        self.ax.set_xlim([-100, 100])
        self.bar = None