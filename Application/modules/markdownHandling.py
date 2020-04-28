from PySide2 import QtGui, QtWidgets
import markdown

def viewInMarkdown(md,extensions,markdownView):
    html = mdToHtml(md,extensions)
    markdownView.setHtml(html)
    imageResize(markdownView)


def mdToHtml(md, extensions):
    html = markdown.markdown(md, extensions = extensions)
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
    pass


def numList(te):
    te.moveCursor()
    te.moveCursor(QtGui.QTextCursor.EndOfLine)
    te.insertPlainText("\n1. Numbered List")


def hyperlink(te):
    # input name
    text, ok = QtWidgets.QInputDialog().getText(None,"Groot","Enter link - ")
    if ok is True:
            linkpath = str(text)
    else:
        return
    te.insertPlainText("[](" + linkpath + ")")
    for _ in range(len(linkpath) + 3):
        te.moveCursor(QtGui.QTextCursor.Left)
    te.setFocus()


def inlineCode(te):
    te.insertPlainText("``")
    te.moveCursor(QtGui.QTextCursor.Left)
    te.setFocus()

def datetimenow(te):
    import datetime
    te.insertPlainText(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"))
    te.setFocus()