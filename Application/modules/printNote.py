from PySide2 import QtPrintSupport,QtWidgets,QtGui,QtCore

def Print(ui):
    printer = QtPrintSupport.QPrinter()
    dialog = QtPrintSupport.QPrintDialog(printer)
    if( dialog.exec() == 0 ):
        return False
    else:
        widget = ui.mdViewer.document()
        widget.print_(printer)
        return True

def printPreview(ui):
    printer = QtPrintSupport.QPrinter()
    dialog = QtPrintSupport.QPrintPreviewDialog(printer)
    dialog.paintRequested.connect(lambda:print(printer,ui))
    if( dialog.exec() == 0 ):
        return False
    else:
        return True

def print(printer,ui):
    widget = ui.mdViewer.document()
    widget.print_(printer)












