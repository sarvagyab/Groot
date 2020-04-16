
from PySide2 import QtWidgets, QtCore
import json

def loadNote(path, name, ui):
    file = QtCore.QFile(path)
    file.open(QtCore.QIODevice.Text | QtCore.QIODevice.ReadWrite)
    stream = QtCore.QTextStream(file)
    ui.textEdit.setText(stream.readAll())

    loadFileName(name,ui.fileName)

def loadFileName(name,fileName):
    fileName.setText(name)
    