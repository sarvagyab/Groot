from PySide2 import QtGui
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