import scrypt
import os
import json
from modules.treeHandling import updateItem
from modules.encryptNote import AEScipher
from modules.noteHandling import writeText
# from modules.encryptNote import encryptNote

def hashPassword(currentNote,currentFileName,password,datalength= 64,encrypted=True):
    if(encrypted == True):
        salt = currentNote['salt']
    else:
        salt = str(os.urandom(datalength)) # add dynamic salt
        aes = AEScipher(password,currentNote)
        writeText(currentNote['path'],aes.Encrypt(),encrypted = True)

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
    currentNote['salt'] = salt
    currentNote['h_pass'] = str(h_password)
    updatedNote = {currentNote['name'] : currentNote}
    print("Stored Password")
    updateItem(updatedNote) 