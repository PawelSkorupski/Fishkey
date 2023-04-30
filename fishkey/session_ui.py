# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_designs\session.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SesionWindow(object):
    def setupUi(self, SesionWindow):
        SesionWindow.setObjectName("SesionWindow")
        SesionWindow.resize(615, 518)
        SesionWindow.setMinimumSize(QtCore.QSize(400, 500))
        SesionWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SesionWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(5000, 5000))
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.correctLabel = QtWidgets.QLabel(self.centralwidget)
        self.correctLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.correctLabel.sizePolicy().hasHeightForWidth()
        )
        self.correctLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.correctLabel.setFont(font)
        self.correctLabel.setAlignment(
            QtCore.Qt.AlignRight
            | QtCore.Qt.AlignTrailing
            | QtCore.Qt.AlignVCenter
        )
        self.correctLabel.setObjectName("correctLabel")
        self.horizontalLayout_2.addWidget(self.correctLabel)
        self.correctCounter = QtWidgets.QLabel(self.centralwidget)
        self.correctCounter.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.correctCounter.setFont(font)
        self.correctCounter.setObjectName("correctCounter")
        self.horizontalLayout_2.addWidget(self.correctCounter)
        self.wrongLabel = QtWidgets.QLabel(self.centralwidget)
        self.wrongLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.wrongLabel.sizePolicy().hasHeightForWidth()
        )
        self.wrongLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wrongLabel.setFont(font)
        self.wrongLabel.setAlignment(
            QtCore.Qt.AlignRight
            | QtCore.Qt.AlignTrailing
            | QtCore.Qt.AlignVCenter
        )
        self.wrongLabel.setObjectName("wrongLabel")
        self.horizontalLayout_2.addWidget(self.wrongLabel)
        self.wrongCounter = QtWidgets.QLabel(self.centralwidget)
        self.wrongCounter.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wrongCounter.setFont(font)
        self.wrongCounter.setObjectName("wrongCounter")
        self.horizontalLayout_2.addWidget(self.wrongCounter)
        self.cardsLeftLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cardsLeftLabel.setFont(font)
        self.cardsLeftLabel.setAlignment(
            QtCore.Qt.AlignRight
            | QtCore.Qt.AlignTrailing
            | QtCore.Qt.AlignVCenter
        )
        self.cardsLeftLabel.setObjectName("cardsLeftLabel")
        self.horizontalLayout_2.addWidget(self.cardsLeftLabel)
        self.cardsLeftCounter = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.cardsLeftCounter.setFont(font)
        self.cardsLeftCounter.setAutoFillBackground(False)
        self.cardsLeftCounter.setAlignment(
            QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
            | QtCore.Qt.AlignVCenter
        )
        self.cardsLeftCounter.setObjectName("cardsLeftCounter")
        self.horizontalLayout_2.addWidget(self.cardsLeftCounter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.shown_word = QtWidgets.QLabel(self.centralwidget)
        self.shown_word.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.shown_word.setFont(font)
        self.shown_word.setAlignment(QtCore.Qt.AlignCenter)
        self.shown_word.setObjectName("shown_word")
        self.verticalLayout.addWidget(self.shown_word)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.secondaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondaryLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.secondaryLabel.setFont(font)
        self.secondaryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.secondaryLabel.setObjectName("secondaryLabel")
        self.verticalLayout.addWidget(self.secondaryLabel)
        self.userGuessLabel = QtWidgets.QLabel(self.centralwidget)
        self.userGuessLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.userGuessLabel.setFont(font)
        self.userGuessLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userGuessLabel.setObjectName("userGuessLabel")
        self.verticalLayout.addWidget(self.userGuessLabel)
        self.input_box = QtWidgets.QLineEdit(self.centralwidget)
        self.input_box.setEnabled(True)
        self.input_box.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.input_box.setFont(font)
        self.input_box.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_box.setText("")
        self.input_box.setAlignment(QtCore.Qt.AlignCenter)
        self.input_box.setClearButtonEnabled(True)
        self.input_box.setObjectName("input_box")
        self.verticalLayout.addWidget(self.input_box)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetMaximumSize
        )
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previousButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.previousButton.sizePolicy().hasHeightForWidth()
        )
        self.previousButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.previousButton.setFont(font)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout.addWidget(self.previousButton)
        self.checkButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkButton.sizePolicy().hasHeightForWidth()
        )
        self.checkButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkButton.setFont(font)
        self.checkButton.setAutoDefault(True)
        self.checkButton.setObjectName("checkButton")
        self.horizontalLayout.addWidget(self.checkButton)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nextButton.sizePolicy().hasHeightForWidth()
        )
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextButton.setFont(font)
        self.nextButton.setAutoDefault(True)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(6, 5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        SesionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SesionWindow)
        self.statusbar.setObjectName("statusbar")
        SesionWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(SesionWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 615, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuPlik = QtWidgets.QMenu(self.menuBar)
        self.menuPlik.setObjectName("menuPlik")
        SesionWindow.setMenuBar(self.menuBar)
        self.actionZapisz = QtWidgets.QAction(SesionWindow)
        self.actionZapisz.setObjectName("actionZapisz")
        self.actionZamknij = QtWidgets.QAction(SesionWindow)
        self.actionZamknij.setObjectName("actionZamknij")
        self.menuPlik.addAction(self.actionZapisz)
        self.menuPlik.addAction(self.actionZamknij)
        self.menuBar.addAction(self.menuPlik.menuAction())

        self.retranslateUi(SesionWindow)
        QtCore.QMetaObject.connectSlotsByName(SesionWindow)
        SesionWindow.setTabOrder(self.input_box, self.checkButton)
        SesionWindow.setTabOrder(self.checkButton, self.nextButton)
        SesionWindow.setTabOrder(self.nextButton, self.previousButton)

    def retranslateUi(self, SesionWindow):
        _translate = QtCore.QCoreApplication.translate
        SesionWindow.setWindowTitle(_translate("SesionWindow", "Sesja"))
        self.correctLabel.setText(_translate("SesionWindow", "Dobrze:"))
        self.correctCounter.setText(_translate("SesionWindow", "0"))
        self.wrongLabel.setText(_translate("SesionWindow", "Źle:"))
        self.wrongCounter.setText(_translate("SesionWindow", "0"))
        self.cardsLeftLabel.setText(_translate("SesionWindow", "Fiszka:"))
        self.cardsLeftCounter.setText(_translate("SesionWindow", "0/1"))
        self.shown_word.setText(_translate("SesionWindow", "_place_holder_"))
        self.secondaryLabel.setText(
            _translate("SesionWindow", "Poprawna odpowiedź: _correct_answer_")
        )
        self.userGuessLabel.setText(
            _translate("SesionWindow", "Twoja odpowiedź: _user_guess_")
        )
        self.input_box.setPlaceholderText(
            _translate("SesionWindow", "Wpisz tutaj")
        )
        self.previousButton.setText(_translate("SesionWindow", "Poprzednie"))
        self.checkButton.setText(_translate("SesionWindow", "Sprawdź"))
        self.nextButton.setText(_translate("SesionWindow", "Następne"))
        self.menuPlik.setTitle(_translate("SesionWindow", "Plik"))
        self.actionZapisz.setText(_translate("SesionWindow", "Zapisz"))
        self.actionZapisz.setShortcut(_translate("SesionWindow", "Ctrl+S"))
        self.actionZamknij.setText(_translate("SesionWindow", "Zamknij"))