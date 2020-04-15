
from PySide2 import QtWidgets, QtCore
import json

def fixTreeViewScrolling(tree):
    tree.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

def fillItem(item,valDict):
    for key,val in valDict.items():
        newItem = QtWidgets.QTreeWidgetItem()
        newItem.setText(0,key)
        if type(val) is dict:
            fillItem(newItem,val)
        item.addChild(newItem)


def loadfileStructure(tree):
    location = "./fileStructure.txt"
    structDict = ""
    tree.topLevelItem(0)
    with open(location,"r") as jsonfile:
        structDict = json.load(jsonfile)
    
    tree.noteStructure = structDict
    item = tree.topLevelItem(0)
    fillItem(item, structDict["Notebooks"])
    item = tree.topLevelItem(1)
    fillItem(item, structDict["Uncategorized"])