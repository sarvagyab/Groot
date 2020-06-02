import datetime
import json
import os

from PySide2 import QtCore,QtGui,QtWidgets

from Application.modules.encryptNote import AEScipher
from Application.modules.fileHandling import currentNote
import Application.modules.treeHandling as treeHandling
import Application.modules.userLogin


def loadNote(_fileName, _textEdit,encryptAll):
    loadFileName(currentNote.getFilename(),_fileName)
    if(isEncryped()): 
        print("encrypted so don't load the file")
        _textEdit.setPlainText("<!--encrypted-->")
        # _textEdit.setPlainText(str(currentNote.getText(False)))
    else:
        _textEdit.setPlainText(str(currentNote.getText(encryptAll)))
    QtWidgets.QApplication.processEvents()

def loadFileName(name,fileName):
    fileName.setText(name)

def pathContainedNotes(diction):
    if("path" in diction and type(diction["path"]) == str):
        if "atchfiles" in diction:
            # print("adding the to be deleted files")
            # print(diction["atchfiles"])
            return ([diction["path"]] + diction["atchfiles"])
        else:
            return [diction["path"]]
    finalList = []
    for keys in diction:
        finalList = finalList + pathContainedNotes(diction[keys]["expanded"])
    return finalList


def addNotebook(window,check):
    # input name
    if check:
        item = window.ui.treeWidget.topLevelItem(0)
    else:
        item = window.ui.treeWidget.currentItem()
    text, ok = QtWidgets.QInputDialog().getText(window,"Groot","Enter the name for new notebook - ",flags= QtCore.Qt.Dialog )
    if ok is True:
        if str(text) != "":
            name = str(text)
        else:
            name = "Untitled"
    else:
        return
    
    deets = treeHandling.itemVal(item)

    # Make changes to fileStructure
    randomString = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    newdict = {}
    newdict["name"] = name
    newdict["expanded"] = {}
    if(item.parent() is None):
        deets[1][deets[0]][randomString] = newdict
    else:
        deets[1][deets[0]]["expanded"][randomString] = newdict

    treeHandling.saveUpdatedJson(deets[2])

    # Update treeWidget
    newItem = QtWidgets.QTreeWidgetItem()
    newItem.setText(0,name)
    newItem.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/subfolder_light.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)        
    newItem.setIcon(0,icon)
    item.addChild(newItem)
    item.setExpanded(True)
    item.treeWidget().setCurrentItem(newItem)


def addNote(item,_plainTextEdit,window):
    # input name
    text, ok = QtWidgets.QInputDialog().getText(window,"Groot","Enter the name for new note - ",flags=QtCore.Qt.Dialog)
    if ok is True:
        if str(text) != "":
            name = str(text)
        else:
            name = "Untitled"
    else:
        return

    deets = treeHandling.itemVal(item)
    randomString = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    path = "./Application/notes/" 
    filename = randomString + ".txt"

    # create notes folder if not exists
    if(not os.path.exists(path)):
        os.makedirs(path)

    # Creating file
    open(os.path.join(path,filename),'a').close()
    # open(path,'a').close()

    # encrypt file
    if(window.encryptAll == True):
        userInfo = Application.modules.userLogin.readUserInfo()
        aes = AEScipher(str(userInfo[1]),currentNote,txt ="",encrypt = True)
        txt = aes.Encrypt()
        if(not isinstance(txt,bytes)):
            print("here")
            txt = bytes(txt,encoding = 'utf8')
        with open(path+filename,'wb') as file:
            file.write(txt)
            file.seek(0)
        print("Encrypted in add note method")
        
    # Add to JSON
    newdict = {}
    newdict["name"] = name
    newdict["expanded"] = {}
    newdict["expanded"]["path"] = path + filename
    newdict["expanded"]["randomString"] = randomString
    if item is item.treeWidget().topLevelItem(1):
        deets[2]["Uncategorized"][randomString] = newdict
    else:
        deets[1][deets[0]]["expanded"][randomString] = newdict
    treeHandling.saveUpdatedJson(deets[2])
    
    # Update treeWidget
    newItem = QtWidgets.QTreeWidgetItem()
    newItem.setText(0,name)
    newItem.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/document_light.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)        
    newItem.setIcon(0,icon)
    item.addChild(newItem)
    item.setExpanded(True)
    item.treeWidget().setCurrentItem(newItem)
    # Focus on plainTextEdit
    _plainTextEdit.setFocus()


def renameNote(item,col):
    deets = treeHandling.itemVal(item)
    dic = deets[1][deets[0]]
    dic["name"] = item.text(0)
    treeHandling.saveUpdatedJson(deets[2])


def deleteNote(item, plainTextEdit,filename):
    toBeDlt = treeHandling.itemVal(item)
    # Notes to be deleted
    notesToBeDeleted = pathContainedNotes(toBeDlt[1][toBeDlt[0]]["expanded"])
    if(currentNote._details["path"] in notesToBeDeleted):
        loadFileName("No Note Selected",filename)
        currentNote.closeFile()
        currentNote._open = False
        plainTextEdit.clear()
    
    # removed from tree
    item.parent().removeChild(item)
    for note in notesToBeDeleted:
        os.remove(note)
    # all files deleted
    del toBeDlt[1][toBeDlt[0]]
    # Updated dictionary
    treeHandling.saveUpdatedJson(toBeDlt[2])
    # Updated JSON


def readText(path):
    file = QtCore.QFile(path)
    file.open(QtCore.QIODevice.Text | QtCore.QIODevice.ReadOnly)
    stream = QtCore.QTextStream(file)
    return stream.readAll()

def writeText(path,txt,encrypted = False):
    cnt = "w"
    if(encrypted == True):
        cnt = "wb"
    with open(path,cnt) as file:
        file.write(txt)
    
def isEncryped():
    if('encrypted' in currentNote._details and currentNote._details['encrypted'] == 'True'):
        return True
    return False