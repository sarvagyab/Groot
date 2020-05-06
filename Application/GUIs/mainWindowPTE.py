# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowPTE.ui'
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

class Ui_Groot(object):
    def setupUi(self, Groot):
        if not Groot.objectName():
            Groot.setObjectName(u"Groot")
        Groot.resize(1602, 795)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Groot.sizePolicy().hasHeightForWidth())
        Groot.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(11)
        Groot.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/App Icon/groot.png", QSize(), QIcon.Normal, QIcon.Off)
        Groot.setWindowIcon(icon)
        Groot.setStyleSheet(u" QScrollBar:vertical {\n"
"     background: #32CC99;\n"
"     width: 15px;\n"
"     margin: 22px 0 22px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: gray;\n"
"     min-height: 40px;\n"
" }\n"
" ")
        self.actionNotes_Tree = QAction(Groot)
        self.actionNotes_Tree.setObjectName(u"actionNotes_Tree")
        self.actionPrint = QAction(Groot)
        self.actionPrint.setObjectName(u"actionPrint")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/16x16/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrint.setIcon(icon1)
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(10)
        self.actionPrint.setFont(font1)
        self.actionQuit = QAction(Groot)
        self.actionQuit.setObjectName(u"actionQuit")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/16x16/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setFont(font1)
        self.actionQuit.setShortcutVisibleInContextMenu(True)
        self.actionMD = QAction(Groot)
        self.actionMD.setObjectName(u"actionMD")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/Format Icons/16x16/markdown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMD.setIcon(icon3)
        self.actionMD_2 = QAction(Groot)
        self.actionMD_2.setObjectName(u"actionMD_2")
        self.actionMD_2.setIcon(icon3)
        self.actionHTML = QAction(Groot)
        self.actionHTML.setObjectName(u"actionHTML")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/Format Icons/16x16/html.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHTML.setIcon(icon4)
        self.actionPDF = QAction(Groot)
        self.actionPDF.setObjectName(u"actionPDF")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/Format Icons/16x16/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPDF.setIcon(icon5)
        self.actionSearch_in_Current_Note = QAction(Groot)
        self.actionSearch_in_Current_Note.setObjectName(u"actionSearch_in_Current_Note")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/16x16/find.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSearch_in_Current_Note.setIcon(icon6)
        self.actionSearch_in_Current_Note.setFont(font1)
        self.actionSearch_in_All_Notes = QAction(Groot)
        self.actionSearch_in_All_Notes.setObjectName(u"actionSearch_in_All_Notes")
        self.actionOptions = QAction(Groot)
        self.actionOptions.setObjectName(u"actionOptions")
        self.actionAbout = QAction(Groot)
        self.actionAbout.setObjectName(u"actionAbout")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/16x16/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon7)
        self.actionAbout.setFont(font1)
        self.actionRequest = QAction(Groot)
        self.actionRequest.setObjectName(u"actionRequest")
        self.actionRequest.setFont(font1)
        self.actionDark_Theme = QAction(Groot)
        self.actionDark_Theme.setObjectName(u"actionDark_Theme")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/16x16/sun_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDark_Theme.setIcon(icon8)
        self.actionDark_Theme.setFont(font1)
        self.actionLight_Theme = QAction(Groot)
        self.actionLight_Theme.setObjectName(u"actionLight_Theme")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/16x16/sun_light.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLight_Theme.setIcon(icon9)
        self.actionLight_Theme.setFont(font1)
        self.actionBold = QAction(Groot)
        self.actionBold.setObjectName(u"actionBold")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/16x16/bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBold.setIcon(icon10)
        self.actionBold.setShortcutVisibleInContextMenu(True)
        self.actionItalic = QAction(Groot)
        self.actionItalic.setObjectName(u"actionItalic")
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/16x16/italic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionItalic.setIcon(icon11)
        self.actionItalic.setShortcutVisibleInContextMenu(True)
        self.actionUnderline = QAction(Groot)
        self.actionUnderline.setObjectName(u"actionUnderline")
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/16x16/underline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUnderline.setIcon(icon12)
        self.actionNew_note = QAction(Groot)
        self.actionNew_note.setObjectName(u"actionNew_note")
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/16x16/doc_new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_note.setIcon(icon13)
        self.actionNew_note.setFont(font1)
        self.actionNew_note.setShortcutVisibleInContextMenu(True)
        self.actionNew_sub_notebook = QAction(Groot)
        self.actionNew_sub_notebook.setObjectName(u"actionNew_sub_notebook")
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/16x16/subfolder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_sub_notebook.setIcon(icon14)
        self.actionNew_sub_notebook.setFont(font1)
        self.actionNew_sub_notebook.setShortcutVisibleInContextMenu(True)
        self.actionNew_notebook = QAction(Groot)
        self.actionNew_notebook.setObjectName(u"actionNew_notebook")
        icon15 = QIcon()
        icon15.addFile(u":/icons/Icons/16x16/folder_plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_notebook.setIcon(icon15)
        self.actionNew_notebook.setFont(font1)
        self.actionNew_notebook.setShortcutVisibleInContextMenu(True)
        self.actionEncrypt_note = QAction(Groot)
        self.actionEncrypt_note.setObjectName(u"actionEncrypt_note")
        icon16 = QIcon()
        icon16.addFile(u":/icons/Icons/16x16/encrypt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEncrypt_note.setIcon(icon16)
        self.actionDecrypt_note = QAction(Groot)
        self.actionDecrypt_note.setObjectName(u"actionDecrypt_note")
        icon17 = QIcon()
        icon17.addFile(u":/icons/Icons/16x16/decrypt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDecrypt_note.setIcon(icon17)
        self.actionSettings = QAction(Groot)
        self.actionSettings.setObjectName(u"actionSettings")
        icon18 = QIcon()
        icon18.addFile(u":/icons/Icons/16x16/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon18)
        self.actionSettings.setFont(font1)
        self.actionSettings.setShortcutVisibleInContextMenu(True)
        self.actionSave_note = QAction(Groot)
        self.actionSave_note.setObjectName(u"actionSave_note")
        icon19 = QIcon()
        icon19.addFile(u":/icons/Icons/16x16/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_note.setIcon(icon19)
        self.actionOpen_note = QAction(Groot)
        self.actionOpen_note.setObjectName(u"actionOpen_note")
        self.actionReport_a_bug = QAction(Groot)
        self.actionReport_a_bug.setObjectName(u"actionReport_a_bug")
        icon20 = QIcon()
        icon20.addFile(u":/icons/Icons/16x16/bug.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionReport_a_bug.setIcon(icon20)
        self.actionReport_a_bug.setFont(font1)
        self.actionLink = QAction(Groot)
        self.actionLink.setObjectName(u"actionLink")
        icon21 = QIcon()
        icon21.addFile(u":/icons/Icons/16x16/link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLink.setIcon(icon21)
        font2 = QFont()
        font2.setFamily(u"Calibri")
        self.actionLink.setFont(font2)
        self.actionLink.setShortcutVisibleInContextMenu(True)
        self.actionImage = QAction(Groot)
        self.actionImage.setObjectName(u"actionImage")
        icon22 = QIcon()
        icon22.addFile(u":/icons/Icons/16x16/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImage.setIcon(icon22)
        self.actionImage.setShortcutVisibleInContextMenu(True)
        self.actionCode = QAction(Groot)
        self.actionCode.setObjectName(u"actionCode")
        self.actionCode.setShortcutVisibleInContextMenu(True)
        self.actionDate_and_Time = QAction(Groot)
        self.actionDate_and_Time.setObjectName(u"actionDate_and_Time")
        self.actionDate_and_Time.setShortcutVisibleInContextMenu(True)
        self.centralwidget = QWidget(Groot)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(252, 252, 252);")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.mainWindow = QWidget(self.centralwidget)
        self.mainWindow.setObjectName(u"mainWindow")
        self.mainWindow.setStyleSheet(u"QWidget{\n"
"	margin:0px;\n"
"	padding:0px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.mainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rootOptions = QWidget(self.mainWindow)
        self.rootOptions.setObjectName(u"rootOptions")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rootOptions.sizePolicy().hasHeightForWidth())
        self.rootOptions.setSizePolicy(sizePolicy1)
        self.rootOptions.setMinimumSize(QSize(0, 0))
        self.rootOptions.setStyleSheet(u"QFrame{\n"
"	border-style:None;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.rootOptions)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.buttonFrame = QFrame(self.rootOptions)
        self.buttonFrame.setObjectName(u"buttonFrame")
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(8)
        self.buttonFrame.setFont(font3)
        self.buttonFrame.setStyleSheet(u"QPushButton{\n"
"	border:None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgba(211,211,211,0.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border:1px solid blue;\n"
"}")
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.buttonFrame)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(3, 0, 0, 0)
        self.newNote = QPushButton(self.buttonFrame)
        self.newNote.setObjectName(u"newNote")
        sizePolicy1.setHeightForWidth(self.newNote.sizePolicy().hasHeightForWidth())
        self.newNote.setSizePolicy(sizePolicy1)
        self.newNote.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(9)
        self.newNote.setFont(font4)
        self.newNote.setCursor(QCursor(Qt.PointingHandCursor))
        self.newNote.setStyleSheet(u"QPushButton{\n"
"	border:None;\n"
"	padding:4px 2px 4px 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgba(211,211,211,0.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border:1px solid blue;\n"
"}")
        self.newNote.setIcon(icon13)

        self.horizontalLayout_12.addWidget(self.newNote)

        self.newNotebook = QPushButton(self.buttonFrame)
        self.newNotebook.setObjectName(u"newNotebook")
        sizePolicy1.setHeightForWidth(self.newNotebook.sizePolicy().hasHeightForWidth())
        self.newNotebook.setSizePolicy(sizePolicy1)
        self.newNotebook.setMinimumSize(QSize(0, 0))
        self.newNotebook.setFont(font4)
        self.newNotebook.setCursor(QCursor(Qt.PointingHandCursor))
        self.newNotebook.setStyleSheet(u"QPushButton{\n"
"	border:None;\n"
"	padding:4px 2px 4px 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgba(211,211,211,0.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border:1px solid blue;\n"
"}")
        self.newNotebook.setIcon(icon15)

        self.horizontalLayout_12.addWidget(self.newNotebook)

        self.newSubNotebook = QPushButton(self.buttonFrame)
        self.newSubNotebook.setObjectName(u"newSubNotebook")
        sizePolicy1.setHeightForWidth(self.newSubNotebook.sizePolicy().hasHeightForWidth())
        self.newSubNotebook.setSizePolicy(sizePolicy1)
        self.newSubNotebook.setMinimumSize(QSize(0, 0))
        self.newSubNotebook.setFont(font4)
        self.newSubNotebook.setCursor(QCursor(Qt.PointingHandCursor))
        self.newSubNotebook.setStyleSheet(u"QPushButton{\n"
"	border:None;\n"
"	padding:4px 2px 4px 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgba(211,211,211,0.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border:1px solid blue;\n"
"}")
        self.newSubNotebook.setIcon(icon14)

        self.horizontalLayout_12.addWidget(self.newSubNotebook)


        self.horizontalLayout_6.addWidget(self.buttonFrame)

        self.findFrame = QFrame(self.rootOptions)
        self.findFrame.setObjectName(u"findFrame")
        self.findFrame.setStyleSheet(u"")
        self.findFrame.setFrameShape(QFrame.StyledPanel)
        self.findFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.findFrame)
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame = QFrame(self.findFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(3, 0, 3, 3)
        self.searchBar = QLineEdit(self.frame)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy1.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy1)
        self.searchBar.setMinimumSize(QSize(250, 28))
        self.searchBar.setFont(font1)
        self.searchBar.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid grey;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid black;\n"
"}")

        self.horizontalLayout_11.addWidget(self.searchBar)

        self.errorLabel = QLabel(self.frame)
        self.errorLabel.setObjectName(u"errorLabel")

        self.horizontalLayout_11.addWidget(self.errorLabel)

        self.wholeWord = QPushButton(self.frame)
        self.wholeWord.setObjectName(u"wholeWord")
        self.wholeWord.setFont(font4)
        self.wholeWord.setCursor(QCursor(Qt.PointingHandCursor))
        self.wholeWord.setStyleSheet(u"QPushButton{\n"
"	border-style:None;\n"
"	padding:6px 4px 6px 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:rgba(211,211,211,0.4);\n"
"}\n"
"\n"
"QPushButton:!checked:hover{\n"
"	padding-top:1px;\n"
"	padding-left:1px;\n"
"}")
        self.wholeWord.setIconSize(QSize(31, 31))
        self.wholeWord.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.wholeWord)

        self.matchCase = QPushButton(self.frame)
        self.matchCase.setObjectName(u"matchCase")
        self.matchCase.setFont(font4)
        self.matchCase.setCursor(QCursor(Qt.PointingHandCursor))
        self.matchCase.setStyleSheet(u"QPushButton{\n"
"	border-style:None;\n"
"	padding:6px 4px 6px 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:rgba(211,211,211,0.4);\n"
"}\n"
"\n"
"QPushButton:!checked:hover{\n"
"	padding-top:1px;\n"
"	padding-left:1px;\n"
"}")
        self.matchCase.setIconSize(QSize(31, 31))
        self.matchCase.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.matchCase)

        self.regexButton = QPushButton(self.frame)
        self.regexButton.setObjectName(u"regexButton")
        self.regexButton.setFont(font4)
        self.regexButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.regexButton.setStyleSheet(u"QPushButton{\n"
"	border-style:None;\n"
"	padding:6px 4px 6px 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:rgba(211,211,211,0.4);\n"
"}\n"
"\n"
"QPushButton:!checked:hover{\n"
"	padding-top:1px;\n"
"	padding-left:1px;\n"
"}s")
        self.regexButton.setIconSize(QSize(31, 31))
        self.regexButton.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.regexButton)


        self.horizontalLayout_10.addWidget(self.frame)

        self.prevMatch = QPushButton(self.findFrame)
        self.prevMatch.setObjectName(u"prevMatch")
        self.prevMatch.setCursor(QCursor(Qt.PointingHandCursor))
        self.prevMatch.setStyleSheet(u"QPushButton{\n"
"	border:None;\n"
"	margin:0px;\n"
"	padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-color:black;\n"
"	background-origin:border-box;\n"
"	padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 1px;\n"
"	padding-left :1px;\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/icons/Icons/32x32/arrow_top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prevMatch.setIcon(icon23)
        self.prevMatch.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.prevMatch)

        self.nextMatch = QPushButton(self.findFrame)
        self.nextMatch.setObjectName(u"nextMatch")
        self.nextMatch.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextMatch.setStyleSheet(u"QPushButton{\n"
"	border:None;\n"
"	margin:0px;\n"
"	padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-color:black;\n"
"	background-origin:border-box;\n"
"	padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 1px;\n"
"	padding-left :1px;\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/icons/Icons/32x32/arrow_bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextMatch.setIcon(icon24)
        self.nextMatch.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.nextMatch)


        self.horizontalLayout_6.addWidget(self.findFrame)

        self.emptySpaceMainOptions = QSpacerItem(800, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.emptySpaceMainOptions)


        self.verticalLayout.addWidget(self.rootOptions)

        self.centralView = QWidget(self.mainWindow)
        self.centralView.setObjectName(u"centralView")
        sizePolicy.setHeightForWidth(self.centralView.sizePolicy().hasHeightForWidth())
        self.centralView.setSizePolicy(sizePolicy)
        self.centralView.setMinimumSize(QSize(0, 0))
        self.centralView.setStyleSheet(u"QWidget{\n"
"	margin:0px;\n"
"	padding:0px;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.centralView)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.treeWidget = QTreeWidget(self.centralView)
        font5 = QFont()
        font5.setPointSize(12)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem.setFont(0, font5);
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1.setFont(0, font5);
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy2)
        self.treeWidget.setMinimumSize(QSize(200, 0))
        self.treeWidget.setFont(font1)
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setStyleSheet(u"QTreeView {\n"
"	background-color:black;\n"
"	color:white;\n"
"	alternate-background-color:gray;\n"
"}\n"
"\n"
"QTreeView::item:selected{\n"
"	color : rgb(53, 113, 242);\n"
"}\n"
"\n"
"QTreeView::item:selected:active{\n"
"	color : rgb(53, 113, 242);\n"
"}\n"
"\n"
"QTreeView::item:selected:!active {\n"
"    /*background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);*/\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    border-image: none;\n"
"	image: url(:/icons/Icons/16x16/branch_close_light.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    border-image: none;\n"
"	image: url(:/icons/Icons/16x16/branch_open_light.png);\n"
"}")
        self.treeWidget.setFrameShape(QFrame.WinPanel)
        self.treeWidget.setFrameShadow(QFrame.Raised)
        self.treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setStretchLastSection(False)

        self.horizontalLayout_5.addWidget(self.treeWidget)

        self.editorArea = QWidget(self.centralView)
        self.editorArea.setObjectName(u"editorArea")
        sizePolicy.setHeightForWidth(self.editorArea.sizePolicy().hasHeightForWidth())
        self.editorArea.setSizePolicy(sizePolicy)
        self.editorArea.setStyleSheet(u"QWidget{\n"
"	background-color:white;\n"
"	margin:0px;\n"
"	padding:0px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.editorArea)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleArea = QWidget(self.editorArea)
        self.titleArea.setObjectName(u"titleArea")
        sizePolicy1.setHeightForWidth(self.titleArea.sizePolicy().hasHeightForWidth())
        self.titleArea.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(3)
        font6.setBold(True)
        font6.setItalic(True)
        font6.setWeight(75)
        font6.setKerning(True)
        self.titleArea.setFont(font6)
        self.titleArea.setStyleSheet(u"padding:0px;\n"
"margin :0px;\n"
"background-color:gray;\n"
"color:white;")
        self.horizontalLayout = QHBoxLayout(self.titleArea)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fileName = QLabel(self.titleArea)
        self.fileName.setObjectName(u"fileName")
        font7 = QFont()
        font7.setFamily(u"Calibri")
        font7.setPointSize(12)
        font7.setUnderline(False)
        self.fileName.setFont(font7)
        self.fileName.setStyleSheet(u"")
        self.fileName.setScaledContents(False)
        self.fileName.setAlignment(Qt.AlignCenter)
        self.fileName.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.fileName)


        self.verticalLayout_2.addWidget(self.titleArea)

        self.editingButtons = QWidget(self.editorArea)
        self.editingButtons.setObjectName(u"editingButtons")
        self.editingButtons.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.editingButtons.sizePolicy().hasHeightForWidth())
        self.editingButtons.setSizePolicy(sizePolicy3)
        self.editingButtons.setMouseTracking(False)
        self.editingButtons.setLayoutDirection(Qt.LeftToRight)
        self.editingButtons.setAutoFillBackground(False)
        self.editingButtons.setStyleSheet(u"QFrame{\n"
"	border-right:2px solid gray;\n"
"	padding:0px;\n"
"	margin:0px;\n"
"	background-color:white;	\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-style:None;\n"
"	padding:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-color:black;\n"
"	background-origin:border-box;\n"
"	padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 1px;\n"
"	padding-left :1px;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.editingButtons)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 2, 0)
        self.formatFrame = QFrame(self.editingButtons)
        self.formatFrame.setObjectName(u"formatFrame")
        self.formatFrame.setStyleSheet(u"QPushButton{\n"
"	margin:0px;\n"
"	padding:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-color:black;\n"
"	background-origin:border-box;\n"
"	padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 1px;\n"
"	padding-left :1px;\n"
"}")
        self.formatFrame.setFrameShape(QFrame.StyledPanel)
        self.formatFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.formatFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.boldButton = QPushButton(self.formatFrame)
        self.boldButton.setObjectName(u"boldButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.boldButton.sizePolicy().hasHeightForWidth())
        self.boldButton.setSizePolicy(sizePolicy4)
        self.boldButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.boldButton.setFocusPolicy(Qt.StrongFocus)
        self.boldButton.setStyleSheet(u"")
        icon25 = QIcon()
        icon25.addFile(u":/icons/Icons/32x32/font_bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boldButton.setIcon(icon25)
        self.boldButton.setIconSize(QSize(32, 32))
        self.boldButton.setAutoExclusive(False)

        self.horizontalLayout_7.addWidget(self.boldButton)

        self.italicButton = QPushButton(self.formatFrame)
        self.italicButton.setObjectName(u"italicButton")
        self.italicButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.italicButton.setStyleSheet(u"")
        icon26 = QIcon()
        icon26.addFile(u":/icons/Icons/32x32/font_italic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.italicButton.setIcon(icon26)
        self.italicButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.italicButton)

        self.numberedList = QPushButton(self.formatFrame)
        self.numberedList.setObjectName(u"numberedList")
        self.numberedList.setCursor(QCursor(Qt.PointingHandCursor))
        self.numberedList.setStyleSheet(u"")
        icon27 = QIcon()
        icon27.addFile(u":/icons/Icons/32x32/numbered_list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.numberedList.setIcon(icon27)
        self.numberedList.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.numberedList)

        self.bullets = QPushButton(self.formatFrame)
        self.bullets.setObjectName(u"bullets")
        self.bullets.setCursor(QCursor(Qt.PointingHandCursor))
        self.bullets.setFocusPolicy(Qt.ClickFocus)
        self.bullets.setStyleSheet(u"")
        icon28 = QIcon()
        icon28.addFile(u":/icons/Icons/32x32/bullets.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bullets.setIcon(icon28)
        self.bullets.setIconSize(QSize(32, 32))
        self.bullets.setCheckable(False)
        self.bullets.setFlat(False)

        self.horizontalLayout_7.addWidget(self.bullets)


        self.horizontalLayout_3.addWidget(self.formatFrame)

        self.insertFrame = QFrame(self.editingButtons)
        self.insertFrame.setObjectName(u"insertFrame")
        self.insertFrame.setStyleSheet(u"QPushButton{\n"
"	margin:0px;\n"
"	padding:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-color:black;\n"
"	background-origin:border-box;\n"
"	padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 1px;\n"
"	padding-left :1px;\n"
"}")
        self.insertFrame.setFrameShape(QFrame.StyledPanel)
        self.insertFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.insertFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.link = QPushButton(self.insertFrame)
        self.link.setObjectName(u"link")
        self.link.setCursor(QCursor(Qt.PointingHandCursor))
        self.link.setStyleSheet(u"")
        icon29 = QIcon()
        icon29.addFile(u":/icons/Icons/32x32/link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.link.setIcon(icon29)
        self.link.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.link)

        self.insertFile = QPushButton(self.insertFrame)
        self.insertFile.setObjectName(u"insertFile")
        self.insertFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.insertFile.setStyleSheet(u"")
        icon30 = QIcon()
        icon30.addFile(u":/icons/Icons/32x32/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.insertFile.setIcon(icon30)
        self.insertFile.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.insertFile)

        self.code = QPushButton(self.insertFrame)
        self.code.setObjectName(u"code")
        self.code.setCursor(QCursor(Qt.PointingHandCursor))
        self.code.setStyleSheet(u"")
        icon31 = QIcon()
        icon31.addFile(u":/icons/Icons/32x32/brackets.png", QSize(), QIcon.Normal, QIcon.Off)
        self.code.setIcon(icon31)
        self.code.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.code)


        self.horizontalLayout_3.addWidget(self.insertFrame)

        self.encryptionFrame = QFrame(self.editingButtons)
        self.encryptionFrame.setObjectName(u"encryptionFrame")
        self.encryptionFrame.setStyleSheet(u"QPushButton{\n"
"	margin:0px;\n"
"	padding:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-color:black;\n"
"	background-origin:border-box;\n"
"	padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 1px;\n"
"	padding-left :1px;\n"
"}")
        self.encryptionFrame.setFrameShape(QFrame.StyledPanel)
        self.encryptionFrame.setFrameShadow(QFrame.Raised)
        self.encryptionFrame.setLineWidth(1)
        self.horizontalLayout_9 = QHBoxLayout(self.encryptionFrame)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.encryptionButton = QPushButton(self.encryptionFrame)
        self.encryptionButton.setObjectName(u"encryptionButton")
        self.encryptionButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.encryptionButton.setStyleSheet(u"")
        icon32 = QIcon()
        icon32.addFile(u":/icons/Icons/32x32/encrypt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.encryptionButton.setIcon(icon32)
        self.encryptionButton.setIconSize(QSize(32, 32))
        self.encryptionButton.setCheckable(True)
        self.encryptionButton.setChecked(False)

        self.horizontalLayout_9.addWidget(self.encryptionButton)

        self.decryptionButton = QPushButton(self.encryptionFrame)
        self.decryptionButton.setObjectName(u"decryptionButton")
        self.decryptionButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.decryptionButton.setStyleSheet(u"")
        icon33 = QIcon()
        icon33.addFile(u":/icons/Icons/32x32/decrypt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.decryptionButton.setIcon(icon33)
        self.decryptionButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.decryptionButton)

        self.permanentDecrypt = QPushButton(self.encryptionFrame)
        self.permanentDecrypt.setObjectName(u"permanentDecrypt")
        self.permanentDecrypt.setCursor(QCursor(Qt.PointingHandCursor))
        self.permanentDecrypt.setStyleSheet(u"image: url(:/icons/Icons/16x16/encrypt_20.png);\n"
"")
        icon34 = QIcon()
        icon34.addFile(u":/icons/Icons/32x32/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.permanentDecrypt.setIcon(icon34)
        self.permanentDecrypt.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.permanentDecrypt)

        self.changePasswordButton = QPushButton(self.encryptionFrame)
        self.changePasswordButton.setObjectName(u"changePasswordButton")
        self.changePasswordButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon35 = QIcon()
        icon35.addFile(u":/icons/Icons/32x32/key.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changePasswordButton.setIcon(icon35)
        self.changePasswordButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.changePasswordButton)


        self.horizontalLayout_3.addWidget(self.encryptionFrame)

        self.dateTime = QPushButton(self.editingButtons)
        self.dateTime.setObjectName(u"dateTime")
        self.dateTime.setCursor(QCursor(Qt.PointingHandCursor))
        self.dateTime.setStyleSheet(u"QPushButton{\n"
"	margin:0px;\n"
"	padding:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-style:solid;\n"
"	border-color:black;\n"
"	background-origin:border-box;\n"
"	padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 1px;\n"
"	padding-left :1px;\n"
"}")
        icon36 = QIcon()
        icon36.addFile(u":/icons/Icons/32x32/clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dateTime.setIcon(icon36)
        self.dateTime.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.dateTime)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.editingButtons)

        self.editingSection = QWidget(self.editorArea)
        self.editingSection.setObjectName(u"editingSection")
        self.editingSection.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.editingSection)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.editingSection)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font8 = QFont()
        font8.setFamily(u"Calibri")
        font8.setPointSize(17)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.plainTextEdit.setFont(font8)
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
"    background-color: white;\n"
"	border-top:1px solid black;\n"
"	border-right:1px solid black;\n"
"	selection-background-color:rgba(243, 255, 77,0.4);\n"
"	selection-color:	darkblue;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.plainTextEdit.setFrameShape(QFrame.Panel)
        self.plainTextEdit.setFrameShadow(QFrame.Raised)
        self.plainTextEdit.setLineWidth(1)
        self.plainTextEdit.setMidLineWidth(0)
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setCenterOnScroll(False)

        self.horizontalLayout_2.addWidget(self.plainTextEdit)

        self.mdViewer = QTextBrowser(self.editingSection)
        self.mdViewer.setObjectName(u"mdViewer")
        sizePolicy.setHeightForWidth(self.mdViewer.sizePolicy().hasHeightForWidth())
        self.mdViewer.setSizePolicy(sizePolicy)
        font9 = QFont()
        font9.setPointSize(17)
        self.mdViewer.setFont(font9)
        self.mdViewer.setStyleSheet(u"QTextBrowser{\n"
"	border-top:1px solid black;\n"
"    background-color: white;\n"
"	selection-background-color:rgba(243, 255, 77,0.4);\n"
"	selection-color:darkblue;\n"
"}\n"
"")
        self.mdViewer.setFrameShape(QFrame.NoFrame)
        self.mdViewer.setFrameShadow(QFrame.Raised)
        self.mdViewer.setLineWidth(1)
        self.mdViewer.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdViewer.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdViewer.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.mdViewer.setOpenLinks(False)

        self.horizontalLayout_2.addWidget(self.mdViewer)


        self.verticalLayout_2.addWidget(self.editingSection)


        self.horizontalLayout_5.addWidget(self.editorArea)


        self.verticalLayout.addWidget(self.centralView)


        self.horizontalLayout_4.addWidget(self.mainWindow)

        Groot.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Groot)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1602, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuImport = QMenu(self.menuFile)
        self.menuImport.setObjectName(u"menuImport")
        self.menuImport.setFont(font1)
        icon37 = QIcon()
        icon37.addFile(u":/icons/Icons/16x16/doc_import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuImport.setIcon(icon37)
        self.menuExport = QMenu(self.menuFile)
        self.menuExport.setObjectName(u"menuExport")
        self.menuExport.setFont(font1)
        icon38 = QIcon()
        icon38.addFile(u":/icons/Icons/16x16/doc_export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuExport.setIcon(icon38)
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuFormat = QMenu(self.menuEdit)
        self.menuFormat.setObjectName(u"menuFormat")
        self.menuFormat.setFont(font1)
        icon39 = QIcon()
        icon39.addFile(u":/icons/Icons/16x16/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuFormat.setIcon(icon39)
        self.menuEncrption = QMenu(self.menuEdit)
        self.menuEncrption.setObjectName(u"menuEncrption")
        self.menuEncrption.setFont(font1)
        self.menuEncrption.setIcon(icon16)
        self.menuInsert = QMenu(self.menuEdit)
        self.menuInsert.setObjectName(u"menuInsert")
        self.menuInsert.setFont(font1)
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        font10 = QFont()
        font10.setFamily(u"Calibri")
        font10.setPointSize(12)
        self.menuView.setFont(font10)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Groot.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew_note)
        self.menuFile.addAction(self.actionNew_sub_notebook)
        self.menuFile.addAction(self.actionNew_notebook)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuImport.addAction(self.actionMD)
        self.menuExport.addAction(self.actionMD_2)
        self.menuExport.addAction(self.actionHTML)
        self.menuExport.addAction(self.actionPDF)
        self.menuEdit.addAction(self.actionSearch_in_Current_Note)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuInsert.menuAction())
        self.menuEdit.addAction(self.menuFormat.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuEncrption.menuAction())
        self.menuFormat.addAction(self.actionBold)
        self.menuFormat.addAction(self.actionItalic)
        self.menuEncrption.addAction(self.actionEncrypt_note)
        self.menuEncrption.addAction(self.actionDecrypt_note)
        self.menuInsert.addAction(self.actionLink)
        self.menuInsert.addAction(self.actionImage)
        self.menuInsert.addAction(self.actionCode)
        self.menuInsert.addAction(self.actionDate_and_Time)
        self.menuView.addAction(self.actionDark_Theme)
        self.menuView.addAction(self.actionLight_Theme)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionReport_a_bug)
        self.menuHelp.addAction(self.actionRequest)

        self.retranslateUi(Groot)

        self.bullets.setDefault(False)


        QMetaObject.connectSlotsByName(Groot)
    # setupUi

    def retranslateUi(self, Groot):
        Groot.setWindowTitle(QCoreApplication.translate("Groot", u"Groot", None))
        self.actionNotes_Tree.setText(QCoreApplication.translate("Groot", u"Notes Tree", None))
        self.actionPrint.setText(QCoreApplication.translate("Groot", u"Print", None))
#if QT_CONFIG(shortcut)
        self.actionPrint.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("Groot", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionMD.setText(QCoreApplication.translate("Groot", u"MD", None))
        self.actionMD_2.setText(QCoreApplication.translate("Groot", u"MD", None))
        self.actionHTML.setText(QCoreApplication.translate("Groot", u"HTML", None))
        self.actionPDF.setText(QCoreApplication.translate("Groot", u"PDF", None))
        self.actionSearch_in_Current_Note.setText(QCoreApplication.translate("Groot", u"Search in Current Note", None))
#if QT_CONFIG(shortcut)
        self.actionSearch_in_Current_Note.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionSearch_in_All_Notes.setText(QCoreApplication.translate("Groot", u"Search in All Notes", None))
        self.actionOptions.setText(QCoreApplication.translate("Groot", u"Options", None))
        self.actionAbout.setText(QCoreApplication.translate("Groot", u"About", None))
        self.actionRequest.setText(QCoreApplication.translate("Groot", u"Request", None))
        self.actionDark_Theme.setText(QCoreApplication.translate("Groot", u"Dark Theme", None))
        self.actionLight_Theme.setText(QCoreApplication.translate("Groot", u"Light Theme", None))
        self.actionBold.setText(QCoreApplication.translate("Groot", u"Bold", None))
#if QT_CONFIG(shortcut)
        self.actionBold.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.actionItalic.setText(QCoreApplication.translate("Groot", u"Italic", None))
#if QT_CONFIG(shortcut)
        self.actionItalic.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionUnderline.setText(QCoreApplication.translate("Groot", u"Underline", None))
#if QT_CONFIG(shortcut)
        self.actionUnderline.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+U", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew_note.setText(QCoreApplication.translate("Groot", u"New note", None))
#if QT_CONFIG(shortcut)
        self.actionNew_note.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew_sub_notebook.setText(QCoreApplication.translate("Groot", u"New sub-notebook", None))
#if QT_CONFIG(shortcut)
        self.actionNew_sub_notebook.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew_notebook.setText(QCoreApplication.translate("Groot", u"New notebook", None))
#if QT_CONFIG(shortcut)
        self.actionNew_notebook.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+J", None))
#endif // QT_CONFIG(shortcut)
        self.actionEncrypt_note.setText(QCoreApplication.translate("Groot", u"Encrypt note", None))
        self.actionDecrypt_note.setText(QCoreApplication.translate("Groot", u"Decrypt note", None))
        self.actionSettings.setText(QCoreApplication.translate("Groot", u"Settings", None))
#if QT_CONFIG(shortcut)
        self.actionSettings.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_note.setText(QCoreApplication.translate("Groot", u"Save note", None))
#if QT_CONFIG(shortcut)
        self.actionSave_note.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen_note.setText(QCoreApplication.translate("Groot", u"Open note", None))
        self.actionReport_a_bug.setText(QCoreApplication.translate("Groot", u"Report a bug", None))
        self.actionLink.setText(QCoreApplication.translate("Groot", u"Link", None))
#if QT_CONFIG(shortcut)
        self.actionLink.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+K", None))
#endif // QT_CONFIG(shortcut)
        self.actionImage.setText(QCoreApplication.translate("Groot", u"File", None))
#if QT_CONFIG(shortcut)
        self.actionImage.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionCode.setText(QCoreApplication.translate("Groot", u"Code", None))
#if QT_CONFIG(shortcut)
        self.actionCode.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+`", None))
#endif // QT_CONFIG(shortcut)
        self.actionDate_and_Time.setText(QCoreApplication.translate("Groot", u"Date and Time", None))
#if QT_CONFIG(shortcut)
        self.actionDate_and_Time.setShortcut(QCoreApplication.translate("Groot", u"Ctrl+Shift+T", None))
#endif // QT_CONFIG(shortcut)
        self.newNote.setText(QCoreApplication.translate("Groot", u"New Note", None))
        self.newNotebook.setText(QCoreApplication.translate("Groot", u"New notebook", None))
        self.newSubNotebook.setText(QCoreApplication.translate("Groot", u"New sub-notebook", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("Groot", u"Search in this note", None))
        self.errorLabel.setText("")
        self.wholeWord.setText(QCoreApplication.translate("Groot", u"Whole word", None))
#if QT_CONFIG(tooltip)
        self.matchCase.setToolTip(QCoreApplication.translate("Groot", u"Case sensitive", None))
#endif // QT_CONFIG(tooltip)
        self.matchCase.setText(QCoreApplication.translate("Groot", u"Match Case", None))
        self.regexButton.setText(QCoreApplication.translate("Groot", u"   Regex   ", None))
#if QT_CONFIG(tooltip)
        self.prevMatch.setToolTip(QCoreApplication.translate("Groot", u"Previous match", None))
#endif // QT_CONFIG(tooltip)
        self.prevMatch.setText("")
#if QT_CONFIG(tooltip)
        self.nextMatch.setToolTip(QCoreApplication.translate("Groot", u"Next match", None))
#endif // QT_CONFIG(tooltip)
        self.nextMatch.setText("")
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Groot", u"Notes", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Groot", u"Notebooks", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Groot", u"Uncategorized", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.fileName.setText(QCoreApplication.translate("Groot", u"<html><head/><body><p><span style=\" color:#ffffff;\">No Note Selected</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.boldButton.setToolTip(QCoreApplication.translate("Groot", u"Bold", None))
#endif // QT_CONFIG(tooltip)
        self.boldButton.setText("")
#if QT_CONFIG(tooltip)
        self.italicButton.setToolTip(QCoreApplication.translate("Groot", u"Italic", None))
#endif // QT_CONFIG(tooltip)
        self.italicButton.setText("")
#if QT_CONFIG(tooltip)
        self.numberedList.setToolTip(QCoreApplication.translate("Groot", u"Numbered list", None))
#endif // QT_CONFIG(tooltip)
        self.numberedList.setText("")
#if QT_CONFIG(tooltip)
        self.bullets.setToolTip(QCoreApplication.translate("Groot", u"Bullets", None))
#endif // QT_CONFIG(tooltip)
        self.bullets.setText("")
#if QT_CONFIG(tooltip)
        self.link.setToolTip(QCoreApplication.translate("Groot", u"Insert link", None))
#endif // QT_CONFIG(tooltip)
        self.link.setText("")
#if QT_CONFIG(tooltip)
        self.insertFile.setToolTip(QCoreApplication.translate("Groot", u"Insert image", None))
#endif // QT_CONFIG(tooltip)
        self.insertFile.setText("")
#if QT_CONFIG(tooltip)
        self.code.setToolTip(QCoreApplication.translate("Groot", u"Insert code", None))
#endif // QT_CONFIG(tooltip)
        self.code.setText("")
#if QT_CONFIG(tooltip)
        self.encryptionButton.setToolTip(QCoreApplication.translate("Groot", u"Encrypt note", None))
#endif // QT_CONFIG(tooltip)
        self.encryptionButton.setText("")
#if QT_CONFIG(tooltip)
        self.decryptionButton.setToolTip(QCoreApplication.translate("Groot", u"Decrypt note", None))
#endif // QT_CONFIG(tooltip)
        self.decryptionButton.setText("")
#if QT_CONFIG(tooltip)
        self.permanentDecrypt.setToolTip(QCoreApplication.translate("Groot", u"Permanent decrypt", None))
#endif // QT_CONFIG(tooltip)
        self.permanentDecrypt.setText("")
#if QT_CONFIG(tooltip)
        self.changePasswordButton.setToolTip(QCoreApplication.translate("Groot", u"Change encryption password of this note", None))
#endif // QT_CONFIG(tooltip)
        self.changePasswordButton.setText("")
#if QT_CONFIG(tooltip)
        self.dateTime.setToolTip(QCoreApplication.translate("Groot", u"Date and time", None))
#endif // QT_CONFIG(tooltip)
        self.dateTime.setText("")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Groot", u"Type here....", None))
        self.menuFile.setTitle(QCoreApplication.translate("Groot", u"File", None))
        self.menuImport.setTitle(QCoreApplication.translate("Groot", u"Import", None))
        self.menuExport.setTitle(QCoreApplication.translate("Groot", u"Export", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Groot", u"Edit", None))
        self.menuFormat.setTitle(QCoreApplication.translate("Groot", u"Format", None))
        self.menuEncrption.setTitle(QCoreApplication.translate("Groot", u"Encrption", None))
        self.menuInsert.setTitle(QCoreApplication.translate("Groot", u"Insert", None))
        self.menuView.setTitle(QCoreApplication.translate("Groot", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Groot", u"Help", None))
    # retranslateUi

