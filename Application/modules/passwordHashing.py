import scrypt
import os
from stat import S_IREAD,SF_IMMUTABLE,S_IWUSR,SF_NOUNLINK,UF_NODUMP,S_ISVTX

def storePassword(password):
    h_pass,salt = hashPassword(password,0.5,64)


def hashPassword(password,maxtime = 0.5,datalength=64):
    """Hash password using scrypt"""
    salt = os.urandom(datalength) # add dynamic salt
    hashed_password = scrypt.hash(password,salt) # hash password
    return (hashed_password,salt) 

def verifyPassword():
    pass
