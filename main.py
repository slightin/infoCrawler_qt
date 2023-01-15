import sys
# from PyQt5.QtGui import QIcon
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("ciap")
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.Ui_main import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # MainWindow.setWindowIcon(QIcon('logo.ico'))
    MainWindow.show()
    sys.exit(app.exec_())