from PyQt5 import QtGui, QtWidgets
from card_edit_ui import Ui_MainWindow
from card import Card
from file_read_write import import_cards, export_cards, IncorrectFileFormatError
from error_dialog import ErrorDialog
from browse_files_dialog import browseFiles
from configuration import sentences_dictionary as translations
import sys
import argparse
import os


class EditWindow(QtWidgets.QMainWindow):
    """
    Card edit window class.
    """

    def __init__(self, path=None, parent=None) -> None:
        super().__init__(parent)
        self._parentWindow = parent
        self.setWindowIcon(QtGui.QIcon("fishkey/logo.png"))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.previousIndex = 0
        self.loading = False
        self.cardList = []
        # Card priority has to be higher than 0,
        # to enable drawing random cards with "weighs"
        self.ui.spinBoxPriority.setMinimum(1)
        self._uiConnections()
        if path is not None:
            self.fileLocation = path
            self._clear_line_edits()
            self._import()
            self._load_comboBox()

    def _uiConnections(self):
        """
        Method connecting all buttons and actions to local methods.
        """
        self.ui.cardListComboBox.currentIndexChanged.connect(
            self._textBoxesFiller
        )

        self.ui.buttonSave.clicked.connect(self._Save)
        self.ui.buttonLoad.clicked.connect(self._browseFiles)
        self.ui.buttonRemove.clicked.connect(self._removeCard)
        self.ui.actionSave.triggered.connect(self._Save)
        self.ui.actionOpen.triggered.connect(self._browseFiles)
        self.ui.actionClose.triggered.connect(self._close)

    def _import(self):
        """
        Method that imports cards from file,
        catches exception and shows error box.
        """
        try:
            self.cardList = import_cards(self.fileLocation)
            pass
        except IncorrectFileFormatError:
            message = translations["incorrect_file"]
            dialog = ErrorDialog(message, parent=self)
            if dialog.exec_():
                self.close()

    def _load(self):
        """
        Method that calls import method, changes current
        and previous selected card to 0.
        Assures correct loading of all input boxes.
        """
        # Allows for closing File Dialog without chosing any file
        self.loading = True
        self._clear_line_edits()
        self._import()
        self.previousIndex = 0
        self._load_comboBox()
        self.loading = False

    def _browseFiles(self):
        """
        Method showing File Input Dialog with only .csv files
        and directories. If correct file is selected, method
        calls methods for importing that file.
        """
        newFileLocation = browseFiles(self)
        if newFileLocation is not None:
            self.fileLocation = newFileLocation
            self._load()

    def _Save(self):
        """
        Saves cardList to file. Making sure that a new Card object is created
        in case of new card that wasn't appended to a list yet.
        """
        index = self.ui.cardListComboBox.currentIndex()
        if index == 0:
            self._create_new_card()
            self._clear_line_edits()
        else:
            self._textBoxesFiller()
        export_cards(self.fileLocation, self.cardList)

    def _removeCard(self):
        """
        Removes current selected card from cardList.
        Calls load_comboBox method to remove this card from
        comboBox list.
        """
        self.loading = True
        self.previousIndex = 0
        index = self.ui.cardListComboBox.currentIndex()
        if index == 0:
            return
        index -= 1
        self._clear_line_edits()
        self.cardList.pop(index)
        self._load_comboBox()
        self.loading = False

    def _load_comboBox(self):
        """
        Loads comboBox with cards main words.
        0 - element is reserved for "Add New" option.
        """
        self.ui.cardListComboBox.clear()
        self.ui.cardListComboBox.addItem(translations["add_new"])
        for card, _ in self.cardList:
            self.ui.cardListComboBox.addItem(card.mainWord)

    def _clear_line_edits(self):
        """
        Clears all user input boxes.
        """
        self.ui.lineEditMain.setText("")
        self.ui.lineEditSecondary.setText("")
        self.ui.lineEditSecondary.setText("")
        self.ui.spinBoxCorrect.setValue(0)
        self.ui.spinBoxIncorrect.setValue(0)
        self.ui.spinBoxPriority.setValue(0)

    def _create_new_card(self):
        """
        Method that takes data from input boxes,
        creates Card item and appends it to cardList.
        """
        mainWord = self.ui.lineEditMain.text()
        secondaryWord = self.ui.lineEditSecondary.text()
        correctAnswers = self.ui.spinBoxCorrect.value()
        incorrectAnswers = self.ui.spinBoxIncorrect.value()
        if not (mainWord == "" or secondaryWord == ""):
            priority = self.ui.spinBoxPriority.value()
            newCard = Card(
                mainWord,
                secondaryWord,
                correctAnswers,
                incorrectAnswers,
                0,
                0,
                priority,
            )
            element = (newCard, 0)
            self.cardList.append(element)
            self.ui.cardListComboBox.addItem(mainWord)

    def _set_card_data(self, card: Card):
        """
        Changes cards data to current text boxes and spin boxes values.

        Arguments
        ---------

        card: Card - card object
        """
        mainText = self.ui.lineEditMain.text()
        secondText = self.ui.lineEditSecondary.text()
        correct = self.ui.spinBoxCorrect.value()
        incorrect = self.ui.spinBoxIncorrect.value()
        priority = self.ui.spinBoxPriority.value()
        card.mainWord = mainText
        card.secondaryWord = secondText
        card.correctAnswers = correct
        card.incorrectAnswers = incorrect
        card.priority = priority

    def _set_input_boxes(self, card: Card):
        """
        Changes text boxes and spin boxes values to card data.

        Arguments
        ---------

        card: Card - card object
        """
        self.ui.lineEditMain.setText(card.mainWord)
        self.ui.lineEditSecondary.setText(card.secondaryWord)
        self.ui.lineEditSecondary.setText(card.secondaryWord)
        self.ui.spinBoxCorrect.setValue(card.correctAnswers)
        self.ui.spinBoxIncorrect.setValue(card.incorrectAnswers)
        self.ui.spinBoxPriority.setValue(card.priority)

    def _textBoxesFiller(self):
        """
        Method that fills all input boxes with current card data.
        When selected card changes, method writes
        not changed data to previous card.
        """
        index = self.ui.cardListComboBox.currentIndex()
        if self.loading is True:
            # Fix for gost cards ater removal
            return
        if self.previousIndex == 0:
            self._create_new_card()
        else:
            # Last index accounted for "add new" combobox option
            normalizedPrevious = self.previousIndex - 1
            card, bucket = self.cardList[normalizedPrevious]
            self._set_card_data(card)

        if index == 0:
            self._clear_line_edits()
            self.previousIndex = 0
            return
        card, bucket = self.cardList[index - 1]
        self._set_input_boxes(card)
        self.previousIndex = index

    def _close(self):
        self.close()

    def closeEvent(self, event):
        """
        Overwrites closeEvent to check if session window was
        launched from main launcher. If so it calls main launcher
        method "load" that reads from current file with cards and
        updates changed data.
        """
        if self._parentWindow is not None:
            self._parentWindow._load()


def guiMain(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--path", nargs="+", help="Path of a file")
    arguments = parser.parse_args()

    if arguments.path is not None:
        paths = [os.path.join(os.getcwd(), path) for path in arguments.path]
        path = paths[0]
    else:
        path = None
    app = QtWidgets.QApplication(sys.argv)
    window = EditWindow(path)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    guiMain(sys.argv)
