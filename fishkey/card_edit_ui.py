# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cardListComboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cardListComboBox.setFont(font)
        self.cardListComboBox.setObjectName("cardListComboBox")
        self.verticalLayout.addWidget(self.cardListComboBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelMain = QtWidgets.QLabel(self.centralwidget)
        self.labelMain.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelMain.setFont(font)
        self.labelMain.setObjectName("labelMain")
        self.verticalLayout_4.addWidget(self.labelMain)
        self.lineEditMain = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditMain.setFont(font)
        self.lineEditMain.setText("")
        self.lineEditMain.setObjectName("lineEditMain")
        self.verticalLayout_4.addWidget(self.lineEditMain)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelSecondary = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSecondary.setFont(font)
        self.labelSecondary.setObjectName("labelSecondary")
        self.verticalLayout_7.addWidget(self.labelSecondary)
        self.lineEditSecondary = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditSecondary.setFont(font)
        self.lineEditSecondary.setObjectName("lineEditSecondary")
        self.verticalLayout_7.addWidget(self.lineEditSecondary)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelCorrect = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCorrect.setFont(font)
        self.labelCorrect.setObjectName("labelCorrect")
        self.verticalLayout_3.addWidget(self.labelCorrect)
        self.spinBoxCorrect = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBoxCorrect.setFont(font)
        self.spinBoxCorrect.setObjectName("spinBoxCorrect")
        self.verticalLayout_3.addWidget(self.spinBoxCorrect)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_incorrect = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_incorrect.setFont(font)
        self.label_incorrect.setObjectName("label_incorrect")
        self.verticalLayout_2.addWidget(self.label_incorrect)
        self.spinBoxIncorrect = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBoxIncorrect.setFont(font)
        self.spinBoxIncorrect.setObjectName("spinBoxIncorrect")
        self.verticalLayout_2.addWidget(self.spinBoxIncorrect)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.labelPriority = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPriority.setFont(font)
        self.labelPriority.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPriority.setObjectName("labelPriority")
        self.verticalLayout.addWidget(self.labelPriority)
        self.spinBoxPriority = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBoxPriority.setFont(font)
        self.spinBoxPriority.setObjectName("spinBoxPriority")
        self.verticalLayout.addWidget(self.spinBoxPriority)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.buttonLoad = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttonLoad.sizePolicy().hasHeightForWidth()
        )
        self.buttonLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonLoad.setFont(font)
        self.buttonLoad.setObjectName("buttonLoad")
        self.horizontalLayout_5.addWidget(self.buttonLoad)
        self.buttonRemove = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttonRemove.sizePolicy().hasHeightForWidth()
        )
        self.buttonRemove.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonRemove.setFont(font)
        self.buttonRemove.setObjectName("buttonRemove")
        self.horizontalLayout_5.addWidget(self.buttonRemove)
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttonSave.sizePolicy().hasHeightForWidth()
        )
        self.buttonSave.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("buttonSave")
        self.horizontalLayout_5.addWidget(self.buttonSave)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 26))
        self.menubar.setObjectName("menubar")
        self.menuPlik = QtWidgets.QMenu(self.menubar)
        self.menuPlik.setObjectName("menuPlik")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOtworz")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionZapisz")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionZamknij")
        self.menuPlik.addAction(self.actionOpen)
        self.menuPlik.addAction(self.actionSave)
        self.menuPlik.addAction(self.actionClose)
        self.menubar.addAction(self.menuPlik.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edycja Fiszek"))
        self.label.setText(_translate("MainWindow", "Wybierz fiszkę:"))
        self.cardListComboBox.setItemText(
            0, _translate("MainWindow", "Dodaj nową")
        )
        self.labelMain.setText(_translate("MainWindow", "Główne słowo:"))
        self.labelSecondary.setText(_translate("MainWindow", "Zakryte słowo:"))
        self.labelCorrect.setText(
            _translate("MainWindow", "Poprawnych odpowiedzi:")
        )
        self.label_incorrect.setText(
            _translate("MainWindow", "Błędnych opdowiedzi:")
        )
        self.labelPriority.setText(_translate("MainWindow", "Priorytet:"))
        self.buttonLoad.setText(_translate("MainWindow", "Wczytaj"))
        self.buttonRemove.setText(_translate("MainWindow", "Usuń"))
        self.buttonSave.setText(_translate("MainWindow", "Zapisz"))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik"))
        self.actionOpen.setText(_translate("MainWindow", "Otwórz"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Zapisz"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionClose.setText(_translate("MainWindow", "Zamknij"))