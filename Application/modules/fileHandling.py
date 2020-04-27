from PySide2 import QtCore
class FILE():
    _file = None
    _details = {"path":""}
    _open = False
    def __init__(self):
        pass
    
    def openFile(self,item,details):
        if(self._open == True):
            self.closeFile() # In case a some previous file was open

        self._item = item
        self._name = item.text(0)
        self._details = details
        self._file = open(self._details["path"],"r+")
        self._open = True

    def closeFile(self):
        self._file.close()
        self._open = False

    def getText(self):
        txt = self._file.read()
        self._file.seek(0)
        return txt

    def getFilename(self):
        return self._name
    
    def getRandomString(self):
        return self._details['randomString']
    
    def saveFile(self,text):
        if not self._open:
            return
        if('encrypted' in self._details and self._details['encrypted'] == 'True'): # don't save is file is encrypted
            return
        self._file.seek(0)
        self._file.truncate()
        self._file.write(text)
        self._file.seek(0)
        # self._file.flush()


currentNote = FILE()