from PySide2 import QtCore, QtGui, QtWidgets
import settingWidget1


class Ui_settingDialog(object):
    def setupUi(self, settingDialog):
        self.w1 = settingWidget1.Ui_Form().setupUi()
        settingDialog.setObjectName("settingDialog")
        settingDialog.resize(929, 833)
        self.gridLayout = QtWidgets.QGridLayout(settingDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(settingDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.mainFrame = QtWidgets.QFrame(settingDialog)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMainFrame = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMainFrame.sizePolicy().hasHeightForWidth())
        self.leftMainFrame.setSizePolicy(sizePolicy)
        self.leftMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMainFrame.setObjectName("leftMainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMainFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchLineEdit = QtWidgets.QLineEdit(self.leftMainFrame)
        self.searchLineEdit.setStyleSheet("QLineEdit {\n"
                                          "    border: none;\n"
                                          "    padding: 2px 5px 2px 27px;\n"
                                          "    margin-right: 0px;\n"
                                          "}\n"
                                          "")
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.verticalLayout.addWidget(self.searchLineEdit)
        self.settingsTreeWidget = QtWidgets.QTreeWidget(self.leftMainFrame)
        self.settingsTreeWidget.setAllColumnsShowFocus(False)
        self.settingsTreeWidget.setHeaderHidden(True)
        self.settingsTreeWidget.setObjectName("settingsTreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.settingsTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.settingsTreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.settingsTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.settingsTreeWidget)
        self.verticalLayout.addWidget(self.settingsTreeWidget)
        self.horizontalLayout.addWidget(self.leftMainFrame)
        self.settingsStackedWidget = QtWidgets.QStackedWidget(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsStackedWidget.sizePolicy().hasHeightForWidth())
        self.settingsStackedWidget.setSizePolicy(sizePolicy)
        self.settingsStackedWidget.setObjectName("settingsStackedWidget")
        self.setting1Page = self.w1
        self.setting1Page.setObjectName("setting1Page")
        self.settingsStackedWidget.addWidget(self.setting1Page)
        self.setting2_1Page = QtWidgets.QWidget()
        self.setting2_1Page.setObjectName("setting2_1Page")
        self.settingsStackedWidget.addWidget(self.setting2_1Page)
        self.setting2_2Page = self.w1
        self.setting2_2Page.setObjectName("setting2_2Page")
        self.settingsStackedWidget.addWidget(self.setting2_2Page)
        self.setting3Page = QtWidgets.QWidget()
        self.setting3Page.setObjectName("setting3Page")
        self.settingsStackedWidget.addWidget(self.setting3Page)
        self.setting4Page = QtWidgets.QWidget()
        self.setting4Page.setObjectName("setting4Page")
        self.settingsStackedWidget.addWidget(self.setting4Page)
        self.horizontalLayout.addWidget(self.settingsStackedWidget)
        self.gridLayout.addWidget(self.mainFrame, 0, 0, 1, 1)

        self.settingDict = {'Setting1': 0, 'Setting2.1': 1, 'Setting2.2': 2, 'Setting3': 3, 'Setting4': 4}

        self.retranslateUi(settingDialog)
        self.settingsStackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(settingDialog)
        self.settingsTreeWidget.itemClicked.connect(self.ShowSettingWidget)

    def ShowSettingWidget(self):
        columnNumber = self.settingsTreeWidget.currentColumn()
        selectedItem = self.settingsTreeWidget.currentItem()
        if(selectedItem.childCount() == 0):
            selectedItemName = selectedItem.text(columnNumber)
            selectedItemIndex = self.settingDict[selectedItemName]
            print(selectedItemIndex, selectedItemName)
            if (selectedItemIndex != -1):
                self.settingsStackedWidget.setCurrentIndex(selectedItemIndex)
            else:
                alert = QtWidgets.QMessageBox(settingDialog)
                alert.setText("Sorry cannot open {0} setting Page".format(selectedItemName))
                alert.setIcon(QtWidgets.QMessageBox.Information)
                alert.show()

    def retranslateUi(self, settingDialog):
        _translate = QtCore.QCoreApplication.translate
        settingDialog.setWindowTitle(_translate("settingDialog", "Settings"))
        self.searchLineEdit.setPlaceholderText(_translate("settingDialog", "Find Settings"))
        self.settingsTreeWidget.headerItem().setText(0, _translate("settingDialog", "1"))
        __sortingEnabled = self.settingsTreeWidget.isSortingEnabled()
        self.settingsTreeWidget.setSortingEnabled(False)
        self.settingsTreeWidget.topLevelItem(0).setText(0, _translate("settingDialog", "Setting1"))
        self.settingsTreeWidget.topLevelItem(1).setText(0, _translate("settingDialog", "Setting2"))
        self.settingsTreeWidget.topLevelItem(1).child(0).setText(0, _translate("settingDialog", "Setting2.1"))
        self.settingsTreeWidget.topLevelItem(1).child(1).setText(0, _translate("settingDialog", "Setting2.2"))
        self.settingsTreeWidget.topLevelItem(2).setText(0, _translate("settingDialog", "Setting3"))
        self.settingsTreeWidget.topLevelItem(3).setText(0, _translate("settingDialog", "Setting4"))
        self.settingsTreeWidget.setSortingEnabled(__sortingEnabled)


