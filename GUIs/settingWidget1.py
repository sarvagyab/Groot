from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self):
        self.Form = QtWidgets.QWidget()
        self.Form.setObjectName("Form")
        self.Form.setEnabled(True)
        self.Form.resize(571, 456)
        self.p1 = QtWidgets.QPushButton(self.Form)
        self.p1.setGeometry(QtCore.QRect(190, 120, 93, 28))
        self.p1.setObjectName("p1")

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        return self.Form

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Form"))
        self.p1.setText(_translate("Form", "p2"))
