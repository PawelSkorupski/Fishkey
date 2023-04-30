from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure
from configuration import sentences_dictionary as translations
from PyQt5 import QtGui, QtWidgets
from statistics_ui import Ui_StatisticsWindow
from statistics_methods import (
    count_learned,
    count_in_buckets,
    total_correct_incorrect_answers,
    count_finished_sessions,
    count_exams,
    average_exam_score,
    average_session_score,
)
import matplotlib

matplotlib.use("Qt5Agg")


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=4, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class StatisticsWindow(QtWidgets.QMainWindow):
    def __init__(self, jsonData, cardList, maxBucket, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_StatisticsWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("fishkey/logo.png"))
        # Load all statistics to variables
        exam_counter = count_exams(jsonData)
        session_counter = count_finished_sessions(jsonData)
        exam_average = average_exam_score(jsonData)
        session_average = average_session_score(jsonData)
        learned_counter = count_learned(cardList, maxBucket)
        buckets_counter = count_in_buckets(cardList, maxBucket)
        correct_incorrect = total_correct_incorrect_answers(cardList)

        # Setting up labels
        exam_counter_text = translations["exam_counter"] + str(exam_counter)
        session_counter_text = translations["session_counter"] + str(
            session_counter
        )
        exam_average_text = translations["avg_exam"] + str(exam_average) + "%"
        session_average_text = (
            translations["avg_session"] + str(session_average) + "%"
        )
        learned_counter_text = translations["learned"] + str(learned_counter)
        self.ui.examCounterLabel.setText(exam_counter_text)
        self.ui.sessionCounterLabel.setText(session_counter_text)
        self.ui.avgExamLabel.setText(exam_average_text)
        self.ui.avgSessionLabel.setText(session_average_text)
        self.ui.learnedLabel.setText(learned_counter_text)

        # Fix for not xlabel not showing up
        matplotlib.rcParams.update({"figure.autolayout": True})
        # Bar plot with numbers of cards in each bucket.
        self.firstPlot = MplCanvas(width=1, height=1, dpi=80)
        firstPlot_labels = [number for number in range(0, maxBucket + 1)]
        firstPlot_colors = [
            "silver",
            "orange",
            "mediumspringgreen",
            "slateblue",
            "peru",
            "pink",
            "lawngreen",
            "crimson",
        ]
        self.firstPlot.axes.bar(
            firstPlot_labels, buckets_counter, color=firstPlot_colors
        )
        self.firstPlot.axes.set_title(
            translations["number_of_cards_in_buckets"]
        )
        self.firstPlot.axes.set_ylabel(translations["number_of_cards"])
        self.firstPlot.axes.set_xlabel(translations["buckets"])

        # Pie chart with answer statistics.
        self.secondPlot = MplCanvas(width=2, height=3, dpi=100)
        secondPlot_labels = [
            translations["correct_answers"],
            translations["incorrect_answers"],
        ]
        secondPlot_colors = ["g", "r"]
        self.secondPlot.axes.pie(
            correct_incorrect,
            labels=secondPlot_labels,
            colors=secondPlot_colors,
            autopct="%1.1f%%",
        )
        self.secondPlot.axes.set_title(translations["answers_plot"])

        # Setting up toolbars.
        firstPlot_toolbar = NavigationToolbar(self.firstPlot, self)
        secondPlot_toolbar = NavigationToolbar(self.secondPlot, self)

        # Adding widgets to layout to display them.
        self.ui.mainLayout.addWidget(firstPlot_toolbar)
        self.ui.mainLayout.addWidget(self.firstPlot)
        self.ui.mainLayout.addWidget(self.ui.line)
        self.ui.mainLayout.addWidget(secondPlot_toolbar)
        self.ui.mainLayout.addWidget(self.secondPlot)
        self.ui.mainLayout.setStretch(4, 1)
        self.ui.mainLayout.setStretch(4, 4)
        self.ui.mainLayout.setStretch(5, 1)
        self.ui.mainLayout.setStretch(6, 1)
        self.ui.mainLayout.setStretch(7, 4)
