from GUIs.mainWindowPTE import Ui_Groot
from modules.treeHandling import fixTreeViewScrolling, loadfileStructure, noteLoader
from modules.markdownHandling import viewInMarkdown
from PySide2 import QtWidgets
import sys


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Groot()
        self.ui.setupUi(self)

        fixTreeViewScrolling(self.ui.treeWidget)
        loadfileStructure(self.ui.treeWidget)
        self.noteChanger()
        # self.markdownViewer()

        self.show()


    def noteChanger(self):
        self.ui.treeWidget.itemSelectionChanged.connect(self.noteChanged)
    
    def noteChanged(self):
        noteLoader(self.ui.treeWidget.selectedItems()[0],self.ui)

    def markdownViewer(self):
        self.ui.plainTextEdit.textChanged.connect(self.textChanged)
    
    def textChanged(self):
        viewInMarkdown(self.ui.plainTextEdit.toPlainText(), self.ui.mdViewer)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())