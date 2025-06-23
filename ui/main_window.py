from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QSizePolicy
,QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from style.colors import Colors
from ui.home_tab import HomeTab
from ui.derivative_tab import DerivativeTab
from ui.integral_tab import IntegralTab
from ui.riemannsum_tab import RiemannSumTab
from ui.gradient_descent_tab import GradientDescentTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CalcStudio")
        self.setMinimumHeight(800)
        self.setMinimumWidth(1422)
        self.showFullScreen()
        self.setStyleSheet(f"background-color: {Colors.SECONDARY};")
        self.init_ui()

    def init_ui(self):

        # === Main Container ===
        mainContainer = QWidget()
        mainLayout = QVBoxLayout(mainContainer)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setCentralWidget(mainContainer)

        # --- Top Bar ---
        topContainer = QWidget()
        topContainer.setStyleSheet(f"background-color: {Colors.DARKGRAY};")
        mainLayout.addWidget(topContainer, stretch=1)
        topContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        topContainer.setStyleSheet(f"background-color: {Colors.SECONDARY}")

        # --- Main Content Area ---
        middleContainer = QWidget()
        middleLayout = QHBoxLayout(middleContainer)
        mainLayout.addWidget(middleContainer, stretch=18)
        middleLayout.setContentsMargins(0, 0, 0, 0)
        middleLayout.setSpacing(0)
        middleContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        wrapperContainer = QWidget()
        middleLayout.addWidget(wrapperContainer, stretch=40)
        wrapperLayout = QHBoxLayout(wrapperContainer)
        wrapperLayout.setContentsMargins(0, 10, 10, 10)

        contentContainer = QTabWidget()
        wrapperLayout.addWidget(contentContainer)

        contentContainer.addTab(HomeTab(self), "Home")
        contentContainer.addTab(DerivativeTab(self), "Derivative")
        contentContainer.addTab(IntegralTab(self), "Integral")
        contentContainer.addTab(RiemannSumTab(self), "Riemann Sum")
        contentContainer.addTab(GradientDescentTab(self), "Gradient Descent")
        contentContainer.setTabPosition(QTabWidget.West)
        contentContainer.setStyleSheet("""
            QTabWidget::pane {
                background-color: {Colors.PRIMARY};
                border-radius: 10px;
            }

            QTabBar::tab {
                height: 125px;
                width: 30px;
                background: "#A9A8A8";
                color: white;
                padding: 10px;
                margin: 2px;
                border-radius: 9px;
                font-size: 17px;
                font-family: 'Helvetica';
            }

            QTabBar::tab:selected {
                background: "#FF6A6A";
                color: white;
            }                  
        """)
        contentContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        middleShadow = QGraphicsDropShadowEffect()
        middleShadow.setBlurRadius(20)
        middleShadow.setXOffset(4)
        middleShadow.setYOffset(4)
        middleShadow.setColor(QColor(0, 0, 0, 100))
        contentContainer.setGraphicsEffect(middleShadow)

        middleSpace = QWidget()
        middleLayout.addWidget(middleSpace, stretch=1)

        # --- Bottom Bar ---
        bottomContainer = QWidget()
        bottomContainer.setStyleSheet(f"background-color: {Colors.SECONDARY};")
        mainLayout.addWidget(bottomContainer, stretch=1)
        bottomContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)