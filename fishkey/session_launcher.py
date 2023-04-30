from PyQt5 import QtCore, QtGui, QtWidgets
from session_ui import Ui_SesionWindow
from end_dialog import CustomDialog
from error_dialog import ErrorDialog
from configuration import sentences_dictionary as translations
from session_class import Session
from file_read_write import (
    IncorrectFileFormatError,
    EmptyBucketsError,
)
import sys
import os
import argparse


class SessionWindow(QtWidgets.QMainWindow):
    """
    Session window class.
    """

    def __init__(
        self, fileLocation, bucketsTotal, lastBucket, parent=None
    ) -> None:
        super().__init__(parent)
        self._parentWindow = parent

        QtWidgets.QShortcut(
            QtGui.QKeySequence(QtCore.Qt.Key_Left),
            self,
            activated=self._previous,
        )
        QtWidgets.QShortcut(
            QtGui.QKeySequence(QtCore.Qt.Key_Right), self, activated=self._next
        )

        self.setWindowIcon(QtGui.QIcon("fishkey/logo.png"))
        self.ui = Ui_SesionWindow()
        self.ui.setupUi(self)
        self._uiConnections()
        self._clearLabels()

        try:
            """
            Tries to create session object. Holding all information
            about current session, card objects and all counters.
            """
            self.session = Session(fileLocation, bucketsTotal, lastBucket)
            self._showCard()
            self._setCounters()
        except IncorrectFileFormatError:
            message = translations["incorrect_file"]
            dialog = ErrorDialog(message, parent=self)
            dialog.show()
            self._lock_input()
        except EmptyBucketsError:
            message = translations["no_cards_selected"]
            dialog = ErrorDialog(message, parent=self)
            dialog.show()
            self._lock_input()

    def _lock_input(self) -> None:
        """
        Locks user input in case of Exception.
        """
        self.ui.userGuessLabel.show()
        self.ui.shown_word.hide()
        self.ui.userGuessLabel.setText(translations["reload"])
        self.ui.nextButton.setEnabled(False)
        self.ui.checkButton.setEnabled(False)
        self.ui.previousButton.setEnabled(False)
        self.ui.input_box.setEnabled(False)
        self.ui.actionZapisz.setEnabled(False)

    def _uiConnections(self) -> None:
        """
        Method connecting all buttons and actions to local methods.
        """
        self.ui.nextButton.clicked.connect(self._next)
        self.ui.previousButton.clicked.connect(self._previous)
        self.ui.checkButton.clicked.connect(self._check)
        self.ui.input_box.returnPressed.connect(self._check)
        self.ui.actionZapisz.triggered.connect(self._save)
        self.ui.actionZamknij.triggered.connect(self._close)

    def _setCounters(self):
        """
        Sets labels with counters.
        """
        self.ui.cardsLeftCounter.setText(
            self.session.completion_level_string()
        )
        self.ui.correctCounter.setText(str(self.session.correct_answers))
        self.ui.wrongCounter.setText(str(self.session.incorrect_answers))

    def _showDialog(self):
        """
        Shows end dialog with session statistics.
        """
        dlg = CustomDialog(
            self, (self.session.correct_answers, self.session.number_of_cards)
        )
        if dlg.exec_():
            # User pressed OK on save dialog.
            self._save()

    def _clearLabels(self):
        """
        Clears labels, used on load.
        """
        self.ui.secondaryLabel.setText("")
        self.ui.userGuessLabel.setText("")
        self.ui.input_box.setText("")

    def _setLabelColor(self, color: str):
        """
        Function setting label colors to argument color.

        Arguments:
        ----------

        color: str - string containging color name.
        More information in PyQt documentation.
        """
        self.ui.shown_word.setStyleSheet(f"color: {color};")
        self.ui.secondaryLabel.setStyleSheet(f"color: {color};")
        self.ui.userGuessLabel.setStyleSheet(f"color: {color};")

    def _setLabelsVisibility(self, visibility: bool):
        """
        Sets visibility of labels.

        Arguments:
        ----------

        visibility: bool - labels visibility status
        """
        if visibility:
            self.ui.secondaryLabel.show()
            self.ui.userGuessLabel.show()
            self.ui.checkButton.setEnabled(False)
        else:
            self.ui.secondaryLabel.hide()
            self.ui.userGuessLabel.hide()
            self.ui.checkButton.setEnabled(True)

    def _showCard(self):
        """
        Function loading current card and setting labels
        with correct card data.
        """
        self.ui.shown_word.setText(self.session.current_card_main_word)
        self._clearLabels()
        if self.session.current_card_last_answer_mark is None:
            # No answer yet.
            self.ui.input_box.show()
            self.ui.input_box.setFocus()
            self._setLabelColor("black")
            self._setLabelsVisibility(False)
            return
        if self.session.current_card_last_answer_mark is True:
            # User answered correctly.
            self._setLabelColor("green")
            self._setLabelsVisibility(True)
        else:
            # User answered with wrong word.
            self._setLabelColor("red")
            self._setLabelsVisibility(True)
        self.ui.input_box.hide()
        correctAnswerText = ""
        correctAnswerText += translations["correct_ans"]
        correctAnswerText += self.session.current_card_secondary_word
        self.ui.secondaryLabel.setText(correctAnswerText)
        userAnswerText = ""
        userAnswerText += translations["user_ans"]
        userAnswerText += self.session.current_card_last_answer
        self.ui.userGuessLabel.setText(userAnswerText)

    def _updateCard(self):
        """
        Updates all window labels to current status.
        """
        self._showCard()
        self._setCounters()

    def _next(self):
        """
        Changes to the next card.
        """
        self.session.move_to_next_previous_card(True)
        self._updateCard()

    def _previous(self):
        """
        Changes to the previous card.
        """
        self.session.move_to_next_previous_card(False)
        self._updateCard()

    def _check(self):
        """
        Marking of user guess.
        Also checks if the session is over,
        and displays dialog.
        """
        userGuess = self.ui.input_box.text()
        self.session.mark_current_card(userGuess)
        self._updateCard()

        # Check if all cards have been completed.
        if self.session.session_completed():
            self._showDialog()

    def _save(self):
        self.session.save_session()
        self.session.save_statistics()

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
    parser.add_argument(
        "-i", "--path", nargs="+", help="Path of a file", required=True
    )
    parser.add_argument(
        "-b",
        "--buckets-total",
        type=int,
        default=5,
        help="Number of buckets in total",
        required=True,
    )
    parser.add_argument("-l", "--last-bucket", type=int, required=True)
    arguments = parser.parse_args()
    paths = [os.path.join(os.getcwd(), path) for path in arguments.path]
    path = paths[0]
    bucket_total = arguments.buckets_total
    last_bucket = arguments.last_bucket

    app = QtWidgets.QApplication(args)
    window = SessionWindow(path, bucket_total, last_bucket)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    guiMain(sys.argv)
