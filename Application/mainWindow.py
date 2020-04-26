from PySide2 import QtWidgets, QtCore, QtGui

# import GUIs
from GUIs.mainWindowPTE import Ui_Groot

# import modules
from modules.GUIchanges import fixTreeViewScrolling, createNotebook, createSubNotebook, createNote, rename, dlt
import mainWindowFunctions


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

        # Connections for renaming
        self.ui.treeWidget.itemDoubleClicked.connect(self.ui.treeWidget.editItem)
        rename.triggered.connect(lambda: self.ui.treeWidget.editItem(self.ui.treeWidget.currentItem(),0))
        self.ui.treeWidget.itemChanged.connect(self._renameNote)

        # Connections for deleting
        dlt.triggered.connect(self.showDeleteDialog)

        # Load tree structure and notes
        self.reloadUI()

        # Timer for Loading the Markdown view when the user has stopped typing for a duration
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)

        # Display notes in Markdown
        self._markdownViewer()

        # Display UI
        self.showMaximized()

        # shortcut bindings
        self.shortcutBinding()

        # Encrypt Note
        self.encryptNote()

        # Decrypt Note
        self.decryptNote()

        # Search in current note
        self.searchInNote()

        # Search mode changed
        self.searchModeChanged()

        # Find next occurance
        self.findNextOccurance()

        # Find prev occurance
        self.findPrevOccurance()

        # Finished search
        self._finishedSearch()
    





Window._noteLoader = mainWindowFunctions._noteLoader
Window.closeEvent = mainWindowFunctions.closeEvent
Window.reloadUI = mainWindowFunctions.reloadUI
Window.decryptNote = mainWindowFunctions.decryptNote
Window.encryptNote = mainWindowFunctions.encryptNote
Window._markdownViewer = mainWindowFunctions._markdownViewer
Window._delayChecker = mainWindowFunctions._delayChecker
Window.showMenu = mainWindowFunctions.showMenu
Window.searchInNote = mainWindowFunctions.searchInNote
Window.searchModeChanged = mainWindowFunctions.searchModeChanged
Window.findNextOccurance = mainWindowFunctions.findNextOccurance
Window.findPrevOccurance = mainWindowFunctions.findPrevOccurance
Window._finishedSearch = mainWindowFunctions._finishedSearch
Window.shortcutBinding = mainWindowFunctions.shortcutBinding
Window.showDeleteDialog = mainWindowFunctions.showDeleteDialog
Window._renameNote = mainWindowFunctions._renameNote