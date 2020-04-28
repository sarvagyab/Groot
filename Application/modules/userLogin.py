import os

from modules.setPassword import password
from modules.passwordHashing import Hash,generateSalt

def setUsernameAndPassword(username,pas,rpas,ui,dialog):
    pwd = password(dialog)
    pwd.pass1 = pas
    pwd.pass2 = rpas
    pwd.ui_p = ui
    pwd.setPassword()
    if(pwd.passwordset == True):
        dialog.accept()
        salt = generateSalt()
        h_pass = Hash(pas,salt)
        storeUsernameAndPasswordInFile('./User',username,"login",h_pass,salt)


def storeUsernameAndPasswordInFile(path,username,filename,h_pass,salt):
    if(not os.path.exists(path)):
        os.makedirs(path)
    with open(os.path.join(path,filename + ".txt"),"w") as store_file:
        txt = username + '\n' + str(h_pass) + '\n' + salt
        store_file.write(txt)

def verifyUser(password,ui,dialog):
    path = './User/login.txt'
    with open(path,"r") as file:
        (username,h_pass,salt) = file.read().split('\n')
    enteredH_pass = Hash(password,salt)
    if(str(enteredH_pass) == h_pass):
        print("user verified")
        dialog.accept()     
    else:
        print("incorrect password")
        MSG = "<html><head/><body><p><span style=\" color:#ff0000;\">Incorrect password</span></p></body></html>"
        ui.Errortext.setText(MSG)
