import copy

from PySide2 import QtWidgets

import Application.modules.userLogin
from Application.modules.treeHandling import getJsonTree
from Application.modules.passwordHashing import Hash
from Application.modules.noteHandling import readText,writeText
from Application.modules.encryptNote import AEScipher

from Application.GUIs.verifyPasswordDialog import Ui_verifyPasswordDialog

encNotes = {}

def traverseDict(Dict,notes):
    if(type(Dict) == type({})):

        if('expanded' in Dict.keys()):
            if('randomString' in Dict['expanded'].keys()):
                resDict = Dict['expanded']
                resDict['name'] = Dict['name']
                notes.append(resDict)
        if(len(Dict.keys())> 0):
            for key in Dict.keys():  
                traverseDict(Dict[key],notes)
    return notes


def getAllNotes():
    fileStruct = getJsonTree()
    return traverseDict(fileStruct,[])

def getEncNoteList():
    EDict = {}
    notes = getAllNotes()
    success = []
    for note in notes:
        if('encrypted' in note): 
            if(note['encrypted'] == 'True'):
                openDialog(note,success)
                if len(success) > 0:
                    encNotes.clear()
                    return (False,False)
    EDict = copy.deepcopy(encNotes)
    encNotes.clear()
    return (EDict,notes)

def _encryptDecryptAllNotes(window,encrypt):
    EDict,notes = getEncNoteList()
    if(EDict == False):
        encNotes.clear()
        return False
    userInfo = Application.modules.userLogin.readUserInfo()
    uPass = userInfo[1]
    if(encrypt == True):
        encryptAllNotes(uPass,notes,EDict)
    else:
        decryptAllNotes(uPass,notes,EDict)
    window.encryptAll = encrypt
    userInfo[3] = str(encrypt) 
    Application.modules.userLogin.storeUserInfoInFile('./Application/User',"login",userInfo)
    return True

def openDialog(note,success):
    ui_pv = Ui_verifyPasswordDialog()
    verifyDialog = QtWidgets.QDialog()
    ui_pv.setupUi(verifyDialog)
    ui_pv.title.setText("<b>"+note['name']+"</b>")
    # signal slots
    ui_pv.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda: closeAndReturn(verifyDialog,success))
    ui_pv.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: fetchPassAndVerify(ui_pv,verifyDialog,note))
    verifyDialog.exec_()

def closeAndReturn(verifyDialog,success):
    verifyDialog.close()
    success.append(0)


def fetchPassAndVerify(ui,dialog,note):
    enteredPass = ui.passwordLineEdit.text()
    salt = note['salt']
    storedPass = note['h_pass']
    hashedPass = str(Hash(enteredPass,salt))
    if(hashedPass == storedPass):
        MSG ="<html><head/><body><p><span style=\" color:#00ff00;\">Correct Password</span></p></body></html>"
        ui.Errortext.setText(MSG)
        dialog.close()
        encNotes[note['randomString']] = enteredPass
    else:
        MSG ="<html><head/><body><p><span style=\" color:#ff0000;\">Incorrect Password</span></p></body></html>"
        ui.Errortext.setText(MSG)


def decryptAllNotes(userPass,notes,encNotes):
    for note in notes:
        randomString = note['randomString']
        path = note['path']
        encrypted = False
        if (randomString in encNotes.keys()):
            encText0 = readText(path) # bytes

            aesD = AEScipher(encNotes[randomString],None,bytes(encText0,encoding = 'utf8'),False)
            Text = aesD.Decrypt() # string

            encrypted = True
        else:
            Text = readText(path) # bytes
        aes = AEScipher(userPass,None,bytes(Text,encoding='utf8'),False)
        outText = aes.Decrypt() # string
        if(encrypted == False):
            writeText(path,outText)
        else:
            if(not isinstance(outText,str)):
                outText = str(outText,encoding='utf8') 
            aesE = AEScipher(encNotes[randomString],None,outText,True)
            outText1 = aesE.Encrypt() # bytes
            writeText(path,outText1,encrypted = True)


def encryptAllNotes(userPass,notes,encNotes):
    for note in notes:
        randomString = note['randomString']
        path = note['path']
        encrypted = False
        if(randomString in encNotes.keys()):
            encText0 = readText(path) # bytes

            aesD = AEScipher(encNotes[randomString],None,bytes(encText0,encoding = 'utf8'),False)
            Text = aesD.Decrypt() # string 
            
            encrypted = True
        else:
            Text = readText(path) # string
        aes = AEScipher(userPass,None,Text,True)
        outText = aes.Encrypt() # bytes

        if(encrypted == False):
            writeText(path,outText,encrypted = True)
        else:
            if(not isinstance(outText,str)):
                outText = str(outText,encoding='utf8') 
            aesE = AEScipher(encNotes[randomString],None,outText,True)
            outText1 = aesE.Encrypt() # bytes
            writeText(path,outText1,encrypted = True)




    


