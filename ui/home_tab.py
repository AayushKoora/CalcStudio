from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSizePolicy)
from  PyQt5.QtCore import Qt
from style.colors import Colors

class HomeTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet(f"background-color: {Colors.LIGHTGRAY};")
        self.init_ui()

    def init_ui(self):
        
        # === Home Tab ===
        self.homeLayout = QHBoxLayout(self)
        self.setLayout(self.homeLayout)

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

        self.title = QLabel("CALCSTUDIO")
        self.homeCont1Layout.addWidget(self.title)
        self.title.setStyleSheet("""
            font-family: 'Arial';
            font-size: 80px;
            color: #595959;
        """)
        self.title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.title.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.description = QLabel("Calculus Visualization Tool")
        self.homeCont1Layout.addWidget(self.description)
        self.description.setStyleSheet("""
            font-family: 'Arial';
            font-size: 50px;
            color: #595959;
        """)
        self.description.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.empty1 = QWidget()
        self.homeCont1Layout.addWidget(self.empty1, stretch=3)

        self.buttonCont = QWidget()
        self.buttonContLayout = QHBoxLayout(self.buttonCont)
        self.homeCont1Layout.addWidget(self.buttonCont, stretch=2)

        self.button1 = QPushButton("Github")
        self.buttonContLayout.addWidget(self.button1, stretch=10)
        self.button1.setStyleSheet("""
            QPushButton {
                background-color: #999999;
                padding: 16px, 16px;
                font-size: 16px;
            }
                                   
            QPushButton:pressed {
                background-color: #88cc88;
            }
        """)

        self.button2 = QPushButton("Tutorial")
        self.buttonContLayout.addWidget(self.button2, stretch=10)
        self.button2.setStyleSheet("""
            QPushButton {
                background-color: #999999;
                padding: 16px, 16px;
                font-size: 16px;
            }
                                   
            QPushButton:pressed {
                background-color: #88cc88;
            }
        """)

        self.buttonSpace = QWidget()
        self.buttonContLayout.addWidget(self.buttonSpace, stretch=30)

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

        self.homeContSpace = QWidget()
        self.homeCont2Layout.addWidget(self.homeContSpace, stretch=8)

        self.tutorial_label = QLabel("CalcStudio Tutorial")
        self.homeCont2Layout.addWidget(self.tutorial_label)
        self.tutorial_label.setStyleSheet("""
            font-family: 'Arial';
            font-size: 40px;
            color: #595959;
            border: 1px solid black;
            border-radius: 2px;
            background-color: #999999;
        """)
        self.tutorial_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.tutorial_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.tutorial = QLabel("Coming Soon")
        self.homeCont2Layout.addWidget(self.tutorial, stretch=70)
        self.tutorial.setStyleSheet("""
            font-family: 'Arial';
            font-size: 20px;
            color: #595959;
            border: 1px solid black;
            border-radius: 2px;
            background-color: #ffffff;
        """)