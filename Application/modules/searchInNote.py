from PySide2.QtGui import QTextDocument,QTextCursor

def searchText(ui):
    ui.plainTextEdit.moveCursor(QTextCursor.Start)
    searched_text = ui.searchBar.text()
    found  = ui.plainTextEdit.find(searched_text)
    if(found == True):
        print("Found {}".format(searched_text))
    else:
        print("Not Found {}".format(searched_text))