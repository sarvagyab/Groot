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
















