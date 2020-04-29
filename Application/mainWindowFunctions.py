import os
import sys

from PySide2 import QtWidgets,QtGui,QtCore

from modules.setPassword import password
from modules.fileHandling import currentNote
from modules.markdownHandling import viewInMarkdown, imageResize
from modules.treeHandling import loadfileStructure, noteLoader,itemVal, isNote,updateItem,getItem
from modules.noteHandling import deleteNote, renameNote, addNote, addNotebook,readText,writeText
from modules.GUIchanges import createNotebook, createSubNotebook, createNote, rename, dlt
from modules.searchInNote import searchText,finishedSearch
from modules.userLogin import setUsernameAndPassword,verifyUser
from modules.encryptNote import AEScipher

def showMenu(self,pos):
    item = self.ui.treeWidget.itemAt(pos)
    if item is None:
        return
    menu = QtWidgets.QMenu()
    if item is self.ui.treeWidget.topLevelItem(0):
        menu.addAction(createNotebook)
    elif item is self.ui.treeWidget.topLevelItem(1):
        menu.addAction(createNote)
    else:
        dets = isNote(item)
        if(dets[0]):
            pass
        else:
            menu.addAction(createSubNotebook)
            menu.addAction(createNote)
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
    changeNote = lambda : noteLoader(self.ui.treeWidget.currentItem(),self.ui.fileName,self.ui.plainTextEdit)
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
    addNote(self.ui.treeWidget.currentItem())


def _renameNote(self,item,col):
    if item.text(0) == "":
        item.setText(0,"Untitled")    
    renameNote(item,0)

# To resize the images automatically when the text changes
def resizeEvent(self,event):
    imageResize(self.ui.mdViewer)

def closeEvent(self,event):
    self.encryptAlldecryptedNotes()
    if currentNote._open:
        currentNote.closeFile()
    event.accept()

def checkFirstLogin(self):
    location = './User/login.txt'
    return os.path.exists(location)

def openSettingsDialog(self):
    from GUIs.settingsDialog import Ui_settingDialog
    ui_settingDialog = Ui_settingDialog()
    settingsDialog = QtWidgets.QDialog()
    ui_settingDialog.setupUi(settingsDialog)
    settingsDialog.exec()

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
        print(note,notes[note])
        path = notes[note]['expanded']['path']
        notes[note]['expanded']['encrypted'] = "True"
        txt = readText(path)
        print(txt)
        print(self.decryptedNotes[note])
        aes = AEScipher(self.decryptedNotes[note],None,txt) 
        enc_txt = aes.Encrypt()
        writeText(path,enc_txt,encrypted = True)
        updateItem({note:notes[note]})


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