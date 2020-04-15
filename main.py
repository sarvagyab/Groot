from GUIs.groot import Ui_Groot
from PySide2 import QtWidgets
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Groot()
        self.ui.setupUi(self)

        self.ui.treeWidget.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.treeWidget.header().setStretchLastSection(False)

        self.show()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())