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
        font.setPointSize(13)
        self.settings.setFont(font)
        self.tabAppearance = QWidget()
        self.tabAppearance.setObjectName(u"tabAppearance")
        self.comboBox = QComboBox(self.tabAppearance)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 70, 161, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.comboBox.setFont(font1)
        self.label_2 = QLabel(self.tabAppearance)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 121, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.tabAppearance)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 160, 101, 21))
        self.label_3.setFont(font2)
        self.fontComboBox = QFontComboBox(self.tabAppearance)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setGeometry(QRect(140, 230, 226, 31))
        self.fontComboBox.setFont(font1)
        self.lineEdit_2 = QLineEdit(self.tabAppearance)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(140, 160, 121, 22))
        self.lineEdit_2.setFont(font1)
        self.label_4 = QLabel(self.tabAppearance)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 230, 111, 31))
        self.label_4.setFont(font2)
        self.settings.addTab(self.tabAppearance, "")
        self.tabPlugins = QWidget()
        self.tabPlugins.setObjectName(u"tabPlugins")
        self.verticalLayout = QVBoxLayout(self.tabPlugins)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox = QCheckBox(self.tabPlugins)
        self.checkBox.setObjectName(u"checkBox")
        font3 = QFont()
        font3.setPointSize(10)
        self.checkBox.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.tabPlugins)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.tabPlugins)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.tabPlugins)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.tabPlugins)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.tabPlugins)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.tabPlugins)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.tabPlugins)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.tabPlugins)
        self.checkBox_9.setObjectName(u"checkBox_9")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setStrikeOut(False)
        self.checkBox_9.setFont(font4)

        self.verticalLayout.addWidget(self.checkBox_9)

        self.settings.addTab(self.tabPlugins, "")
        self.tabEncryption = QWidget()
        self.tabEncryption.setObjectName(u"tabEncryption")
        self.lineEdit = QLineEdit(self.tabEncryption)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 70, 271, 31))
        self.lineEdit.setFont(font1)
        self.label = QLabel(self.tabEncryption)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 441, 41))
        self.label.setFont(font2)
        self.checkBox_10 = QCheckBox(self.tabEncryption)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setGeometry(QRect(10, 140, 261, 31))
        self.checkBox_10.setFont(font2)
        self.pushButton = QPushButton(self.tabEncryption)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 220, 221, 31))
        self.pushButton.setFont(font2)
        self.settings.addTab(self.tabEncryption, "")

        self.gridLayout.addWidget(self.settings, 0, 0, 1, 1)


        self.retranslateUi(settingDialog)

        self.settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settingDialog)
    # setupUi

    def retranslateUi(self, settingDialog):
        settingDialog.setWindowTitle(QCoreApplication.translate("settingDialog", u"Settings", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("settingDialog", u"Light Theme", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("settingDialog", u"Dark Theme", None))

        self.label_2.setText(QCoreApplication.translate("settingDialog", u"Theme:", None))
        self.label_3.setText(QCoreApplication.translate("settingDialog", u"Font size:", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("settingDialog", u"Enter size", None))
        self.label_4.setText(QCoreApplication.translate("settingDialog", u"Font Family:", None))
        self.settings.setTabText(self.settings.indexOf(self.tabAppearance), QCoreApplication.translate("settingDialog", u"Appearance", None))
        self.checkBox.setText(QCoreApplication.translate("settingDialog", u"Tables", None))
        self.checkBox_2.setText(QCoreApplication.translate("settingDialog", u"Footnotes", None))
        self.checkBox_3.setText(QCoreApplication.translate("settingDialog", u"Definition Lists", None))
        self.checkBox_4.setText(QCoreApplication.translate("settingDialog", u"Markdown in HTML", None))
        self.checkBox_5.setText(QCoreApplication.translate("settingDialog", u"Superscript", None))
        self.checkBox_6.setText(QCoreApplication.translate("settingDialog", u"Subscript", None))
        self.checkBox_7.setText(QCoreApplication.translate("settingDialog", u"Auto Detect Links", None))
        self.checkBox_8.setText(QCoreApplication.translate("settingDialog", u"Smart Symbols", None))
        self.checkBox_9.setText(QCoreApplication.translate("settingDialog", u"Strike", None))
        self.settings.setTabText(self.settings.indexOf(self.tabPlugins), QCoreApplication.translate("settingDialog", u"Plugins", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("settingDialog", u"Enter Password", None))
        self.label.setText(QCoreApplication.translate("settingDialog", u"Enter Password to access encyption settings", None))
        self.checkBox_10.setText(QCoreApplication.translate("settingDialog", u"Encrypt all notes", None))
        self.pushButton.setText(QCoreApplication.translate("settingDialog", u"Change Password", None))
        self.settings.setTabText(self.settings.indexOf(self.tabEncryption), QCoreApplication.translate("settingDialog", u"Encryption", None))
    # retranslateUi

