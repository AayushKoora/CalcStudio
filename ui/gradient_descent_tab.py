from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSizePolicy
from  PyQt5.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from sympy import *
from style.colors import Colors
import random

class GradientDescentTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet(f"background-color: {Colors.LIGHTGRAY};")
        self.init_ui()

    def init_ui(self):

        # === Gradient Descent ===
        self.grdLayout = QHBoxLayout(self)
        self.setLayout(self.grdLayout)

        # --- Container One ---
        self.grdCont1 = QWidget()
        self.grdCont1Layout = QVBoxLayout(self.grdCont1)
        self.grdLayout.addWidget(self.grdCont1, stretch=4)
        # self.grdCont1.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)

        self.grdTitle = QLabel("CALCSTUDIO")
        self.grdCont1Layout.addWidget(self.grdTitle)
        self.grdTitle.setStyleSheet("""
            font-family: 'Arial';
            font-size: 80px;
            color: #595959;
        """)
        self.grdTitle.setAlignment(Qt.AlignLeft | Qt. AlignVCenter)
        self.grdTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grdSubTitle = QLabel("Multivariable: Gradient Descent")
        self.grdCont1Layout.addWidget(self.grdSubTitle)
        self.grdSubTitle.setStyleSheet("""
            font-family: 'Arial';
            font-size: 50px;
            color: #595959;
        """)
        self.grdSubTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grdFuncLabel = QLabel("Function Input: ")
        self.grdCont1Layout.addWidget(self.grdFuncLabel)
        self.grdFuncLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.grdFuncLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grdFuncCont = QWidget()
        self.grdCont1Layout.addWidget(self.grdFuncCont)
        self.grdFuncContLayout = QHBoxLayout(self.grdFuncCont)
        self.grdFuncCont.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grdFuncInput = QLineEdit()
        self.grdFuncContLayout.addWidget(self.grdFuncInput, stretch=4)
        self.grdFuncInput.setStyleSheet("""
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
        self.grdFuncInput.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grdSubmit = QPushButton("Submit")
        self.grdSubmit.clicked.connect(self.timer)
        self.grdFuncContLayout.addWidget(self.grdSubmit, stretch=1)
        self.grdSubmit.setStyleSheet("""
            QPushButton {
                background-color: #999999;
                padding: 16px, 16px;
                font-size: 16px;
            }
                                   
            QPushButton:pressed {
                background-color: #88cc88;
            }
        """)

        self.grdLearnLabel = QLabel("Learning Rate: ")
        self.grdCont1Layout.addWidget(self.grdLearnLabel)
        self.grdLearnLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.grdLearnLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grdLearnInput = QLineEdit()
        self.grdCont1Layout.addWidget(self.grdLearnInput)
        self.grdLearnInput.setStyleSheet("""
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
        self.grdLearnInput.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grdContourLabel = QLabel("Contour Plot ")
        self.grdCont1Layout.addWidget(self.grdContourLabel)
        self.grdContourLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.grdContourLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grdFailLabel = QLabel("...")
        self.grdCont1Layout.addWidget(self.grdFailLabel)
        self.grdFailLabel.setStyleSheet("""
            font-family: 'Arial';
            font-size: 30px;
            color: #595959;
        """)
        self.grdFailLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        # --- Container Two ---
        self.grdCont2 = QWidget()
        self.grdCont2Layout = QVBoxLayout(self.grdCont2)
        self.grdLayout.addWidget(self.grdCont2, stretch=6)
        # self.grdCont2.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)

        self.fig = Figure()
        self.grdCanvas = FigureCanvas(self.fig)
        self.grdCont2Layout.addWidget(self.grdCanvas)
        self.axGrd = self.fig.add_subplot(111, projection = '3d')

        self.timer = QTimer()
        self.timer.timeout.connect(self.gradientDescent)

    def parseInputs(self):
        self.x, self.y = symbols("x y")

        self.grdFailLabel.setText(f"...")

        try:
            self.x0 = float(random.randint(1, 100))
            self.y0 = float(random.randint(1, 100))
            self.learning_rate = float(self.grdLearnInput.text())
            self.grdFunc = sympify(self.grdFuncInput.text())
            self.XgrdDeriv = diff(self.grdFunc, self.x)
            self.YgrdDeriv = diff(self.grdFunc, self.y)
        except Exception as e:
            self.grdFailLabel.setText(f"Invalid input.")


        self.step_x, self.step_y = 1.0, 1.0
        self.n = 0


    def gradientDescent(self):

        if abs(self.step_x) <= .001 or abs(self.step_y) <= .001:
            self.timer.stop()
            self.grdContourLabel.setText(f"Converged at step {self.n}")
            return
        else:
            try:
                self.step_x = float(self.learning_rate*self.XgrdDeriv.subs({self.x: self.x0, self.y: self.y0}))
                self.step_y = float(self.learning_rate*self.YgrdDeriv.subs({self.x: self.x0, self.y: self.y0}))

                self.x0 = self.x0 - self.step_x
                self.y0 = self.y0 - self.step_y

                z = float(self.grdFunc.subs({self.x: self.x0, self.y: self.y0}))
                self.n += 1

                self.grdContourLabel.setText(f"Step {self.n}: (x: {self.x0:.4f}, y: {self.y0:.4f}, z: {z:.4f})")
                print(f"Step {self.n}: ({self.x0, self.y0, z})")
            except Exception as e:
                self.grdFailLabel.setText("Error Computing Algorithm")

        self.axGrd.clear()

        self.axGrd.set_xlabel('X Axis')
        self.axGrd.set_ylabel('Y Axis')
        self.axGrd.set_zlabel('Z Axis')

        x_val = np.linspace(1, 100, 100)
        y_val = np.linspace(1, 100, 100)

        X, Y = np.meshgrid(x_val, y_val)

        try:
            np_func = lambdify((self.x, self.y), self.grdFunc)
            Z = np_func(X, Y)

            self.axGrd.plot_surface(X, Y, Z, alpha=.5)
            self.axGrd.scatter(self.x0, self.y0, z, color='red', s=50)
            self.grdCanvas.draw()
        except Exception as e:
            self.grdFailLabel.setText(f"Error Plotting Function.")

        return
    
    def timer(self):
        self.parseInputs()
        if not self.timer.isActive():
            self.timer.start(500)
