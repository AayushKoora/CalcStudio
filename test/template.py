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
        self.remLayout = QHBoxLayout(self)
        self.setLayout(self.remLayout)

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

        # --- Container Two ---
        self.remCont2 = QWidget()
        self.remCont2Layout = QVBoxLayout(self.remCont2)
        self.remLayout.addWidget(self.remCont2, stretch=6)
        # self.remCont2.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;
        # """)