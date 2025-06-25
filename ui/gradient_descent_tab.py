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

        # === Gradient Descent === # Start
        self.grdLayout = QHBoxLayout(self)
        self.setLayout(self.grdLayout)
        self.grdLayout.setContentsMargins(0, 0, 0, 0)
        self.grdLayout.setSpacing(0)

        # --- Container One --- # Start
        self.grdCont1 = QWidget()
        self.grdCont1Layout = QVBoxLayout(self.grdCont1)
        self.grdLayout.addWidget(self.grdCont1, stretch=55)
        self.grdCont1Layout.setContentsMargins(0, 0, 0, 0)
        self.grdCont1Layout.setSpacing(0)
        # self.grdCont1.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)

        self.grdCont1Space0 = QWidget()
        self.grdCont1Layout.addWidget(self.grdCont1Space0, stretch=41)

        ## --- Heading Container --- ## Start
        self.grdCont1Head = QWidget()
        self.grdCont1HeadLayout = QHBoxLayout(self.grdCont1Head)
        self.grdCont1Layout.addWidget(self.grdCont1Head, stretch=96)
        self.grdCont1HeadLayout.setContentsMargins(0, 0, 0, 0)
        self.grdCont1HeadLayout.setSpacing(0)

        self.grdCont1Space1 = QWidget()
        self.grdCont1HeadLayout.addWidget(self.grdCont1Space1, stretch=2)
        self.grdCont1Space1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        ### --- Content in Heading Container --- ### Start
        self.grdCont1Head1 = QWidget()
        self.grdCont1Head1Layout = QVBoxLayout(self.grdCont1Head1)
        self.grdCont1HeadLayout.addWidget(self.grdCont1Head1, stretch=2)
        self.grdCont1Head1Layout.setContentsMargins(0, 0, 0, 0)
        self.grdCont1Head1Layout.setSpacing(0)

        self.grdTitle = QLabel("CALCSTUDIO")
        self.grdCont1Head1Layout.addWidget(self.grdTitle)
        self.grdTitle.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 80px;
            color: #595959;
            font-weight: bold;
        """)
        self.grdTitle.setAlignment(Qt.AlignLeft | Qt. AlignVCenter)
        self.grdTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grdSubTitle = QLabel("Multivariable: Gradient Descent")
        self.grdCont1Head1Layout.addWidget(self.grdSubTitle)
        self.grdSubTitle.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.grdSubTitle.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        ### --- Content in Heading Container --- ### End

        self.grdCont1Space2 = QWidget()
        self.grdCont1HeadLayout.addWidget(self.grdCont1Space2, stretch=2)
        self.grdSubTitle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.grdCont1Space2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        ## --- Heading Container --- ## End

        self.grdSpace20 = QWidget()
        self.grdCont1Layout.addWidget(self.grdSpace20, stretch=37)

        ## --- Info Container --- ## Start
        self.grdCont1Info = QWidget()
        self.grdCont1Layout.addWidget(self.grdCont1Info, stretch=124)
        self.grdInfoContLayout = QHBoxLayout(self.grdCont1Info)
        self.grdInfoContLayout.setContentsMargins(0, 0, 0, 0)
        self.grdInfoContLayout.setSpacing(0)

        self.grdCont1Space3 = QWidget()
        self.grdInfoContLayout.addWidget(self.grdCont1Space3, stretch=1)

        ### --- Content in Info Container --- ### Start
        self.grdCont1Info1 = QWidget()
        self.grdInfoContLayout.addWidget(self.grdCont1Info1, stretch=14)
        self.grdInfoContLayout1 = QVBoxLayout(self.grdCont1Info1)
        self.grdInfoContLayout1.setContentsMargins(0, 0, 0, 0)
        self.grdInfoContLayout1.setSpacing(20)

        self.grdFuncInput = QLineEdit()
        self.grdInfoContLayout1.addWidget(self.grdFuncInput, stretch=4)
        self.grdFuncInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grdFuncInput.setAlignment(Qt.AlignLeft)
        self.grdFuncInput.setPlaceholderText("  Function Input: ")
        self.grdFuncInput.setStyleSheet("""
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
        self.grdFuncInput.setFixedHeight(50)

        self.grdLearnInput = QLineEdit()
        self.grdInfoContLayout1.addWidget(self.grdLearnInput)
        self.grdLearnInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grdLearnInput.setAlignment(Qt.AlignLeft)
        self.grdLearnInput.setPlaceholderText("  Learning Rate: ")
        self.grdLearnInput.setStyleSheet("""
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
        self.grdLearnInput.setFixedHeight(50)

        self.grdContourLabel = QLabel("Values: ")
        self.grdInfoContLayout1.addWidget(self.grdContourLabel)
        self.grdContourLabel.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.grdContourLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.grdFailLabel = QLabel("...")
        self.grdInfoContLayout1.addWidget(self.grdFailLabel)
        self.grdFailLabel.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.grdFailLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        ### --- Content in Info Container --- ### End

        self.grdCont1Space8 = QWidget()
        self.grdInfoContLayout.addWidget(self.grdCont1Space8, stretch=1)

        ## --- Info Container --- ## End

        self.grdCont1Space9 = QWidget()
        self.grdCont1Layout.addWidget(self.grdCont1Space9, stretch=147)

        ## --- Button Container --- ## Start
        self.grdCont1Button = QWidget()
        self.grdCont1Layout.addWidget(self.grdCont1Button, stretch=46)
        self.grdCont1ButtonLayout = QHBoxLayout(self.grdCont1Button)
        self.grdCont1ButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.grdCont1ButtonLayout.setSpacing(0)

        self.grdCont1Space10 = QWidget()
        self.grdCont1ButtonLayout.addWidget(self.grdCont1Space10, stretch=1)

        self.grdSubmit = QPushButton("MINIMIZE")
        self.grdSubmit.clicked.connect(self.startTimer)
        self.grdCont1ButtonLayout.addWidget(self.grdSubmit, stretch=6)
        self.grdSubmit.setStyleSheet("""
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

        self.grdCont1Space11 = QWidget()
        self.grdCont1ButtonLayout.addWidget(self.grdCont1Space11, stretch=1)

        ## --- Button Container --- ## End

        self.grdSpace = QWidget()
        self.grdCont1Layout.addWidget(self.grdSpace, stretch=108)

        # --- Container One --- # End

        # --- Container Two --- # Start
        self.grdCont2 = QWidget()
        self.grdCont2Layout = QVBoxLayout(self.grdCont2)
        self.grdLayout.addWidget(self.grdCont2, stretch=45)
        # self.grdCont2.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)

        self.fig = Figure(figsize=(6, 7))
        self.grdCanvas = FigureCanvas(self.fig)
        self.grdCanvas.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.grdCont2Layout.addWidget(self.grdCanvas)
        self.axGrd = self.fig.add_subplot(111, projection = '3d')

        self.timer = QTimer()
        self.timer.timeout.connect(self.gradientDescent)

        # --- Container Two --- # End

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
            self.grdContourLabel.setText(f"Converged at Step {self.n}")
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
            np_func = lambdify((self.x, self.y), self.grdFunc, 'numpy')
            Z = np_func(X, Y)

            if not isinstance(Z, np.ndarray):
                Z = np.full_like(X, Z)

            if not np.all(np.isfinite(Z)):
                self.grdFailLabel.setText("Function undefined/infinite in plotting region.")
                self.timer.stop()
                self.axGrd.clear()
                self.grdCanvas.draw()
                return

            self.axGrd.plot_surface(X, Y, Z, alpha=0.5, color='#FF6A6A')

            if not np.isfinite(z):
                self.grdFailLabel.setText("Z value is not finite.")
                self.timer.stop()
                self.axGrd.clear()
                self.grdCanvas.draw()
                return

            self.axGrd.scatter(self.x0, self.y0, z, color='black', s=50)
            self.grdCanvas.draw()
        except Exception as e:
            self.grdFailLabel.setText(f"Error Plotting Function.")
            return
    
    def startTimer(self):
        self.parseInputs()
        if not self.timer.isActive():
            self.timer.start(500)
