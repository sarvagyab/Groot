from PySide2 import QtGui, QtWidgets
import markdown, datetime, shutil

def viewInMarkdown(md,extensions,markdownView):
    html = mdToHtml(md, extensions)
    markdownView.setHtml(html)
    imageResize(markdownView)


def mdToHtml(md, _extensions):
    html = markdown.markdown(md, extensions = ["sane_lists"] + _extensions)
    return html


def imageResize(markdownView):
    markdownView.moveCursor(QtGui.QTextCursor.Start)
    while True:
        currentBlock = markdownView.textCursor().block()
        it = currentBlock.begin()
        while it.atEnd() is not True:
            fragment = it.fragment()
            if(fragment.isValid()):
                if( fragment.charFormat().isImageFormat() ):
                    newImageFormat = fragment.charFormat().toImageFormat()
                    path = newImageFormat.name()
                    img = QtGui.QImage(path)
                    if(img.width() > (markdownView.width()-30)):
                        newImageFormat.setWidth(markdownView.width()-30)
                        if(newImageFormat.isValid()):
                            helper = markdownView.textCursor()
                            helper.setPosition(fragment.position())
                            helper.setPosition(fragment.position() + fragment.length(), QtGui.QTextCursor.KeepAnchor)
                            helper.setCharFormat(newImageFormat)
            it+=1
        no = markdownView.textCursor().blockNumber()
        markdownView.moveCursor(QtGui.QTextCursor.NextBlock)
        if(markdownView.textCursor().blockNumber() == no):
            return


def bold(te):
    textCursor = te.textCursor()
    if(textCursor.hasSelection()):
        length = textCursor.selectionEnd() - textCursor.selectionStart()
        text = textCursor.selectedText()
        textCursor.removeSelectedText()
        textCursor.insertText("**" + text + "**")
        for _ in range(length + 2):
            te.moveCursor(QtGui.QTextCursor.Left)
        for _ in range(length):
            te.moveCursor(QtGui.QTextCursor.Right,QtGui.QTextCursor.KeepAnchor)
    else:
        textCursor.insertText("**strong text**")
        for _ in range(len("strong text") + 2):
            te.moveCursor(QtGui.QTextCursor.Left)
        for _ in range(len("strong text")):
            te.moveCursor(QtGui.QTextCursor.Right,QtGui.QTextCursor.KeepAnchor)
    te.setFocus()


def italic(te):
    textCursor = te.textCursor()
    if(textCursor.hasSelection()):
        length = textCursor.selectionEnd() - textCursor.selectionStart()
        text = textCursor.selectedText()
        textCursor.removeSelectedText()
        textCursor.insertText("*" + text + "*")
        for _ in range(length + 1):
            te.moveCursor(QtGui.QTextCursor.Left)
        for _ in range(length):
            te.moveCursor(QtGui.QTextCursor.Right,QtGui.QTextCursor.KeepAnchor)
    else:
        textCursor.insertText("*italic text*")
        for _ in range(len("italic text") + 1):
            te.moveCursor(QtGui.QTextCursor.Left)
        for _ in range(len("italic text")):
            te.moveCursor(QtGui.QTextCursor.Right,QtGui.QTextCursor.KeepAnchor)
    te.setFocus()


def bulletList(te):
    te.moveCursor(QtGui.QTextCursor.StartOfLine)
    te.moveCursor(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.KeepAnchor)
    text = te.textCursor().selectedText()
    text = text.strip()
    if text == "":
        # check above line
        te.moveCursor(QtGui.QTextCursor.Up) 
        te.moveCursor(QtGui.QTextCursor.StartOfLine)
        te.moveCursor(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.KeepAnchor)
        text2 = te.textCursor().selectedText()
        te.moveCursor(QtGui.QTextCursor.Down)
        text2 = text2.strip()
        
        if len(text2) == 0 or (len(text2)!=1 and text2[0] == "-" and text2[1] == " "):
            te.moveCursor(QtGui.QTextCursor.StartOfLine)
            te.insertPlainText("- Bullet List")

        else:
            te.moveCursor(QtGui.QTextCursor.EndOfLine)
            te.insertPlainText("\n- Bullet List")
    
    else:
        te.moveCursor(QtGui.QTextCursor.EndOfLine)
        if len(text) == 1 or text[0] != "-" or text[1] != " ":
            te.insertPlainText("\n\n- Bullet List")
        else:
            te.insertPlainText("\n- Bullet List")
    
    for _ in range(len("Bullet List")):
        te.moveCursor(QtGui.QTextCursor.Left)
    for _ in range(len("Bullet List")):
        te.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)   
    te.setFocus()


def checkInt(check):
    try:
        int(check)
        return True
    except:
        return False

def index(text):
    for i in range(len(text)):
        if not checkInt(text[i]):
            return i

def checkIfList(text):
    text = text.strip()
    if(len(text)==0):
        return 0
    ind = index(text)
    if ind == 0:
        return -1
    else:
        if len(text)<(ind+2):
            return -1
        else:
            if text[ind] != "." or text[ind+1] != " ":
                return -1
            else:
                return int(text[:ind])

def numList(te):
    te.moveCursor(QtGui.QTextCursor.StartOfLine)
    te.moveCursor(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.KeepAnchor)
    text = te.textCursor().selectedText()
    text = text.strip()
    if text == "":
        # check above line
        te.moveCursor(QtGui.QTextCursor.Up) 
        te.moveCursor(QtGui.QTextCursor.StartOfLine)
        te.moveCursor(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.KeepAnchor)
        text2 = te.textCursor().selectedText()
        ans = checkIfList(text2)
        te.moveCursor(QtGui.QTextCursor.Down)
        # if above line is  not a list
        # leave a line and then start the list
        if ans == -1:
            te.moveCursor(QtGui.QTextCursor.EndOfLine)
            te.insertPlainText("\n1. Numbered List")
        # else continue with this line
        else:
            te.moveCursor(QtGui.QTextCursor.StartOfLine)
            te.insertPlainText(str(ans+1) + ". Numbered List")
    else:
        ans = checkIfList(text)
        if (ans == -1):
            te.moveCursor(QtGui.QTextCursor.EndOfLine)
            te.insertPlainText("\n\n1. Numbered List")
        else:
            te.moveCursor(QtGui.QTextCursor.EndOfLine)
            te.insertPlainText("\n" + str(ans+1) + ". Numbered List")
    
    for _ in range(len("Numbered List")):
        te.moveCursor(QtGui.QTextCursor.Left)
    for _ in range(len("Numbered List")):
        te.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)   
    te.setFocus()


def hyperlink(te):
    # input name
    text, ok = QtWidgets.QInputDialog().getText(None,"Groot","Enter link - ")
    if ok is True:
            linkpath = str(text)
    else:
        return
    te.insertPlainText("[Visit " + linkpath + "](" + linkpath + ")")
    for _ in range(2*len(linkpath) + 9):
        te.moveCursor(QtGui.QTextCursor.Left)
    for _ in range(6 + len(linkpath)):
        te.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)
    te.setFocus()


def inlineCode(te):
    te.insertPlainText("`inline code`")
    for _ in range(len("inline code") + 1):
        te.moveCursor(QtGui.QTextCursor.Left)
    for _ in range(len("inline code")):
        te.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)
    te.setFocus()

def datetimenow(te):
    te.insertPlainText(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"))
    te.setFocus()


def attachFile(te):
    filename, _ = QtWidgets.QFileDialog().getOpenFileName(None,"Attach File","./")
    # print(filename)
    randomString = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    destination = shutil.copyfile(filename,"./atch/" + randomString)
    # print(destination)
    te.insertPlainText("![fileName](" + destination + ")")
    for _ in range(len("fileName](" + destination + ")")):
        te.moveCursor(QtGui.QTextCursor.Left)
    for _ in range(len("filename")):
        te.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)
    te.setFocus()