from PySide2 import QtWidgets,QtCore
from Application.mainWindow import Window
import sys

def main():
    try:
        from PyQt5.QtWinExtras import QtWin
        myappid = 'mycompany.myproduct.subproduct.version'
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
    except ImportError:
        pass
    
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()