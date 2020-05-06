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
    if(encrypt == True):
        encryptAllNotes(userInfo[1],userInfo[2],notes)
    else:
        decryptAllNotes(userInfo[1],userInfo[2],notes)
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


def decryptAllNotes(userPass,userSalt,notes):
    for note in notes:
        randomString = note['randomString']
        path = note['path']
        encrypted = False
        if (randomString in encNotes.keys()):
            encText0 = readText(path) # bytes
            aesD = AEScipher(encNotes[randomString],None,encText0,False)
            Text = bytes(aesD.Decrypt(),'utf8') # bytes
            encrypted = True
        else:
            Text = readText(path) # bytes
        aes = AEScipher(userPass,None,Text,False)
        outText = aes.Decrypt() # string
        if(encrypted == False):
            writeText(path,outText)
        else:
            aesE = AEScipher(encNotes[randomString],None,outText,True)
            outText1 = aesE.Encrypt() # bytes
            writeText(path,outText1,encrypted = True)


def encryptAllNotes(userPass,userSalt,notes):
    for note in notes:
        randomString = note['randomString']
        path = note['path']
        encrypted = False
        if(randomString in encNotes.keys()):
            encText0 = readText(path) # bytes
            aesD = AEScipher(encNotes[randomString],None,encText0,False)
            Text = aesD.Decrypt() # string 
            encrypted = True
        else:
            Text = readText(path) # string
        aes = AEScipher(userPass,None,Text,True)
        outText = aes.Encrypt() # bytes
        if(encrypted == False):
            writeText(path,outText,encrypted = True)
        else:
            outText = str(outText)
            aesE = AEScipher(encNotes[randomString],None,outText,True)
            outText1 = aesE.Encrypt() # bytes
            writeText(path,outText1,encrypted = True)




    


