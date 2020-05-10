# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordDialog.ui'
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

import Application.resource_rc

class Ui_passwordDialog(object):
    def setupUi(self, passwordDialog):
        if not passwordDialog.objectName():
            passwordDialog.setObjectName(u"passwordDialog")
        passwordDialog.resize(586, 289)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(passwordDialog.sizePolicy().hasHeightForWidth())
        passwordDialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(9)
        passwordDialog.setFont(font)
        passwordDialog.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/16x16/key.png", QSize(), QIcon.Normal, QIcon.Off)
        passwordDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(passwordDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(passwordDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.mainFrame = QFrame(passwordDialog)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upperFrame = QFrame(self.mainFrame)
        self.upperFrame.setObjectName(u"upperFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.upperFrame.sizePolicy().hasHeightForWidth())
        self.upperFrame.setSizePolicy(sizePolicy1)
        self.upperFrame.setFrameShape(QFrame.StyledPanel)
        self.upperFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.upperFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.instruction = QLabel(self.upperFrame)
        self.instruction.setObjectName(u"instruction")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.instruction.sizePolicy().hasHeightForWidth())
        self.instruction.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(8)
        self.instruction.setFont(font1)
        self.instruction.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.instruction.setWordWrap(False)

        self.gridLayout_2.addWidget(self.instruction, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.upperFrame)

        self.lowerFrame = QFrame(self.mainFrame)
        self.lowerFrame.setObjectName(u"lowerFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lowerFrame.sizePolicy().hasHeightForWidth())
        self.lowerFrame.setSizePolicy(sizePolicy3)
        self.lowerFrame.setFrameShape(QFrame.StyledPanel)
        self.lowerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.lowerFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.password = QLabel(self.lowerFrame)
        self.password.setObjectName(u"password")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.password)

        self.passwordLineEdit = QLineEdit(self.lowerFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(9)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.passwordLineEdit.sizePolicy().hasHeightForWidth())
        self.passwordLineEdit.setSizePolicy(sizePolicy5)
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
        sizePolicy4.setHeightForWidth(self.Repassword.sizePolicy().hasHeightForWidth())
        self.Repassword.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.Repassword)

        self.RepasswordLineEdit = QLineEdit(self.lowerFrame)
        self.RepasswordLineEdit.setObjectName(u"RepasswordLineEdit")
        sizePolicy5.setHeightForWidth(self.RepasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.RepasswordLineEdit.setSizePolicy(sizePolicy5)
        self.RepasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.RepasswordLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.lowerFrame)

        self.errorFrame = QFrame(self.mainFrame)
        self.errorFrame.setObjectName(u"errorFrame")
        sizePolicy3.setHeightForWidth(self.errorFrame.sizePolicy().hasHeightForWidth())
        self.errorFrame.setSizePolicy(sizePolicy3)
        self.errorFrame.setFrameShape(QFrame.StyledPanel)
        self.errorFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.errorFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Errortext = QLabel(self.errorFrame)
        self.Errortext.setObjectName(u"Errortext")
        sizePolicy2.setHeightForWidth(self.Errortext.sizePolicy().hasHeightForWidth())
        self.Errortext.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.Errortext)


        self.verticalLayout.addWidget(self.errorFrame)


        self.gridLayout.addWidget(self.mainFrame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.passwordLineEdit, self.RepasswordLineEdit)

        self.retranslateUi(passwordDialog)

        QMetaObject.connectSlotsByName(passwordDialog)
    # setupUi

    def retranslateUi(self, passwordDialog):
        passwordDialog.setWindowTitle(QCoreApplication.translate("passwordDialog", u"Please enter your password", None))
        self.instruction.setText(QCoreApplication.translate("passwordDialog", u"<html><head/><body><p>Please enter <span style=\" font-weight:600;\">password </span>to enter encrypt the note.</p><p>Keep in mind that you have to <span style=\" font-weight:600;\">remember </span>your password to read the content of the note</p><p>and that you can <span style=\" font-weight:600;\">only</span> do that <span style=\" font-weight:600;\">in Groot</span>.</p></body></html>", None))
        self.password.setText(QCoreApplication.translate("passwordDialog", u"<html><head/><body><p><span style=\" font-size:9pt;\">Password</span></p></body></html>", None))
        self.passwordLineEdit.setText("")
        self.Repassword.setText(QCoreApplication.translate("passwordDialog", u"<html><head/><body><p><span style=\" font-size:9pt;\">Re-enter Password</span></p></body></html>", None))
        self.Errortext.setText(QCoreApplication.translate("passwordDialog", u"<html><head/><body><p><span style=\" color:#ff0000;\">Password must contain atleast 8 character with atleast 1 digit and 1 capital letter.</span></p></body></html>", None))
    # retranslateUi

