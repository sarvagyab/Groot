# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowPTE.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Groot(object):
    def setupUi(self, Groot):
        Groot.setObjectName("Groot")
        Groot.resize(1602, 795)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Groot.sizePolicy().hasHeightForWidth())
        Groot.setSizePolicy(sizePolicy)
        self.actionNotes_Tree = QAction(Groot)
        self.actionNotes_Tree.setObjectName(u"actionNotes_Tree")
        self.actionPrint = QAction(Groot)
        self.actionPrint.setObjectName(u"actionPrint")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/16x16/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrint.setIcon(icon)
        self.actionQuit = QAction(Groot)
        self.actionQuit.setObjectName(u"actionQuit")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/16x16/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon1)
        self.actionQuit.setShortcutVisibleInContextMenu(True)
        self.actionMD = QAction(Groot)
        self.actionMD.setObjectName(u"actionMD")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/Format Icons/16x16/markdown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMD.setIcon(icon2)
        self.actionMD_2 = QAction(Groot)
        self.actionMD_2.setObjectName(u"actionMD_2")
        self.actionMD_2.setIcon(icon2)
        self.actionHTML = QAction(Groot)
        self.actionHTML.setObjectName(u"actionHTML")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/Format Icons/16x16/html.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHTML.setIcon(icon3)
        self.actionPDF = QAction(Groot)
        self.actionPDF.setObjectName(u"actionPDF")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/Format Icons/16x16/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPDF.setIcon(icon4)
        self.actionSearch_in_Current_Note = QAction(Groot)
        self.actionSearch_in_Current_Note.setObjectName(u"actionSearch_in_Current_Note")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/16x16/find.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSearch_in_Current_Note.setIcon(icon5)
        self.actionSearch_in_All_Notes = QAction(Groot)
        self.actionSearch_in_All_Notes.setObjectName(u"actionSearch_in_All_Notes")
        self.actionOptions = QAction(Groot)
        self.actionOptions.setObjectName(u"actionOptions")
        self.actionAbout = QAction(Groot)
        self.actionAbout.setObjectName(u"actionAbout")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/16x16/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon6)
        self.actionRequest = QAction(Groot)
        self.actionRequest.setObjectName(u"actionRequest")
        self.actionDark_Theme = QAction(Groot)
        self.actionDark_Theme.setObjectName(u"actionDark_Theme")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/16x16/sun_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDark_Theme.setIcon(icon7)
        self.actionLight_Theme = QAction(Groot)
        self.actionLight_Theme.setObjectName(u"actionLight_Theme")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/16x16/sun_light.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLight_Theme.setIcon(icon8)
        self.actionBold = QAction(Groot)
        self.actionBold.setObjectName(u"actionBold")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/16x16/bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBold.setIcon(icon9)
        self.actionBold.setShortcutVisibleInContextMenu(True)
        self.actionItalic = QAction(Groot)
        self.actionItalic.setObjectName(u"actionItalic")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/16x16/italic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionItalic.setIcon(icon10)
        self.actionItalic.setShortcutVisibleInContextMenu(True)
        self.actionUnderline = QAction(Groot)
        self.actionUnderline.setObjectName(u"actionUnderline")
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/16x16/underline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUnderline.setIcon(icon11)
        self.actionNew_note = QAction(Groot)
        self.actionNew_note.setObjectName(u"actionNew_note")
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/16x16/doc_new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_note.setIcon(icon12)
        self.actionNew_note.setShortcutVisibleInContextMenu(True)
        self.actionNew_sub_notebook = QAction(Groot)
        self.actionNew_sub_notebook.setObjectName(u"actionNew_sub_notebook")
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/16x16/subfolder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_sub_notebook.setIcon(icon13)
        self.actionNew_sub_notebook.setShortcutVisibleInContextMenu(True)
        self.actionNew_notebook = QAction(Groot)
        self.actionNew_notebook.setObjectName(u"actionNew_notebook")
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/16x16/folder_plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_notebook.setIcon(icon14)
        self.actionNew_notebook.setShortcutVisibleInContextMenu(True)
        self.actionEncrypt_note = QAction(Groot)
        self.actionEncrypt_note.setObjectName(u"actionEncrypt_note")
        icon15 = QIcon()
        icon15.addFile(u":/icons/Icons/16x16/encrypt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEncrypt_note.setIcon(icon15)
        self.actionDecrypt_note = QAction(Groot)
        self.actionDecrypt_note.setObjectName(u"actionDecrypt_note")
        icon16 = QIcon()
        icon16.addFile(u":/icons/Icons/16x16/decrypt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDecrypt_note.setIcon(icon16)
        self.actionSettings = QAction(Groot)
        self.actionSettings.setObjectName(u"actionSettings")
        icon17 = QIcon()
        icon17.addFile(u":/icons/Icons/16x16/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon17)
        self.actionSettings.setShortcutVisibleInContextMenu(True)
        self.actionSave_note = QAction(Groot)
        self.actionSave_note.setObjectName(u"actionSave_note")
        icon18 = QIcon()
        icon18.addFile(u":/icons/Icons/16x16/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_note.setIcon(icon18)
        self.actionOpen_note = QAction(Groot)
        self.actionOpen_note.setObjectName(u"actionOpen_note")
        self.actionReport_a_bug = QAction(Groot)
        self.actionReport_a_bug.setObjectName(u"actionReport_a_bug")
        icon19 = QIcon()
        icon19.addFile(u":/icons/Icons/16x16/bug.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionReport_a_bug.setIcon(icon19)
        self.actionLink = QAction(Groot)
        self.actionLink.setObjectName(u"actionLink")
        icon20 = QIcon()
        icon20.addFile(u":/icons/Icons/16x16/link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLink.setIcon(icon20)
        self.actionLink.setShortcutVisibleInContextMenu(True)
        self.actionImage = QAction(Groot)
        self.actionImage.setObjectName(u"actionImage")
        icon21 = QIcon()
        icon21.addFile(u":/icons/Icons/16x16/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImage.setIcon(icon21)
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
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mainWindow = QtWidgets.QWidget(self.centralwidget)
        self.mainWindow.setStyleSheet("QWidget{\n"
"    margin:0px;\n"
"    padding:0px;\n"
"}")
        self.mainWindow.setObjectName("mainWindow")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rootOptions = QtWidgets.QWidget(self.mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rootOptions.sizePolicy().hasHeightForWidth())
        self.rootOptions.setSizePolicy(sizePolicy)
        self.rootOptions.setMinimumSize(QtCore.QSize(0, 0))
        self.rootOptions.setStyleSheet("QFrame{\n"
"    border-style:None;\n"
"}")
        self.rootOptions.setObjectName("rootOptions")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.rootOptions)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.buttonFrame = QtWidgets.QFrame(self.rootOptions)
        self.buttonFrame.setStyleSheet("QPushButton{\n"
"    border:None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(211,211,211,0.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border:1px solid blue;\n"
"}")
        self.buttonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.buttonFrame.setObjectName("buttonFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.buttonFrame)
        self.horizontalLayout_12.setContentsMargins(3, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.newNote = QtWidgets.QPushButton(self.buttonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newNote.sizePolicy().hasHeightForWidth())
        self.newNote.setSizePolicy(sizePolicy)
        self.newNote.setMinimumSize(QtCore.QSize(0, 0))
        self.newNote.setStyleSheet("QPushButton{\n"
"    border:None;\n"
"    padding:4px 2px 4px 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(211,211,211,0.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border:1px solid blue;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/doc_new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newNote.setIcon(icon)
        self.newNote.setObjectName("newNote")
        self.horizontalLayout_12.addWidget(self.newNote)
        self.newNotebook = QtWidgets.QPushButton(self.buttonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newNotebook.sizePolicy().hasHeightForWidth())
        self.newNotebook.setSizePolicy(sizePolicy)
        self.newNotebook.setMinimumSize(QtCore.QSize(0, 0))
        self.newNotebook.setStyleSheet("QPushButton{\n"
"    border:None;\n"
"    padding:4px 2px 4px 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(211,211,211,0.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border:1px solid blue;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/folder_plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newNotebook.setIcon(icon1)
        self.newNotebook.setObjectName("newNotebook")
        self.horizontalLayout_12.addWidget(self.newNotebook)
        self.newSubNotebook = QtWidgets.QPushButton(self.buttonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newSubNotebook.sizePolicy().hasHeightForWidth())
        self.newSubNotebook.setSizePolicy(sizePolicy)
        self.newSubNotebook.setMinimumSize(QtCore.QSize(0, 0))
        self.newSubNotebook.setStyleSheet("QPushButton{\n"
"    border:None;\n"
"    padding:4px 2px 4px 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(211,211,211,0.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border:1px solid blue;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/subfolder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newSubNotebook.setIcon(icon2)
        self.newSubNotebook.setObjectName("newSubNotebook")
        self.horizontalLayout_12.addWidget(self.newSubNotebook)
        self.horizontalLayout_6.addWidget(self.buttonFrame)
        self.findFrame = QtWidgets.QFrame(self.rootOptions)
        self.findFrame.setStyleSheet("")
        self.findFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.findFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.findFrame.setObjectName("findFrame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.findFrame)
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame = QtWidgets.QFrame(self.findFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_11.setContentsMargins(3, 0, 3, 3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.searchBar = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setMinimumSize(QtCore.QSize(250, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchBar.setFont(font)
        self.searchBar.setStyleSheet("QLineEdit{\n"
"    border: 1px solid grey;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid black;\n"
"}")
        self.searchBar.setObjectName("searchBar")
        self.horizontalLayout_11.addWidget(self.searchBar)
        self.errorLabel = QtWidgets.QLabel(self.frame)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.horizontalLayout_11.addWidget(self.errorLabel)
        self.wholeWord = QtWidgets.QPushButton(self.frame)
        self.wholeWord.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wholeWord.setStyleSheet("QPushButton{\n"
"    border-style:None;\n"
"    padding:6px 4px 6px 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:rgba(211,211,211,0.4);\n"
"}\n"
"\n"
"QPushButton:!checked:hover{\n"
"    padding-top:1px;\n"
"    padding-left:1px;\n"
"}")
        self.wholeWord.setIconSize(QtCore.QSize(31, 31))
        self.wholeWord.setCheckable(True)
        self.wholeWord.setObjectName("wholeWord")
        self.horizontalLayout_11.addWidget(self.wholeWord)
        self.matchCase = QtWidgets.QPushButton(self.frame)
        self.matchCase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.matchCase.setStyleSheet("QPushButton{\n"
"    border-style:None;\n"
"    padding:6px 4px 6px 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:rgba(211,211,211,0.4);\n"
"}\n"
"\n"
"QPushButton:!checked:hover{\n"
"    padding-top:1px;\n"
"    padding-left:1px;\n"
"}")
        self.matchCase.setIconSize(QtCore.QSize(31, 31))
        self.matchCase.setCheckable(True)
        self.matchCase.setObjectName("matchCase")
        self.horizontalLayout_11.addWidget(self.matchCase)
        self.regexButton = QtWidgets.QPushButton(self.frame)
        self.regexButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.regexButton.setStyleSheet("QPushButton{\n"
"    border-style:None;\n"
"    padding:6px 4px 6px 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:rgba(211,211,211,0.4);\n"
"}\n"
"\n"
"QPushButton:!checked:hover{\n"
"    padding-top:1px;\n"
"    padding-left:1px;\n"
"}s")
        self.regexButton.setIconSize(QtCore.QSize(31, 31))
        self.regexButton.setCheckable(True)
        self.regexButton.setObjectName("regexButton")
        self.horizontalLayout_11.addWidget(self.regexButton)
        self.horizontalLayout_10.addWidget(self.frame)
        self.prevMatch = QtWidgets.QPushButton(self.findFrame)
        self.prevMatch.setStyleSheet("QPushButton{\n"
"    border:None;\n"
"    margin:0px;\n"
"    padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style:solid;\n"
"    border-color:black;\n"
"    background-origin:border-box;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top: 1px;\n"
"    padding-left :1px;\n"
"}")
        self.prevMatch.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/arrow_top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevMatch.setIcon(icon3)
        self.prevMatch.setIconSize(QtCore.QSize(20, 20))
        self.prevMatch.setObjectName("prevMatch")
        self.horizontalLayout_10.addWidget(self.prevMatch)
        self.nextMatch = QtWidgets.QPushButton(self.findFrame)
        self.nextMatch.setStyleSheet("QPushButton{\n"
"    border:None;\n"
"    margin:0px;\n"
"    padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style:solid;\n"
"    border-color:black;\n"
"    background-origin:border-box;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top: 1px;\n"
"    padding-left :1px;\n"
"}")
        self.nextMatch.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/arrow_bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextMatch.setIcon(icon4)
        self.nextMatch.setIconSize(QtCore.QSize(20, 20))
        self.nextMatch.setObjectName("nextMatch")
        self.horizontalLayout_10.addWidget(self.nextMatch)
        self.horizontalLayout_6.addWidget(self.findFrame)
        spacerItem = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addWidget(self.rootOptions)
        self.centralView = QtWidgets.QWidget(self.mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralView.sizePolicy().hasHeightForWidth())
        self.centralView.setSizePolicy(sizePolicy)
        self.centralView.setMinimumSize(QtCore.QSize(0, 0))
        self.centralView.setStyleSheet("QWidget{\n"
"    margin:0px;\n"
"    padding:0px;\n"
"}")
        self.centralView.setObjectName("centralView")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralView)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralView)
        self.treeWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setStyleSheet("QTreeView {\n"
"    background-color:black;\n"
"    color:white;\n"
"    alternate-background-color:gray;\n"
"}\n"
"\n"
"")
        self.treeWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        item_0.setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        item_0.setFont(0, font)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setStretchLastSection(False)
        self.horizontalLayout_5.addWidget(self.treeWidget)
        self.editorArea = QtWidgets.QWidget(self.centralView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editorArea.sizePolicy().hasHeightForWidth())
        self.editorArea.setSizePolicy(sizePolicy)
        self.editorArea.setStyleSheet("QWidget{\n"
"    background-color:white;\n"
"    margin:0px;\n"
"    padding:0px;\n"
"}\n"
"")
        self.editorArea.setObjectName("editorArea")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.editorArea)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleArea = QtWidgets.QWidget(self.editorArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleArea.sizePolicy().hasHeightForWidth())
        self.titleArea.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(3)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.titleArea.setFont(font)
        self.titleArea.setStyleSheet("padding:0px;\n"
"margin :0px;\n"
"background-color:grey;")
        self.titleArea.setObjectName("titleArea")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleArea)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileName = QtWidgets.QLabel(self.titleArea)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fileName.setFont(font)
        self.fileName.setStyleSheet("")
        self.fileName.setScaledContents(False)
        self.fileName.setAlignment(QtCore.Qt.AlignCenter)
        self.fileName.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.fileName.setObjectName("fileName")
        self.horizontalLayout.addWidget(self.fileName)
        self.verticalLayout_2.addWidget(self.titleArea)
        self.editingButtons = QtWidgets.QWidget(self.editorArea)
        self.editingButtons.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editingButtons.sizePolicy().hasHeightForWidth())
        self.editingButtons.setSizePolicy(sizePolicy)
        self.editingButtons.setMouseTracking(False)
        self.editingButtons.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.editingButtons.setAutoFillBackground(False)
        self.editingButtons.setStyleSheet("QFrame{\n"
"    border-right:2px solid gray;\n"
"    padding:0px;\n"
"    margin:0px;\n"
"    background-color:white;    \n"
"}\n"
"\n"
"QPushButton{\n"
"    border-style:None;\n"
"    padding:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style:solid;\n"
"    border-color:black;\n"
"    background-origin:border-box;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top: 1px;\n"
"    padding-left :1px;\n"
"}")
        self.editingButtons.setObjectName("editingButtons")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.editingButtons)
        self.horizontalLayout_3.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formatFrame = QtWidgets.QFrame(self.editingButtons)
        self.formatFrame.setStyleSheet("QPushButton{\n"
"    margin:0px;\n"
"    padding:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style:solid;\n"
"    border-color:black;\n"
"    background-origin:border-box;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top: 1px;\n"
"    padding-left :1px;\n"
"}")
        self.formatFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.formatFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.formatFrame.setObjectName("formatFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.formatFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.boldButton = QtWidgets.QPushButton(self.formatFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boldButton.sizePolicy().hasHeightForWidth())
        self.boldButton.setSizePolicy(sizePolicy)
        self.boldButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boldButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.boldButton.setStyleSheet("")
        self.boldButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/font_bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boldButton.setIcon(icon5)
        self.boldButton.setIconSize(QtCore.QSize(32, 32))
        self.boldButton.setAutoExclusive(False)
        self.boldButton.setObjectName("boldButton")
        self.horizontalLayout_7.addWidget(self.boldButton)
        self.italicButton = QtWidgets.QPushButton(self.formatFrame)
        self.italicButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.italicButton.setStyleSheet("")
        self.italicButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/font_italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italicButton.setIcon(icon6)
        self.italicButton.setIconSize(QtCore.QSize(32, 32))
        self.italicButton.setObjectName("italicButton")
        self.horizontalLayout_7.addWidget(self.italicButton)
        self.numberedList = QtWidgets.QPushButton(self.formatFrame)
        self.numberedList.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.numberedList.setStyleSheet("")
        self.numberedList.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/numbered_list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.numberedList.setIcon(icon7)
        self.numberedList.setIconSize(QtCore.QSize(32, 32))
        self.numberedList.setObjectName("numberedList")
        self.horizontalLayout_7.addWidget(self.numberedList)
        self.bullets = QtWidgets.QPushButton(self.formatFrame)
        self.bullets.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bullets.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bullets.setStyleSheet("")
        self.bullets.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/bullets.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bullets.setIcon(icon8)
        self.bullets.setIconSize(QtCore.QSize(32, 32))
        self.bullets.setCheckable(False)
        self.bullets.setDefault(False)
        self.bullets.setFlat(False)
        self.bullets.setObjectName("bullets")
        self.horizontalLayout_7.addWidget(self.bullets)
        self.horizontalLayout_3.addWidget(self.formatFrame)
        self.insertFrame = QtWidgets.QFrame(self.editingButtons)
        self.insertFrame.setStyleSheet("QPushButton{\n"
"    margin:0px;\n"
"    padding:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style:solid;\n"
"    border-color:black;\n"
"    background-origin:border-box;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top: 1px;\n"
"    padding-left :1px;\n"
"}")
        self.insertFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.insertFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.insertFrame.setObjectName("insertFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.insertFrame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.link = QtWidgets.QPushButton(self.insertFrame)
        self.link.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.link.setStyleSheet("")
        self.link.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.link.setIcon(icon9)
        self.link.setIconSize(QtCore.QSize(32, 32))
        self.link.setObjectName("link")
        self.horizontalLayout_8.addWidget(self.link)
        self.insertFile = QtWidgets.QPushButton(self.insertFrame)
        self.insertFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.insertFile.setStyleSheet("")
        self.insertFile.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insertFile.setIcon(icon10)
        self.insertFile.setIconSize(QtCore.QSize(32, 32))
        self.insertFile.setObjectName("insertFile")
        self.horizontalLayout_8.addWidget(self.insertFile)
        self.code = QtWidgets.QPushButton(self.insertFrame)
        self.code.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.code.setStyleSheet("")
        self.code.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/brackets.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.code.setIcon(icon11)
        self.code.setIconSize(QtCore.QSize(32, 32))
        self.code.setObjectName("code")
        self.horizontalLayout_8.addWidget(self.code)
        self.horizontalLayout_3.addWidget(self.insertFrame)
        self.encryptionFrame = QtWidgets.QFrame(self.editingButtons)
        self.encryptionFrame.setStyleSheet("QPushButton{\n"
"    margin:0px;\n"
"    padding:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style:solid;\n"
"    border-color:black;\n"
"    background-origin:border-box;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top: 1px;\n"
"    padding-left :1px;\n"
"}")
        self.encryptionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.encryptionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.encryptionFrame.setLineWidth(1)
        self.encryptionFrame.setObjectName("encryptionFrame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.encryptionFrame)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.encryptionButton = QtWidgets.QPushButton(self.encryptionFrame)
        self.encryptionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.encryptionButton.setStyleSheet("")
        self.encryptionButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/encrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encryptionButton.setIcon(icon12)
        self.encryptionButton.setIconSize(QtCore.QSize(32, 32))
        self.encryptionButton.setCheckable(True)
        self.encryptionButton.setChecked(False)
        self.encryptionButton.setObjectName("encryptionButton")
        self.horizontalLayout_9.addWidget(self.encryptionButton)
        self.decryptionButton = QtWidgets.QPushButton(self.encryptionFrame)
        self.decryptionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decryptionButton.setStyleSheet("")
        self.decryptionButton.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/decrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.decryptionButton.setIcon(icon13)
        self.decryptionButton.setIconSize(QtCore.QSize(32, 32))
        self.decryptionButton.setObjectName("decryptionButton")
        self.horizontalLayout_9.addWidget(self.decryptionButton)
        self.permanentDecrypt = QtWidgets.QPushButton(self.encryptionFrame)
        self.permanentDecrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.permanentDecrypt.setStyleSheet("image: url(:/icons/Icons/16x16/encrypt_20.png);\n"
"")
        self.permanentDecrypt.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.permanentDecrypt.setIcon(icon14)
        self.permanentDecrypt.setIconSize(QtCore.QSize(32, 32))
        self.permanentDecrypt.setObjectName("permanentDecrypt")
        self.horizontalLayout_9.addWidget(self.permanentDecrypt)
        self.changePasswordButton = QtWidgets.QPushButton(self.encryptionFrame)
        self.changePasswordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changePasswordButton.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changePasswordButton.setIcon(icon15)
        self.changePasswordButton.setIconSize(QtCore.QSize(32, 32))
        self.changePasswordButton.setObjectName("changePasswordButton")
        self.horizontalLayout_9.addWidget(self.changePasswordButton)
        self.horizontalLayout_3.addWidget(self.encryptionFrame)
        self.dateTime = QtWidgets.QPushButton(self.editingButtons)
        self.dateTime.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateTime.setStyleSheet("")
        self.dateTime.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dateTime.setIcon(icon16)
        self.dateTime.setIconSize(QtCore.QSize(32, 32))
        self.dateTime.setObjectName("dateTime")
        self.horizontalLayout_3.addWidget(self.dateTime)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.editingButtons)
        self.editingSection = QtWidgets.QWidget(self.editorArea)
        self.editingSection.setStyleSheet("")
        self.editingSection.setObjectName("editingSection")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.editingSection)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.editingSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit{\n"
"    background-color: white;\n"
"    border-top:1px solid black;\n"
"    border-right:1px solid black;\n"
"    selection-background-color:rgba(243, 255, 77,0.4);\n"
"    selection-color:    darkblue;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Panel)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit.setLineWidth(1)
        self.plainTextEdit.setMidLineWidth(0)
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setCenterOnScroll(False)

        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        self.mdViewer = QtWidgets.QTextBrowser(self.editingSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdViewer.sizePolicy().hasHeightForWidth())
        self.mdViewer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.mdViewer.setFont(font)
        self.mdViewer.setStyleSheet("QTextBrowser{\n"
"    border-top:1px solid black;\n"
"    background-color: white;\n"
"    selection-background-color:rgba(243, 255, 77,0.4);\n"
"    selection-color:darkblue;\n"
"}\n"
"")
        self.mdViewer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mdViewer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mdViewer.setLineWidth(1)
        self.mdViewer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdViewer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdViewer.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.mdViewer.setOpenLinks(False)
        self.mdViewer.setObjectName("mdViewer")
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
        icon36 = QIcon()
        icon36.addFile(u":/icons/Icons/16x16/doc_import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuImport.setIcon(icon36)
        self.menuExport = QMenu(self.menuFile)
        self.menuExport.setObjectName(u"menuExport")
        icon37 = QIcon()
        icon37.addFile(u":/icons/Icons/16x16/doc_export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuExport.setIcon(icon37)
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuFormat = QMenu(self.menuEdit)
        self.menuFormat.setObjectName(u"menuFormat")
        icon38 = QIcon()
        icon38.addFile(u":/icons/Icons/16x16/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuFormat.setIcon(icon38)
        self.menuEncrption = QMenu(self.menuEdit)
        self.menuEncrption.setObjectName(u"menuEncrption")
        self.menuEncrption.setIcon(icon15)
        self.menuInsert = QMenu(self.menuEdit)
        self.menuInsert.setObjectName(u"menuInsert")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
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
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Groot)
        QtCore.QMetaObject.connectSlotsByName(Groot)

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
        self.treeWidget.topLevelItem(0).setText(0, _translate("Groot", "Notebooks"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Groot", "Uncategorized"))
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

