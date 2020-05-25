from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from main import *
import sys


class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.WindowInit()

    def Components(self):
        Label1 = QLabel("Hello!", self)

    def WindowInit(self):
        self.setWindowTitle("CV Collector")
        self.resize(200, 200)
        self.setFixedSize(self.size())
        self.Components()
        #self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())