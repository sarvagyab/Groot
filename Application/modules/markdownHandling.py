import markdown, datetime, shutil
import copy
import json,os
import pymdownx
from markdown.extensions.sane_lists import SaneListExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.footnotes import FootnoteExtension
from markdown.extensions.def_list import DefListExtension
from markdown.extensions.md_in_html import MarkdownInHtmlExtension
from pymdownx.magiclink import MagiclinkExtension
from pymdownx.caret import InsertSupExtension
from pymdownx.smartsymbols import SmartSymbolsExtension
from pymdownx.tilde import DeleteSubExtension


from PySide2 import QtGui, QtWidgets, QtCore, QtPrintSupport

from Application.modules.fileHandling import currentNote
from Application.modules.treeHandling import itemVal, saveUpdatedJson
from Application.modules.userLogin import readUserInfo
from Application.modules.noteHandling import readText
from Application.modules.encryptNote import AEScipher

def scrolling(oneBar,twoBar,searchBar):
    # note it's not perfect because qt has a problem such that when typing at the last line
    # the scroll automatically remains at the bottom which is good
    # but it's value does not get updated according the new size of scrollbar 
    # which breaks the synchronous scrolling until scrollbar is moved manually
    # which updates the values
    if(not searchBar.hasFocus()):
        Max = oneBar.maximum() 
        x = 0
        if(Max != 0):
            x = (oneBar.value()*twoBar.maximum())/Max
        if twoBar.signalsBlocked(): return
        oneBar.blockSignals(True)
        twoBar.setValue(x)
        oneBar.blockSignals(False)


def cntLinesAbove(ptedit):
    st = QtCore.QPoint(0,0)
    startpos = ptedit.cursorForPosition(st)  
    # startpos.select(QtGui.QTextCursor.LineUnderCursor)  
    # print(startpos.selectedText())
    cnt = 0
    # print("Starting pos = " + str(startpos.position()))
    # print("The lines I am going up by")
    while True: 
        val = startpos.movePosition(QtGui.QTextCursor.Up)
        # print("checking position = " + str(startpos.position()))
        # print(val)
        if(val == False): break
        # startpos.select(QtGui.QTextCursor.LineUnderCursor)
        # print(startpos.selectedText())
        # startpos.clearSelection()
        # startpos.movePosition(QtGui.QTextCursor.StartOfLine)
        cnt+=1
        # print("Start  position - " + str(startpos.position()))
        # print("cnt = " + str(cnt))
    return cnt

def printfirstvisibleline(markdownview):
    st = QtCore.QPoint(0,0)
    startpos = markdownview.cursorForPosition(st)  
    startpos.select(QtGui.QTextCursor.LineUnderCursor)  
    return startpos.selectedText()

def viewInMarkdown(ptedit,extensions,configs,markdownView,searchBar):

    md = ptedit.toPlainText()
    currentPosition = ptedit.textCursor().position()
    # print("CUrrent position = " + str(currentPosition))
    ed = QtCore.QPoint(ptedit.viewport().width()-1,ptedit.viewport().height()-1)
    cnt = cntLinesAbove(ptedit)
    # print("to match cnt = " + str(cnt))
    cntformarkdown = cntLinesAbove(markdownView)
    
    # print("after counting - ")
    # printfirstvisibleline(markdownView)

    html = mdToHtml(md, extensions,configs)
    markdownView.setHtml(html)
    imageResize(markdownView)

    # print("after new set")
    # print("cout<<'hello world'" + printfirstvisibleline(markdownView))
    markdownView.moveCursor(QtGui.QTextCursor.Start)
    # cur = markdownView.textCursor()
    # cur.setPosition(0)
    # markdownView.setTextCursor(cur)

    print("after going to top - ")
    printfirstvisibleline(markdownView)

    # print("markdown seperation begins - \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # print(markdownView.textCursor().position())
    prev = -1
    nooftimesnochange = 0
    while True:
        # print(cntLinesAbove(markdownView))
        cntmd = cntLinesAbove(markdownView)
        # print("cnt for markdown = " + str(cntformarkdown))
        # print("markdown lines above - " + str(cntmd))
        # print("checking for infinity loop")
        if cntmd == prev: nooftimesnochange+=1
        else: 
            prev = cntmd
            nooftimesnochange = 0

        # if(cntformarkdown<=cntmd): break
        if(cntformarkdown<=cntmd or nooftimesnochange>50): break
        markdownView.moveCursor(QtGui.QTextCursor.Down)

    # print("markdown seperation ends - \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    ptedit.moveCursor(QtGui.QTextCursor.Start)
    if(cnt != 0):
        # print("The lines above are more than 0")
        while True: 
            ptedit.moveCursor(QtGui.QTextCursor.Down)
            newcnt = cntLinesAbove(ptedit)
            # print("cnting = " + str(newcnt))
            if(newcnt >= cnt): break
    
    # print("Final above lines = " + str(cntLinesAbove(ptedit)))
    # print("Current position as of before shifting = " + str(ptedit.textCursor().position()))
    while(ptedit.textCursor().position() != currentPosition):
        if(currentPosition>ptedit.textCursor().position()): ptedit.moveCursor(QtGui.QTextCursor.Right)
        else: ptedit.moveCursor(QtGui.QTextCursor.Left)  
    
    # print("after setting = " + str(markdownView.textCursor().position()))



def imageResize(markdownView):
    doc = markdownView.document()
    count = doc.blockCount()
    for i in range(1,count+1):
        currentBlock = doc.findBlockByNumber(i)
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



def mdToHtml(md, _extensions,configs):
    html = markdown.markdown(md, extensions = [SaneListExtension(),TableExtension(),FencedCodeExtension(),DeleteSubExtension(**configs)] + strToClassEXt(_extensions))
    return html

def strToClassEXt(extensions):
    e_idx = []
    if("nl2br" in extensions):
        e_idx.append(Nl2BrExtension())
    if("footnotes" in extensions):
        e_idx.append(FootnoteExtension())
    if("def_list" in extensions):
        e_idx.append(DefListExtension())
    if("md_in_html" in extensions):
        e_idx.append(MarkdownInHtmlExtension())
    if("pymdownx.caret" in extensions):
        e_idx.append(InsertSupExtension(smart_insert = False, insert = False))
    if("pymdownx.magiclink" in extensions):
        e_idx.append(MagiclinkExtension())
    if("pymdownx.smartsymbols" in extensions):
        e_idx.append(SmartSymbolsExtension())
    return e_idx


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


def hyperlink(window):
    # input name
    te = window.ui.plainTextEdit
    icon = QtGui.QIcon()
    dialog = QtWidgets.QInputDialog()
    icon.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/link.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
    text, ok = dialog.getText(window,"Groot","Enter link - ",flags= QtCore.Qt.Dialog)
    dialog.setWindowIcon(icon)
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


def attachFile(window):
    te = window.ui.plainTextEdit
    if currentNote._open == False: 
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Groot","Cannot attach images when no note is currently loaded",QtWidgets.QMessageBox.Ok)
        msg.setParent(window,QtCore.Qt.Window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/attention.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.exec_()
        return
    filename, _ = QtWidgets.QFileDialog().getOpenFileName(None,"Attach File","./")
    # print(filename)
    if filename == "":
        return
    randomString = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    if(not os.path.exists("./Application/atch")):
        os.makedirs("./Application/atch")
    destination = shutil.copyfile(filename,"./Application/atch/" + randomString)
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

    with open("./Application/settings.json","r") as sets:
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
        else:
            plugSets["supExt"] = False
            extensions.remove(ext)
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
            ext = ""
            plugSets["strikeExt"] = True
            configs["smart_delete"] = True
            configs["delete"] = True
        else:
            plugSets["strikeExt"] = False
            configs["smart_delete"] = False
            configs["delete"] = False
    elif text == "subscript":
        if check:
            ext = ""
            plugSets["subExt"] = True
            configs["subscript"] = True
        else:
            plugSets["subExt"] = False
            configs["subscript"] = False

    location = "./Application/settings.json"
    with open(location,"w") as jsonfile:
        json.dump(settings,jsonfile)
    # print("Json Updated")
    if check and ext!="":
        extensions+=[ext]


def exportAsPdf(window):
    mdView = window.ui.mdViewer
    if ("encrypted" in currentNote._details) and currentNote._details["encrypted"] == "True":
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Groot", "Cannot Export Encrypted Files",QtWidgets.QMessageBox.Ok)
        msg.setParent(window,QtCore.Qt.Window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/attention.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.exec_()
        return
    filename, _ = QtWidgets.QFileDialog().getSaveFileName(None,"Export Pdf","./")
    if filename != "":
        if QtCore.QFileInfo(filename).suffix() != "pdf":
            filename+=".pdf"
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        mdView.document().print_(printer)


def exportAsMarkdown(window):
    mdtext = window.ui.plainTextEdit.toPlainText()
    if ("encrypted" in currentNote._details) and currentNote._details["encrypted"] == "True":
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Groot", "Cannot Export Encrypted Files",QtWidgets.QMessageBox.Ok)
        msg.setParent(window,QtCore.Qt.Window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/attention.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.exec_()
        return
    filename, _ = QtWidgets.QFileDialog().getSaveFileName(None,"Export Markdown","./")
    if filename != "":
        if QtCore.QFileInfo(filename).suffix() != "md":
            filename+=".md"
        with open(filename,"w", encoding="utf-8") as newfile:
            newfile.write(mdtext)


def exportAsHtml(window, extensions,configs):
    mdtext = window.ui.plainTextEdit.toPlainText()
    if ("encrypted" in currentNote._details) and currentNote._details["encrypted"] == "True":
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Groot", "Cannot Export Encrypted Files",QtWidgets.QMessageBox.Ok)
        msg.setParent(window,QtCore.Qt.Window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/attention.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.exec_()
        return
    filename, _ = QtWidgets.QFileDialog().getSaveFileName(None,"Export Html","./")
    if filename != "":
        if QtCore.QFileInfo(filename).suffix() != "html":
            filename+=".html"
        with open(filename,"w", encoding="utf-8") as newfile:
            newfile.write(mdToHtml(mdtext,extensions,configs))


def importMD(item):
    # Input file
    filename, _ = QtWidgets.QFileDialog().getOpenFileName(None,"Attach File","./","Markdown(*.md)")
    if filename == "":
        return

    # Creating file in our app
    randomString = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    directory = "./Application/notes/"
    path = directory + randomString
    if(not os.path.exists(directory)):
        os.makedirs(directory)
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
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/document_light.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)        
    newItem.setIcon(0,icon)
    item.addChild(newItem)
    item.setExpanded(True)
    item.treeWidget().setCurrentItem(newItem)