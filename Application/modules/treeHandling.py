
from PySide2 import QtWidgets, QtCore
from modules.fileHandling import currentNote
import json


def getJsonTree():
    location = "../Application/fileStructure.json"
    structDict  = ""
    with open(location,"r") as jsonfile:
        structDict = json.load(jsonfile)
    return structDict


def saveUpdatedJson(structDict):
    location = "../Application/fileStructure.json"
    with open(location,"w") as jsonfile:
        json.dump(structDict,jsonfile)


def fillItem(item,valDict):
    for key,val in valDict.items():
        newItem = QtWidgets.QTreeWidgetItem()
        newItem.setText(0,val["name"])
        newItem.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        if "path" in val["expanded"] and type(val["expanded"]["path"]) == str:
            pass
        else :
            fillItem(newItem,val["expanded"])

        item.addChild(newItem)


def loadfileStructure(tree):
    structDict = getJsonTree()
    item = tree.topLevelItem(0)
    item.takeChildren() # Current design is such that whenever a new note is created or a note is deleted the note is deleted from json and the file structure is reloaded. This design can be changed later
    fillItem(item, structDict["Notebooks"])
    item = tree.topLevelItem(1)
    item.takeChildren()
    fillItem(item, structDict["Uncategorized"])


def getLineage(item):
    if item.parent() is None:
        return [item.text(0)]
    else:
        return getLineage(item.parent()) + [item.parent().indexOfChild(item)]


def _itemVal(pathList,noteTree):
    keyindex = pathList.pop()
    for item in pathList:
        keys = [*noteTree]
        noteTree = noteTree[keys[item]]["expanded"]
    key  = [*noteTree][keyindex]
    return [key,noteTree]


# returns the value associated with an item in treeWidget
def itemVal(item):
    structDict = getJsonTree()
    pathList = getLineage(item)
    if len(pathList) == 1:
        return [pathList[0],structDict,structDict]
    return _itemVal(pathList[1:],structDict[pathList[0]]) + [structDict]


def isNote(item):
    details = itemVal(item)
    details = details[1][details[0]]
    if("expanded" in details and "path" in details["expanded"] and type(details["expanded"]["path"]) == str):
        return [True,details["expanded"]]
    return [False,[]]


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


def noteLoader(item, _fileName, _textEdit):
    note = isNote(item)
    if(note[0]):
        currentNote.openFile(item,note[1])
        from modules.noteHandling import loadNote
        loadNote(_fileName,_textEdit)
