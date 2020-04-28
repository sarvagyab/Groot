# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsDialog.ui'
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
        settingDialog.resize(929, 833)
        self.gridLayout = QGridLayout(settingDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(settingDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.mainFrame = QFrame(settingDialog)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMainFrame = QFrame(self.mainFrame)
        self.leftMainFrame.setObjectName(u"leftMainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMainFrame.sizePolicy().hasHeightForWidth())
        self.leftMainFrame.setSizePolicy(sizePolicy)
        self.leftMainFrame.setFrameShape(QFrame.StyledPanel)
        self.leftMainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.leftMainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchLineEdit = QLineEdit(self.leftMainFrame)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	padding: 2px 5px 2px 27px;\n"
"	margin-right: 0px;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.searchLineEdit)

        self.settingsTreeWidget = QTreeWidget(self.leftMainFrame)
        QTreeWidgetItem(self.settingsTreeWidget)
        self.settingsTreeWidget.setObjectName(u"settingsTreeWidget")
        self.settingsTreeWidget.setAllColumnsShowFocus(False)
        self.settingsTreeWidget.setHeaderHidden(True)

        self.verticalLayout.addWidget(self.settingsTreeWidget)


        self.horizontalLayout.addWidget(self.leftMainFrame)

        self.settingsStackedWidget = QStackedWidget(self.mainFrame)
        self.settingsStackedWidget.setObjectName(u"settingsStackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settingsStackedWidget.sizePolicy().hasHeightForWidth())
        self.settingsStackedWidget.setSizePolicy(sizePolicy1)
        self.encryptionSetting = QWidget()
        self.encryptionSetting.setObjectName(u"encryptionSetting")
        self.horizontalLayout_2 = QHBoxLayout(self.encryptionSetting)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.encryptionSetting)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox)

        self.verticalSpacer = QSpacerItem(20, 540, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame)

        self.settingsStackedWidget.addWidget(self.encryptionSetting)
        self.setting2Page = QWidget()
        self.setting2Page.setObjectName(u"setting2Page")
        self.settingsStackedWidget.addWidget(self.setting2Page)
        self.setting2_1Page = QWidget()
        self.setting2_1Page.setObjectName(u"setting2_1Page")
        self.settingsStackedWidget.addWidget(self.setting2_1Page)
        self.setting2_2Page = QWidget()
        self.setting2_2Page.setObjectName(u"setting2_2Page")
        self.settingsStackedWidget.addWidget(self.setting2_2Page)
        self.setting3Page = QWidget()
        self.setting3Page.setObjectName(u"setting3Page")
        self.settingsStackedWidget.addWidget(self.setting3Page)
        self.setting4Page = QWidget()
        self.setting4Page.setObjectName(u"setting4Page")
        self.settingsStackedWidget.addWidget(self.setting4Page)

        self.horizontalLayout.addWidget(self.settingsStackedWidget)


        self.gridLayout.addWidget(self.mainFrame, 0, 0, 1, 1)


        self.retranslateUi(settingDialog)

        self.settingsStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settingDialog)
    # setupUi

    def retranslateUi(self, settingDialog):
        settingDialog.setWindowTitle(QCoreApplication.translate("settingDialog", u"Settings", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("settingDialog", u"Find Settings", None))
        ___qtreewidgetitem = self.settingsTreeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("settingDialog", u"1", None));

        __sortingEnabled = self.settingsTreeWidget.isSortingEnabled()
        self.settingsTreeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.settingsTreeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("settingDialog", u"Encryption", None));
        self.settingsTreeWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("settingDialog", u"Enter password to change this option.", None))
        self.label_2.setText(QCoreApplication.translate("settingDialog", u"password", None))
        self.checkBox.setText(QCoreApplication.translate("settingDialog", u"Encrypt all notes", None))
    # retranslateUi

