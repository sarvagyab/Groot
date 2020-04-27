from modules.noteHandling import writeText,readText
from modules.treeHandling import updateItem
import hashlib
import base64
from Cryptodome import Random
from Cryptodome.Cipher import AES



class AEScipher():
    def __init__(self,key,currentNote,encrypt = True):
        self.bs = AES.block_size
        self.currentNote  = currentNote
        self.__key__ = hashlib.sha256(key.encode()).digest()
        if(encrypt == True):
            self.raw = currentNote.getText()
        else:
            self.enc = currentNote.getText()

    def Encrypt(self):
        pad = lambda s: s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
        self.raw = base64.b64encode(pad(self.raw).encode('utf8'))
        iv = Random.get_random_bytes(self.bs)
        cipher = AES.new(key= self.__key__, mode= AES.MODE_CFB,iv= iv)
        enc_text = base64.b64encode(iv + cipher.encrypt(self.raw))
        self.currentNote._details['encrypted'] = "True"
        updateItem({self.currentNote.getRandomString():self.currentNote._details})
        print("file encrypted")
        return enc_text

    def Decrypt(self):
        passphrase = self.__key__
        unpad = lambda s: s[:-ord(s[-1:])]
        self.enc = base64.b64decode(self.enc)
        iv = self.enc[:self.bs]
        cipher = AES.new(self.__key__, AES.MODE_CFB, iv)
        decrpt_txt =  unpad(base64.b64decode(cipher.decrypt(self.enc[self.bs:])).decode('utf8'))
        self.currentNote._details['encrypted'] = "False"
        updateItem({self.currentNote.getRandomString():self.currentNote._details})
        print("file decrypted")
        return decrpt_txt
    
        