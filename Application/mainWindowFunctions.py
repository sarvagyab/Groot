import os
import sys
import json

from PySide2 import QtWidgets,QtGui,QtCore

from modules.setPassword import password
from modules.fileHandling import currentNote
from modules.markdownHandling import viewInMarkdown, imageResize, importMD, pluginHandler
from modules.treeHandling import loadfileStructure, noteLoader,itemVal, isNote,updateItem,getItem
from modules.noteHandling import deleteNote, renameNote, addNote, addNotebook,readText,writeText
from modules.GUIchanges import createNotebook, createSubNotebook, createNote, rename, dlt, importer, exportPDF, exportHTML, exportMD
from modules.searchInNote import searchText,finishedSearch
from modules.userLogin import setUsernameAndPassword,verifyUser
from modules.encryptNote import AEScipher
from GUIs.settingsDialog import Ui_settingDialog

def showMenu(self,pos):
    item = self.ui.treeWidget.itemAt(pos)
    if item is None:
        return
    menu = QtWidgets.QMenu()
    if item is self.ui.treeWidget.topLevelItem(0):
        menu.addAction(createNotebook)
    elif item is self.ui.treeWidget.topLevelItem(1):
        menu.addAction(importer)
        menu.addAction(createNote)
    else:
        dets = isNote(item)
        if(dets[0]):
            exporter = QtWidgets.QMenu()
            exporter.setTitle("Export")
            exporter.addAction(exportMD)
            exporter.addAction(exportHTML)
            exporter.addAction(exportPDF)
            menu.addMenu(exporter)
            pass
        else:
            menu.addAction(createSubNotebook)
            menu.addAction(createNote)
            menu.addAction(importer)
        menu.addAction(rename)
        menu.addAction(dlt)
    menu.exec_(self.ui.treeWidget.mapToGlobal(pos))


def shortcutBinding(self):
    QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+F"),self).activated.connect(lambda:self.ui.searchBar.setFocus())

def _delayChecker(self):
    if(self.timer.isActive()):
        self.timer.stop()
    self.timer.start(self.DELAY)

def _noteLoader(self):
    changeNote = lambda : noteLoader(self.ui)
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
    
def searchModeChanged(self):
    self.ui.wholeWord.clicked.connect(lambda:searchText(self.ui))
    self.ui.regexButton.clicked.connect(lambda:searchText(self.ui))
    self.ui.matchCase.clicked.connect(lambda:searchText(self.ui))

def findNextOccurance(self):
    self.ui.searchBar.returnPressed.connect(lambda :searchText(self.ui,QtGui.QTextCursor.NextCharacter))
    self.ui.nextMatch.clicked.connect(lambda :searchText(self.ui,QtGui.QTextCursor.NextCharacter))

def findPrevOccurance(self):
    shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("shift+Return"),self.ui.searchBar)
    shortcut.activated.connect(lambda:searchText(self.ui,QtGui.QTextCursor.PreviousCharacter,reversed = True))
    self.ui.prevMatch.clicked.connect(lambda :searchText(self.ui,QtGui.QTextCursor.PreviousCharacter,reversed = True))

def _finishedSearch(self):
    self.ui.searchBar.editingFinished.connect(lambda :finishedSearch(self.ui.errorLabel))

def reloadUI(self):
    loadfileStructure(self.ui.treeWidget)
    self._noteLoader()


def showDeleteDialog(self):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Delete Confirmation?")
    msg.setText("Are you sure you want to delete " + self.ui.treeWidget.currentItem().text(0) + " ?")
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
    msg.button(QtWidgets.QMessageBox.Ok).clicked.connect(lambda: deleteNote(self.ui.treeWidget.currentItem(),self.ui.plainTextEdit, self.ui.fileName))
    msg.exec_()


def _addNotebook(self):
    if(self.ui.treeWidget.currentItem() is self.ui.treeWidget.topLevelItem(0)):
        addNotebook(self.ui.treeWidget.currentItem())
    return


def _addSubNotebook(self):
    if  (self.ui.treeWidget.currentItem() is self.ui.treeWidget.topLevelItem(0)) or \
        (self.ui.treeWidget.currentItem() is self.ui.treeWidget.topLevelItem(1)) or \
        (isNote(self.ui.treeWidget.currentItem())[0]):
            return
    addNotebook(self.ui.treeWidget.currentItem())


def _addNote(self):
    if  (self.ui.treeWidget.currentItem() is None) or \
        (self.ui.treeWidget.currentItem() is self.ui.treeWidget.topLevelItem(0)) or \
        (isNote(self.ui.treeWidget.currentItem())[0]):
            return
    addNote(self.ui.treeWidget.currentItem(),self.ui.plainTextEdit)


def _renameNote(self,item,col):
    if item.text(0) == "":
        item.setText(0,"Untitled")    
    renameNote(item,0)

# To resize the images automatically when the text changes
def resizeEvent(self,event):
    imageResize(self.ui.mdViewer)

def _importMD(self):
    item = self.ui.treeWidget.currentItem()
    if (item is None) or (item is self.ui.treeWidget.topLevelItem(0)) or (isNote(item)[0]):
        item = self.ui.treeWidget.topLevelItem(1)
    importMD(item)

def closeEvent(self,event):
    self.encryptAlldecryptedNotes()
    if currentNote._open:
        currentNote.closeFile()
    event.accept()

def checkFirstLogin(self):
    location = './User/login.txt'
    return os.path.exists(location)

def pluginConnections(self,settings):
    settings.hardExt.stateChanged.connect(lambda: pluginHandler("hardbreak",settings.hardExt.isChecked(),self.mdExtensions,self.mdExtensionsConfigs))
    settings.footnotesExt.stateChanged.connect(lambda: pluginHandler("footnotes",settings.footnotesExt.isChecked(),self.mdExtensions,self.mdExtensionsConfigs))
    settings.defListsExt.stateChanged.connect(lambda: pluginHandler("defLists",settings.defListsExt.isChecked(),self.mdExtensions,self.mdExtensionsConfigs))
    settings.mdExt.stateChanged.connect(lambda: pluginHandler("mdExt",settings.mdExt.isChecked(),self.mdExtensions,self.mdExtensionsConfigs))
    settings.supExt.stateChanged.connect(lambda: pluginHandler("superscript",settings.supExt.isChecked(),self.mdExtensions,self.mdExtensionsConfigs))
    settings.subExt.stateChanged.connect(lambda: pluginHandler("subscript",settings.subExt.isChecked(),self.mdExtensions,self.mdExtensionsConfigs))
    settings.linkExt.stateChanged.connect(lambda: pluginHandler("autolink",settings.linkExt.isChecked(),self.mdExtensions,self.mdExtensionsConfigs))
    settings.symbolsExt.stateChanged.connect(lambda: pluginHandler("symbols",settings.symbolsExt.isChecked(),self.mdExtensions,self.mdExtensionsConfigs))
    settings.strikeExt.stateChanged.connect(lambda: pluginHandler("strike",settings.strikeExt.isChecked(),self.mdExtensions,self.mdExtensionsConfigs))


# Added the ui_settingDialog to Window object
def createSettingsDialog(self):
    self.ui_settingDialog = Ui_settingDialog()
    self.settingsDialog = QtWidgets.QDialog()
    self.ui_settingDialog.setupUi(self.settingsDialog)
    self.pluginConnections(self.ui_settingDialog)


def loadPlugSettings(self,plugSettings):
    if(plugSettings["hardExt"]):
        self.ui_settingDialog.hardExt.setCheckState(QtCore.Qt.Checked)
    else:
        self.ui_settingDialog.hardExt.setCheckState(QtCore.Qt.Unchecked)
    
    if(plugSettings["footnotesExt"]):
        self.ui_settingDialog.footnotesExt.setCheckState(QtCore.Qt.Checked)
    else:
        self.ui_settingDialog.footnotesExt.setCheckState(QtCore.Qt.Unchecked)

    if(plugSettings["defListsExt"]):
        self.ui_settingDialog.defListsExt.setCheckState(QtCore.Qt.Checked)
    else:
        self.ui_settingDialog.defListsExt.setCheckState(QtCore.Qt.Unchecked)

    if(plugSettings["mdExt"]):
        self.ui_settingDialog.mdExt.setCheckState(QtCore.Qt.Checked)
    else:
        self.ui_settingDialog.mdExt.setCheckState(QtCore.Qt.Unchecked)

    if(plugSettings["supExt"]):
        self.ui_settingDialog.supExt.setCheckState(QtCore.Qt.Checked)
    else:
        self.ui_settingDialog.supExt.setCheckState(QtCore.Qt.Unchecked)

    if(plugSettings["subExt"]):
        self.ui_settingDialog.subExt.setCheckState(QtCore.Qt.Checked)
    else:
        self.ui_settingDialog.subExt.setCheckState(QtCore.Qt.Unchecked)

    if(plugSettings["linkExt"]):
        self.ui_settingDialog.linkExt.setCheckState(QtCore.Qt.Checked)
    else:
        self.ui_settingDialog.linkExt.setCheckState(QtCore.Qt.Unchecked)

    if(plugSettings["symbolsExt"]):
        self.ui_settingDialog.symbolsExt.setCheckState(QtCore.Qt.Checked)
    else:
        self.ui_settingDialog.symbolsExt.setCheckState(QtCore.Qt.Unchecked)

    if(plugSettings["strikeExt"]):
        self.ui_settingDialog.strikeExt.setCheckState(QtCore.Qt.Checked)
    else:
        self.ui_settingDialog.strikeExt.setCheckState(QtCore.Qt.Unchecked)


def loadAppearSettings(self,appearSettings):
    pass


def loadSettings(self):
    with open("./settings.json","r") as sets:
        settings = json.load(sets)
    plugSettings = settings["Plugins"]
    appearSettings = settings["Appearance"]
    self.loadPlugSettings(plugSettings)
    self.loadAppearSettings(appearSettings)


def openLoginDialog(self):
    from GUIs.loginDialog import Ui_loginDialog
    loginDialog = QtWidgets.QDialog()
    ui_loginDialog = Ui_loginDialog()
    ui_loginDialog.setupUi(loginDialog)
    ui_loginDialog.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: verifyUser(ui_loginDialog.passwordLineEdit.text(),ui_loginDialog,loginDialog))
    ui_loginDialog.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.closeDialogAndMainWindow(loginDialog))
    if(loginDialog.exec() == 0):
        self.closeDialogAndMainWindow(loginDialog)

def encryptAlldecryptedNotes(self):
    notes = getItem(list(self.decryptedNotes.keys()))
    for note in notes:
        path = notes[note]['expanded']['path']
        notes[note]['expanded']['encrypted'] = "True"
        txt = readText(path)
        aes = AEScipher(self.decryptedNotes[note],None,txt) 
        enc_txt = aes.Encrypt()
        writeText(path,enc_txt,encrypted = True)
        updateItem({note:notes[note]})

def permenantDecrypt(self):
    print("permenant decrypt click")
    randomstring = currentNote._details['randomString']
    pwd = password(self)
    pwd.openVerifyPasswordDialog(True)

def changeEncryptionPassword(self):
    print("change encryption button clicked")
    pwd = password(self)
    pwd.openChangeEncryptionPasswordDialog()

def openFirstLoginDialog(self):
    from GUIs.firstLoginDialog import Ui_firstLoginDialog
    firstLoginDialog = QtWidgets.QDialog()
    ui_firstLoginDialog = Ui_firstLoginDialog()
    ui_firstLoginDialog.setupUi(firstLoginDialog)
    ui_firstLoginDialog.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.closeDialogAndMainWindow(firstLoginDialog))
    ui_firstLoginDialog.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda:setUsernameAndPassword(ui_firstLoginDialog.username.text(),ui_firstLoginDialog.passwordLineEdit.text(),ui_firstLoginDialog.repasswordLineEdit.text(),ui_firstLoginDialog,firstLoginDialog))
    if(firstLoginDialog.exec() == 0):
        self.closeDialogAndMainWindow(firstLoginDialog)

def closeDialogAndMainWindow(self,dialog = None):
    if(dialog != None):
        dialog.close()
    self.close()
    sys.exit()