from PySide2.QtGui import QTextDocument,QTextCursor
from PySide2.QtCore import QRegExp,Qt


def searchText(ui,cursor = QTextCursor.Start,reversed = False):
    ui.errorLabel.setText("")
    ui.plainTextEdit.moveCursor(cursor) # set the cursor at the beginning of the text
    ui.mdViewer.moveCursor(cursor)
    search_text = ui.searchBar.text()
    matchWholeWord = ui.wholeWord.isChecked()
    matchregex = ui.regexButton.isChecked()
    matchCase = ui.matchCase.isChecked()
    sb_m = ui.mdViewer.verticalScrollBar()
    prev_sliderPos = sb_m.value()
    found = False
    if(matchregex == True): 
        if(matchCase == True): 
            search_regex = QRegExp(search_text,Qt.CaseSensitive)
            if(matchWholeWord == True):
                mode = QTextDocument.FindWholeWords
                if(reversed == True):
                    mode = mode | QTextDocument.FindBackward
                found = ui.plainTextEdit.find(search_regex,mode)
                ui.mdViewer.find(search_regex,mode)
            else:
                if(reversed == True):
                    mode = QTextDocument.FindBackward
                    found = ui.plainTextEdit.find(search_regex,mode)
                    ui.mdViewer.find(search_regex,mode)
                else:    
                    found = ui.plainTextEdit.find(search_regex)
                    ui.mdViewer.find(search_regex)
        else:
            search_regex = QRegExp(search_text,Qt.CaseInsensitive)
            if(matchWholeWord == True):
                mode = QTextDocument.FindWholeWords
                if(reversed == True):
                    mode = mode | QTextDocument.FindBackward
                found = ui.plainTextEdit.find(search_regex,mode)
                ui.mdViewer.find(search_regex,mode)
            else:
                if(reversed == True):
                    mode = QTextDocument.FindBackward
                    found = ui.plainTextEdit.find(search_regex,mode)
                    ui.mdViewer.find(search_regex,mode)
                else:    
                    found = ui.plainTextEdit.find(search_regex)
                    ui.mdViewer.find(search_regex)
    else:
        if(matchCase == True):
            mode = QTextDocument.FindCaseSensitively
            if(reversed == True ):
                mode = mode | QTextDocument.FindBackward
            if(matchWholeWord == True):
                mode = mode |QTextDocument.FindWholeWords
                found = ui.plainTextEdit.find(search_text,mode)
                ui.mdViewer.find(search_text,mode)
        else:
            if(matchWholeWord == True):
                mode = QTextDocument.FindWholeWords
                if(reversed == True):
                    mode = mode | QTextDocument.FindBackward
                found = ui.plainTextEdit.find(search_text,mode)
                ui.mdViewer.find(search_text,mode)
            else:
                if(reversed == True):
                    found = ui.plainTextEdit.find(search_text,QTextDocument.FindBackward)
                    ui.mdViewer.find(search_text,QTextDocument.FindBackward)
                else:
                    found = ui.plainTextEdit.find(search_text)
                    ui.mdViewer.find(search_text)
    curr_sliderPos = sb_m.value()
    if(prev_sliderPos != curr_sliderPos):
        scrollToCenter(sb_m)
    if(found == False):
        MSG = "<html><head/><body><p><span style=\" color:#ff0000;\">No results</span></p></body></html>"
        ui.errorLabel.setText(MSG)

def finishedSearch(textLabel):
    textLabel.setText("")

def scrollToCenter(sb_m):
    sb_m.setValue(sb_m.value()+sb_m.pageStep()/2)