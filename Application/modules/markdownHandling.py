from PySide2 import QtGui, QtWidgets, QtCore, QtPrintSupport
import markdown, datetime, shutil
from modules.fileHandling import currentNote
from modules.treeHandling import itemVal, saveUpdatedJson
from modules.userLogin import readUserInfo
from modules.noteHandling import readText
from modules.encryptNote import AEScipher
import pymdownx
import json

def viewInMarkdown(md,extensions,markdownView):
    html = mdToHtml(md, extensions)
    markdownView.setHtml(html)
    imageResize(markdownView)


def mdToHtml(md, _extensions):
    html = markdown.markdown(md, extensions = ["sane_lists","tables","fenced_code"] + _extensions, extension_configs = {"pymdownx.tilde":{"subscript":False}})
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
    if filename == "":
        return
    randomString = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    if currentNote._open == False:
        QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Groot","Cannot attach images when no note is currently loaded",QtWidgets.QMessageBox.Ok).exec_()
        return
    destination = shutil.copyfile(filename,"./atch/" + randomString)
    # print(destination)
    te.insertPlainText("![fileName](" + destination + ")")
    item = currentNote._item
    deets = itemVal(item)
    temp = deets[1][deets[0]]["expanded"]
    if "atchfiles" in temp: pass
    else:
        temp["atchfiles"] = []
    # print("Attaching file")
    temp["atchfiles"]+=[destination]
    saveUpdatedJson(deets[2])

    for _ in range(len("fileName](" + destination + ")")):
        te.moveCursor(QtGui.QTextCursor.Left)
    for _ in range(len("filename")):
        te.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)
    te.setFocus()


def copyMarkdownLink():
    nm = currentNote._name
    rd = currentNote._details["randomString"]
    txt = "[" + nm + "](./" + rd + ")"
    QtGui.QClipboard().setText(txt)

def pluginHandler(text,check,extensions, configs):

    with open("./settings.json","r") as sets:
        settings = json.load(sets)
    
    plugSets = settings["Plugins"]

    if text == "hardbreak":
        ext = "nl2br"
        if check: 
            plugSets["hardExt"] = True
        else:
            plugSets["hardExt"] = False
            extensions.remove(ext)
    elif text == "footnotes":
        ext = "footnotes"
        if check:
            plugSets["footnotesExt"] = True
        else:
            plugSets["footnotesExt"] = False
            extensions.remove(ext)
    elif text == "defLists":
        ext = "def_list"
        if check:
            plugSets["defListsExt"] = True
        else:
            plugSets["defListsExt"] = False
            extensions.remove(ext)
    elif text == "mdExt":
        ext = "md_in_html"
        if check:
            plugSets["mdExt"] = True
        else:
            plugSets["mdExt"] = False
            extensions.remove(ext)
    elif text == "superscript":
        ext = "pymdownx.caret"
        if check:
            plugSets["supExt"] = True
            configs[ext] = {"smart_insert":False, "insert": False}
        else:
            plugSets["supExt"] = False
            extensions.remove(ext)
            del configs[ext]
    elif text == "autolink":
        ext = "pymdownx.magiclink"
        if check:
            plugSets["linkExt"] = True
        else:
            plugSets["linkExt"] = False
            extensions.remove(ext)
    elif text == "symbols":
        ext = "pymdownx.smartsymbols"
        if check:
            plugSets["symbolsExt"] = True
        else:
            plugSets["symbolsExt"] = False
            extensions.remove(ext)
    elif text == "strike":
        if check:
            plugSets["strikeExt"] = True
            if "pymdownx.tilde" in extensions:
                ext = ""
                configs["pymdownx.tilde"]["smart_delete"] = True
                configs["pymdownx.tilde"]["delete"] = True
            else:
                ext = "pymdownx.tilde"
                configs["pymdownx.tilde"] = {}
                configs["pymdownx.tilde"]["smart_delete"] = True
                configs["pymdownx.tilde"]["delete"] = True
                configs["pymdownx.tilde"]["subscript"] = False
        else:
            plugSets["strikeExt"] = False
            if configs["pymdownx.tilde"]["subscript"]:
                configs["pymdownx.tilde"]["smart_delete"] = False
                configs["pymdownx.tilde"]["delete"] = False
            else:
                extensions.remove("pymdownx.tilde")
                del configs["pymdownx.tilde"]
    
    elif text == "subscript":
        if check:
            plugSets["subExt"] = True
            if "pymdownx.tilde" in extensions:
                ext = ""
                configs["pymdownx.tilde"]["subscript"] = True
            else:
                ext = "pymdownx.tilde"
                configs["pymdownx.tilde"] = {}
                configs["pymdownx.tilde"]["smart_delete"] = False
                configs["pymdownx.tilde"]["delete"] = False
                configs["pymdownx.tilde"]["subscript"] = True
        else:
            plugSets["subExt"] = False
            if configs["pymdownx.tilde"]["delete"]:
                configs["pymdownx.tilde"]["subscript"] = False
            else:
                extensions.remove("pymdownx.tilde")
                del configs["pymdownx.tilde"]

    location = "./settings.json"
    with open(location,"w") as jsonfile:
        json.dump(settings,jsonfile)
    # print("Json Updated")
    if check and ext!="":
        extensions+=[ext]


def exportAsPdf(mdView):
    if ("encrypted" in currentNote._details) and currentNote._details["encrypted"] == "True":
        QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Groot", "Cannot Export Encrypted Files",QtWidgets.QMessageBox.Ok).exec_()
        return
    filename, _ = QtWidgets.QFileDialog().getSaveFileName(None,"Export Pdf","./")
    if filename != "":
        if QtCore.QFileInfo(filename).suffix() != "pdf":
            filename+=".pdf"
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        mdView.document().print_(printer)


def exportAsMarkdown(mdtext):
    if ("encrypted" in currentNote._details) and currentNote._details["encrypted"] == "True":
        QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Groot", "Cannot Export Encrypted Files",QtWidgets.QMessageBox.Ok).exec_()
        return
    filename, _ = QtWidgets.QFileDialog().getSaveFileName(None,"Export Markdown","./")
    if filename != "":
        if QtCore.QFileInfo(filename).suffix() != "md":
            filename+=".md"
        with open(filename,"w") as newfile:
            newfile.write(mdtext)


def exportAsHtml(mdtext, extensions):
    if ("encrypted" in currentNote._details) and currentNote._details["encrypted"] == "True":
        QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Groot", "Cannot Export Encrypted Files",QtWidgets.QMessageBox.Ok).exec_()
        return
    filename, _ = QtWidgets.QFileDialog().getSaveFileName(None,"Export Html","./")
    if filename != "":
        if QtCore.QFileInfo(filename).suffix() != "html":
            filename+=".html"
        with open(filename,"w") as newfile:
            newfile.write(mdToHtml(mdtext,extensions))


def importMD(item):
    # Input file
    filename, _ = QtWidgets.QFileDialog().getOpenFileName(None,"Attach File","./","Markdown(*.md)")
    if filename == "":
        return

    # Creating file in our app
    randomString = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    path = "./notes/" + randomString + ".txt"
    shutil.copyfile(filename,path)

    # Encrypt file
    userInfo = readUserInfo()
    txt = readText(path)
    aes = AEScipher(str(userInfo[1]),currentNote,txt = txt,encrypt = True)
    txt = aes.Encrypt()
    if(not isinstance(txt,bytes)):
        txt = bytes(txt)
    with open(path,'wb') as file:
        file.write(txt)
        file.seek(0)
    print("Encrypting after importing")

    # Add to JSON
    info = QtCore.QFileInfo(filename)
    newdict = {}
    newdict["name"] = info.fileName()[:-len("." + info.suffix())]
    newdict["expanded"] = {}
    newdict["expanded"]["path"] = path
    newdict["expanded"]["randomString"] = randomString
    deets = itemVal(item)
    if item.parent() is None:
        deets[2]["Uncategorized"][randomString] = newdict
    else:
        deets[1][deets[0]]["expanded"][randomString] = newdict

    saveUpdatedJson(deets[2])

    # Update treeWidget
    newItem = QtWidgets.QTreeWidgetItem()
    newItem.setText(0,newdict["name"])
    newItem.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
    item.addChild(newItem)
    item.setExpanded(True)
    item.treeWidget().setCurrentItem(newItem)