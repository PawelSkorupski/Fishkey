from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_FiszkiWindow
from file_read_write import (
    import_cards,
    import_session_stats,
    count_cards_to_N_bucket,
    IncorrectFileFormatError,
    statistics_data_file_name,
    NonExistantBucketError,
    seconds_to_minutes_and_seconds,
)
from statistics_methods import NotEnoughDataToDisplayError
from configuration import sentences_dictionary as translations
from configuration import maximal_bucket
from error_dialog import ErrorDialog
from browse_files_dialog import browseFiles
import session_launcher
import card_edit_launcher
import statistics_window
import exam_launcher
import sys
import os
import argparse


class FiszkiWindow(QtWidgets.QMainWindow):
    """
    Main application window.
    """

    def __init__(self, fileLocation, parent=None) -> None:
        super().__init__(parent)
        self._maxBucketNumber = maximal_bucket
        self.setWindowIcon(QtGui.QIcon("fishkey/logo.png"))
        self.ui = Ui_FiszkiWindow()
        self.ui.setupUi(self)
        self._uiConnections()
        self._cardList = []
        self._fileLocation = fileLocation
        if self._fileLocation is None:
            self._noFileSelected()
        else:
            self._load()

    def _uiConnections(self):
        """
        Method connecting all buttons and actions to local methods.
        """
        self.ui.sessionButton.clicked.connect(self._session)
        self.ui.examButton.clicked.connect(self._exam)
        self.ui.statisticsButton.clicked.connect(self._statistics)
        self.ui.editButton.clicked.connect(self._edit)
        self.ui.actionOpen.triggered.connect(self._browseFiles)
        self.ui.actionStatistics.triggered.connect(self._statistics)
        self.ui.actionZamknij.triggered.connect(self._close)
        self.ui.bucketNumberSpinBox.valueChanged.connect(
            self._session_button_card_counter
        )
        self.ui.timeForCardSpinBox.valueChanged.connect(
            self._exam_button_time_counter
        )
        self.ui.cardNumberSpinBox.valueChanged.connect(
            self._exam_button_time_counter
        )

    def _noFileSelected(self):
        """
        Changing central label and disabling user input,
        used if there is no file selected.
        """
        self.ui.file_nameLabel.setText(translations["open_file"])
        self._buttonEnabler(False)

    def _browseFiles(self):
        """
        Method showing File Input Dialog with only .csv files
        and directories. If correct file is selected, method
        calls methods for importing that file.
        """
        newFileLocation = browseFiles(self)
        if newFileLocation is not None:
            self._fileLocation = newFileLocation
            self._load()

    def _set_labels(self):
        """
        Setting labels with card counters.
        """

        # Set file name label
        file_name = os.path.basename(self._fileLocation)
        file_name = file_name.replace(".csv", "")
        self.ui.file_nameLabel.setText(file_name)

        # Set labels containing numbers of cards and buckets
        cardNumber = f'{translations["number_of_cards"]}{len(self._cardList)}'
        self.ui.cardNumberLabel.setText(cardNumber)
        bucketNumber = (
            f'{translations["number_of_buckets"]}{self._maxBucketNumber}'
        )
        self.ui.bucketNumberLabel.setText(bucketNumber)
        self.ui.sessionButton.setText(translations["session"])

    def _buttonEnabler(self, enabled) -> None:
        """
        Enables or diables user input methods.

        Arguments:
        ----------

        enabled: bool - New button state.
        """
        self.ui.sessionButton.setEnabled(enabled)
        self.ui.examButton.setEnabled(enabled)
        self.ui.statisticsButton.setEnabled(enabled)
        self.ui.editButton.setEnabled(enabled)

    def _load(self):
        """
        Imports cardList and sets maximal spinBox values.
        """
        try:
            self._cardList = import_cards(self._fileLocation)
            # Enable buttons
            self._buttonEnabler(True)

            self.ui.bucketNumberSpinBox.setMaximum(self._maxBucketNumber)
            self.ui.cardNumberSpinBox.setMaximum(len(self._cardList))
            self._set_labels()
            self._session_button_card_counter()
            self._exam_button_time_counter()
        except IncorrectFileFormatError:
            self.ui.file_nameLabel.setText(
                translations["incorrect_file_label"]
            )
            message = translations["incorrect_file"]
            dialog = ErrorDialog(message, parent=self)
            dialog.show()
        except NonExistantBucketError:
            message = translations["incorrect_file"]
            dialog = ErrorDialog(message, parent=self)
            dialog.show()

    def _session_button_card_counter(self):
        """
        Sets session button label to number of chosen cards.
        """
        if len(self._cardList) != 0:
            numberOfBuckets = self.ui.bucketNumberSpinBox.value()
            numberOfBuckets -= 1
            count = count_cards_to_N_bucket(
                self._cardList, numberOfBuckets, self._maxBucketNumber
            )
            self.ui.sessionButton.setText(
                translations["session"]
                + "\n"
                + translations["cards"]
                + str(count)
            )

    def _exam_button_time_counter(self):
        """
        Sets exam button label to time for exam.
        """
        if len(self._cardList) != 0:
            numberOfCards = self.ui.cardNumberSpinBox.value()
            timeForOneCard = self.ui.timeForCardSpinBox.value()
            timeForExam = numberOfCards * timeForOneCard
            minutes, seconds = seconds_to_minutes_and_seconds(timeForExam)
            if seconds < 10:
                seconds = f"0{seconds}"
            self.ui.examButton.setText(
                translations["exam"] + f"\n{minutes}:{seconds}"
            )

    def _session(self):
        """
        Creates and shows session window with correct arguments.
        """
        maxBucketNumber = self._maxBucketNumber
        numberOfBuckets = self.ui.bucketNumberSpinBox.value()
        try:
            session_window = session_launcher.SessionWindow(
                self._fileLocation,
                maxBucketNumber,
                numberOfBuckets,
                parent=self,
            )
            session_window.show()
        except NonExistantBucketError:
            message = translations["incorrect_file"]
            dialog = ErrorDialog(message, parent=self)
            dialog.show()

    def _exam(self):
        """
        Creates and shows exam window with correct arguments.
        """
        numberOfCards = self.ui.cardNumberSpinBox.value()
        timeForOneCard = self.ui.timeForCardSpinBox.value()
        exam_window = exam_launcher.ExamWindow(
            self._fileLocation, numberOfCards, timeForOneCard, parent=self
        )
        exam_window.show()

    def _edit(self):
        """
        Creates and shows edit window with correct arguments.
        """
        edit_window = card_edit_launcher.EditWindow(
            self._fileLocation, parent=self
        )
        edit_window.show()

    def _statistics(self):
        """
        Creates and shows statistics window with correct arguments.
        """
        try:
            statsFileLocation = statistics_data_file_name(self._fileLocation)
            jsonData = import_session_stats(statsFileLocation)
            statistics_screen = statistics_window.StatisticsWindow(
                jsonData, self._cardList, self._maxBucketNumber, parent=self
            )
            statistics_screen.show()
        except FileNotFoundError:
            message = translations["file_not_found"]
            dialog = ErrorDialog(message, parent=self)
            dialog.show()
        except (IncorrectFileFormatError, NonExistantBucketError):
            message = translations["incorrect_file"]
            dialog = ErrorDialog(message, parent=self)
            dialog.show()
        except NotEnoughDataToDisplayError:
            message = translations["not_enough_statistics"]
            dialog = ErrorDialog(message, parent=self)
            dialog.show()

    def _close(self):
        """
        Closes whole application, with all children windows.
        """
        QtCore.QCoreApplication.quit()


def guiMain(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--path", nargs="+", help="Path of a file")
    arguments = parser.parse_args()

    if arguments.path is not None:
        paths = [os.path.join(os.getcwd(), path) for path in arguments.path]
        path = paths[0]
    else:
        path = None

    app = QtWidgets.QApplication(args)
    window = FiszkiWindow(path)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    guiMain(sys.argv)
