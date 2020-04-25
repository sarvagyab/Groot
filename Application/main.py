from PySide2 import QtWidgets
from mainWindow import Window
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())