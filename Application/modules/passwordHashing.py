import scrypt
import os
import json
from modules.treeHandling import updateItem
from modules.encryptNote import AEScipher
# from modules.encryptNote import encryptNote

def hashPassword(currentNote,currentFileName,password,datalength= 64):
    print("Hashed password")
    salt = str(os.urandom(datalength)) # add dynamic salt
    h_pass= Hash(password,salt)
    storePassword(currentNote,currentFileName,h_pass,salt)
    aes = AEScipher(password,currentNote)

def Hash(password,salt,datalength=64):
    """Hash password using scrypt"""
    hashed_password = scrypt.hash(password,salt) # hash password
    return hashed_password

def storePassword(currentNote,currentFileName,h_password,salt):
    """
    Need to add checks for already encrypted files
    """
    print("Stored Password")
    currentNote['salt'] = salt
    currentNote['h_pass'] = str(h_password)
    # print(currentFileName,currentNote)
    updatedNote = {currentFileName : currentNote}
    # print(updatedNote)
    updateItem(updatedNote) 

def verifyPassword():
    pass
