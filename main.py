from qt_import import *
from gui.windows.gui_main_window import *
import os
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # WINDOW TITLE
        self.setWindowTitle("Controle de Estoque em Python e PySide6")

        self.gui = GUI_MainWindow()
        self.gui.setup_gui(self)

        # SHOW MAIN WINDOW
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
