
from PySide2 import QtWidgets
# from modules.noteHandling import renameNote, dltNote, addSubNotebook, addNotebook, addNote
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

# noteMenu = QtWidgets.QMenu()
# noteMenu.addAction(rename)
# noteMenu.addAction(dlt)

