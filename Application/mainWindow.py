from PySide2 import QtWidgets, QtCore, QtGui

# import GUIs
from GUIs.mainWindowPTE import Ui_Groot

# import modules
from modules.GUIchanges import fixTreeViewScrolling, createNotebook, createSubNotebook, createNote, rename, dlt
import mainWindowFunctions
from modules.markdownHandling import bold, italic, numList, bulletList, hyperlink, inlineCode, datetimenow, attachFile

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Initializing UI
        self.ui = Ui_Groot()
        self.ui.setupUi(self)
        self.encryptAll = True
        # Bring the cursor to text editor
        self.ui.plainTextEdit.setFocus()

        # To be used to change color of Arrows to white in QtreeWidget
        # self.ui.treeWidget.setStyleSheet(
        #     u"QTreeWidget::branch:open{ image:url(white-arrow.png);}"
        # )
        self.decryptedNotes= {} # all notes that were encrypted and decrypted in this session
        self.encryptedInSession = {} # all notes that are encrypted in this session

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

        # connection for creating new notebook
        createNotebook.triggered.connect(self._addNotebook)
        self.ui.newNotebook.clicked.connect(self._addNotebook)

        # connection for creating new subnotebook
        createSubNotebook.triggered.connect(self._addSubNotebook)
        self.ui.newSubNotebook.clicked.connect(self._addSubNotebook)

        # connection for creating new note
        createNote.triggered.connect(self._addNote)
        self.ui.newNote.clicked.connect(self._addNote)

        # bold connection
        self.ui.boldButton.clicked.connect(lambda: bold(self.ui.plainTextEdit))

        # italic connection
        self.ui.italicButton.clicked.connect(lambda: italic(self.ui.plainTextEdit))

        # numbered list connection
        self.ui.numberedList.clicked.connect(lambda: numList(self.ui.plainTextEdit))

        # bullet list connection
        self.ui.bullets.clicked.connect(lambda: bulletList(self.ui.plainTextEdit))

        # hyperlink connection
        self.ui.link.clicked.connect(lambda: hyperlink(self.ui.plainTextEdit))

        # inline code connection
        self.ui.code.clicked.connect(lambda: inlineCode(self.ui.plainTextEdit))

        # date time connection
        self.ui.dateTime.clicked.connect(lambda: datetimenow(self.ui.plainTextEdit))

        # attaching file connection
        self.ui.insertFile.clicked.connect(lambda: attachFile(self.ui.plainTextEdit))
        
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

        # open settings
        self.ui.actionSettings.triggered.connect(lambda:self.openSettingsDialog())

        # close main window from menu
        self.ui.actionQuit.triggered.connect(lambda:self.closeDialogAndMainWindow())

        if(self.checkFirstLogin()):
            QtCore.QTimer.singleShot(0,self,self.openLoginDialog())
        else:
            QtCore.QTimer.singleShot(0,self,self.openFirstLoginDialog())




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
Window._addNote = mainWindowFunctions._addNote
Window._addNotebook = mainWindowFunctions._addNotebook
Window._addSubNotebook = mainWindowFunctions._addSubNotebook
Window.resizeEvent = mainWindowFunctions.resizeEvent
Window.openLoginDialog = mainWindowFunctions.openLoginDialog
Window.openFirstLoginDialog = mainWindowFunctions.openFirstLoginDialog
Window.checkFirstLogin = mainWindowFunctions.checkFirstLogin
Window.closeDialogAndMainWindow = mainWindowFunctions.closeDialogAndMainWindow
Window.openSettingsDialog = mainWindowFunctions.openSettingsDialog
Window.encryptAlldecryptedNotes = mainWindowFunctions.encryptAlldecryptedNotes
