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


class Ui_Groot(object):
    def setupUi(self, Groot):
        if not Groot.objectName():
            Groot.setObjectName(u"Groot")
        Groot.resize(1207, 552)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Groot.sizePolicy().hasHeightForWidth())
        Groot.setSizePolicy(sizePolicy)
        Groot.setStyleSheet(u"background-color: rgba(252, 252, 252, 252);")
        self.actionNotes_Tree = QAction(Groot)
        self.actionNotes_Tree.setObjectName(u"actionNotes_Tree")
        self.actionPrint = QAction(Groot)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionQuit = QAction(Groot)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionMD = QAction(Groot)
        self.actionMD.setObjectName(u"actionMD")
        self.actionMD_2 = QAction(Groot)
        self.actionMD_2.setObjectName(u"actionMD_2")
        self.actionHTML = QAction(Groot)
        self.actionHTML.setObjectName(u"actionHTML")
        self.actionPDF = QAction(Groot)
        self.actionPDF.setObjectName(u"actionPDF")
        self.actionSearch_in_Current_Note = QAction(Groot)
        self.actionSearch_in_Current_Note.setObjectName(u"actionSearch_in_Current_Note")
        self.actionSearch_in_All_Notes = QAction(Groot)
        self.actionSearch_in_All_Notes.setObjectName(u"actionSearch_in_All_Notes")
        self.actionOptions = QAction(Groot)
        self.actionOptions.setObjectName(u"actionOptions")
        self.actionAbout = QAction(Groot)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionRequest = QAction(Groot)
        self.actionRequest.setObjectName(u"actionRequest")
        self.actionDark_Theme = QAction(Groot)
        self.actionDark_Theme.setObjectName(u"actionDark_Theme")
        self.actionLight_Theme = QAction(Groot)
        self.actionLight_Theme.setObjectName(u"actionLight_Theme")
        self.centralwidget = QWidget(Groot)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(252, 252, 252);")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.mainWindow = QWidget(self.centralwidget)
        self.mainWindow.setObjectName(u"mainWindow")
        self.verticalLayout = QVBoxLayout(self.mainWindow)
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
        self.horizontalLayout_6 = QHBoxLayout(self.rootOptions)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.newNote = QPushButton(self.rootOptions)
        self.newNote.setObjectName(u"newNote")
        sizePolicy1.setHeightForWidth(self.newNote.sizePolicy().hasHeightForWidth())
        self.newNote.setSizePolicy(sizePolicy1)
        self.newNote.setMinimumSize(QSize(0, 0))
        self.newNote.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.newNote)

        self.newNotebook = QPushButton(self.rootOptions)
        self.newNotebook.setObjectName(u"newNotebook")
        sizePolicy1.setHeightForWidth(self.newNotebook.sizePolicy().hasHeightForWidth())
        self.newNotebook.setSizePolicy(sizePolicy1)
        self.newNotebook.setMinimumSize(QSize(0, 0))
        self.newNotebook.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.newNotebook)

        self.newSubNotebook = QPushButton(self.rootOptions)
        self.newSubNotebook.setObjectName(u"newSubNotebook")
        sizePolicy1.setHeightForWidth(self.newSubNotebook.sizePolicy().hasHeightForWidth())
        self.newSubNotebook.setSizePolicy(sizePolicy1)
        self.newSubNotebook.setMinimumSize(QSize(0, 0))
        self.newSubNotebook.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.newSubNotebook)

        self.lineEdit = QLineEdit(self.rootOptions)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(250, 28))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.emptySpaceMainOptions = QSpacerItem(800, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.emptySpaceMainOptions)


        self.verticalLayout.addWidget(self.rootOptions)

        self.centralView = QWidget(self.mainWindow)
        self.centralView.setObjectName(u"centralView")
        sizePolicy.setHeightForWidth(self.centralView.sizePolicy().hasHeightForWidth())
        self.centralView.setSizePolicy(sizePolicy)
        self.centralView.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.centralView)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.treeWidget = QTreeWidget(self.centralView)
        font1 = QFont()
        font1.setPointSize(12)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem.setFont(0, font1);
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1.setFont(0, font1);
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy2)
        self.treeWidget.setMinimumSize(QSize(200, 0))
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setStyleSheet(u"background-color:rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
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
        self.verticalLayout_2 = QVBoxLayout(self.editorArea)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleArea = QWidget(self.editorArea)
        self.titleArea.setObjectName(u"titleArea")
        sizePolicy1.setHeightForWidth(self.titleArea.sizePolicy().hasHeightForWidth())
        self.titleArea.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(3)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        font2.setKerning(True)
        self.titleArea.setFont(font2)
        self.titleArea.setStyleSheet(u"border: 100px ;\n"
"border-bottom-color: rgb(255, 255, 127);")
        self.horizontalLayout = QHBoxLayout(self.titleArea)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fileName = QLabel(self.titleArea)
        self.fileName.setObjectName(u"fileName")
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(12)
        self.fileName.setFont(font3)
        self.fileName.setStyleSheet(u"")
        self.fileName.setScaledContents(False)
        self.fileName.setAlignment(Qt.AlignCenter)
        self.fileName.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.fileName)


        self.verticalLayout_2.addWidget(self.titleArea)

        self.editingButtons = QWidget(self.editorArea)
        self.editingButtons.setObjectName(u"editingButtons")
        self.editingButtons.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.editingButtons.sizePolicy().hasHeightForWidth())
        self.editingButtons.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.editingButtons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                
        self.boldButton = QPushButton(self.editingButtons)
        self.boldButton.setObjectName(u"boldButton")
        self.boldButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.boldButton)

        self.italicButton = QPushButton(self.editingButtons)
        self.italicButton.setObjectName(u"italicButton")
        self.italicButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.italicButton)

        self.imageButton = QPushButton(self.editingButtons)
        self.imageButton.setObjectName(u"imageButton")
        self.imageButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.imageButton)

        self.link = QPushButton(self.editingButtons)
        self.link.setObjectName(u"link")
        self.link.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.link)

        self.code = QPushButton(self.editingButtons)
        self.code.setObjectName(u"code")
        self.code.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.code)

        self.numberedList = QPushButton(self.editingButtons)
        self.numberedList.setObjectName(u"numberedList")
        self.numberedList.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.numberedList)

        self.bullets = QPushButton(self.editingButtons)
        self.bullets.setObjectName(u"bullets")
        self.bullets.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.bullets.setCheckable(False)
        self.bullets.setFlat(False)

        self.horizontalLayout_3.addWidget(self.bullets)

        self.heading = QPushButton(self.editingButtons)
        self.heading.setObjectName(u"heading")
        self.heading.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.heading)

        self.horizaontalRule = QPushButton(self.editingButtons)
        self.horizaontalRule.setObjectName(u"horizaontalRule")
        self.horizaontalRule.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.horizaontalRule)

        self.dateTime = QPushButton(self.editingButtons)
        self.dateTime.setObjectName(u"dateTime")
        self.dateTime.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_3.addWidget(self.dateTime)

        #Encryption Button
        self.encryptionButton = QPushButton(self.editingButtons)
        self.encryptionButton.setObjectName(u"encryptionButton")
        self.encryptionButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_3.addWidget(self.encryptionButton)
        
        #Decryption Button
        self.decryptionButton = QPushButton(self.editingButtons)
        self.decryptionButton.setObjectName(u"encryptionButton")
        self.decryptionButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_3.addWidget(self.decryptionButton)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.editingButtons)

        self.editingSection = QWidget(self.editorArea)
        self.editingSection.setObjectName(u"editingSection")
        self.horizontalLayout_2 = QHBoxLayout(self.editingSection)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 7, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.editingSection)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(17)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.plainTextEdit.setFont(font4)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(248, 248, 248);\n"
"border-color: rgba(252, 252, 252, 252);\n"
"\n"
"border-width:0px\n"
"")
        self.plainTextEdit.setFrameShape(QFrame.Panel)
        self.plainTextEdit.setFrameShadow(QFrame.Raised)
        self.plainTextEdit.setLineWidth(1)
        self.plainTextEdit.setMidLineWidth(0)
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.horizontalLayout_2.addWidget(self.plainTextEdit)

        self.mdViewer = QTextBrowser(self.editingSection)
        self.mdViewer.setObjectName(u"mdViewer")
        sizePolicy.setHeightForWidth(self.mdViewer.sizePolicy().hasHeightForWidth())
        self.mdViewer.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(17)
        self.mdViewer.setFont(font5)
        self.mdViewer.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.mdViewer.setFrameShape(QFrame.NoFrame)
        self.mdViewer.setFrameShadow(QFrame.Plain)
        self.mdViewer.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdViewer.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdViewer.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.mdViewer)


        self.verticalLayout_2.addWidget(self.editingSection)


        self.horizontalLayout_5.addWidget(self.editorArea)


        self.verticalLayout.addWidget(self.centralView)


        self.horizontalLayout_4.addWidget(self.mainWindow)

        Groot.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Groot)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1207, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuImport = QMenu(self.menuFile)
        self.menuImport.setObjectName(u"menuImport")
        self.menuExport = QMenu(self.menuFile)
        self.menuExport.setObjectName(u"menuExport")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Groot.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNotes_Tree)
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionQuit)
        self.menuImport.addAction(self.actionMD)
        self.menuExport.addAction(self.actionMD_2)
        self.menuExport.addAction(self.actionHTML)
        self.menuExport.addAction(self.actionPDF)
        self.menuEdit.addAction(self.actionSearch_in_Current_Note)
        self.menuEdit.addAction(self.actionSearch_in_All_Notes)
        self.menuView.addAction(self.actionDark_Theme)
        self.menuView.addAction(self.actionLight_Theme)
        self.menuTools.addAction(self.actionOptions)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionRequest)

        self.retranslateUi(Groot)

        self.bullets.setDefault(False)


        QMetaObject.connectSlotsByName(Groot)
    # setupUi

    def retranslateUi(self, Groot):
        Groot.setWindowTitle(QCoreApplication.translate("Groot", u"Groot", None))
        self.actionNotes_Tree.setText(QCoreApplication.translate("Groot", u"Notes Tree", None))
        self.actionPrint.setText(QCoreApplication.translate("Groot", u"Print", None))
        self.actionQuit.setText(QCoreApplication.translate("Groot", u"Quit", None))
        self.actionMD.setText(QCoreApplication.translate("Groot", u"MD", None))
        self.actionMD_2.setText(QCoreApplication.translate("Groot", u"MD", None))
        self.actionHTML.setText(QCoreApplication.translate("Groot", u"HTML", None))
        self.actionPDF.setText(QCoreApplication.translate("Groot", u"PDF", None))
        self.actionSearch_in_Current_Note.setText(QCoreApplication.translate("Groot", u"Search in Current Note", None))
        self.actionSearch_in_All_Notes.setText(QCoreApplication.translate("Groot", u"Search in All Notes", None))
        self.actionOptions.setText(QCoreApplication.translate("Groot", u"Options", None))
        self.actionAbout.setText(QCoreApplication.translate("Groot", u"About", None))
        self.actionRequest.setText(QCoreApplication.translate("Groot", u"Request", None))
        self.actionDark_Theme.setText(QCoreApplication.translate("Groot", u"Dark Theme", None))
        self.actionLight_Theme.setText(QCoreApplication.translate("Groot", u"Light Theme", None))
        self.newNote.setText(QCoreApplication.translate("Groot", u"New Note", None))
        self.newNotebook.setText(QCoreApplication.translate("Groot", u"New Notebook", None))
        self.newSubNotebook.setText(QCoreApplication.translate("Groot", u"New sub-notebook", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Groot", u"Search this note", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Groot", u"Notes", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Groot", u"Notebooks", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Groot", u"Uncategorized", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.fileName.setText(QCoreApplication.translate("Groot", u"Testing Name", None))
        
        self.boldButton.setText(QCoreApplication.translate("Groot", u"Bold", None))
        self.italicButton.setText(QCoreApplication.translate("Groot", u"Italic", None))
        self.imageButton.setText(QCoreApplication.translate("Groot", u"Image", None))
        self.encryptionButton.setText(QCoreApplication.translate("Groot", u"Encryption", None))
        self.decryptionButton.setText(QCoreApplication.translate("Groot", u"Decryption", None))

        self.link.setText(QCoreApplication.translate("Groot", u"Link", None))
        self.code.setText(QCoreApplication.translate("Groot", u"Code", None))
        self.numberedList.setText(QCoreApplication.translate("Groot", u"Numbered List", None))
        self.bullets.setText(QCoreApplication.translate("Groot", u"Bullets", None))
        self.heading.setText(QCoreApplication.translate("Groot", u"Heading", None))
        self.horizaontalRule.setText(QCoreApplication.translate("Groot", u"Horizontal Line", None))
        self.dateTime.setText(QCoreApplication.translate("Groot", u"Date and Time", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Groot", u"Type here....", None))
        self.menuFile.setTitle(QCoreApplication.translate("Groot", u"File", None))
        self.menuImport.setTitle(QCoreApplication.translate("Groot", u"Import", None))
        self.menuExport.setTitle(QCoreApplication.translate("Groot", u"Export", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Groot", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("Groot", u"View", None))
        self.menuTools.setTitle(QCoreApplication.translate("Groot", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Groot", u"Help", None))
    # retranslateUi

