
from PySide2 import QtWidgets


def fixTreeViewScrolling(tree):
    tree.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)


createNotebook = QtWidgets.QAction()
createNotebook.setText("New notebook")

createSubNotebook = QtWidgets.QAction()
createSubNotebook.setText("New sub-notebook")

createNote = QtWidgets.QAction()
createNote.setText("New note")

rename = QtWidgets.QAction()
rename.setText("Rename")

dlt = QtWidgets.QAction()
dlt.setText("Delete")

