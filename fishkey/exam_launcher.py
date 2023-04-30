from PyQt5 import QtCore, QtGui, QtWidgets
from exam_ui import Ui_SesionWindow
from end_dialog import CustomDialog
from error_dialog import ErrorDialog
from file_read_write import IncorrectFileFormatError
from exam_class import Exam, NegativeTimeError
from configuration import sentences_dictionary as translations
import os
import argparse
import sys


class ExamWindow(QtWidgets.QMainWindow):
    """
    Exam window class.
    """

    def __init__(
        self, fileLocation, numberOfCards, timeForCard, parent=None
    ) -> None:
        super().__init__(parent)
        # @TODO Set as app arguments
        self._fileLocation = fileLocation
        self._numberOfCards = numberOfCards

        try:
            self._exam = Exam(fileLocation, numberOfCards, timeForCard)
        except IncorrectFileFormatError:
            dialog = ErrorDialog(translations["file_load_error"], parent=self)
            dialog.show()
            self.close()
            return

        # Create timer object
        self._timer = QtCore.QTimer(self)
        # Add a method with the timer
        self._timer.timeout.connect(self._second_passed)
        # Call start() method to modify the timer value
        self._timer.start(1000)

        self.ui = Ui_SesionWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("fishkey/logo.png"))
        self._UiConnections()
        self._showCard()
        self._setCountersLabels()

    def _UiConnections(self):
        """
        Method connecting all buttons and actions to local methods.
        """
        self.ui.nextButton.clicked.connect(self._nextCard)
        self.ui.input_box.returnPressed.connect(self._nextCard)

    def _second_passed(self):
        if self._exam.time_passed:
            self._end_exam()
        else:
            self._exam.update_time()
        self._setTimeLabel()

    def showDialog(self):
        """
        Showing end dialog with exam results.
        """
        dlg = CustomDialog(
            self, (self._exam.correct_answers, self._exam.number_of_cards)
        )
        if dlg.exec_():
            self._save()

    def _showCard(self):
        self.ui.shown_word.setText(self._exam.current_card_main_word)

    def _setTimeLabel(self):
        self.ui.timeRemaining_label.setText(self._exam.time_left_str)

    def _setCountersLabels(self):
        self.ui.cardsLeftCounter.setText(self._exam.completion_level_string())
        self.ui.correctCounter.setText(str(self._exam.correct_answers))
        self.ui.wrongCounter.setText(str(self._exam.incorrect_answers))
        self._setTimeLabel()

    def _end_exam(self):
        self.ui.input_box.returnPressed.disconnect()
        self.ui.nextButton.setEnabled(False)
        self.ui.shown_word.setText("KONIEC")
        self._timer.stop()
        self.showDialog()

    def _nextCard(self):
        """
        Changes to the next card.
        Calls validate answer, set counter and
        check if the exam is over.
        """

        self._validateAnswer()
        self._exam.move_to_next_previous_card(True)
        self._setCountersLabels()
        self.ui.input_box.setText("")

        if self._exam.session_completed():
            self._end_exam()
            return

        self._showCard()

    def _validateAnswer(self):
        """
        Gets user answer; and marks it.
        """
        answer = self.ui.input_box.text()
        self._exam.validate_current_card(answer)

    def _save(self):
        """
        Generates and saves satatistics to json file.
        Saves statistics to a json file.
        """
        self._exam.save_statistics()
        self._exam.save_session()

    def closeEvent(self, event):
        self._timer.stop()
        del self._timer


def guiMain(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--path", nargs="+", help="Path of a file", required=True
    )
    parser.add_argument("-n", "--number-of-cards", type=int, required=True)
    parser.add_argument(
        "-t",
        "--time-per-card",
        help="Time per card in seconds",
        type=int,
        required=True,
    )
    arguments = parser.parse_args()

    paths = [os.path.join(os.getcwd(), path) for path in arguments.path]
    path = paths[0]
    numberOfCards = arguments.number_of_cards
    timeForCard = arguments.time_per_card

    try:
        app = QtWidgets.QApplication(args)
        window = ExamWindow(path, numberOfCards, timeForCard)
        window.show()
        sys.exit(app.exec_())
    except NegativeTimeError:
        print(translations["negative_time"])


if __name__ == "__main__":
    guiMain(sys.argv)
