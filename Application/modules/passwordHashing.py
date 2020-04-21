import scrypt
import os
from stat import S_IREAD,SF_IMMUTABLE,S_IWUSR,SF_NOUNLINK,UF_NODUMP,S_ISVTX

def storePassword(password):
    h_pass,salt = hashPassword(password,0.5,64)
    file_path = os.path.join('../user','config.txt') # define path 
    if( not os.path.exists('../user')): # create directory is not exists
        os.makedirs('../user')
    if(not os.path.isfile(file_path)): # eheck if file exist  
        with open(file_path,"wb") as file: 
            os.chmod(file_path,S_IWUSR)
            file.write(h_pass)
            os.chmod(file_path,S_ISVTX)
            file.close()


def hashPassword(password,maxtime = 0.5,datalength=64):
    """Hash password using scrypt"""
    salt = os.urandom(datalength) # add dynamic salt
    hashed_password = scrypt.encrypt(salt,password,maxtime = maxtime) # encrypt password
    return (hashed_password,salt) 

def verifyPassword():
    pass
