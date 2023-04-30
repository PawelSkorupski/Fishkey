from PyQt5 import QtGui, QtWidgets


class ErrorDialog(QtWidgets.QDialog):
    def __init__(self, errorMessage: str, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon("fishkey/logo.png"))
        self.setWindowTitle("Wystąpił Błąd")

        QBtn = QtWidgets.QDialogButtonBox.Ok

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QtWidgets.QVBoxLayout()
        font = QtGui.QFont()
        font.setPointSize(14)
        message = QtWidgets.QLabel(errorMessage)
        message.setFont(font)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
