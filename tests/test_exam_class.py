from exam_class import Exam
from file_rw import cardTupleList


def mock_random_cards(cardList: cardTupleList, numberOfCards):
    newCardList = []
    for index in range(numberOfCards):
        newCardList.append(cardList[index][0])
    return newCardList


def mock_select_cards(argument):
    argument._selectedCardList = mock_random_cards(
        argument._cardList, argument._numberOfCards
    )


Exam._select_cards = mock_select_cards


def test_initialization():
    fileLocation = "tests/test_card_data.csv"
    numberOfCards = 6
    timePerCard = 10
    exam = Exam(fileLocation, numberOfCards, timePerCard)

    assert exam.correct_answers == 0
    assert exam.incorrect_answers == 0
    assert exam.number_of_cards == 6
    assert exam.learned == 0
    assert exam.current_card_index == 0
    assert exam.current_card_main_word == "szkoła"
    assert exam.current_card_secondary_word == "school"
    assert exam.current_card_last_answer == ""
    assert exam.current_card_last_answer_mark is None


def test_next_previous_card():
    fileLocation = "tests/test_card_data.csv"
    numberOfCards = 10
    timePerCard = 10
    exam = Exam(fileLocation, numberOfCards, timePerCard)

    assert exam.correct_answers == 0
    assert exam.incorrect_answers == 0
    assert exam.current_card_main_word == "szkoła"
    assert exam.current_card_secondary_word == "school"
    assert exam.current_card_last_answer == ""
    assert exam.current_card_last_answer_mark is None

    exam.move_to_next_previous_card(True)

    assert exam.correct_answers == 0
    assert exam.incorrect_answers == 0
    assert exam.current_card_main_word == "dziewczyna"
    assert exam.current_card_secondary_word == "girl"
    assert exam.current_card_last_answer == ""
    assert exam.current_card_last_answer_mark is None

    exam.move_to_next_previous_card(True)
    exam.move_to_next_previous_card(True)

    assert exam.correct_answers == 0
    assert exam.incorrect_answers == 0
    assert exam.current_card_main_word == "okno"
    assert exam.current_card_secondary_word == "window"
    assert exam.current_card_last_answer == ""
    assert exam.current_card_last_answer_mark is None

    for x in range(100):
        exam.move_to_next_previous_card(True)

    assert exam.correct_answers == 0
    assert exam.incorrect_answers == 0
    assert exam.current_card_main_word == "tytoń"
    assert exam.current_card_secondary_word == "tobacco"
    assert exam.current_card_last_answer == ""
    assert exam.current_card_last_answer_mark is None

    exam.move_to_next_previous_card(False)

    assert exam.correct_answers == 0
    assert exam.incorrect_answers == 0
    assert exam.current_card_main_word == "zeszyt"
    assert exam.current_card_secondary_word == "notebook"
    assert exam.current_card_last_answer == ""
    assert exam.current_card_last_answer_mark is None

    for x in range(100):
        exam.move_to_next_previous_card(False)

    assert exam.correct_answers == 0
    assert exam.incorrect_answers == 0
    assert exam.current_card_main_word == "szkoła"
    assert exam.current_card_secondary_word == "school"
    assert exam.current_card_last_answer == ""
    assert exam.current_card_last_answer_mark is None


def test_card_marking():
    fileLocation = "tests/test_card_data.csv"
    numberOfCards = 6
    timePerCard = 1
    exam = Exam(fileLocation, numberOfCards, timePerCard)

    assert exam.correct_answers == 0
    assert exam.incorrect_answers == 0
    assert exam.current_card_main_word == "szkoła"
    assert exam.current_card_secondary_word == "school"
    assert exam.current_card_last_answer == ""
    assert exam.current_card_last_answer_mark is None

    exam.mark_current_card("school")

    assert exam.correct_answers == 1
    assert exam.incorrect_answers == 0
    assert exam.current_card_main_word == "szkoła"
    assert exam.current_card_secondary_word == "school"
    assert exam.current_card_last_answer == "school"
    assert exam.current_card_last_answer_mark is True

    exam.move_to_next_previous_card(True)
    exam.move_to_next_previous_card(True)

    exam.mark_current_card("wrong guess")

    assert exam.correct_answers == 1
    assert exam.incorrect_answers == 1
    assert exam.current_card_main_word == "polska"
    assert exam.current_card_secondary_word == "poland"
    assert exam.current_card_last_answer == "wrong guess"
    assert exam.current_card_last_answer_mark is False

    exam.move_to_next_previous_card(True)

    exam.mark_current_card("wrong guess")

    assert exam.correct_answers == 1
    assert exam.incorrect_answers == 2
    assert exam.current_card_main_word == "okno"
    assert exam.current_card_secondary_word == "window"
    assert exam.current_card_last_answer == "wrong guess"
    assert exam.current_card_last_answer_mark is False


def test_completion_level_string():
    fileLocation = "tests/test_card_data.csv"
    numberOfCards = 8
    timePerCard = 10
    exam = Exam(fileLocation, numberOfCards, timePerCard)
    assert exam.number_of_cards == numberOfCards

    completion = exam.completion_level_string()
    expected = f"{1}/{numberOfCards}"
    assert completion == expected

    exam.move_to_next_previous_card(True)
    exam.move_to_next_previous_card(True)
    exam.move_to_next_previous_card(True)

    completion = exam.completion_level_string()
    expected = f"{4}/{numberOfCards}"
    assert completion == expected

    exam.move_to_next_previous_card(True)
    exam.move_to_next_previous_card(True)

    completion = exam.completion_level_string()
    expected = f"{6}/{numberOfCards}"
    assert completion == expected

    exam.move_to_next_previous_card(False)
    exam.move_to_next_previous_card(False)

    completion = exam.completion_level_string()
    expected = f"{4}/{numberOfCards}"
    assert completion == expected

    for x in range(20):
        exam.move_to_next_previous_card(True)

    completion = exam.completion_level_string()
    expected = f"{numberOfCards}/{numberOfCards}"
    assert completion == expected


def test_level_completion():
    fileLocation = "tests/test_card_data.csv"
    numberOfCards = 6
    timePerCard = 10
    exam = Exam(fileLocation, numberOfCards, timePerCard)

    assert not exam.session_completed()
    exam.mark_current_card("school")
    exam.move_to_next_previous_card(True)

    assert not exam.session_completed()
    exam.mark_current_card("girl")
    exam.move_to_next_previous_card(True)

    assert not exam.session_completed()
    exam.mark_current_card("poland")
    exam.move_to_next_previous_card(True)

    assert not exam.session_completed()
    exam.mark_current_card("window")
    exam.move_to_next_previous_card(True)

    assert not exam.session_completed()
    exam.mark_current_card("alcohol")
    exam.move_to_next_previous_card(True)

    assert not exam.session_completed()
    exam.mark_current_card("perfume")
    exam.move_to_next_previous_card(True)

    assert exam.session_completed()


def test_statistics():
    fileLocation = "tests/test_card_data.csv"
    numberOfCards = 6
    timePerCard = 10
    exam = Exam(fileLocation, numberOfCards, timePerCard)
    fileLocation = "tests/test_card_data.csv"

    exam.mark_current_card("school")
    exam.move_to_next_previous_card(True)

    exam.mark_current_card("girl")
    exam.move_to_next_previous_card(True)

    exam.mark_current_card("poland")
    exam.move_to_next_previous_card(True)

    exam.mark_current_card("window")
    exam.move_to_next_previous_card(True)

    exam.mark_current_card("alcohol")
    exam.move_to_next_previous_card(True)

    statistics = exam.statistics()
    assert statistics["exam"] is True
    assert statistics["finished"] is False
    assert statistics["correctAnswers"] == 5
    assert statistics["incorrectAnswers"] == 0
    assert statistics["learned"] == 0

    exam.mark_current_card("Wrong_guess")
    statistics = exam.statistics()
    assert statistics["exam"] is True
    assert statistics["finished"] is True
    assert statistics["correctAnswers"] == 5
    assert statistics["incorrectAnswers"] == 1
    assert statistics["learned"] == 0


def test_time():
    fileLocation = "tests/test_card_data.csv"
    numberOfCards = 6
    timePerCard = 15
    exam = Exam(fileLocation, numberOfCards, timePerCard)
    fileLocation = "tests/test_card_data.csv"

    assert exam.seconds_left == 0
    assert exam.minutes_left == 0
    for _ in range(5):
        exam.update_time()
    assert exam.seconds_left == 25
    assert exam.minutes_left == 1
    assert not exam.time_passed

    exam.mark_current_card("school")
    exam.move_to_next_previous_card(True)

    for _ in range(3):
        exam.update_time()

    assert exam.seconds_left == 22
    assert exam.minutes_left == 1
    assert not exam.time_passed

    exam.mark_current_card("girl")
    exam.move_to_next_previous_card(True)

    for _ in range(10):
        exam.update_time()

    assert exam.seconds_left == 12
    assert exam.minutes_left == 1
    assert not exam.time_passed

    exam.mark_current_card("poland")
    exam.move_to_next_previous_card(True)

    for _ in range(30):
        exam.update_time()

    assert exam.seconds_left == 42
    assert exam.minutes_left == 0
    assert not exam.time_passed

    exam.mark_current_card("window")
    exam.move_to_next_previous_card(True)

    for _ in range(50):
        exam.update_time()

    assert exam.seconds_left == 0
    assert exam.minutes_left == 0
    assert exam.time_passed

    exam.mark_current_card("alcohol")
    exam.current_card_last_answer_mark is None


def test_time_string():
    fileLocation = "tests/test_card_data.csv"
    numberOfCards = 6
    timePerCard = 15
    exam = Exam(fileLocation, numberOfCards, timePerCard)

    for _ in range(5):
        exam.update_time()
    assert exam.time_left_str == "1:25"

    for _ in range(10):
        exam.update_time()
    assert exam.time_left_str == "1:15"
    for _ in range(10):
        exam.update_time()
    assert exam.time_left_str == "1:05"

    exam.update_time()
    assert exam.time_left_str == "1:04"
    exam.update_time()
    assert exam.time_left_str == "1:03"
    exam.update_time()
    assert exam.time_left_str == "1:02"
    exam.update_time()
    assert exam.time_left_str == "1:01"
    exam.update_time()
    assert exam.time_left_str == "1:00"
    exam.update_time()
    assert exam.time_left_str == "0:59"
    for _ in range(58):
        exam.update_time()
    assert exam.time_left_str == "0:01"
    exam.update_time()
    assert exam.time_left_str == "0:00"
    for _ in range(420):
        exam.update_time()
    assert exam.time_left_str == "0:00"


def test_str():
    fileLocation = "tests/test_card_data.csv"
    numberOfCards = 6
    timePerCard = 15
    exam = Exam(fileLocation, numberOfCards, timePerCard)

    exam.mark_current_card("school")
    exam.move_to_next_previous_card(True)

    expected = "Exam: Correct: 1 Incorrect: 0"
    assert expected == str(exam)

    exam.mark_current_card("girl")
    exam.move_to_next_previous_card(True)

    expected = "Exam: Correct: 2 Incorrect: 0"
    assert expected == str(exam)

    exam.mark_current_card("Po land")
    exam.move_to_next_previous_card(True)

    expected = "Exam: Correct: 2 Incorrect: 1"
    assert expected == str(exam)

    exam.mark_current_card("window")
    exam.move_to_next_previous_card(True)

    expected = "Exam: Correct: 3 Incorrect: 1"
    assert expected == str(exam)

    exam.mark_current_card("i love")
    exam.move_to_next_previous_card(True)

    expected = "Exam: Correct: 3 Incorrect: 2"
    assert expected == str(exam)
