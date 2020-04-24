
from PySide2 import QtCore, QtWidgets
from modules.fileHandling import currentNote
import json

def loadNote(_fileName, _textEdit):
    loadFileName(currentNote.getFilename(),_fileName)
    _textEdit.setPlainText(currentNote.getText())
    QtWidgets.QApplication.processEvents()

def loadFileName(name,fileName):
    fileName.setText(name)

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
    