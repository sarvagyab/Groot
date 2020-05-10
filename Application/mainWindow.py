from PySide2 import QtWidgets, QtCore, QtGui

# import GUIs
from Application.GUIs.mainWindowPTE import Ui_Groot

# import modules
import Application.mainWindowFunctions
from Application.modules.userLogin import readUserInfo,storeUserInfoInFile
from Application.modules.GUIchanges import fixTreeViewScrolling, createNotebook, createSubNotebook, createNote, rename, dlt, importer, exportPDF, exportHTML, exportMD, copyLink
from Application.modules.markdownHandling import bold, italic, numList, bulletList, hyperlink, inlineCode, datetimenow, attachFile, exportAsPdf, exportAsHtml, exportAsMarkdown, importMD, copyMarkdownLink
from Application.GUIs.settingsDialog import Ui_settingDialog

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Initializing UI
        self.ui = Ui_Groot()
        self.ui.setupUi(self)
        
        self.mdExtensions = []  # Extensions for changing behaviour of markdown viewer
        self.mdExtensionsConfigs = {} # Extensions configurations for changing the behaviour of extensions in markdown

        
        if(self.checkFirstLogin()):
            QtCore.QTimer.singleShot(0,self,self.openLoginDialog())
        else:
            QtCore.QTimer.singleShot(0,self,self.openFirstLoginDialog())

        self.userInfo = readUserInfo()
        if(self.userInfo[3] == "True"):
            self.encryptAll = True
        else:
            self.encryptAll = False
            
        # Create settings Dialog
        self.createSettingsDialog()
        self.loadSettings()

        # Bring the cursor to text editor
        self.ui.plainTextEdit.setFocus()

        self.decryptedNotes= {} # all notes that were encrypted and decrypted in this session
        self.encryptedInSession = {} # all notes that are encrypted in this session

        self.DELAY = 1000   # Delay in displaying Markdown
        
        # Fix no Scrollbar issue in notes tree when file names go out of box
        fixTreeViewScrolling(self.ui.treeWidget)
        
        # Parallel Scrolling for text editor and markdown viewer
        self.fixScrolling()

        self.ui.treeWidget.customContextMenuRequested.connect(self.showMenu)

        # Connections for renaming
        self.ui.treeWidget.itemDoubleClicked.connect(self.ui.treeWidget.editItem)
        rename.triggered.connect(lambda: self.ui.treeWidget.editItem(self.ui.treeWidget.currentItem(),0))
        self.ui.treeWidget.itemChanged.connect(self._renameNote)

        # Connections for deleting
        dlt.triggered.connect(self.showDeleteDialog)

        # Connection for self linking
        self.ui.mdViewer.anchorClicked.connect(self.handleLinks)

        # connection for creating new notebook
        createNotebook.triggered.connect(self._addNotebook)
        self.ui.newNotebook.clicked.connect(self._addNotebook)
        self.ui.actionNew_notebook.triggered.connect(self._addNotebook)

        # connection for creating new subnotebook
        createSubNotebook.triggered.connect(self._addSubNotebook)
        self.ui.newSubNotebook.clicked.connect(self._addSubNotebook)
        self.ui.actionNew_sub_notebook.triggered.connect(self._addSubNotebook)

        # connection for creating new note
        createNote.triggered.connect(self._addNote)
        self.ui.newNote.clicked.connect(self._addNote)
        self.ui.actionNew_note.triggered.connect(self._addNote)

        # bold connection
        self.ui.boldButton.clicked.connect(lambda: bold(self.ui.plainTextEdit))
        self.ui.actionBold.triggered.connect(lambda: bold(self.ui.plainTextEdit))

        # italic connection
        self.ui.italicButton.clicked.connect(lambda: italic(self.ui.plainTextEdit))
        self.ui.actionItalic.triggered.connect(lambda: italic(self.ui.plainTextEdit))

        # numbered list connection
        self.ui.numberedList.clicked.connect(lambda: numList(self.ui.plainTextEdit))

        # bullet list connection
        self.ui.bullets.clicked.connect(lambda: bulletList(self.ui.plainTextEdit))

        # hyperlink connection
        self.ui.link.clicked.connect(lambda: hyperlink(self))
        self.ui.actionLink.triggered.connect(lambda: hyperlink(self))

        # inline code connection
        self.ui.code.clicked.connect(lambda: inlineCode(self.ui.plainTextEdit))
        self.ui.actionCode.triggered.connect(lambda: inlineCode(self.ui.plainTextEdit))

        # date time connection
        self.ui.dateTime.clicked.connect(lambda: datetimenow(self.ui.plainTextEdit))
        self.ui.actionDate_and_Time.triggered.connect(lambda: datetimenow(self.ui.plainTextEdit))
        
        # attaching file connection
        self.ui.insertFile.clicked.connect(lambda: attachFile(self))
        self.ui.actionImage.triggered.connect(lambda: attachFile(self))

        # attach copying of markdown link
        copyLink.triggered.connect(copyMarkdownLink)

        # export as PDF connection
        self.ui.actionPDF.triggered.connect(lambda: exportAsPdf(self))
        exportPDF.triggered.connect(lambda: exportAsPdf(self))

        # export as Markdown connection
        self.ui.actionMD_2.triggered.connect(lambda: exportAsMarkdown(self))
        exportMD.triggered.connect(lambda: exportAsMarkdown(self))

        # export as Html connection
        self.ui.actionHTML.triggered.connect(lambda: exportAsHtml(self,self.mdExtensions))
        exportHTML.triggered.connect(lambda: exportAsHtml(self,self.mdExtensions))
       
        # search in note connection
        self.ui.actionSearch_in_Current_Note.triggered.connect(lambda:self.ui.searchBar.setFocus())

        # encryption connection
        self.ui.actionEncrypt_note.triggered.connect(lambda :self.openEncryptionWithMenu())

        # decryption connection
        self.ui.actionDecrypt_note.triggered.connect(lambda:self.openDecryptionWithMenu())

        # print connection
        self.ui.actionPrint.triggered.connect(lambda:self.printingNote())

        # print preview connection
        self.ui.actionPrint_preview.triggered.connect(lambda:self._printPreview())

        # import MD file
        self.ui.actionMD.triggered.connect(self._importMD)
        importer.triggered.connect(lambda: importMD(self.ui.treeWidget.currentItem()))


        # Load tree structure and notes
        self.reloadUI()

        # Permanent decrypt click
        self.ui.permanentDecrypt.clicked.connect(lambda: self.permenantDecrypt())

        # change encryption password
        self.ui.changePasswordButton.clicked.connect(lambda : self.changeEncryptionPassword())

        # Timer for Loading the Markdown view when the user has stopped typing for a duration
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)

        # Display notes in Markdown
        self._markdownViewer()

        # Display UI
        self.showMaximized()

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
        self.ui.actionSettings.triggered.connect(self.settingsDialog.exec_)

        # close main window from menu
        self.ui.actionQuit.triggered.connect(lambda:self.closeDialogAndMainWindow())

     



Window._noteLoader = Application.mainWindowFunctions._noteLoader
Window.closeEvent = Application.mainWindowFunctions.closeEvent
Window.reloadUI = Application.mainWindowFunctions.reloadUI
Window.decryptNote = Application.mainWindowFunctions.decryptNote
Window.encryptNote = Application.mainWindowFunctions.encryptNote
Window._markdownViewer = Application.mainWindowFunctions._markdownViewer
Window._delayChecker = Application.mainWindowFunctions._delayChecker
Window.showMenu = Application.mainWindowFunctions.showMenu
Window.searchInNote = Application.mainWindowFunctions.searchInNote
Window.searchModeChanged = Application.mainWindowFunctions.searchModeChanged
Window.findNextOccurance = Application.mainWindowFunctions.findNextOccurance
Window.findPrevOccurance = Application.mainWindowFunctions.findPrevOccurance
Window._finishedSearch = Application.mainWindowFunctions._finishedSearch
Window.showDeleteDialog = Application.mainWindowFunctions.showDeleteDialog
Window._renameNote = Application.mainWindowFunctions._renameNote
Window._addNote = Application.mainWindowFunctions._addNote
Window._addNotebook = Application.mainWindowFunctions._addNotebook
Window._addSubNotebook = Application.mainWindowFunctions._addSubNotebook
Window.resizeEvent = Application.mainWindowFunctions.resizeEvent
Window.openLoginDialog = Application.mainWindowFunctions.openLoginDialog
Window.openFirstLoginDialog = Application.mainWindowFunctions.openFirstLoginDialog
Window.checkFirstLogin = Application.mainWindowFunctions.checkFirstLogin
Window.closeDialogAndMainWindow = Application.mainWindowFunctions.closeDialogAndMainWindow
Window.encryptAlldecryptedNotes = Application.mainWindowFunctions.encryptAlldecryptedNotes
Window.permenantDecrypt = Application.mainWindowFunctions.permenantDecrypt
Window.changeEncryptionPassword = Application.mainWindowFunctions.changeEncryptionPassword
Window._importMD = Application.mainWindowFunctions._importMD
Window.createSettingsDialog = Application.mainWindowFunctions.createSettingsDialog
Window.pluginConnections = Application.mainWindowFunctions.pluginConnections
Window.loadSettings = Application.mainWindowFunctions.loadSettings
Window.loadPlugSettings = Application.mainWindowFunctions.loadPlugSettings
Window.loadAppearSettings = Application.mainWindowFunctions.loadAppearSettings
Window.appearConnections = Application.mainWindowFunctions.appearConnections
Window.setPlainTextEditFont = Application.mainWindowFunctions.setPlainTextEditFont
Window.handleLinks = Application.mainWindowFunctions.handleLinks
Window.analyzeLink = Application.mainWindowFunctions.analyzeLink
Window.searchForFilename = Application.mainWindowFunctions.searchForFilename
Window.searchInBooks = Application.mainWindowFunctions.searchInBooks
Window.fixScrolling = Application.mainWindowFunctions.fixScrolling
Window.encryptionSettings = Application.mainWindowFunctions.encryptionSettings
Window._verifyUser = Application.mainWindowFunctions._verifyUser
Window.encryptAllChoiceChanged = Application.mainWindowFunctions.encryptAllChoiceChanged
Window.changeUserPasswordSettings = Application.mainWindowFunctions.changeUserPasswordSettings
Window.changeUserPassword = Application.mainWindowFunctions.changeUserPassword
Window.openEncryptionWithMenu = Application.mainWindowFunctions.openEncryptionWithMenu
Window.openDecryptionWithMenu = Application.mainWindowFunctions.openDecryptionWithMenu
Window.printingNote = Application.mainWindowFunctions.printingNote
Window._printPreview = Application.mainWindowFunctions._printPreview
