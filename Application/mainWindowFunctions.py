
from modules.setPassword import password
from modules.fileHandling import currentNote
from modules.markdownHandling import viewInMarkdown
from modules.treeHandling import loadfileStructure, noteLoader,itemVal


def _delayChecker(self):
    if(self.timer.isActive()):
        self.timer.stop()
    self.timer.start(self.DELAY)

def _noteLoader(self):
    changeNote = lambda : noteLoader(self.ui.treeWidget.selectedItems()[0],self.ui.fileName,self.ui.plainTextEdit)
    self.ui.treeWidget.itemSelectionChanged.connect(changeNote)

def _markdownViewer(self):
    mdView = lambda: viewInMarkdown(self.ui.plainTextEdit.toPlainText(),self.mdExtensions,self.ui.mdViewer)
    sFile = lambda: currentNote.saveFile(self.ui.plainTextEdit.toPlainText())
    self.timer.timeout.connect(sFile)
    self.timer.timeout.connect(mdView)
    self.ui.plainTextEdit.textChanged.connect(self._delayChecker)


def encryptNote(self):
    self.passwdE = password(self)
    self.ui.encryptionButton.clicked.connect(lambda: self.passwdE.openPasswordDialog())

    
def decryptNote(self):
    self.passwdD = password(self)
    self.ui.decryptionButton.clicked.connect(lambda: self.passwdD.openVerifyPasswordDialog())

    
def reloadUI(self):
    loadfileStructure(self.ui.treeWidget)
    self._noteLoader()

    
def closeEvent(self,event):
    currentNote.closeFile()
    event.accept()


