from session_class import Session


def test_initialization():
    fileLocation = "tests/test_card_data.csv"
    bucketsTotal = 5
    lastBucket = 2
    session = Session(fileLocation, bucketsTotal, lastBucket)

    assert session.correct_answers == 0
    assert session.incorrect_answers == 0
    assert session.number_of_cards == 6
    assert session.learned == 0
    assert session.current_card_index == 0
    assert session.current_card_main_word == "szkoła"
    assert session.current_card_secondary_word == "school"
    assert session.current_card_last_answer == ""
    assert session.current_card_last_answer_mark is None


def test_next_previous_card():
    fileLocation = "tests/test_card_data.csv"
    bucketsTotal = 5
    lastBucket = 5
    session = Session(fileLocation, bucketsTotal, lastBucket)

    assert session.correct_answers == 0
    assert session.incorrect_answers == 0
    assert session.current_card_main_word == "szkoła"
    assert session.current_card_secondary_word == "school"
    assert session.current_card_last_answer == ""
    assert session.current_card_last_answer_mark is None

    session.move_to_next_previous_card(True)

    assert session.correct_answers == 0
    assert session.incorrect_answers == 0
    assert session.current_card_main_word == "dziewczyna"
    assert session.current_card_secondary_word == "girl"
    assert session.current_card_last_answer == ""
    assert session.current_card_last_answer_mark is None

    session.move_to_next_previous_card(True)
    session.move_to_next_previous_card(True)

    assert session.correct_answers == 0
    assert session.incorrect_answers == 0
    assert session.current_card_main_word == "okno"
    assert session.current_card_secondary_word == "window"
    assert session.current_card_last_answer == ""
    assert session.current_card_last_answer_mark is None

    for x in range(100):
        session.move_to_next_previous_card(True)

    assert session.correct_answers == 0
    assert session.incorrect_answers == 0
    assert session.current_card_main_word == "tytoń"
    assert session.current_card_secondary_word == "tobacco"
    assert session.current_card_last_answer == ""
    assert session.current_card_last_answer_mark is None

    session.move_to_next_previous_card(False)

    assert session.correct_answers == 0
    assert session.incorrect_answers == 0
    assert session.current_card_main_word == "zeszyt"
    assert session.current_card_secondary_word == "notebook"
    assert session.current_card_last_answer == ""
    assert session.current_card_last_answer_mark is None

    for x in range(100):
        session.move_to_next_previous_card(False)

    assert session.correct_answers == 0
    assert session.incorrect_answers == 0
    assert session.current_card_main_word == "szkoła"
    assert session.current_card_secondary_word == "school"
    assert session.current_card_last_answer == ""
    assert session.current_card_last_answer_mark is None


def test_card_marking():
    fileLocation = "tests/test_card_data.csv"
    bucketsTotal = 5
    lastBucket = 5
    session = Session(fileLocation, bucketsTotal, lastBucket)

    assert session.correct_answers == 0
    assert session.incorrect_answers == 0
    assert session.current_card_main_word == "szkoła"
    assert session.current_card_secondary_word == "school"
    assert session.current_card_last_answer == ""
    assert session.current_card_last_answer_mark is None

    session.mark_current_card("school")

    assert session.correct_answers == 1
    assert session.incorrect_answers == 0
    assert session.current_card_main_word == "szkoła"
    assert session.current_card_secondary_word == "school"
    assert session.current_card_last_answer == "school"
    assert session.current_card_last_answer_mark is True
    # Card internal correct in a row answers >= 3
    assert session._currentBucket == 5

    session.move_to_next_previous_card(True)
    session.move_to_next_previous_card(True)

    session.mark_current_card("wrong guess")

    assert session.correct_answers == 1
    assert session.incorrect_answers == 1
    assert session.current_card_main_word == "polska"
    assert session.current_card_secondary_word == "poland"
    assert session.current_card_last_answer == "wrong guess"
    assert session.current_card_last_answer_mark is False
    assert session._currentBucket == 1

    session.move_to_next_previous_card(True)

    session.mark_current_card("wrong guess")

    assert session.correct_answers == 1
    assert session.incorrect_answers == 2
    assert session.current_card_main_word == "okno"
    assert session.current_card_secondary_word == "window"
    assert session.current_card_last_answer == "wrong guess"
    assert session.current_card_last_answer_mark is False
    assert session._currentBucket == 1


def test_completion_level_string():
    fileLocation = "tests/test_card_data.csv"
    bucketsTotal = 5
    lastBucket = 5
    numberOfCards = 10
    session = Session(fileLocation, bucketsTotal, lastBucket)
    assert session.number_of_cards == numberOfCards

    completion = session.completion_level_string()
    expected = f"{1}/{numberOfCards}"
    assert completion == expected

    session.move_to_next_previous_card(True)
    session.move_to_next_previous_card(True)
    session.move_to_next_previous_card(True)

    completion = session.completion_level_string()
    expected = f"{4}/{numberOfCards}"
    assert completion == expected

    session.move_to_next_previous_card(True)
    session.move_to_next_previous_card(True)

    completion = session.completion_level_string()
    expected = f"{6}/{numberOfCards}"
    assert completion == expected

    session.move_to_next_previous_card(False)
    session.move_to_next_previous_card(False)

    completion = session.completion_level_string()
    expected = f"{4}/{numberOfCards}"
    assert completion == expected

    for x in range(20):
        session.move_to_next_previous_card(True)

    completion = session.completion_level_string()
    expected = f"{numberOfCards}/{numberOfCards}"
    assert completion == expected


def test_level_completion():
    fileLocation = "tests/test_card_data.csv"
    bucketsTotal = 5
    lastBucket = 2
    session = Session(fileLocation, bucketsTotal, lastBucket)

    assert not session.session_completed()
    session.mark_current_card("school")
    session.move_to_next_previous_card(True)

    assert not session.session_completed()
    session.mark_current_card("girl")
    session.move_to_next_previous_card(True)

    assert not session.session_completed()
    session.mark_current_card("poland")
    session.move_to_next_previous_card(True)

    assert not session.session_completed()
    session.mark_current_card("window")
    session.move_to_next_previous_card(True)

    assert not session.session_completed()
    session.mark_current_card("alcohol")
    session.move_to_next_previous_card(True)

    assert not session.session_completed()
    session.mark_current_card("perfume")
    session.move_to_next_previous_card(True)

    assert session.session_completed()


def test_statistics():
    fileLocation = "tests/test_card_data.csv"
    bucketsTotal = 5
    lastBucket = 2
    session = Session(fileLocation, bucketsTotal, lastBucket)

    session.mark_current_card("school")
    session.move_to_next_previous_card(True)

    session.mark_current_card("girl")
    session.move_to_next_previous_card(True)

    session.mark_current_card("poland")
    session.move_to_next_previous_card(True)

    session.mark_current_card("window")
    session.move_to_next_previous_card(True)

    session.mark_current_card("alcohol")
    session.move_to_next_previous_card(True)

    statistics = session.statistics()
    assert statistics["exam"] is False
    assert statistics["finished"] is False
    assert statistics["lastBucket"] == 2
    assert statistics["correctAnswers"] == 5
    assert statistics["incorrectAnswers"] == 0
    assert statistics["learned"] == 0

    session.mark_current_card("Wrong_guess")
    statistics = session.statistics()
    assert statistics["exam"] is False
    assert statistics["finished"] is True
    assert statistics["lastBucket"] == 2
    assert statistics["correctAnswers"] == 5
    assert statistics["incorrectAnswers"] == 1
    assert statistics["learned"] == 0


def test_str():
    fileLocation = "tests/test_card_data.csv"
    bucketsTotal = 5
    lastBucket = 2
    session = Session(fileLocation, bucketsTotal, lastBucket)

    session.mark_current_card("school")
    session.move_to_next_previous_card(True)

    expected = "Session: Correct: 1 Incorrect: 0"
    assert expected == str(session)

    session.mark_current_card("girl")
    session.move_to_next_previous_card(True)

    expected = "Session: Correct: 2 Incorrect: 0"
    assert expected == str(session)

    session.mark_current_card("Po land")
    session.move_to_next_previous_card(True)

    expected = "Session: Correct: 2 Incorrect: 1"
    assert expected == str(session)

    session.mark_current_card("window")
    session.move_to_next_previous_card(True)

    expected = "Session: Correct: 3 Incorrect: 1"
    assert expected == str(session)

    session.mark_current_card("i love")
    session.move_to_next_previous_card(True)

    expected = "Session: Correct: 3 Incorrect: 2"
    assert expected == str(session)
