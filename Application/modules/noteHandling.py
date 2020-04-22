import os
from stat import S_IREAD
from PySide2 import QtCore, QtWidgets
import json

def loadNote(path, _textEdit):
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
    if(encrypted == True):
        cnt = "wb"
        print("saved Encrypted file")
    with open(path,cnt) as file:
        file.write(txt)
    