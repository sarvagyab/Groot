import os

from modules.Exceptions import *
import modules.passwordHashing

def setUsernameAndPassword(username,pas,rpas,ui,dialog):
    if(isValidPassword(pas,rpas) == True):
        dialog.accept()
        salt = modules.passwordHashing.generateSalt()
        h_pass = modules.passwordHashing.Hash(pas,salt)
        storeUsernameAndPasswordInFile('./User',username,"login",h_pass,salt)


def storeUsernameAndPasswordInFile(path,username,filename,h_pass,salt):
    if(not os.path.exists(path)):
        os.makedirs(path)
    with open(os.path.join(path,filename + ".txt"),"w") as store_file:
        txt = username + '\n' + str(h_pass) + '\n' + salt + '\n' + "True"
        store_file.write(txt)

def verifyUser(password,ui,dialog):
    (username,h_pass,salt,encryptAll) = readUserInfo()
    enteredH_pass = modules.passwordHashing.Hash(password,salt)
    if(str(enteredH_pass) == h_pass):
        print("user verified")
        dialog.accept()     
    else:
        print("incorrect password")
        MSG = "<html><head/><body><p><span style=\" color:#ff0000;\">Incorrect password</span></p></body></html>"
        ui.Errortext.setText(MSG)

def readUserInfo():
    path = './User/login.txt'
    with open(path,"r") as file:
        return file.read().split('\n')

def isValidPassword(pass1,pass2):
    try:
        arePasswordSame(pass1,pass2)
        doesLengthGt8(pass1)
        doesContainCapitalLetter(pass1)
        doesContainDigit(pass1)
        return True
    except:
        return False

def arePasswordSame(pass1,pass2):
        """Check whether entered passwards are same or not"""
        if(pass1 != pass2):
            ERROR_MSG = "Passwards did not match"
            raise PasswardDidNotMatchError(ERROR_MSG)

def doesLengthGt8(pass1):
    """Check whether entered passwards have length greater than 8 or not"""
    if(len(pass1) < 8):
        ERROR_MSG = "Password must contain atleast 8 characters."
        raise LengthNotEnoughError(ERROR_MSG) 

def doesContainCapitalLetter(pass1):
    """Check whether entered passwards have atleast one capital letter or not"""    
    if(not any(x.isupper() for x in pass1)):
        ERROR_MSG = "Password must contain atleast one capital letter"
        raise DoesNotContainCapitalLetterError(ERROR_MSG)

def doesContainDigit(pass1):
    """Check whether entered passwards have atleast one digit or not"""    
    if(not any(x.isdigit() for x in pass1)):
        ERROR_MSG = "Password must contain atleast one digit"
        raise DoesNotContainCapitalLetterError(ERROR_MSG)
    
