from PySide2 import QtWidgets, QtCore, QtGui

# import GUIs
from GUIs.mainWindowPTE import Ui_Groot

# import modules
from modules.treeHandling import fixTreeViewScrolling, loadfileStructure, noteLoader,itemVal
from modules.markdownHandling import viewInMarkdown
from modules.setPassword import password
from modules.fileHandling import currentNote
from modules.searchInNote import searchText

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Initializing UI
        self.ui = Ui_Groot()
        self.ui.setupUi(self)

        # To be used to change color of Arrows to white in QtreeWidget
        # self.ui.treeWidget.setStyleSheet(
        #     u"QTreeWidget::branch:open{ image:url(white-arrow.png);}"
        # )

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

        # Encrypt Note
        self.encryptNote()

        # Decrypt Note
        self.decryptNote()

        # Display UI
        self.showMaximized()

        #Search in the current note
        self.searchInNote()


    def _delayChecker(self):
        if(self.timer.isActive()):
            self.timer.stop()
        self.timer.start(self.DELAY)


    def _noteLoader(self):
        changeNote = lambda : noteLoader(self.ui.treeWidget.selectedItems()[0],self.ui.fileName,self.ui.plainTextEdit)
        self.ui.treeWidget.itemSelectionChanged.connect(changeNote)


    def _markdownViewer(self):
        mdView = lambda: viewInMarkdown(self.ui.plainTextEdit.toPlainText(),self.mdExtensions,self.ui.mdViewer)
        sFile = lambda: currentNote.saveFile(self.ui.plainTextEdit.toPlainText())
        self.timer.timeout.connect(sFile)
        self.timer.timeout.connect(mdView)
        self.ui.plainTextEdit.textChanged.connect(self._delayChecker)


    def encryptNote(self):
        self.passwdE = password(self)
        self.ui.encryptionButton.clicked.connect(lambda: self.passwdE.openPasswordDialog())

    def decryptNote(self):
        self.passwdD = password(self)
        self.ui.decryptionButton.clicked.connect(lambda: self.passwdD.openVerifyPasswordDialog())

    def searchInNote(self):
        self.ui.searchBar.textChanged.connect(lambda: searchText(self.ui))
    

    def reloadUI(self):
        loadfileStructure(self.ui.treeWidget)
        self._noteLoader()

    def closeEvent(self,event):
        currentNote.saveFile(self.ui.plainTextEdit.toPlainText())
        currentNote.closeFile()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())