# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firstLoginDialog.ui'
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

import resource_rc

class Ui_firstLoginDialog(object):
    def setupUi(self, firstLoginDialog):
        if not firstLoginDialog.objectName():
            firstLoginDialog.setObjectName(u"firstLoginDialog")
        firstLoginDialog.resize(565, 288)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(firstLoginDialog.sizePolicy().hasHeightForWidth())
        firstLoginDialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(9)
        firstLoginDialog.setFont(font)
        firstLoginDialog.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/16x16/key.png", QSize(), QIcon.Normal, QIcon.Off)
        firstLoginDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(firstLoginDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(firstLoginDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.mainFrame = QFrame(firstLoginDialog)
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
        self.gridLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.instruction = QLabel(self.upperFrame)
        self.instruction.setObjectName(u"instruction")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.instruction.sizePolicy().hasHeightForWidth())
        self.instruction.setSizePolicy(sizePolicy2)
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
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.usernameLabel = QLabel(self.lowerFrame)
        self.usernameLabel.setObjectName(u"usernameLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.usernameLabel.sizePolicy().hasHeightForWidth())
        self.usernameLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.usernameLabel)

        self.username = QLineEdit(self.lowerFrame)
        self.username.setObjectName(u"username")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(9)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy5)
        self.username.setTabletTracking(False)
        self.username.setInputMethodHints(Qt.ImhNone)
        self.username.setEchoMode(QLineEdit.Normal)
        self.username.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.username)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.password = QLabel(self.lowerFrame)
        self.password.setObjectName(u"password")
        sizePolicy4.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.password)

        self.passwordLineEdit = QLineEdit(self.lowerFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        sizePolicy5.setHeightForWidth(self.passwordLineEdit.sizePolicy().hasHeightForWidth())
        self.passwordLineEdit.setSizePolicy(sizePolicy5)
        self.passwordLineEdit.setTabletTracking(False)
        self.passwordLineEdit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.passwordLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.repassword = QLabel(self.lowerFrame)
        self.repassword.setObjectName(u"repassword")
        sizePolicy4.setHeightForWidth(self.repassword.sizePolicy().hasHeightForWidth())
        self.repassword.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.repassword)

        self.repasswordLineEdit = QLineEdit(self.lowerFrame)
        self.repasswordLineEdit.setObjectName(u"repasswordLineEdit")
        sizePolicy5.setHeightForWidth(self.repasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.repasswordLineEdit.setSizePolicy(sizePolicy5)
        self.repasswordLineEdit.setTabletTracking(False)
        self.repasswordLineEdit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.repasswordLineEdit.setEchoMode(QLineEdit.Password)
        self.repasswordLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.repasswordLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


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
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Errortext.sizePolicy().hasHeightForWidth())
        self.Errortext.setSizePolicy(sizePolicy6)

        self.verticalLayout_4.addWidget(self.Errortext)


        self.verticalLayout.addWidget(self.errorFrame)


        self.gridLayout.addWidget(self.mainFrame, 0, 0, 1, 1)


        self.retranslateUi(firstLoginDialog)

        QMetaObject.connectSlotsByName(firstLoginDialog)
    # setupUi

    def retranslateUi(self, firstLoginDialog):
        firstLoginDialog.setWindowTitle(QCoreApplication.translate("firstLoginDialog", u"Please enter your password", None))
        self.instruction.setText(QCoreApplication.translate("firstLoginDialog", u"<html><head/><body><p>You must login to use Groot.</p></body></html>", None))
        self.usernameLabel.setText(QCoreApplication.translate("firstLoginDialog", u"<html><head/><body><p><span style=\" font-size:9pt;\">Username</span></p></body></html>", None))
        self.username.setText("")
        self.password.setText(QCoreApplication.translate("firstLoginDialog", u"<html><head/><body><p><span style=\" font-size:9pt;\">Password</span></p></body></html>", None))
        self.passwordLineEdit.setText("")
        self.repassword.setText(QCoreApplication.translate("firstLoginDialog", u"<html><head/><body><p><span style=\" font-size:9pt;\">Re-enter password</span></p></body></html>", None))
        self.repasswordLineEdit.setText("")
        self.Errortext.setText(QCoreApplication.translate("firstLoginDialog", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

