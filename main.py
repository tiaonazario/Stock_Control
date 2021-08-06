from qt_import import *
import os
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window Title
        self.setWindowTitle("Controle de Estoque em Python e PySide6")

        # Show Main Window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
