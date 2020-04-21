from PySide2 import QtWidgets

#GUI
from GUIs.passwordDialog import Ui_passwordDialog

from modules.Exceptions import *
from modules.passwordHashing import storePassword


class password(object):
    def __init__(self):
        self.ERROR_MSG = ""
        self.passwordset = False
    
    def openPasswordDialog(self):
        print("Encryption button clicked")
        self.ui_p = Ui_passwordDialog()
        
        # slot-signals
        self.ui_p.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda:self.passwordEntered())
        self.ui_p.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.ui_p.passwordDialog.close())
       
        self.passwordEntered()
    
    def passwordEntered(self):
        self.pass1 = self.ui_p.passwordLineEdit.text()
        self.pass2 = self.ui_p.RepasswordLineEdit.text()
        self.setPassword()


    def setPassword(self):
        """ Check whether password entered in 'password' and 're-enter password' fields are same or not."""
        try:
            self.arePasswordSame()
            self.doesLengthGt8()
            self.doesContainCapitalLetter()
            self.doesContainDigit()
        except:
            self.displayInstruction()
        else:
            self.ERROR_MSG = "Password is set successfully."
            self.passwordset = True
            self.displayInstruction()
            # storePassword(pass1)
    
    def displayInstruction(self):
        # Prepare message to display
        if(self.passwordset == False):
            MSG ="<html><head/><body><p><span style=\" color:#ff0000;\">"+self.ERROR_MSG+"</span></p></body></html>"
        else:
            MSG ="<html><head/><body><p><span style=\" color:#00ff0d;\">"+self.ERROR_MSG+"</span></p></body></html>"
        self.ui_p.Errortext.setText(MSG)


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

