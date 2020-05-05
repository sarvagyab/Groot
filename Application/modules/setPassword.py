from PySide2 import QtWidgets

#GUI
from GUIs.passwordDialog import Ui_passwordDialog
from GUIs.verifyPasswordDialog import Ui_verifyPasswordDialog
from GUIs.changePasswordDialog import Ui_changePasswordDialog

from modules.Exceptions import *
from modules.passwordHashing import hashPassword
from modules.treeHandling import itemVal,_itemVal,updateItem
from modules.encryptNote import AEScipher
from modules.noteHandling import writeText
from modules.fileHandling import currentNote
import modules.userLogin

class password(object):
    def __init__(self,Window,ui = None):
        self.ERROR_MSG = ""
        self.passwordset = False
        self.verifiedPassword = False
        self.main_Window = Window
        self.pass1 = ""
        self.pass2 = ""
        self.ui_p = ui
    
    def openPasswordDialog(self):
        if(currentNote._file != None):
            print("Encryption button clicked")
            # First check whether any note is selected or not
            self.currentNote = currentNote
            self.currentFileName = self.currentNote._name
            randomstring = self.currentNote._details['randomString']
            if( randomstring in self.main_Window.decryptedNotes):
                self.pass1 = self.main_Window.decryptedNotes[randomstring]
                hashPassword(self.currentNote,self.currentFileName,self.pass1,self.main_Window,datalength = 64 ,encrypted=False)
            else:
                self.ui_p = Ui_passwordDialog()
                if(self.currentNote._open == True):
                    print("Trying to encrypt {}".format(self.currentFileName))
                    # slot-signals
                    self.ui_p.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda:self.passwordEntered())
                    self.ui_p.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.closeDialog(self.ui_p.passwordDialog))

    def openVerifyPasswordDialog(self,permanentdecrypt = False):
        if(currentNote._file != None):
            self.currentNote = currentNote
            self.currentFileName = self.currentNote.getFilename()
            print("Decryption button clicked",self.currentFileName,permanentdecrypt)
            randomstring = self.currentNote._details['randomString']
            if(randomstring in self.main_Window.encryptedInSession):
                self.pass1 = self.main_Window.encryptedInSession[randomstring]
                self.verifyAndDecryptPassword(use_savedPassword= True,permanentdecrypt = permanentdecrypt)
            else:
                if(self.currentNote._open == True and self.isEncrypted()):
                    self.ui_pv = Ui_verifyPasswordDialog()
                    self.verifyDialog = QtWidgets.QDialog()
                    self.ui_pv.setupUi(self.verifyDialog)
                    self.verifyDialog.show()
                    print("Trying to Decrypt {}".format(self.currentFileName))

                    # slot-signals
                    self.ui_pv.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.closeDialog(self.verifyDialog))
                    self.ui_pv.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda:self.verifyAndDecryptPassword(use_savedPassword=False,permanentdecrypt = permanentdecrypt))

    def openChangeEncryptionPasswordDialog(self):
        if(currentNote._file != None):
            self.currentNote = currentNote
            self.currentFileName = self.currentNote.getFilename()
            self.ui_p = Ui_changePasswordDialog()
            self.ui_p.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.closeDialog(self.ui_p.changePasswordDialog))
            self.ui_p.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda:self.changeEncryptionPassword())

    def passwordEntered(self):
        self.pass1 = self.ui_p.passwordLineEdit.text()
        self.pass2 = self.ui_p.RepasswordLineEdit.text()
        self.setPassword()
        if(self.passwordset == True ):
            print("Password valid")
            self.closeDialog(self.ui_p.passwordDialog)
            hashPassword(self.currentNote,self.currentFileName,self.pass1,self.main_Window,datalength = 64 ,encrypted=False)
            
    def verifyAndDecryptPassword(self,use_savedPassword = False,permanentdecrypt = False):
        if(use_savedPassword == False):
            if(self.verifyPassword(self.ui_pv.passwordLineEdit,self.ui_pv.Errortext) == False):
                return
            
        # now decrypting and displaying decrypted note
        self.decryptAndDisplay() # display decrypted text

        self.main_Window.ui.encryptionButton.setEnabled(True) # enable encryption button
        self.main_Window.ui.decryptionButton.setEnabled(False) # disable decryption button
        self.main_Window.ui.permanentDecrypt.setEnabled(False) # disable decryption button
        self.main_Window.ui.changePasswordButton.setEnabled(False)
        # update in json tree
        self.updateJson()    

        # Add this note to the dict
        if(permanentdecrypt == False):
            self.updateDList()
        self.updateEList()    

        if(use_savedPassword == False):
            self.closeDialog(self.verifyDialog) # close dialog
        return True
        
    def verifyPassword(self,_passwordLineEdit,_errorLineEdit):
        self.pass1 = _passwordLineEdit.text()
        hashed_pass = str(hashPassword(self.currentNote,self.currentFileName,self.pass1,self.main_Window,datalength = 64,encrypted = True))
        fetched_pass = self.currentNote._details['h_pass']
        if(hashed_pass == fetched_pass):
            print("verified")
            self.verifiedPassword = False
            return True
        else:
            self.ERROR_MSG = "Incorrect Password"
            self.displayInstruction(_errorLineEdit)
            return False

    
    def decryptAndDisplay(self):
        txt = currentNote.getText(False)
        aes = AEScipher(self.pass1,self.currentNote,txt = txt,encrypt = False) # Prepare to decrypt the file
        d_txt = aes.Decrypt()                                       # decrypted text
        userinfo =modules.userLogin.readUserInfo()
        if(userinfo[3] == 'True'):
            writeText(self.currentNote._details['path'],bytes(d_txt,encoding='utf8'),encrypted = True) # write decrypted text in file 
            aes_1 = AEScipher(userinfo[1],self.currentNote,txt = bytes(d_txt,encoding='utf8'),encrypt = False)
            d_txt_1 = aes_1.Decrypt()
            self.main_Window.ui.plainTextEdit.setPlainText(d_txt_1)
        else:
            self.main_Window.ui.plainTextEdit.setPlainText(d_txt)
            writeText(self.currentNote._details['path'],d_txt) # write decrypted text in file 


    def changeEncryptionPassword(self):
        if(self.verifyPassword(self.ui_p.oldPasswordLine,self.ui_p.Errortext) == True):
            self.decryptAndDisplay()
            self.pass1 = self.ui_p.passwordLineEdit.text()
            self.pass2 = self.ui_p.RepasswordLineEdit.text()
            self.setPassword()
            if(self.passwordset == True):
                self.closeDialog(self.ui_p.changePasswordDialog)
                hashPassword(self.currentNote,self.currentFileName,self.pass1,self.main_Window,datalength = 64 ,encrypted=False)




    def setPassword(self):
        """ Check whether password entered in 'password' and 're-enter password' fields are same or not."""
        try:
            self.arePasswordSame()
            self.doesLengthGt8()
            self.doesContainCapitalLetter()
            self.doesContainDigit()
        except:
            self.displayInstruction(self.ui_p.Errortext)
        else:
            self.ERROR_MSG = "Password is set successfully."
            self.passwordset = True
            self.displayInstruction(self.ui_p.Errortext)
    
    def isEncrypted(self):
        if(self.currentNote._details['encrypted'] == "True"):
            return True
        print("First encrypt the file")
        return False

    def displayInstruction(self,_textEdit):
        # Prepare message to display
        if(self.passwordset == False or self.verifiedPassword == False):
            MSG ="<html><head/><body><p><span style=\" color:#ff0000;\">"+self.ERROR_MSG+"</span></p></body></html>"
        else:
            MSG ="<html><head/><body><p><span style=\" color:#00ff0d;\">"+self.ERROR_MSG+"</span></p></body></html>"
        _textEdit.setText(MSG)


    def arePasswordSame(self):
        """Check whether entered passwards are same or not"""
        if(self.pass1 != self.pass2):
            self.ERROR_MSG = "Passwards did not match"
            raise PasswardDidNotMatchError(self.ERROR_MSG)

    def doesLengthGt8(self):
        """Check whether entered passwards have length greater than 8 or not"""
        if(len(self.pass1) < 8):
            self.ERROR_MSG = "Password must contain atleast 8 characters."
            raise LengthNotEnoughError(self.ERROR_MSG) 

    def doesContainCapitalLetter(self):
        """Check whether entered passwards have atleast one capital letter or not"""    
        if(not any(x.isupper() for x in self.pass1)):
            self.ERROR_MSG = "Password must contain atleast one capital letter"
            raise DoesNotContainCapitalLetterError(self.ERROR_MSG)

    def doesContainDigit(self):
        """Check whether entered passwards have atleast one digit or not"""    
        if(not any(x.isdigit() for x in self.pass1)):
            self.ERROR_MSG = "Password must contain atleast one digit"
            raise DoesNotContainCapitalLetterError(self.ERROR_MSG)
    
    def closeDialog(self,ui_dialog):
        ui_dialog.close()

    def updateDList(self):
        randomstring = currentNote._details['randomString']
        if(randomstring not in self.main_Window.decryptedNotes):
            print(randomstring)
            self.main_Window.decryptedNotes[randomstring] = self.pass1
    
    def updateEList(self):
        randomstring = currentNote._details['randomString']
        if(randomstring in self.main_Window.encryptedInSession):
            self.main_Window.encryptedInSession.pop(randomstring)

    def updateJson(self):
        updateDict = {}
        updateDict['name'] = self.currentNote._name
        self.currentNote._details['encrypted'] = "False"
        updateDict['expanded'] = self.currentNote._details
        updateItem({self.currentNote.getRandomString():updateDict})