import scrypt
import os
import json
from modules.treeHandling import updateItem
from modules.encryptNote import AEScipher
from modules.noteHandling import writeText

def hashPassword(currentNote,currentFileName,password,main_window,datalength= 64,encrypted=True):
    if(encrypted == True):
        salt = currentNote._details['salt']
    else:
        salt = generateSalt() # add dynamic salt
        aes = AEScipher(password,currentNote)
        enc_txt = aes.Encrypt()
        writeText(currentNote._details['path'],enc_txt,encrypted = True)
        main_window.ui.plainTextEdit.setPlainText("<!--encrypted-->")
        main_window.ui.encryptionButton.setEnabled(False)
        main_window.ui.decryptionButton.setEnabled(True)
        main_window.ui.permanentDecrypt.setEnabled(True)
        currentNote._details['encrypted'] = "True"
        updateJson(currentNote)
        removeFromDList(main_window,currentNote)
        addInEList(main_window,currentNote,password)

    h_pass= Hash(password,salt)
    print("Hashed password")
    if(encrypted == False):
        storePassword(currentNote,currentFileName,h_pass,salt)
    return h_pass

def Hash(password,salt,datalength=64):
    """Hash password using scrypt"""
    hashed_password = scrypt.hash(password,salt) # hash password
    return hashed_password

def storePassword(currentNote,currentFileName,h_password,salt):
    """
    Need to add checks for already encrypted files
    """
    updateDict = {}
    updateDict['name'] = currentNote._name
    currentNote._details['salt'] = salt
    currentNote._details['h_pass'] = str(h_password)
    updateDict['expanded'] = currentNote._details
    updateItem({currentNote.getRandomString():updateDict})
    print("Stored Password")

def generateSalt(datalength = 64):
    return str(os.urandom(datalength))

def updateJson(currentNote):
    updateDict = {}
    updateDict['name'] = currentNote._name
    updateDict['expanded'] = currentNote._details
    updateItem({currentNote.getRandomString():updateDict})

def removeFromDList(main_window,currentNote):
    randomstring= currentNote._details['randomString']
    if(randomstring in main_window.decryptedNotes.keys()):
        main_window.decryptedNotes.pop(randomstring)

def addInEList(main_window,currentNote,password):
    randomstring= currentNote._details['randomString']
    if(not randomstring in main_window.encryptedInSession.keys()):
        main_window.encryptedInSession[randomstring] = password
    