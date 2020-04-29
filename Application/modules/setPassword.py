from PySide2 import QtWidgets

#GUI
from GUIs.passwordDialog import Ui_passwordDialog
from GUIs.verifyPasswordDialog import Ui_verifyPasswordDialog

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

    def openVerifyPasswordDialog(self):
        print("Decryption button clicked")
        # First check whether any note is selected or not
        self.currentNote = currentNote
        if(self.currentNote._open == True and self.isEncrypted()):
            self.currentFileName = self.currentNote.getFilename()
            self.ui_pv = Ui_verifyPasswordDialog()
            print("Trying to Decrypt {}".format(self.currentFileName))

            # slot-signals
            self.ui_pv.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.closeDialog(self.ui_pv.verifyPasswordDialog))
            self.ui_pv.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda:self.verifyAndDecryptPassword())

    
    def passwordEntered(self):
        self.pass1 = self.ui_p.passwordLineEdit.text()
        self.pass2 = self.ui_p.RepasswordLineEdit.text()
        self.setPassword()
        if(self.passwordset == True ):
            print("Password valid")
            self.closeDialog(self.ui_p.passwordDialog)
            hashPassword(self.currentNote,self.currentFileName,self.pass1,self.main_Window,datalength = 64 ,encrypted=False)
            
    def verifyAndDecryptPassword(self):
        self.pass1 = self.ui_pv.passwordLineEdit.text()
        hashed_pass = str(hashPassword(self.currentNote,self.currentFileName,self.pass1,self.main_Window,datalength = 64,encrypted = True))
        fetched_pass = self.currentNote._details['h_pass']
        if(hashed_pass == fetched_pass):
            print("verified")
            self.verifiedPassword = False

            # now decrypting and displaying decrypted note
            txt = currentNote.getText(False)
            aes = AEScipher(self.pass1,self.currentNote,txt = txt,encrypt = False) # Prepare to decrypt the file
            d_txt = aes.Decrypt()                                       # decrypted text
            writeText(self.currentNote._details['path'],bytes(d_txt,encoding='utf8'),encrypted = True) # write decrypted text in file 
            userinfo =modules.userLogin.readUserInfo()
            aes_1 = AEScipher(userinfo[1],self.currentNote,txt = bytes(d_txt,encoding='utf8'),encrypt = False)
            d_txt_1 = aes_1.Decrypt()
            self.main_Window.ui.plainTextEdit.setPlainText(d_txt_1) # display decrypted text
            self.main_Window.ui.encryptionButton.setEnabled(True) # enable encryption button
            self.main_Window.ui.decryptionButton.setEnabled(False) # disable decryption button
            # update in json tree
            self.updateJson()    

            # Add this note to the dict
            self.updateDList()    

            self.closeDialog(self.ui_pv.verifyPasswordDialog) # close dialog
            return True
        else:
            self.ERROR_MSG = "Incorrect Password"
            self.displayInstruction(self.ui_pv.Errortext)
            return False


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
        print("First encrypt the file you motherfucker")
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
            self.main_Window.decryptedNotes[randomstring] = self.pass1

    def updateJson(self):
        updateDict = {}
        updateDict['name'] = self.currentNote._name
        self.currentNote._details['encrypted'] = "False"
        updateDict['expanded'] = self.currentNote._details
        updateItem({self.currentNote.getRandomString():updateDict})