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
        self.centralwidget = QtWidgets.QWidget(Groot)
        self.centralwidget.setStyleSheet("background-color:rgb(252, 252, 252);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
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
        self.editingButtons.setObjectName("editingButtons")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.editingButtons)
        self.horizontalLayout_3.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formatFrame = QtWidgets.QFrame(self.editingButtons)
        self.formatFrame.setStyleSheet("QPushButton{\n"
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
        self.pushButton_3 = QtWidgets.QPushButton(self.insertFrame)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon10)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_8.addWidget(self.pushButton_3)
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
        self.horizontalLayout_3.addWidget(self.encryptionFrame)
        self.dateTime = QtWidgets.QPushButton(self.editingButtons)
        self.dateTime.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateTime.setStyleSheet("")
        self.dateTime.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/Icons/32x32/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dateTime.setIcon(icon14)
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
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setCenterOnScroll(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
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
        self.mdViewer.setObjectName("mdViewer")
        self.horizontalLayout_2.addWidget(self.mdViewer)
        self.verticalLayout_2.addWidget(self.editingSection)
        self.horizontalLayout_5.addWidget(self.editorArea)
        self.verticalLayout.addWidget(self.centralView)
        self.horizontalLayout_4.addWidget(self.mainWindow)
        Groot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Groot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1602, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport = QtWidgets.QMenu(self.menuFile)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/doc_import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuImport.setIcon(icon15)
        self.menuImport.setObjectName("menuImport")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/doc_export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuExport.setIcon(icon16)
        self.menuExport.setObjectName("menuExport")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFormat = QtWidgets.QMenu(self.menuEdit)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuFormat.setIcon(icon17)
        self.menuFormat.setObjectName("menuFormat")
        self.menuEncrption = QtWidgets.QMenu(self.menuEdit)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/encrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuEncrption.setIcon(icon18)
        self.menuEncrption.setObjectName("menuEncrption")
        self.menuInsert = QtWidgets.QMenu(self.menuEdit)
        self.menuInsert.setObjectName("menuInsert")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Groot.setMenuBar(self.menubar)
        self.actionNotes_Tree = QtWidgets.QAction(Groot)
        self.actionNotes_Tree.setObjectName("actionNotes_Tree")
        self.actionPrint = QtWidgets.QAction(Groot)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon19)
        self.actionPrint.setObjectName("actionPrint")
        self.actionQuit = QtWidgets.QAction(Groot)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon20)
        self.actionQuit.setObjectName("actionQuit")
        self.actionMD = QtWidgets.QAction(Groot)
        self.actionMD.setObjectName("actionMD")
        self.actionMD_2 = QtWidgets.QAction(Groot)
        self.actionMD_2.setObjectName("actionMD_2")
        self.actionHTML = QtWidgets.QAction(Groot)
        self.actionHTML.setObjectName("actionHTML")
        self.actionPDF = QtWidgets.QAction(Groot)
        self.actionPDF.setObjectName("actionPDF")
        self.actionSearch_in_Current_Note = QtWidgets.QAction(Groot)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch_in_Current_Note.setIcon(icon21)
        self.actionSearch_in_Current_Note.setObjectName("actionSearch_in_Current_Note")
        self.actionSearch_in_All_Notes = QtWidgets.QAction(Groot)
        self.actionSearch_in_All_Notes.setObjectName("actionSearch_in_All_Notes")
        self.actionOptions = QtWidgets.QAction(Groot)
        self.actionOptions.setObjectName("actionOptions")
        self.actionAbout = QtWidgets.QAction(Groot)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon22)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRequest = QtWidgets.QAction(Groot)
        self.actionRequest.setObjectName("actionRequest")
        self.actionDark_Theme = QtWidgets.QAction(Groot)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/sun_dark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDark_Theme.setIcon(icon23)
        self.actionDark_Theme.setObjectName("actionDark_Theme")
        self.actionLight_Theme = QtWidgets.QAction(Groot)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/sun_light.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLight_Theme.setIcon(icon24)
        self.actionLight_Theme.setObjectName("actionLight_Theme")
        self.actionBold = QtWidgets.QAction(Groot)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon25)
        self.actionBold.setShortcutVisibleInContextMenu(True)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtWidgets.QAction(Groot)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon26)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtWidgets.QAction(Groot)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnderline.setIcon(icon27)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionNew_note = QtWidgets.QAction(Groot)
        self.actionNew_note.setIcon(icon)
        self.actionNew_note.setObjectName("actionNew_note")
        self.actionNew_sub_notebook = QtWidgets.QAction(Groot)
        self.actionNew_sub_notebook.setIcon(icon2)
        self.actionNew_sub_notebook.setObjectName("actionNew_sub_notebook")
        self.actionNew_notebook = QtWidgets.QAction(Groot)
        self.actionNew_notebook.setIcon(icon1)
        self.actionNew_notebook.setObjectName("actionNew_notebook")
        self.actionEncrypt_note = QtWidgets.QAction(Groot)
        self.actionEncrypt_note.setIcon(icon18)
        self.actionEncrypt_note.setObjectName("actionEncrypt_note")
        self.actionDecrypt_note = QtWidgets.QAction(Groot)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/decrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDecrypt_note.setIcon(icon28)
        self.actionDecrypt_note.setObjectName("actionDecrypt_note")
        self.actionSettings = QtWidgets.QAction(Groot)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon29)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSave_note = QtWidgets.QAction(Groot)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_note.setIcon(icon30)
        self.actionSave_note.setObjectName("actionSave_note")
        self.actionOpen_note = QtWidgets.QAction(Groot)
        self.actionOpen_note.setObjectName("actionOpen_note")
        self.actionReport_a_bug = QtWidgets.QAction(Groot)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReport_a_bug.setIcon(icon31)
        self.actionReport_a_bug.setObjectName("actionReport_a_bug")
        self.actionLink = QtWidgets.QAction(Groot)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLink.setIcon(icon32)
        self.actionLink.setObjectName("actionLink")
        self.actionImage = QtWidgets.QAction(Groot)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/icons/Icons/16x16/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImage.setIcon(icon33)
        self.actionImage.setObjectName("actionImage")
        self.menuImport.addAction(self.actionMD)
        self.menuExport.addAction(self.actionMD_2)
        self.menuExport.addAction(self.actionHTML)
        self.menuExport.addAction(self.actionPDF)
        self.menuFile.addAction(self.actionNew_note)
        self.menuFile.addAction(self.actionNew_sub_notebook)
        self.menuFile.addAction(self.actionNew_notebook)
        self.menuFile.addAction(self.actionSave_note)
        self.menuFile.addAction(self.actionNotes_Tree)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuFormat.addAction(self.actionBold)
        self.menuFormat.addAction(self.actionItalic)
        self.menuFormat.addAction(self.actionUnderline)
        self.menuEncrption.addAction(self.actionEncrypt_note)
        self.menuEncrption.addAction(self.actionDecrypt_note)
        self.menuInsert.addAction(self.actionLink)
        self.menuInsert.addAction(self.actionImage)
        self.menuEdit.addAction(self.actionSearch_in_Current_Note)
        self.menuEdit.addAction(self.actionSearch_in_All_Notes)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuInsert.menuAction())
        self.menuEdit.addAction(self.menuFormat.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuEncrption.menuAction())
        self.menuView.addAction(self.actionDark_Theme)
        self.menuView.addAction(self.actionLight_Theme)
        self.menuTools.addAction(self.actionOptions)
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
        _translate = QtCore.QCoreApplication.translate
        Groot.setWindowTitle(_translate("Groot", "Groot"))
        self.newNote.setText(_translate("Groot", "New Note"))
        self.newNotebook.setText(_translate("Groot", "New notebook"))
        self.newSubNotebook.setText(_translate("Groot", "New sub-notebook"))
        self.searchBar.setPlaceholderText(_translate("Groot", "Search in this note"))
        self.wholeWord.setText(_translate("Groot", "Whole word"))
        self.matchCase.setToolTip(_translate("Groot", "Case sensitive"))
        self.matchCase.setText(_translate("Groot", "Match Case"))
        self.regexButton.setText(_translate("Groot", "   Regex   "))
        self.prevMatch.setToolTip(_translate("Groot", "Previous match"))
        self.nextMatch.setToolTip(_translate("Groot", "Next match"))
        self.treeWidget.headerItem().setText(0, _translate("Groot", "Notes"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Groot", "Notebooks"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Groot", "Uncategorized"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.fileName.setText(_translate("Groot", "<html><head/><body><p><span style=\" color:#ffffff;\">Testing Name</span></p></body></html>"))
        self.boldButton.setToolTip(_translate("Groot", "Bold"))
        self.italicButton.setToolTip(_translate("Groot", "Italic"))
        self.numberedList.setToolTip(_translate("Groot", "Numbered list"))
        self.bullets.setToolTip(_translate("Groot", "Bullets"))
        self.link.setToolTip(_translate("Groot", "Insert link"))
        self.pushButton_3.setToolTip(_translate("Groot", "Insert image"))
        self.code.setToolTip(_translate("Groot", "Insert code"))
        self.encryptionButton.setToolTip(_translate("Groot", "Encrypt note"))
        self.decryptionButton.setToolTip(_translate("Groot", "Decrypt note"))
        self.dateTime.setToolTip(_translate("Groot", "Date and time"))
        self.plainTextEdit.setPlaceholderText(_translate("Groot", "Type here...."))
        self.menuFile.setTitle(_translate("Groot", "File"))
        self.menuImport.setTitle(_translate("Groot", "Import"))
        self.menuExport.setTitle(_translate("Groot", "Export"))
        self.menuEdit.setTitle(_translate("Groot", "Edit"))
        self.menuFormat.setTitle(_translate("Groot", "Format"))
        self.menuEncrption.setTitle(_translate("Groot", "Encrption"))
        self.menuInsert.setTitle(_translate("Groot", "Insert"))
        self.menuView.setTitle(_translate("Groot", "View"))
        self.menuTools.setTitle(_translate("Groot", "Tools"))
        self.menuHelp.setTitle(_translate("Groot", "Help"))
        self.actionNotes_Tree.setText(_translate("Groot", "Notes Tree"))
        self.actionPrint.setText(_translate("Groot", "Print"))
        self.actionPrint.setShortcut(_translate("Groot", "Ctrl+P"))
        self.actionQuit.setText(_translate("Groot", "Quit"))
        self.actionMD.setText(_translate("Groot", "MD"))
        self.actionMD_2.setText(_translate("Groot", "MD"))
        self.actionHTML.setText(_translate("Groot", "HTML"))
        self.actionPDF.setText(_translate("Groot", "PDF"))
        self.actionSearch_in_Current_Note.setText(_translate("Groot", "Search in Current Note"))
        self.actionSearch_in_All_Notes.setText(_translate("Groot", "Search in All Notes"))
        self.actionOptions.setText(_translate("Groot", "Options"))
        self.actionAbout.setText(_translate("Groot", "About"))
        self.actionRequest.setText(_translate("Groot", "Request"))
        self.actionDark_Theme.setText(_translate("Groot", "Dark Theme"))
        self.actionLight_Theme.setText(_translate("Groot", "Light Theme"))
        self.actionBold.setText(_translate("Groot", "Bold"))
        self.actionBold.setShortcut(_translate("Groot", "Ctrl+B"))
        self.actionItalic.setText(_translate("Groot", "Italic"))
        self.actionItalic.setShortcut(_translate("Groot", "Ctrl+I"))
        self.actionUnderline.setText(_translate("Groot", "Underline"))
        self.actionUnderline.setShortcut(_translate("Groot", "Ctrl+U"))
        self.actionNew_note.setText(_translate("Groot", "New note"))
        self.actionNew_note.setShortcut(_translate("Groot", "Ctrl+N"))
        self.actionNew_sub_notebook.setText(_translate("Groot", "New sub-notebook"))
        self.actionNew_notebook.setText(_translate("Groot", "New notebook"))
        self.actionEncrypt_note.setText(_translate("Groot", "Encrypt note"))
        self.actionDecrypt_note.setText(_translate("Groot", "Decrypt note"))
        self.actionSettings.setText(_translate("Groot", "Settings"))
        self.actionSave_note.setText(_translate("Groot", "Save note"))
        self.actionSave_note.setShortcut(_translate("Groot", "Ctrl+S"))
        self.actionOpen_note.setText(_translate("Groot", "Open note"))
        self.actionReport_a_bug.setText(_translate("Groot", "Report a bug"))
        self.actionLink.setText(_translate("Groot", "Link"))
        self.actionImage.setText(_translate("Groot", "Image"))
import resource_rc
