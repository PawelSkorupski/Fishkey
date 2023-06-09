# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FiszkiWindow(object):
    def setupUi(self, FiszkiWindow):
        FiszkiWindow.setObjectName("FiszkiWindow")
        FiszkiWindow.resize(575, 454)
        FiszkiWindow.setMinimumSize(QtCore.QSize(575, 454))
        font = QtGui.QFont()
        font.setPointSize(14)
        FiszkiWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(FiszkiWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_nameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.file_nameLabel.setFont(font)
        self.file_nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.file_nameLabel.setObjectName("file_nameLabel")
        self.verticalLayout.addWidget(self.file_nameLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cardNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.cardNumberLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cardNumberLabel.setObjectName("cardNumberLabel")
        self.horizontalLayout_6.addWidget(self.cardNumberLabel)
        self.bucketNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.bucketNumberLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bucketNumberLabel.setObjectName("bucketNumberLabel")
        self.horizontalLayout_6.addWidget(self.bucketNumberLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth()
        )
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.bucketNumberSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bucketNumberSpinBox.sizePolicy().hasHeightForWidth()
        )
        self.bucketNumberSpinBox.setSizePolicy(sizePolicy)
        self.bucketNumberSpinBox.setMinimum(1)
        self.bucketNumberSpinBox.setObjectName("bucketNumberSpinBox")
        self.verticalLayout_4.addWidget(self.bucketNumberSpinBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.sessionButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sessionButton.sizePolicy().hasHeightForWidth()
        )
        self.sessionButton.setSizePolicy(sizePolicy)
        self.sessionButton.setObjectName("sessionButton")
        self.horizontalLayout_3.addWidget(self.sessionButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.cardNumberSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.cardNumberSpinBox.setMinimum(1)
        self.cardNumberSpinBox.setObjectName("cardNumberSpinBox")
        self.verticalLayout_5.addWidget(self.cardNumberSpinBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.timeForCardSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.timeForCardSpinBox.setMinimum(1)
        self.timeForCardSpinBox.setMaximum(5000)
        self.timeForCardSpinBox.setObjectName("timeForCardSpinBox")
        self.verticalLayout_5.addWidget(self.timeForCardSpinBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.examButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.examButton.sizePolicy().hasHeightForWidth()
        )
        self.examButton.setSizePolicy(sizePolicy)
        self.examButton.setObjectName("examButton")
        self.horizontalLayout_4.addWidget(self.examButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.statisticsButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.statisticsButton.sizePolicy().hasHeightForWidth()
        )
        self.statisticsButton.setSizePolicy(sizePolicy)
        self.statisticsButton.setObjectName("statisticsButton")
        self.horizontalLayout_5.addWidget(self.statisticsButton)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.editButton.sizePolicy().hasHeightForWidth()
        )
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_5.addWidget(self.editButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(7, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        FiszkiWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FiszkiWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuPlik = QtWidgets.QMenu(self.menubar)
        self.menuPlik.setObjectName("menuPlik")
        self.menuStatystyki = QtWidgets.QMenu(self.menubar)
        self.menuStatystyki.setObjectName("menuStatystyki")
        FiszkiWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FiszkiWindow)
        self.statusbar.setObjectName("statusbar")
        FiszkiWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(FiszkiWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionZamknij = QtWidgets.QAction(FiszkiWindow)
        self.actionZamknij.setObjectName("actionZamknij")
        self.actionStatistics = QtWidgets.QAction(FiszkiWindow)
        self.actionStatistics.setObjectName("actionStatistics")
        self.menuPlik.addAction(self.actionOpen)
        self.menuPlik.addAction(self.actionZamknij)
        self.menuStatystyki.addAction(self.actionStatistics)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuStatystyki.menuAction())

        self.retranslateUi(FiszkiWindow)
        QtCore.QMetaObject.connectSlotsByName(FiszkiWindow)

    def retranslateUi(self, FiszkiWindow):
        _translate = QtCore.QCoreApplication.translate
        FiszkiWindow.setWindowTitle(_translate("FiszkiWindow", "Fiszki"))
        self.file_nameLabel.setText(_translate("FiszkiWindow", "_file_name_"))
        self.cardNumberLabel.setText(
            _translate("FiszkiWindow", "Liczba Fiszek: 0")
        )
        self.bucketNumberLabel.setText(
            _translate("FiszkiWindow", "Liczba Kubeczków: 0")
        )
        self.label_2.setText(
            _translate("FiszkiWindow", "Liczba wybranych Kubeczków:")
        )
        self.sessionButton.setText(_translate("FiszkiWindow", "Sesja"))
        self.label_3.setText(
            _translate("FiszkiWindow", "Liczba wybranych Fiszek:")
        )
        self.label.setText(
            _translate("FiszkiWindow", "Czas na jedną Fiszkę: (s)")
        )
        self.examButton.setText(_translate("FiszkiWindow", "Egzamin"))
        self.statisticsButton.setText(_translate("FiszkiWindow", "Statystyki"))
        self.editButton.setText(_translate("FiszkiWindow", "Edycja"))
        self.menuPlik.setTitle(_translate("FiszkiWindow", "Plik"))
        self.menuStatystyki.setTitle(_translate("FiszkiWindow", "Statystyki"))
        self.actionOpen.setText(_translate("FiszkiWindow", "Otwórz"))
        self.actionOpen.setShortcut(_translate("FiszkiWindow", "Ctrl+O"))
        self.actionZamknij.setText(_translate("FiszkiWindow", "Zamknij"))
        self.actionStatistics.setText(
            _translate("FiszkiWindow", "Wyświetl okno")
        )
