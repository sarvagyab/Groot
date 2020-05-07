import os
import sys
import json

from PySide2 import QtWidgets,QtGui,QtCore

from modules.setPassword import password
from modules.fileHandling import currentNote
from modules.markdownHandling import viewInMarkdown, imageResize, importMD, pluginHandler, scrolling
from modules.treeHandling import loadfileStructure, noteLoader,itemVal, isNote,updateItem,getItem
from modules.noteHandling import deleteNote, renameNote, addNote, addNotebook,readText,writeText
from modules.GUIchanges import createNotebook, createSubNotebook, createNote, rename, dlt, importer, exportPDF, exportHTML, exportMD, copyLink
from modules.searchInNote import searchText,finishedSearch
from modules.userLogin import setUsernameAndPassword,verifyUser,changePassword
from modules.encryptAllNotes import _encryptDecryptAllNotes
from modules.encryptNote import AEScipher
from GUIs.settingsDialog import Ui_settingDialog

def fixScrolling(self):
    edBar = self.ui.plainTextEdit.verticalScrollBar()
    mdBar = self.ui.mdViewer.verticalScrollBar()
    searchBar = self.ui.searchBar
    edBar.valueChanged.connect(lambda:scrolling(edBar,mdBar,searchBar))
    mdBar.valueChanged.connect(lambda:scrolling(mdBar,edBar,searchBar))

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
            menu.addAction(copyLink)
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


def _delayChecker(self):
    if(self.timer.isActive()):
        self.timer.stop()
    self.timer.start(self.DELAY)

def _noteLoader(self):
    changeNote = lambda : noteLoader(self.ui,self.encryptAll)
    self.ui.treeWidget.itemSelectionChanged.connect(changeNote)

def _markdownViewer(self):
    mdView = lambda: viewInMarkdown(self.ui.plainTextEdit.toPlainText(),self.mdExtensions,self.ui.mdViewer)
    sFile = lambda: currentNote.saveFile(self.ui.plainTextEdit.toPlainText(),self.encryptAll)
    self.timer.timeout.connect(sFile)
    self.timer.timeout.connect(mdView)
    self.ui.plainTextEdit.textChanged.connect(self._delayChecker)




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
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/delete_note.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
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
    addNote(self.ui.treeWidget.currentItem(),self.ui.plainTextEdit,self)


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

def setPlainTextEditFont(self):
    family = self.ui_settingDialog.fontChoice.currentText()
    size = int(self.ui_settingDialog.fontSizeValue.text())
    with open("./settings.json","r+") as sets:
        settings = json.load(sets)
        settings["Appearance"]["size"] = size
        settings["Appearance"]["family"] = family
        sets.seek(0)
        sets.truncate()
        json.dump(settings,sets)
    font = QtGui.QFont(family,size)
    self.ui.plainTextEdit.setFont(font)

def appearConnections(self,settings):
    settings.fontSizeValue.textChanged.connect(self.setPlainTextEditFont)
    settings.fontChoice.currentFontChanged.connect(self.setPlainTextEditFont)

# Added the ui_settingDialog to Window object
def createSettingsDialog(self):
    self.ui_settingDialog = Ui_settingDialog()
    self.settingsDialog = QtWidgets.QDialog()
    self.ui_settingDialog.setupUi(self.settingsDialog)
    self.ui_settingDialog.closeMe.clicked.connect(self.settingsDialog.close)
    self.ui_settingDialog.encryptAllChoice.setChecked(self.encryptAll)
    self.ui_settingDialog.settings.setTabIcon(0,QtGui.QIcon(":/icons/Icons/32x32/display.png"))
    self.ui_settingDialog.settings.setTabIcon(1,QtGui.QIcon(":/icons/Icons/32x32/box.png"))
    self.ui_settingDialog.settings.setTabIcon(2,QtGui.QIcon(":/icons/Icons/32x32/encrypt.png"))
    self.ui_settingDialog.settings.setTabIcon(3,QtGui.QIcon(":/icons/Icons/32x32/user.png"))
    self.pluginConnections(self.ui_settingDialog)
    self.encryptionSettings(self.ui_settingDialog)
    self.changeUserPasswordSettings(self.ui_settingDialog)
    # Appearance connections are made in loadSettings


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
    self.ui_settingDialog.fontSizeValue.setValue(appearSettings["size"])
    self.ui_settingDialog.fontChoice.setCurrentText(appearSettings["family"])
    font = QtGui.QFont(appearSettings["family"],int(appearSettings["size"]))
    self.ui.plainTextEdit.setFont(font)


def loadSettings(self):
    with open("./settings.json","r") as sets:
        settings = json.load(sets)
    plugSettings = settings["Plugins"]
    appearSettings = settings["Appearance"]
    self.loadPlugSettings(plugSettings)
    self.loadAppearSettings(appearSettings)
    self.appearConnections(self.ui_settingDialog)



def analyzeLink(self,url):
    text = url.toString()
    # print(text)
    # print(text[:2])
    if(text[:2]!="./"): return False
    return True

def searchInBooks(self, randomString, diction):
    keys = [*diction]
    if randomString in keys:
        return [keys.index(randomString)]
    for i in range(len(keys)):
        if "path" in diction[keys[i]]["expanded"] and type(diction[keys[i]]["expanded"]["path"])==str: continue 
        result = self.searchInBooks(randomString,diction[keys[i]]["expanded"])
        if result != []:
            return [i] + result
    return []

def searchForFilename(self,randomString):
    with open("./fileStructure.json","r") as nt:
        files = json.load(nt)
    print("searching in uncategorized")
    keys = [*files["Uncategorized"]]
    if randomString in keys:
        print([1] + [keys.index(randomString)])
        return [1] + [keys.index(randomString)]
    print("searching in notebooks")
    path = self.searchInBooks(randomString,files["Notebooks"])
    if path == []:
        print("No such note present")
        return []
    else:
        path = [0] + path
        print(path)
        return path


def handleLinks(self,url):
    # print(url.scheme())
    if url.scheme() == "ftp" or url.scheme() == "http" or url.scheme() == "https":
        QtGui.QDesktopServices.openUrl(url)
    else:
        print("Analyzing")
        check = self.analyzeLink(url)
        if check == False:
            msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,"Groot","Cannot open this link",QtWidgets.QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/attention.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
            msg.setWindowIcon(icon)
            msg.exec_()
            print("doesn't turn out to be a link") 
            return
        else:
            print("Determined to be link")
            filename = url.toString()[2:]
            item = self.searchForFilename(filename)
            if item == []:
                msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,"Groot","Cannot open this link",QtWidgets.QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/attention.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.exec_()
                return
            getToItem = self.ui.treeWidget.topLevelItem(item[0])
            print(getToItem.text(0))
            for i in range(1,len(item)):
                getToItem = getToItem.child(item[i])
                print(getToItem.text(0))

            self.ui.treeWidget.setCurrentItem(getToItem)

def encryptNote(self):
    self.passwdE = password(self)
    self.ui.encryptionButton.clicked.connect(lambda: self.passwdE.openPasswordDialog())
    
def decryptNote(self):
    self.passwdD = password(self)
    self.ui.decryptionButton.clicked.connect(lambda: self.passwdD.openVerifyPasswordDialog())

def openEncryptionWithMenu(self):
    self.passwdE = password(self)
    self.passwdE.openPasswordDialog()

def openDecryptionWithMenu(self):
    self.passwdD = password(self)
    self.passwdD.openVerifyPasswordDialog()

def changeUserPasswordSettings(self,settings):
    settings.okPushButton.clicked.connect(lambda : self.changeUserPassword(settings))
    # clear = lambda line1,line2,line3: line1.setText("") line2.setText("") line3.setText("") 
    settings.cancelPushButton.clicked.connect(
            lambda : (settings.oldPasswordLineEdit.setText(""),
            settings.passwordLineEdit_2.setText(""),
            settings.RepasswordLineEdit.setText("")))


def changeUserPassword(self,settings):
    if(verifyUser(settings.oldPasswordLineEdit.text(),settings.Errortext_2)):
        username = self.userInfo[0]
        newPass = settings.passwordLineEdit_2.text()
        h_pass, salt = setUsernameAndPassword(username,newPass,settings.RepasswordLineEdit.text(),dialog = None,store = False)
        changePassword(h_pass,salt)
        settings.oldPasswordLineEdit.setText("")
        settings.passwordLineEdit_2.setText("")
        settings.RepasswordLineEdit.setText("")
        settings.Errortext_2.setText("<html><head/><body><p><span style=\" color:#00ff00;\">New password set</span></p></body></html>")

def openLoginDialog(self):
    from GUIs.loginDialog import Ui_loginDialog
    loginDialog = QtWidgets.QDialog()
    ui_loginDialog = Ui_loginDialog()
    ui_loginDialog.setupUi(loginDialog)
    ui_loginDialog.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: verifyUser(ui_loginDialog.passwordLineEdit.text(),ui_loginDialog.Errortext,loginDialog))
    ui_loginDialog.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.closeDialogAndMainWindow(loginDialog))
    ui_loginDialog.passwordLineEdit.setFocus()
    if(loginDialog.exec() == 0):
        self.closeDialogAndMainWindow(loginDialog)

def encryptionSettings(self,settings):
    settings.okPushButton_2.clicked.connect(lambda :self._verifyUser(settings))

def _verifyUser(self,settings):
    if(verifyUser(settings.enterPwd.text(),settings.Errortext)):
        settings.enterPwd.setText("")
        settings.encryptAllChoice.setEnabled(True)
        settings.Errortext.setText("")
        settings.encryptAllChoice.stateChanged.connect(lambda:self.encryptAllChoiceChanged(settings.encryptAllChoice))

def encryptAllChoiceChanged(self,checkbox):
    if(checkbox.isChecked()):
        if(self.encryptAll == False):
            print("Store encrypted notes")
            _encryptDecryptAllNotes(self,True)
    else:
        if(self.encryptAll == True):
            print("Store decrypted notes")
            _encryptDecryptAllNotes(self,False)
        

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
    if(currentNote._file != None):
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
    ui_firstLoginDialog.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda:setUsernameAndPassword(ui_firstLoginDialog.username.text(),ui_firstLoginDialog.passwordLineEdit.text(),ui_firstLoginDialog.repasswordLineEdit.text(),firstLoginDialog))
    if(firstLoginDialog.exec() == 0):
        self.closeDialogAndMainWindow(firstLoginDialog)

def closeDialogAndMainWindow(self,dialog = None):
    if(dialog != None):
        dialog.close()
    self.close()
    sys.exit()