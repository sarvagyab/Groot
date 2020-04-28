import scrypt
import os
import json
from modules.treeHandling import updateItem
from modules.encryptNote import AEScipher
from modules.noteHandling import writeText
# from modules.encryptNote import encryptNote

def hashPassword(currentNote,currentFileName,password,datalength= 64,encrypted=True):
    if(encrypted == True):
        salt = currentNote._details['salt']
    else:
        salt = generateSalt() # add dynamic salt
        aes = AEScipher(password,currentNote)
        writeText(currentNote._details['path'],aes.Encrypt(),encrypted = True)

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