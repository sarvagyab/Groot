import os

import Application.modules.encryptAllNotes
import Application.modules.passwordHashing
from Application.modules.Exceptions import *

def setUsernameAndPassword(username,pas,rpas,errorText,dialog = None,store = True):
    if(username == ''):
        showErrorOnDialog("Enter Username",errorText)
        return
    if(isValidPassword(pas,rpas,errorText) == True):
        if (dialog is not None):
            dialog.accept()
        salt = Application.modules.passwordHashing.generateSalt()
        h_pass = Application.modules.passwordHashing.Hash(pas,salt) # bytes
        if(store == True):
            userInfo = [username,str(h_pass),salt,"True"]
            storeUserInfoInFile('./Application/User',"login",userInfo)
        return (str(h_pass),salt)


def storeUserInfoInFile(path,filename,userInfo):
    if(not os.path.exists(path)):
        os.makedirs(path)
    with open(os.path.join(path,filename + ".txt"),"w",encoding='utf8') as store_file:
        txt = ''
        for info in userInfo:
            txt += info + '\n'     
        store_file.write(txt)

def verifyUser(password,label,dialog = None):
    (username,h_pass,salt,encryptAll) = readUserInfo()
    enteredH_pass = Application.modules.passwordHashing.Hash(password,salt)
    if(str(enteredH_pass) == h_pass):
        print("user verified")
        MSG = "<html><head/><body><p><span style=\" color:#00ff00;\">Correct password</span></p></body></html>"
        label.setText(MSG)
        if(dialog is not None):
                dialog.accept()
        return True
    else:
        print("incorrect password")
        MSG = "<html><head/><body><p><span style=\" color:#ff0000;\">Incorrect password</span></p></body></html>"
        label.setText(MSG)
        return False

def readUserInfo():
    path = './Application/User/login.txt'
    if(not os.path.exists(path)):
        os.makedirs(path)
    with open(path,"r") as file:
        return file.read().strip().split('\n')

def isValidPassword(pass1,pass2,errorText):
    try:
        arePasswordSame(pass1,pass2)
        doesLengthGt8(pass1)
        doesContainCapitalLetter(pass1)
        doesContainDigit(pass1)
        showErrorOnDialog("Correct Password",errorText,alert=False)
        return True
    except PasswardDidNotMatchError:
        ERROR_MSG = "Passwards did not match"
        showErrorOnDialog(ERROR_MSG,errorText)
        return False
    except LengthNotEnoughError:
        ERROR_MSG = "Password must contain atleast 8 characters."
        showErrorOnDialog(ERROR_MSG,errorText)
        return False
    except DoesNotContainCapitalLetterError:
        ERROR_MSG = "Password must contain atleast one capital letter"
        showErrorOnDialog(ERROR_MSG,errorText)
        return False
    except DoesNotContainCapitalLetterError:
        ERROR_MSG = "Password must contain atleast one digit"
        showErrorOnDialog(ERROR_MSG,errorText)
        return False
        

def showErrorOnDialog(msg,errorText,alert = True):
    if alert:
        MSG = "<html><head/><body><p><span style=\" color:#ff0000;\">"+msg+"</span></p></body></html>"
    else:
        MSG = "<html><head/><body><p><span style=\" color:#00ff00;\">"+msg+"</span></p></body></html>"
    errorText.setText(MSG)

def changePassword(h_pass,salt):
    EncDict,notes = Application.modules.encryptAllNotes.getEncNoteList()
    if(EncDict == False):
        print("here")
        return False
    userInfo = readUserInfo()
    oldPass = userInfo[1]
    print(EncDict)
    if(userInfo[3] == 'True'):
        Application.modules.encryptAllNotes.decryptAllNotes(oldPass,notes,EncDict) # decrypt all notes using old password
        Application.modules.encryptAllNotes.encryptAllNotes(h_pass,notes,EncDict) # encrypt all notes using new password
    userInfo[1] = h_pass
    userInfo[2] = salt
    storeUserInfoInFile('./Application/User',"login",userInfo) # store new pass
    return True


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
    
