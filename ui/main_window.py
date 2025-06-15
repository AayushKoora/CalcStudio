from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget)
from PyQt5.QtCore import Qt
from style.colors import Colors
from ui.home_tab import HomeTab
from ui.derivative_tab import DerivativeTab
from ui.integral_tab import IntegralTab
from ui.riemannsum_tab import RiemannSumTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CalcStudio")
        self.setMinimumHeight(400)
        self.setMinimumWidth(711)
        self.setMaximumHeight(900)
        self.setMaximumWidth(1600)
        self.showFullScreen()
        self.setStyleSheet(f"background-color: {Colors.LIGHTGRAY};")

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

        # --- Main Content Area ---
        contentContainer = QTabWidget()
        mainLayout.addWidget(contentContainer, stretch=8)
        contentContainer.addTab(HomeTab(self), "Home")
        contentContainer.addTab(DerivativeTab(self), "Derivative")
        contentContainer.addTab(IntegralTab(self), "Integral")
        contentContainer.addTab(RiemannSumTab(self), "Riemann Sum")
        contentContainer.setTabPosition(QTabWidget.West)
        contentContainer.setStyleSheet("""
            QTabWidget::pane {
                background-color: #2f2f2f;
                border: 5px solid #595959;
            }

            QTabBar::tab {
                background: #444;
                color: white;
                padding: 10px;
                margin: 2px;
                border-radius: 4px;
            }

            QTabBar::tab:selected {
                background: #88cc88;
                color: black;
            }                  
        """)

        # --- Bottom Bar ---
        bottomContainer = QWidget()
        bottomContainer.setStyleSheet(f"background-color: {Colors.DARKGRAY};")
        mainLayout.addWidget(bottomContainer, stretch=1)