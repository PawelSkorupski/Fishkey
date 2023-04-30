from PyQt5 import QtGui, QtWidgets


class CustomDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, score=(0, 0)):
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon("fishkey/logo.png"))
        self.setWindowTitle("Koniec Egzaminu")

        QBtn = (
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        )

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        font = QtGui.QFont()
        font.setPointSize(14)
        message = QtWidgets.QLabel(
            f"Twój wynik to {score[0]}/{score[1]} \nCzy chcesz zapisać wynik?"
        )
        message.setFont(font)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
