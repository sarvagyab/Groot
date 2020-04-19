
from PySide2 import QtWidgets, QtCore
from modules.noteHandling import loadNote, loadFileName
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
    location = "./Application/fileStructure.json"
    structDict = ""
    tree.topLevelItem(0)
    with open(location,"r") as jsonfile:
        structDict = json.load(jsonfile)
    
    item = tree.topLevelItem(0)
    item.takeChildren()
    fillItem(item, structDict["Notebooks"])
    item = tree.topLevelItem(1)
    item.takeChildren()
    fillItem(item, structDict["Uncategorized"])



def itemVal(item,noteTree):
    if (item.text(0)!="Notebooks" and item.text(0)!= "Uncategorized"):
        return itemVal(item.parent(),noteTree)[item.text(0)]

    return noteTree[item.text(0)]



def noteLoader(item, _fileName, _textEdit):
    structDict = ""
    location = "./Application/fileStructure.json"
    with open(location,"r") as jsonfile:
        structDict = json.load(jsonfile)
    
    val = itemVal(item,structDict)
    if(type(val) == str):
        loadFileName(item.text(0),_fileName)
        loadNote(val, _textEdit)


    