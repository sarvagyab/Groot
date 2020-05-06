# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changePasswordDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_changePasswordDialog(object):
    def setupUi(self, changePasswordDialog):
        if not changePasswordDialog.objectName():
            changePasswordDialog.setObjectName(u"changePasswordDialog")
        changePasswordDialog.resize(565, 286)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(changePasswordDialog.sizePolicy().hasHeightForWidth())
        changePasswordDialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(11)
        changePasswordDialog.setFont(font)
        changePasswordDialog.setFocusPolicy(Qt.NoFocus)
        self.gridLayout = QGridLayout(changePasswordDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(changePasswordDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.mainFrame = QFrame(changePasswordDialog)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lowerFrame = QFrame(self.mainFrame)
        self.lowerFrame.setObjectName(u"lowerFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lowerFrame.sizePolicy().hasHeightForWidth())
        self.lowerFrame.setSizePolicy(sizePolicy1)
        self.lowerFrame.setFrameShape(QFrame.StyledPanel)
        self.lowerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.lowerFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.oldPassword = QLabel(self.lowerFrame)
        self.oldPassword.setObjectName(u"oldPassword")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.oldPassword.sizePolicy().hasHeightForWidth())
        self.oldPassword.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.oldPassword)

        self.oldPasswordLine = QLineEdit(self.lowerFrame)
        self.oldPasswordLine.setObjectName(u"oldPasswordLine")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(9)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.oldPasswordLine.sizePolicy().hasHeightForWidth())
        self.oldPasswordLine.setSizePolicy(sizePolicy3)
        self.oldPasswordLine.setTabletTracking(False)
        self.oldPasswordLine.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.oldPasswordLine.setEchoMode(QLineEdit.Password)
        self.oldPasswordLine.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.oldPasswordLine)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.password = QLabel(self.lowerFrame)
        self.password.setObjectName(u"password")
        self.password.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.password)

        self.passwordLineEdit = QLineEdit(self.lowerFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.passwordLineEdit.sizePolicy().hasHeightForWidth())
        self.passwordLineEdit.setSizePolicy(sizePolicy3)
        self.passwordLineEdit.setTabletTracking(False)
        self.passwordLineEdit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.passwordLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Repassword = QLabel(self.lowerFrame)
        self.Repassword.setObjectName(u"Repassword")
        self.Repassword.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.Repassword.sizePolicy().hasHeightForWidth())
        self.Repassword.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.Repassword)

        self.RepasswordLineEdit = QLineEdit(self.lowerFrame)
        self.RepasswordLineEdit.setObjectName(u"RepasswordLineEdit")
        self.RepasswordLineEdit.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.RepasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.RepasswordLineEdit.setSizePolicy(sizePolicy3)
        self.RepasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.RepasswordLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.lowerFrame)

        self.errorFrame = QFrame(self.mainFrame)
        self.errorFrame.setObjectName(u"errorFrame")
        sizePolicy1.setHeightForWidth(self.errorFrame.sizePolicy().hasHeightForWidth())
        self.errorFrame.setSizePolicy(sizePolicy1)
        self.errorFrame.setFrameShape(QFrame.StyledPanel)
        self.errorFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.errorFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Errortext = QLabel(self.errorFrame)
        self.Errortext.setObjectName(u"Errortext")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Errortext.sizePolicy().hasHeightForWidth())
        self.Errortext.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(8)
        self.Errortext.setFont(font1)

        self.verticalLayout_4.addWidget(self.Errortext)


        self.verticalLayout.addWidget(self.errorFrame)


        self.gridLayout.addWidget(self.mainFrame, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        QWidget.setTabOrder(self.passwordLineEdit, self.RepasswordLineEdit)

        self.retranslateUi(changePasswordDialog)

        QMetaObject.connectSlotsByName(changePasswordDialog)
    # setupUi

    def retranslateUi(self, changePasswordDialog):
        changePasswordDialog.setWindowTitle(QCoreApplication.translate("changePasswordDialog", u"Please enter your password", None))
        self.oldPassword.setText(QCoreApplication.translate("changePasswordDialog", u"<html><head/><body><p><span style=\" font-size:9pt;\">Old password</span></p></body></html>", None))
        self.oldPasswordLine.setText("")
        self.password.setText(QCoreApplication.translate("changePasswordDialog", u"<html><head/><body><p><span style=\" font-size:9pt;\">New password</span></p></body></html>", None))
        self.passwordLineEdit.setText("")
        self.Repassword.setText(QCoreApplication.translate("changePasswordDialog", u"<html><head/><body><p><span style=\" font-size:9pt;\">Re-enter </span></p><p><span style=\" font-size:9pt;\">new Password</span></p></body></html>", None))
        self.Errortext.setText(QCoreApplication.translate("changePasswordDialog", u"<html><head/><body><p><span style=\" color:#ff0000;\">Password must contain atleast 8 character with atleast 1 digit and 1 capital letter.</span></p></body></html>", None))
    # retranslateUi

