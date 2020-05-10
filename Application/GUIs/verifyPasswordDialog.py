# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'verifyPasswordDialog.ui'
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

class Ui_verifyPasswordDialog(object):
    def setupUi(self, verifyPasswordDialog):
        if not verifyPasswordDialog.objectName():
            verifyPasswordDialog.setObjectName(u"verifyPasswordDialog")
        verifyPasswordDialog.resize(599, 327)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(verifyPasswordDialog.sizePolicy().hasHeightForWidth())
        verifyPasswordDialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(11)
        verifyPasswordDialog.setFont(font)
        verifyPasswordDialog.setFocusPolicy(Qt.TabFocus)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/16x16/key.png", QSize(), QIcon.Normal, QIcon.Off)
        verifyPasswordDialog.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(verifyPasswordDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.mainFrame = QFrame(verifyPasswordDialog)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.mainFrame)
        self.title.setObjectName(u"title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.title)

        self.upperFrame = QFrame(self.mainFrame)
        self.upperFrame.setObjectName(u"upperFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.upperFrame.sizePolicy().hasHeightForWidth())
        self.upperFrame.setSizePolicy(sizePolicy2)
        self.upperFrame.setFrameShape(QFrame.StyledPanel)
        self.upperFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.upperFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.instruction = QLabel(self.upperFrame)
        self.instruction.setObjectName(u"instruction")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.instruction.sizePolicy().hasHeightForWidth())
        self.instruction.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(9)
        self.instruction.setFont(font1)
        self.instruction.setFrameShape(QFrame.NoFrame)
        self.instruction.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.instruction.setWordWrap(False)

        self.gridLayout_2.addWidget(self.instruction, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.upperFrame)

        self.lowerFrame = QFrame(self.mainFrame)
        self.lowerFrame.setObjectName(u"lowerFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lowerFrame.sizePolicy().hasHeightForWidth())
        self.lowerFrame.setSizePolicy(sizePolicy4)
        self.lowerFrame.setFrameShape(QFrame.StyledPanel)
        self.lowerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.lowerFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.password = QLabel(self.lowerFrame)
        self.password.setObjectName(u"password")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(3)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.password)

        self.passwordLineEdit = QLineEdit(self.lowerFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(9)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.passwordLineEdit.sizePolicy().hasHeightForWidth())
        self.passwordLineEdit.setSizePolicy(sizePolicy6)
        self.passwordLineEdit.setTabletTracking(False)
        self.passwordLineEdit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.passwordLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.lowerFrame)

        self.errorFrame = QFrame(self.mainFrame)
        self.errorFrame.setObjectName(u"errorFrame")
        sizePolicy4.setHeightForWidth(self.errorFrame.sizePolicy().hasHeightForWidth())
        self.errorFrame.setSizePolicy(sizePolicy4)
        self.errorFrame.setFrameShape(QFrame.StyledPanel)
        self.errorFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.errorFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Errortext = QLabel(self.errorFrame)
        self.Errortext.setObjectName(u"Errortext")
        sizePolicy1.setHeightForWidth(self.Errortext.sizePolicy().hasHeightForWidth())
        self.Errortext.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.Errortext)


        self.verticalLayout.addWidget(self.errorFrame)


        self.verticalLayout_3.addWidget(self.mainFrame)

        self.buttonBox = QDialogButtonBox(verifyPasswordDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(verifyPasswordDialog)

        QMetaObject.connectSlotsByName(verifyPasswordDialog)
    # setupUi

    def retranslateUi(self, verifyPasswordDialog):
        verifyPasswordDialog.setWindowTitle(QCoreApplication.translate("verifyPasswordDialog", u"Please enter your password", None))
        self.title.setText("")
        self.instruction.setText(QCoreApplication.translate("verifyPasswordDialog", u"<html><head/><body><p>Please enter <span style=\" font-weight:600;\">password </span>to enter decrypt the note.</p><p>Keep in mind that you have to <span style=\" font-weight:600;\">remember </span>your password to read the content of the note</p><p>and that you can <span style=\" font-weight:600;\">only</span> do that <span style=\" font-weight:600;\">in Groot</span>.</p></body></html>", None))
        self.password.setText(QCoreApplication.translate("verifyPasswordDialog", u"<html><head/><body><p><span style=\" font-size:9pt;\">Password</span></p></body></html>", None))
        self.passwordLineEdit.setText("")
        self.Errortext.setText(QCoreApplication.translate("verifyPasswordDialog", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

