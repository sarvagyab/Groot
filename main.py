from GUIs.mainWindow import Ui_Groot
from modules.treeHandling import fixTreeViewScrolling
from PySide2 import QtWidgets
import sys


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Groot()
        self.ui.setupUi(self)

        fixTreeViewScrolling(self.ui.treeWidget)

        self.show()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())