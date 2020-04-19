from PySide2 import QtWidgets
from .Exceptions import *

ERROR_MSG = ""

def setPassword(pass1,pass2,errorLabel):
    """ Check whether password entered in 'password' and 're-enter password' fields are same or not."""
    try:
        arePasswordSame(pass1,pass2)
        doesLengthGt8(pass1)
        doesContainCapitalLetter(pass1)
        doesContainDigit(pass1)
    except:
        displayInstruction(errorLabel,False)
    else:
        global ERROR_MSG
        ERROR_MSG = "Password is set successfully."
        displayInstruction(errorLabel,True)   

def arePasswordSame(pass1,pass2):
    """Check whether entered passwards are same or not"""
    if(pass1 != pass2):
        global ERROR_MSG 
        ERROR_MSG = "Passwards did not match"
        raise PasswardDidNotMatchError(ERROR_MSG)

def doesLengthGt8(pass1):
    """Check whether entered passwards have length greater than 8 or not"""
    if(len(pass1) < 8):
        global ERROR_MSG 
        ERROR_MSG = "Password must contain atleast 8 characters."
        raise LengthNotEnoughError(ERROR_MSG) 

def doesContainCapitalLetter(pass1):
    """Check whether entered passwards have atleast one capital letter or not"""    
    if(not any(x.isupper() for x in pass1)):
        global ERROR_MSG 
        ERROR_MSG = "Password must contain atleast one capital letter"
        raise DoesNotContainCapitalLetterError(ERROR_MSG)

def doesContainDigit(pass1):
    """Check whether entered passwards have atleast one digit or not"""    
    if(not any(x.isdigit() for x in pass1)):
        global ERROR_MSG 
        ERROR_MSG = "Password must contain atleast one digit"
        raise DoesNotContainCapitalLetterError(ERROR_MSG)

def displayInstruction(errorLabel,success):
    """Display instructions to the user using QLabel Widget"""
    # Prepare message to display
    if(success == False):
        MSG ="<html><head/><body><p><span style=\" color:#ff0000;\">"+ERROR_MSG+"</span></p></body></html>"
    else:
        MSG ="<html><head/><body><p><span style=\" color:#00ff0d;\">"+ERROR_MSG+"</span></p></body></html>"
    errorLabel.setText(MSG)