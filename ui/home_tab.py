from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSizePolicy)
from  PyQt5.QtCore import Qt
from style.colors import Colors

class HomeTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet(f"background-color: {Colors.PRIMARY};")
        self.init_ui()

    def init_ui(self):
        
        # === Home Tab ===
        self.homeLayout = QHBoxLayout(self)
        self.setLayout(self.homeLayout)
        self.homeLayout.setContentsMargins(0, 0, 0, 0)
        self.homeLayout.setSpacing(0)

        # --- Space One ---
        self.homeSpace1 = QWidget()
        self.homeLayout.addWidget(self.homeSpace1, stretch=1)
        # self.homeSpace1.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;        
        # """)

        # --- Container One ---
        self.homeCont1 = QWidget()
        self.homeCont1Layout = QVBoxLayout(self.homeCont1)
        self.homeCont1Layout.setSpacing(0)
        self.homeLayout.addWidget(self.homeCont1, stretch=4)
        # self.homeCont1.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;        
        # """)

        self.space = QWidget()
        self.homeCont1Layout.addWidget(self.space, stretch=41)

        self.title = QLabel("CALCSTUDIO")
        self.homeCont1Layout.addWidget(self.title)
        self.title.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 80px;
            color: #595959;
            font-weight: bold;
        """)
        self.title.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.description = QLabel("Calculus Visualization Tool")
        self.homeCont1Layout.addWidget(self.description, stretch=37)
        self.description.setStyleSheet("""
            font-family: 'Helvetica';
            font-size: 30px;
            color: #595959;
        """)
        self.description.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.description.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.empty1 = QWidget()
        self.homeCont1Layout.addWidget(self.empty1, stretch=301)

        self.buttonCont = QWidget()
        self.buttonContLayout = QHBoxLayout(self.buttonCont)
        self.homeCont1Layout.addWidget(self.buttonCont, stretch=41)

        self.button1 = QPushButton("Github")
        self.buttonContLayout.addWidget(self.button1, stretch=10)
        self.button1.setStyleSheet("""
            QPushButton {
                background-color: #FF6A6A;
                padding: 16px, 16px;
                font-size: 16px;
            }
        """)

        self.button2 = QPushButton("Tutorial")
        self.buttonContLayout.addWidget(self.button2, stretch=10)
        self.button2.setStyleSheet("""
            QPushButton {
                background-color: #FF6A6A;
                padding: 16px, 16px;
                font-size: 16px;
            }
        """)

        self.buttonSpace = QWidget()
        self.buttonContLayout.addWidget(self.buttonSpace, stretch=30)

        self.space4 = QWidget()
        self.homeCont1Layout.addWidget(self.space4, stretch=119)

        # --- Space Two ---
        self.homeSpace2 = QWidget()
        self.homeLayout.addWidget(self.homeSpace2, stretch=1)
        # self.homeSpace2.setStyleSheet("""
        # # border: 2px solid black;
        # # border-radius: 5px;        
        # # """)

        # --- Container Two ---
        self.homeCont2 = QWidget()
        self.homeCont2Layout = QVBoxLayout(self.homeCont2)
        self.homeCont2Layout.setSpacing(0)
        self.homeLayout.addWidget(self.homeCont2, stretch=4)
        # self.homeCont2.setStyleSheet("""
        # border: 2px solid black;
        # border-radius: 5px;        
        # """)