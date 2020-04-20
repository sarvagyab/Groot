from PySide2 import QtWidgets, QtCore, QtGui
from GUIs.mainWindowPTE import Ui_Groot
from modules.treeHandling import fixTreeViewScrolling, loadfileStructure, noteLoader
from modules.markdownHandling import viewInMarkdown
import sys


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Initializing UI
        self.ui = Ui_Groot()
        self.ui.setupUi(self)

        self.DELAY = 1000   # Delay in displaying Markdown
        self.mdExtensions = []  # Extensions for changing behaviour of markdown viewer
        
        # Fix no Scrollbar issue in notes tree when file names go out of box
        fixTreeViewScrolling(self.ui.treeWidget)

        # Load notes in notes Tree
        loadfileStructure(self.ui.treeWidget)

        # Timer for Loading the Markdown view when the user has stopped typing for a duration
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)

        # Switching notes in textEdit
        self._noteLoader()

        # Display notes in Markdown
        self._markdownViewer()

        # Display UI
        self.showMaximized() 


    def _delayChecker(self):
        if(self.timer.isActive()):
            self.timer.stop()
        self.timer.start(self.DELAY)


    def _noteLoader(self):
        changeNote = lambda : noteLoader(self.ui.treeWidget.selectedItems()[0],self.ui.fileName,self.ui.plainTextEdit)
        self.ui.treeWidget.itemSelectionChanged.connect(changeNote)


    def _markdownViewer(self):
        mdView = lambda: viewInMarkdown(self.ui.plainTextEdit.toPlainText(),self.mdExtensions,self.ui.mdViewer)
        self.timer.timeout.connect(mdView)
        self.ui.plainTextEdit.textChanged.connect(self._delayChecker)

    

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())