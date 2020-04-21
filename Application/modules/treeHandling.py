
from PySide2 import QtWidgets, QtCore
from modules.noteHandling import loadNote, loadFileName
import json


def getJsonTree():
    location = "../Application/fileStructure.json"
    structDict  = ""
    with open(location,"r") as jsonfile:
        structDict = json.load(jsonfile)
    return structDict

def fixTreeViewScrolling(tree):
    tree.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)


def fillItem(item,valDict):
    for key,val in valDict.items():
        newItem = QtWidgets.QTreeWidgetItem()
        newItem.setText(0,key)
        if "path" in val and type(val["path"]) == str:
            pass
        else :
            fillItem(newItem,val)

        item.addChild(newItem)


def loadfileStructure(tree):
    structDict = getJsonTree()
    item = tree.topLevelItem(0)
    item.takeChildren() # Current design is such that whenever a new note is created or a note is deleted the note is deleted from json and the file structure is reloaded. This design can be changed later
    fillItem(item, structDict["Notebooks"])
    item = tree.topLevelItem(1)
    item.takeChildren()
    fillItem(item, structDict["Uncategorized"])


def _itemVal(item,noteTree):
    if (item.text(0)!="Notebooks" and item.text(0)!= "Uncategorized"):
        return _itemVal(item.parent(),noteTree)[item.text(0)]

    return noteTree[item.text(0)]


# returns the value associated with an item in treeWidget
def itemVal(item):
    structDict = getJsonTree()
    return _itemVal(item,structDict)

def _updateItem(changeDict,structDict): # DFS
    if(type(structDict) == type({})): 
        for key in changeDict.keys():
            if(key in structDict.keys()): # found the key
                structDict[key] = changeDict[key]
            elif(len(structDict.keys())> 0):
                for key in structDict.keys():
                    _updateItem(changeDict,structDict[key])

def updateItem(changeDict):
    structDict = getJsonTree()
    _updateItem(changeDict,structDict)
    saveUpdatedJson(structDict) # save updated json to the file

def saveUpdatedJson(structDict):
    location = "../Application/fileStructure.json"
    with open(location,"w") as jsonfile:
        json.dump(structDict,jsonfile)
    
def noteLoader(item, _fileName, _textEdit):
    val = itemVal(item)
    if("path" in val and type(val["path"]) == str):
        loadFileName(item.text(0),_fileName)
        loadNote(val["path"], _textEdit)
