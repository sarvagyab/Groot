from PySide2 import QtWidgets, QtCore, QtGui

# import GUIs
from GUIs.mainWindowPTE import Ui_Groot

# import modules
from modules.GUIchanges import fixTreeViewScrolling, createNotebook, createSubNotebook, createNote, rename, dlt
import mainWindowFunctions
from modules.treeHandling import isNote


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

        self.ui.treeWidget.customContextMenuRequested.connect(self.showMenu)

        # Load tree structure and notes
        self.reloadUI()

        # Timer for Loading the Markdown view when the user has stopped typing for a duration
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)

        # Display notes in Markdown
        self._markdownViewer()

        # Encrypt Note
        self.encryptNote()

        # Decrypt Note
        self.decryptNote()

        # Display UI
        self.showMaximized()


    def showMenu(self,pos):
        item = self.ui.treeWidget.itemAt(pos)
        if item is None:
            return
        menu = QtWidgets.QMenu()
        if item is self.ui.treeWidget.topLevelItems(0):
            menu.addAction(createNotebook)
        elif item is self.ui.treeWidget.topLevelItems(1):
            menu.addAction(createNote)
        else:
            menu.addAction(rename)
            menu.addAction(dlt)
            dets = isNote(item)
            if(dets[0]):
                pass
            else:
                menu.addAction(createSubNotebook)
                menu.addAction(createNote)
        menu.exec_(self.ui.treeWidget.mapToGlobal(pos))





Window._noteLoader = mainWindowFunctions._noteLoader
Window.closeEvent = mainWindowFunctions.closeEvent
Window.reloadUI = mainWindowFunctions.reloadUI
Window.decryptNote = mainWindowFunctions.decryptNote
Window.encryptNote = mainWindowFunctions.encryptNote
Window._markdownViewer = mainWindowFunctions._markdownViewer
Window._delayChecker = mainWindowFunctions._delayChecker