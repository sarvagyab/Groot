# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\New Main Window 4 - Adding file Structure.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Groot(object):
    def setupUi(self, Groot):
        Groot.setObjectName("Groot")
        Groot.resize(1018, 552)
        Groot.setStyleSheet("border-bottom-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(Groot)
        self.centralwidget.setStyleSheet("\n"
"background-color: rgb(77, 77, 77);\n"
"background-color: rgb(42, 42, 42);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mainWindow = QtWidgets.QWidget(self.centralwidget)
        self.mainWindow.setObjectName("mainWindow")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.newNote = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newNote.sizePolicy().hasHeightForWidth())
        self.newNote.setSizePolicy(sizePolicy)
        self.newNote.setMinimumSize(QtCore.QSize(0, 0))
        self.newNote.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newNote.setObjectName("newNote")
        self.horizontalLayout_6.addWidget(self.newNote)
        self.newNotebook = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newNotebook.sizePolicy().hasHeightForWidth())
        self.newNotebook.setSizePolicy(sizePolicy)
        self.newNotebook.setMinimumSize(QtCore.QSize(0, 0))
        self.newNotebook.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.newNotebook.setObjectName("newNotebook")
        self.horizontalLayout_6.addWidget(self.newNotebook)
        self.newSubNotebook = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newSubNotebook.sizePolicy().hasHeightForWidth())
        self.newSubNotebook.setSizePolicy(sizePolicy)
        self.newSubNotebook.setMinimumSize(QtCore.QSize(0, 0))
        self.newSubNotebook.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newSubNotebook.setObjectName("newSubNotebook")
        self.horizontalLayout_6.addWidget(self.newSubNotebook)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget)
        self.centralView = QtWidgets.QWidget(self.mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralView.sizePolicy().hasHeightForWidth())
        self.centralView.setSizePolicy(sizePolicy)
        self.centralView.setMinimumSize(QtCore.QSize(0, 0))
        self.centralView.setObjectName("centralView")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralView)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setStyleSheet("background-color:rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);")
        self.treeWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.treeWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.treeWidget.setRootIsDecorated(False)
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
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_1.setFont(0, font)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_5 = QtWidgets.QTreeWidgetItem(item_4)
        item_6 = QtWidgets.QTreeWidgetItem(item_5)
        item_7 = QtWidgets.QTreeWidgetItem(item_6)
        item_8 = QtWidgets.QTreeWidgetItem(item_7)
        item_9 = QtWidgets.QTreeWidgetItem(item_8)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_1.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_1.setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        item_0.setFont(0, font)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setStretchLastSection(True)
        self.horizontalLayout_5.addWidget(self.treeWidget)
        self.editorArea = QtWidgets.QWidget(self.centralView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editorArea.sizePolicy().hasHeightForWidth())
        self.editorArea.setSizePolicy(sizePolicy)
        self.editorArea.setObjectName("editorArea")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.editorArea)
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
        self.titleArea.setStyleSheet("border: 100px ;\n"
"border-bottom-color: rgb(255, 255, 127);")
        self.titleArea.setObjectName("titleArea")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleArea)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileName = QtWidgets.QLabel(self.titleArea)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fileName.setFont(font)
        self.fileName.setStyleSheet("color: rgb(255, 255, 255);")
        self.fileName.setScaledContents(False)
        self.fileName.setAlignment(QtCore.Qt.AlignCenter)
        self.fileName.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.fileName.setObjectName("fileName")
        self.horizontalLayout.addWidget(self.fileName)
        self.verticalLayout_2.addWidget(self.titleArea)
        self.editingButtons = QtWidgets.QWidget(self.editorArea)
        self.editingButtons.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editingButtons.sizePolicy().hasHeightForWidth())
        self.editingButtons.setSizePolicy(sizePolicy)
        self.editingButtons.setObjectName("editingButtons")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.editingButtons)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.editingButtons)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.editingButtons)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.editingButtons)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.link = QtWidgets.QPushButton(self.editingButtons)
        self.link.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.link.setObjectName("link")
        self.horizontalLayout_3.addWidget(self.link)
        self.code = QtWidgets.QPushButton(self.editingButtons)
        self.code.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.code.setObjectName("code")
        self.horizontalLayout_3.addWidget(self.code)
        self.numberedList = QtWidgets.QPushButton(self.editingButtons)
        self.numberedList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numberedList.setObjectName("numberedList")
        self.horizontalLayout_3.addWidget(self.numberedList)
        self.bullets = QtWidgets.QPushButton(self.editingButtons)
        self.bullets.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bullets.setCheckable(False)
        self.bullets.setDefault(False)
        self.bullets.setFlat(False)
        self.bullets.setObjectName("bullets")
        self.horizontalLayout_3.addWidget(self.bullets)
        self.heading = QtWidgets.QPushButton(self.editingButtons)
        self.heading.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.heading.setObjectName("heading")
        self.horizontalLayout_3.addWidget(self.heading)
        self.horizaontalRule = QtWidgets.QPushButton(self.editingButtons)
        self.horizaontalRule.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizaontalRule.setObjectName("horizaontalRule")
        self.horizontalLayout_3.addWidget(self.horizaontalRule)
        self.dateTime = QtWidgets.QPushButton(self.editingButtons)
        self.dateTime.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.dateTime.setObjectName("dateTime")
        self.horizontalLayout_3.addWidget(self.dateTime)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.editingButtons)
        self.editingSection = QtWidgets.QWidget(self.editorArea)
        self.editingSection.setObjectName("editingSection")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.editingSection)
        self.horizontalLayout_2.setContentsMargins(0, 7, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.editingSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit.setLineWidth(1)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.mdViewer = QtWidgets.QTextBrowser(self.editingSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdViewer.sizePolicy().hasHeightForWidth())
        self.mdViewer.setSizePolicy(sizePolicy)
        self.mdViewer.setStyleSheet("color: rgb(255, 255, 255);")
        self.mdViewer.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mdViewer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdViewer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mdViewer.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.mdViewer.setObjectName("mdViewer")
        self.horizontalLayout_2.addWidget(self.mdViewer)
        self.verticalLayout_2.addWidget(self.editingSection)
        self.horizontalLayout_5.addWidget(self.editorArea)
        self.verticalLayout.addWidget(self.centralView)
        self.horizontalLayout_4.addWidget(self.mainWindow)
        Groot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Groot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport = QtWidgets.QMenu(self.menuFile)
        self.menuImport.setObjectName("menuImport")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
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
        self.actionPrint.setObjectName("actionPrint")
        self.actionQuit = QtWidgets.QAction(Groot)
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
        self.actionSearch_in_Current_Note.setObjectName("actionSearch_in_Current_Note")
        self.actionSearch_in_All_Notes = QtWidgets.QAction(Groot)
        self.actionSearch_in_All_Notes.setObjectName("actionSearch_in_All_Notes")
        self.actionOptions = QtWidgets.QAction(Groot)
        self.actionOptions.setObjectName("actionOptions")
        self.actionAbout = QtWidgets.QAction(Groot)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRequest = QtWidgets.QAction(Groot)
        self.actionRequest.setObjectName("actionRequest")
        self.actionDark_Theme = QtWidgets.QAction(Groot)
        self.actionDark_Theme.setObjectName("actionDark_Theme")
        self.actionLight_Theme = QtWidgets.QAction(Groot)
        self.actionLight_Theme.setObjectName("actionLight_Theme")
        self.menuImport.addAction(self.actionMD)
        self.menuExport.addAction(self.actionMD_2)
        self.menuExport.addAction(self.actionHTML)
        self.menuExport.addAction(self.actionPDF)
        self.menuFile.addAction(self.actionNotes_Tree)
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionSearch_in_Current_Note)
        self.menuEdit.addAction(self.actionSearch_in_All_Notes)
        self.menuView.addAction(self.actionDark_Theme)
        self.menuView.addAction(self.actionLight_Theme)
        self.menuTools.addAction(self.actionOptions)
        self.menuHelp.addAction(self.actionAbout)
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
        self.newNotebook.setText(_translate("Groot", "New Notebook"))
        self.newSubNotebook.setText(_translate("Groot", "New sub-notebook"))
        self.lineEdit.setPlaceholderText(_translate("Groot", "Search this note"))
        self.treeWidget.headerItem().setText(0, _translate("Groot", "Notes"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Groot", "Notebooks"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Groot", "asdf"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("Groot", "asdf"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).setText(0, _translate("Groot", "wer"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).child(0).setText(0, _translate("Groot", "ttasdfasdfsadfsadfsadfsa"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).child(0).child(0).setText(0, _translate("Groot", "asdfasdfasgsdaf"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).child(0).child(0).child(0).setText(0, _translate("Groot", "sgdhgasdfas"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).setText(0, _translate("Groot", "wertwegsdf"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).setText(0, _translate("Groot", "kladamcklzjfsa;odf"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).setText(0, _translate("Groot", "awehr;iowej"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Groot", "asdf"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("Groot", "laha"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Groot", "Uncategorized"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.fileName.setText(_translate("Groot", "Testing Name"))
        self.pushButton_5.setText(_translate("Groot", "Bold"))
        self.pushButton_4.setText(_translate("Groot", "Italic"))
        self.pushButton_3.setText(_translate("Groot", "Image"))
        self.link.setText(_translate("Groot", "Link"))
        self.code.setText(_translate("Groot", "Code"))
        self.numberedList.setText(_translate("Groot", "Numbered List"))
        self.bullets.setText(_translate("Groot", "Bullets"))
        self.heading.setText(_translate("Groot", "Heading"))
        self.horizaontalRule.setText(_translate("Groot", "Horizontal Line"))
        self.dateTime.setText(_translate("Groot", "Date and Time"))
        self.textEdit.setPlaceholderText(_translate("Groot", "Type here...."))
        self.menuFile.setTitle(_translate("Groot", "File"))
        self.menuImport.setTitle(_translate("Groot", "Import"))
        self.menuExport.setTitle(_translate("Groot", "Export"))
        self.menuEdit.setTitle(_translate("Groot", "Edit"))
        self.menuView.setTitle(_translate("Groot", "View"))
        self.menuTools.setTitle(_translate("Groot", "Tools"))
        self.menuHelp.setTitle(_translate("Groot", "Help"))
        self.actionNotes_Tree.setText(_translate("Groot", "Notes Tree"))
        self.actionPrint.setText(_translate("Groot", "Print"))
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
