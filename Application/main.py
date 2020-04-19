from GUIs.mainWindowPTE import Ui_Groot
from modules.treeHandling import fixTreeViewScrolling, loadfileStructure, noteLoader
from modules.markdownHandling import viewInMarkdown
from PySide2 import QtWidgets, QtCore
import sys


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Initializing UI
        self.ui = Ui_Groot()
        self.ui.setupUi(self)
        
        # Fix no Scrollbar issue in notes tree when file names go out of box
        fixTreeViewScrolling(self.ui.treeWidget)

        # Load notes in notes Tree
        loadfileStructure(self.ui.treeWidget)

        # Switching notes in textEdit
        self._noteLoader()

        # Display notes in Markdown
        self.markdownViewer()

        # Display UI
        self.show()


    def _noteLoader(self):
        changeNote = lambda : noteLoader(self.ui.treeWidget.selectedItems()[0],self.ui.fileName,self.ui.plainTextEdit)
        self.ui.treeWidget.itemSelectionChanged.connect(changeNote)

    def markdownViewer(self):
        loadNew = lambda : viewInMarkdown(self.ui.plainTextEdit.toPlainText(),self.ui.mdViewer)
        self.ui.plainTextEdit.textChanged.connect(loadNew)
    


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())