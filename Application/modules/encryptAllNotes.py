from PySide2 import QtWidgets

from modules.treeHandling import getJsonTree
from modules.passwordHashing import Hash
from modules.userLogin import readUserInfo,storeUserInfoInFile
from modules.noteHandling import readText,writeText
from modules.encryptNote import AEScipher

from GUIs.verifyPasswordDialog import Ui_verifyPasswordDialog

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

def _encryptDecryptAllNotes(window,encrypt):
    notes = getAllNotes()
    for note in notes:
        if('encrypted' in note): 
            if(note['encrypted'] == 'True'):
                openDialog(note)
    userInfo = readUserInfo()
    encrpytDecryptAllNotes(userInfo[1],userInfo[2],notes,encrypt)
    window.encryptAll = encrypt
    userInfo[3] = str(encrypt) 
    storeUserInfoInFile('./User',"login",userInfo)

def openDialog(note):
    ui_pv = Ui_verifyPasswordDialog()
    verifyDialog = QtWidgets.QDialog()
    ui_pv.setupUi(verifyDialog)
    # signal slots 
    ui_pv.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:verifyDialog.close())
    ui_pv.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: fetchPassAndVerify(ui_pv,verifyDialog,note))
    ui_pv.title.setText("<b>"+note['name']+"</b>")
    verifyDialog.exec()

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
        return


def encrpytDecryptAllNotes(userPass,userSalt,notes,encrypt):
    for note in notes:
        randomString = note['randomString']
        path = note['path']
        encrypted = False
        if (randomString in encNotes.keys()):
            encText0 = readText(path)
            aesD = AEScipher(encNotes[randomString],None,encText0,False)
            if(encrypt == False):
                Text = bytes(aesD.Decrypt(),'utf8') # bytes
            else:
                Text = aesD.Decrypt() # string
            encrypted = True
        else:
            Text = readText(path)
        if(encrypt == True):
            aes = AEScipher(userPass,None,Text,True)
            outText = aes.Encrypt() # bytes
        else:
            aes = AEScipher(userPass,None,Text,False)
            outText = aes.Decrypt() # string
        if(encrypted == True):
            aesE = AEScipher(encNotes[randomString],None,str(outText),True)
            txt = aesE.Encrypt() # bytes
            writeText(path,txt,encrypted = True)
        else:
            if(encrypt == True):
                writeText(path,outText,encrypted = True)
            else:
                writeText(path,outText)




    


