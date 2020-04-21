
from PySide2 import QtCore, QtWidgets
import json

def loadNote(path, _textEdit):
    file = QtCore.QFile(path)
    file.open(QtCore.QIODevice.Text | QtCore.QIODevice.ReadWrite)
    stream = QtCore.QTextStream(file)
    _textEdit.setPlainText(stream.readAll())
    QtWidgets.QApplication.processEvents()


def loadFileName(name,fileName):
    fileName.setText(name)
    