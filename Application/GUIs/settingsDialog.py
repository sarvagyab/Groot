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


class Ui_settingDialog(object):
    def setupUi(self, settingDialog):
        if not settingDialog.objectName():
            settingDialog.setObjectName(u"settingDialog")
        settingDialog.resize(870, 461)
        self.gridLayout = QGridLayout(settingDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.settings = QTabWidget(settingDialog)
        self.settings.setObjectName(u"settings")
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
        self.enterPwd = QLineEdit(self.tabEncryption)
        self.enterPwd.setObjectName(u"enterPwd")
        self.enterPwd.setGeometry(QRect(10, 70, 271, 31))
        self.enterPwd.setFont(font1)
        self.enterPwdLabel = QLabel(self.tabEncryption)
        self.enterPwdLabel.setObjectName(u"enterPwdLabel")
        self.enterPwdLabel.setGeometry(QRect(10, 20, 441, 41))
        self.enterPwdLabel.setFont(font1)
        self.encryptAllChoice = QCheckBox(self.tabEncryption)
        self.encryptAllChoice.setObjectName(u"encryptAllChoice")
        self.encryptAllChoice.setGeometry(QRect(10, 140, 261, 31))
        self.encryptAllChoice.setFont(font1)
        self.changePwdChoice = QPushButton(self.tabEncryption)
        self.changePwdChoice.setObjectName(u"changePwdChoice")
        self.changePwdChoice.setGeometry(QRect(10, 220, 221, 31))
        self.changePwdChoice.setFont(font1)
        self.settings.addTab(self.tabEncryption, "")

        self.gridLayout.addWidget(self.settings, 0, 0, 1, 1)


        self.retranslateUi(settingDialog)

        self.settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settingDialog)
    # setupUi

    def retranslateUi(self, settingDialog):
        settingDialog.setWindowTitle(QCoreApplication.translate("settingDialog", u"Settings", None))
        self.themeChoice.setItemText(0, QCoreApplication.translate("settingDialog", u"Light Theme", None))
        self.themeChoice.setItemText(1, QCoreApplication.translate("settingDialog", u"Dark Theme", None))

        self.themeLabel.setText(QCoreApplication.translate("settingDialog", u"Theme:", None))
        self.fontSizeLabel.setText(QCoreApplication.translate("settingDialog", u"Font size:", None))
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
        self.enterPwd.setPlaceholderText(QCoreApplication.translate("settingDialog", u"Enter Password", None))
        self.enterPwdLabel.setText(QCoreApplication.translate("settingDialog", u"Enter Password to access encyption settings:", None))
        self.encryptAllChoice.setText(QCoreApplication.translate("settingDialog", u"Encrypt all notes", None))
        self.changePwdChoice.setText(QCoreApplication.translate("settingDialog", u"Change Password", None))
        self.settings.setTabText(self.settings.indexOf(self.tabEncryption), QCoreApplication.translate("settingDialog", u"Encryption", None))
    # retranslateUi

