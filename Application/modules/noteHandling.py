
from PySide2 import QtCore, QtWidgets
from modules.fileHandling import currentNote
from modules.treeHandling import itemVal, saveUpdatedJson
import json, os

def loadNote(_fileName, _textEdit):
    loadFileName(currentNote.getFilename(),_fileName)
    _textEdit.setPlainText(currentNote.getText())
    QtWidgets.QApplication.processEvents()

def loadFileName(name,fileName):
    fileName.setText(name)

def createNote():
    pass

def renameNote(item,col):
    deets = itemVal(item)
    dic = deets[1][deets[0]]
    dic["name"] = item.text(0)
    saveUpdatedJson(deets[2])


def pathContainedNotes(diction):
    if("path" in diction and type(diction["path"]) == str):
        return [diction["path"]]
    finalList = []
    for keys in diction:
        finalList = finalList + pathContainedNotes(diction[keys]["expanded"])
    return finalList


def deleteNote(item, plainTextEdit,filename):
    toBeDlt = itemVal(item)
    # Notes to be deleted
    notesToBeDeleted = pathContainedNotes(toBeDlt[1][toBeDlt[0]]["expanded"])
    if(currentNote._details["path"] in notesToBeDeleted):
        loadFileName("No Note Selected",filename)
        currentNote.closeFile()
        plainTextEdit.clear()
    item.parent().removeChild(item)
    for note in notesToBeDeleted:
        os.remove(note)
    # all files deleted
    del toBeDlt[1][toBeDlt[0]]
    # Updated dictionary
    saveUpdatedJson(toBeDlt[2])
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
        print("saved Encrypted file")
    with open(path,cnt) as file:
        file.write(txt)
    