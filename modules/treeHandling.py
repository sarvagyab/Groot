
from PySide2 import QtWidgets

def fixTreeViewScrolling(tree):
    tree.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
    tree.header().setStretchLastSection(False)