
from PySide2 import QtCore, QtWidgets
import json

def loadNote(path, _textEdit):
    # file = QtCore.QFile(path)
    # file.open(QtCore.QIODevice.Text | QtCore.QIODevice.ReadWrite)
    # stream = QtCore.QTextStream(file)
    _textEdit.setPlainText(readText(path))
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
    if(encrypted == True): # comment the whole text
        txt = "<!--Encrypted Fuck off -->"
    with open(path,cnt) as file:
        file.write(txt)
    print("saved Encrypted file")
    