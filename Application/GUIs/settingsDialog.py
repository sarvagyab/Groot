# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsDialog2.ui'
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

class Ui_settingDialog(object):
    def setupUi(self, settingDialog):
        if not settingDialog.objectName():
            settingDialog.setObjectName(u"settingDialog")
        settingDialog.resize(870, 461)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/16x16/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        settingDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(settingDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 2, 5, 5)
        self.widget = QWidget(settingDialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 30))
        self.widget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(757, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeMe = QPushButton(self.widget)
        self.closeMe.setObjectName(u"closeMe")
        self.closeMe.setMinimumSize(QSize(0, 20))

        self.horizontalLayout.addWidget(self.closeMe)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.settings = QTabWidget(settingDialog)
        self.settings.setObjectName(u"settings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(14)
        self.settings.setFont(font)
        self.tabAppearance = QWidget()
        self.tabAppearance.setObjectName(u"tabAppearance")
        self.themeChoice = QComboBox(self.tabAppearance)
        self.themeChoice.addItem("")
        self.themeChoice.addItem("")
        self.themeChoice.setObjectName(u"themeChoice")
        self.themeChoice.setGeometry(QRect(10, 70, 161, 31))
        font1 = QFont()
        font1.setPointSize(13)
        self.themeChoice.setFont(font1)
        self.themeLabel = QLabel(self.tabAppearance)
        self.themeLabel.setObjectName(u"themeLabel")
        self.themeLabel.setGeometry(QRect(10, 30, 121, 31))
        self.themeLabel.setFont(font1)
        self.fontSizeLabel = QLabel(self.tabAppearance)
        self.fontSizeLabel.setObjectName(u"fontSizeLabel")
        self.fontSizeLabel.setGeometry(QRect(10, 160, 111, 31))
        self.fontSizeLabel.setFont(font1)
        self.fontChoice = QFontComboBox(self.tabAppearance)
        self.fontChoice.setObjectName(u"fontChoice")
        self.fontChoice.setGeometry(QRect(140, 230, 226, 31))
        self.fontChoice.setFont(font1)
        self.fontFamilyLabel = QLabel(self.tabAppearance)
        self.fontFamilyLabel.setObjectName(u"fontFamilyLabel")
        self.fontFamilyLabel.setGeometry(QRect(10, 230, 111, 31))
        self.fontFamilyLabel.setFont(font1)
        self.fontSizeValue = QSpinBox(self.tabAppearance)
        self.fontSizeValue.setObjectName(u"fontSizeValue")
        self.fontSizeValue.setGeometry(QRect(140, 160, 191, 31))
        self.fontSizeValue.setMinimum(1)
        self.fontSizeValue.setMaximum(255)
        self.settings.addTab(self.tabAppearance, "")
        self.tabPlugins = QWidget()
        self.tabPlugins.setObjectName(u"tabPlugins")
        self.verticalLayout = QVBoxLayout(self.tabPlugins)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hardExt = QCheckBox(self.tabPlugins)
        self.hardExt.setObjectName(u"hardExt")
        font2 = QFont()
        font2.setPointSize(10)
        self.hardExt.setFont(font2)

        self.verticalLayout.addWidget(self.hardExt)

        self.footnotesExt = QCheckBox(self.tabPlugins)
        self.footnotesExt.setObjectName(u"footnotesExt")
        self.footnotesExt.setFont(font2)

        self.verticalLayout.addWidget(self.footnotesExt)

        self.defListsExt = QCheckBox(self.tabPlugins)
        self.defListsExt.setObjectName(u"defListsExt")
        self.defListsExt.setFont(font2)

        self.verticalLayout.addWidget(self.defListsExt)

        self.mdExt = QCheckBox(self.tabPlugins)
        self.mdExt.setObjectName(u"mdExt")
        self.mdExt.setFont(font2)

        self.verticalLayout.addWidget(self.mdExt)

        self.supExt = QCheckBox(self.tabPlugins)
        self.supExt.setObjectName(u"supExt")
        self.supExt.setFont(font2)

        self.verticalLayout.addWidget(self.supExt)

        self.subExt = QCheckBox(self.tabPlugins)
        self.subExt.setObjectName(u"subExt")
        self.subExt.setFont(font2)

        self.verticalLayout.addWidget(self.subExt)

        self.linkExt = QCheckBox(self.tabPlugins)
        self.linkExt.setObjectName(u"linkExt")
        self.linkExt.setFont(font2)

        self.verticalLayout.addWidget(self.linkExt)

        self.symbolsExt = QCheckBox(self.tabPlugins)
        self.symbolsExt.setObjectName(u"symbolsExt")
        self.symbolsExt.setFont(font2)

        self.verticalLayout.addWidget(self.symbolsExt)

        self.strikeExt = QCheckBox(self.tabPlugins)
        self.strikeExt.setObjectName(u"strikeExt")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setStrikeOut(False)
        self.strikeExt.setFont(font3)

        self.verticalLayout.addWidget(self.strikeExt)

        self.settings.addTab(self.tabPlugins, "")
        self.tabEncryption = QWidget()
        self.tabEncryption.setObjectName(u"tabEncryption")
        self.enterPwdLabel = QLabel(self.tabEncryption)
        self.enterPwdLabel.setObjectName(u"enterPwdLabel")
        self.enterPwdLabel.setGeometry(QRect(10, 20, 441, 41))
        self.enterPwdLabel.setFont(font1)
        self.encryptAllChoice = QCheckBox(self.tabEncryption)
        self.encryptAllChoice.setObjectName(u"encryptAllChoice")
        self.encryptAllChoice.setEnabled(False)
        self.encryptAllChoice.setGeometry(QRect(10, 140, 261, 31))
        self.encryptAllChoice.setFont(font1)
        self.encryptAllChoice.setChecked(True)
        self.frame_2 = QFrame(self.tabEncryption)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 60, 451, 57))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(57)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 10, 9)
        self.enterPwd = QLineEdit(self.frame_2)
        self.enterPwd.setObjectName(u"enterPwd")
        self.enterPwd.setFont(font1)
        self.enterPwd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.enterPwd)

        self.okPushButton_2 = QPushButton(self.frame_2)
        self.okPushButton_2.setObjectName(u"okPushButton_2")

        self.horizontalLayout_6.addWidget(self.okPushButton_2)

        self.Errortext = QLabel(self.tabEncryption)
        self.Errortext.setObjectName(u"Errortext")
        self.Errortext.setGeometry(QRect(490, 65, 281, 31))
        self.settings.addTab(self.tabEncryption, "")
        self.userTab = QWidget()
        self.userTab.setObjectName(u"userTab")
        self.verticalLayout_2 = QVBoxLayout(self.userTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 6, -1, 6)
        self.oldPassword = QLabel(self.userTab)
        self.oldPassword.setObjectName(u"oldPassword")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.oldPassword.sizePolicy().hasHeightForWidth())
        self.oldPassword.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.oldPassword)

        self.oldPasswordLineEdit = QLineEdit(self.userTab)
        self.oldPasswordLineEdit.setObjectName(u"oldPasswordLineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(9)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.oldPasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.oldPasswordLineEdit.setSizePolicy(sizePolicy3)
        self.oldPasswordLineEdit.setTabletTracking(False)
        self.oldPasswordLineEdit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.oldPasswordLineEdit.setEchoMode(QLineEdit.Password)
        self.oldPasswordLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.oldPasswordLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 6, -1, 6)
        self.password_2 = QLabel(self.userTab)
        self.password_2.setObjectName(u"password_2")
        sizePolicy2.setHeightForWidth(self.password_2.sizePolicy().hasHeightForWidth())
        self.password_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.password_2)

        self.passwordLineEdit_2 = QLineEdit(self.userTab)
        self.passwordLineEdit_2.setObjectName(u"passwordLineEdit_2")
        sizePolicy3.setHeightForWidth(self.passwordLineEdit_2.sizePolicy().hasHeightForWidth())
        self.passwordLineEdit_2.setSizePolicy(sizePolicy3)
        self.passwordLineEdit_2.setTabletTracking(False)
        self.passwordLineEdit_2.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.passwordLineEdit_2.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit_2.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.passwordLineEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, 6)
        self.Repassword = QLabel(self.userTab)
        self.Repassword.setObjectName(u"Repassword")
        sizePolicy2.setHeightForWidth(self.Repassword.sizePolicy().hasHeightForWidth())
        self.Repassword.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.Repassword)

        self.RepasswordLineEdit = QLineEdit(self.userTab)
        self.RepasswordLineEdit.setObjectName(u"RepasswordLineEdit")
        sizePolicy3.setHeightForWidth(self.RepasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.RepasswordLineEdit.setSizePolicy(sizePolicy3)
        self.RepasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.RepasswordLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.Errortext_2 = QLabel(self.userTab)
        self.Errortext_2.setObjectName(u"Errortext_2")

        self.verticalLayout_2.addWidget(self.Errortext_2)

        self.frame = QFrame(self.userTab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(94)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(200, 0, 200, 0)
        self.okPushButton = QPushButton(self.frame)
        self.okPushButton.setObjectName(u"okPushButton")

        self.horizontalLayout_5.addWidget(self.okPushButton)

        self.cancelPushButton = QPushButton(self.frame)
        self.cancelPushButton.setObjectName(u"cancelPushButton")

        self.horizontalLayout_5.addWidget(self.cancelPushButton)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settings.addTab(self.userTab, "")

        self.gridLayout.addWidget(self.settings, 0, 0, 1, 1)


        self.retranslateUi(settingDialog)

        self.closeMe.setDefault(True)
        self.settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settingDialog)
    # setupUi

    def retranslateUi(self, settingDialog):
        settingDialog.setWindowTitle(QCoreApplication.translate("settingDialog", u"Settings", None))
        self.closeMe.setText(QCoreApplication.translate("settingDialog", u"OK", None))
        self.themeChoice.setItemText(0, QCoreApplication.translate("settingDialog", u"Light Theme", None))
        self.themeChoice.setItemText(1, QCoreApplication.translate("settingDialog", u"Dark Theme", None))

        self.themeLabel.setText(QCoreApplication.translate("settingDialog", u"Theme:", None))
        self.fontSizeLabel.setText(QCoreApplication.translate("settingDialog", u"Font Size:", None))
        self.fontFamilyLabel.setText(QCoreApplication.translate("settingDialog", u"Font Family:", None))
        self.settings.setTabText(self.settings.indexOf(self.tabAppearance), QCoreApplication.translate("settingDialog", u"Appearance", None))
        self.hardExt.setText(QCoreApplication.translate("settingDialog", u"Enable hard breaks", None))
        self.footnotesExt.setText(QCoreApplication.translate("settingDialog", u"Enable Footnotes", None))
        self.defListsExt.setText(QCoreApplication.translate("settingDialog", u"Enable Definition Lists", None))
        self.mdExt.setText(QCoreApplication.translate("settingDialog", u"Enable Markdown in HTML", None))
        self.supExt.setText(QCoreApplication.translate("settingDialog", u"Enable Superscript", None))
        self.subExt.setText(QCoreApplication.translate("settingDialog", u"Enable Subscript", None))
        self.linkExt.setText(QCoreApplication.translate("settingDialog", u"Enable Auto Detect Links", None))
        self.symbolsExt.setText(QCoreApplication.translate("settingDialog", u"Enable Smart Symbols", None))
        self.strikeExt.setText(QCoreApplication.translate("settingDialog", u"Enable Strike", None))
        self.settings.setTabText(self.settings.indexOf(self.tabPlugins), QCoreApplication.translate("settingDialog", u"Plugins", None))
        self.enterPwdLabel.setText(QCoreApplication.translate("settingDialog", u"Enter Password to access encyption settings:", None))
        self.encryptAllChoice.setText(QCoreApplication.translate("settingDialog", u"Encrypt all notes", None))
        self.enterPwd.setPlaceholderText(QCoreApplication.translate("settingDialog", u"Enter Password", None))
        self.okPushButton_2.setText(QCoreApplication.translate("settingDialog", u"Ok", None))
        self.settings.setTabText(self.settings.indexOf(self.tabEncryption), QCoreApplication.translate("settingDialog", u"Encryption", None))
        self.oldPassword.setText(QCoreApplication.translate("settingDialog", u"Old Password", None))
        self.oldPasswordLineEdit.setText("")
        self.password_2.setText(QCoreApplication.translate("settingDialog", u"New Password", None))
        self.passwordLineEdit_2.setText("")
        self.Repassword.setText(QCoreApplication.translate("settingDialog", u"Re-enter Password", None))
        self.Errortext_2.setText("")
        self.okPushButton.setText(QCoreApplication.translate("settingDialog", u"OK", None))
        self.cancelPushButton.setText(QCoreApplication.translate("settingDialog", u"Cancel", None))
        self.settings.setTabText(self.settings.indexOf(self.userTab), QCoreApplication.translate("settingDialog", u"User", None))
    # retranslateUi

