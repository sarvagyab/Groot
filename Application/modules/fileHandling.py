
class FILE():
    def __init__(self,item,details):
        self._item = item
        self._details = details
        self._file = open(self._details["path"],"r+")
    
    def openFile(self,item,details):
        self.closeFile() # In case a some previous file was open

        self._name = item.text(0)
        self._details = details
        self._file = open(self._details["path"],"r+")

    def closeFile(self):
        self._file.close()

    def getText(self):
        return self._file.read()

    def getFilename(self):
        return self._name
    
    def saveFile(self,text):
        self._file.seek(0)
        self._file.truncate()
        self._file.write(text)
        # self._file.flush()


currentNote = FILE("MarkdownGuide",{"path" : "../Application/notes/note4.txt"})