from card import Card


def test_normalize_input():
    card = Card("Książka", "abook", 0, 0, 0, 0, 2)
    assert card.normalize_input("Książka") == "książka"
    assert card.normalize_input(" OKNO ") == "okno"
    assert card.normalize_input(" Pierwsze Drugie ") == "pierwsze drugie"
    assert card.normalize_input(" Idealne, pokrycie ") == "idealne pokrycie"


def test_create_cards():
    card = Card("Książka", " a book", 0, 2, 0, 0, 3)
    assert card.mainWord == "książka"
    assert card.secondaryWord == "a book"
    assert card.correctAnswers == 0
    assert card.incorrectAnswers == 2
    assert card.priority == 3


def test_card_modification():
    card = Card("Książka", " a book", 0, 2, 0, 0, 2)
    card.mainWord = " Stół"
    card.secondaryWord = "a, table "
    card.correctAnswers += 1
    card.incorrectAnswers -= 1
    card.priority = 5

    assert card.mainWord == "stół"
    assert card.secondaryWord == "a table"
    assert card.correctAnswers == 1
    assert card.incorrectAnswers == 1
    assert card.priority == 5


def test_validate_answer():
    card = Card("Książka", "a book", 0, 2, 0, 1, 2)
    assert card.validate_answer(" A BOOK")
    assert not card.validate_answer("a booklet")


def test_mark_answer():
    card = Card("Książka", "a book", 0, 2, 1, 0, 3)
    assert card.validate_answer(" A BOOK")
    assert card.correctAnswers == 0
    assert card.incorrectAnswers == 2
    assert card.lastAnswerMark is None
    assert card.mark("A book")
    assert card.correctAnswers == 1
    assert card.incorrectAnswers == 2
    assert card.correctAnswersInRow == 2
    assert card.incorrectAnswersInRow == 0
    assert card.lastAnswerMark is True
    assert card.mark("A BooK")
    assert card.correctAnswersInRow == 3
    assert card.incorrectAnswersInRow == 0
    assert card.lastAnswerMark is True
    assert not card.mark("A clock")
    assert card.correctAnswers == 2
    assert card.incorrectAnswers == 3
    assert card.correctAnswersInRow == 0
    assert card.incorrectAnswersInRow == 1
    assert card.lastAnswerMark is False
    assert not card.mark("An umbrella")
    assert card.correctAnswersInRow == 0
    assert card.incorrectAnswersInRow == 2


def test_clear():
    card = Card("Książka", "a book", 0, 2, 0, 0, 1)
    assert card.mark(" A BOOK")
    assert card.mark("a book")
    assert card.mark("A bOOk")
    assert card.correctAnswersInRow == 3
    assert card.incorrectAnswersInRow == 0
    card.clear_last_answers()
    assert card.correctAnswersInRow == 0
    assert card.incorrectAnswersInRow == 0


def test_calculate_bucket():
    card = Card("Książka", "a book", 4, 2, 1, 0, 1)
    card.mark("a book")
    assert card.calculate_next_bucket(1, 5, 3) == 2
    card2 = Card("Książka", "a book", 4, 2, 4, 0, 4)
    card2.mark("a book")
    assert card2.calculate_next_bucket(5, 10, 3) == 10
    card3 = Card("Książka", "a book", 4, 2, 0, 1, 4)
    card3.mark("a booklet")
    assert card3.calculate_next_bucket(5, 10, 3) == 4
    card4 = Card("Książka", "a book", 4, 2, 0, 2, 4)
    card4.mark("a booklet")
    assert card4.calculate_next_bucket(5, 10, 3) == 0


def test_str():
    card = Card("Książka", "a book", 4, 2, 1, 0, 1)
    card.mark("a book")
    expected = "książka:a book Last answer mark: True"
    assert str(card) == expected
    card = Card("Książka", "a book", 8, 4, 1, 6, 1)
    card.mark("a booking.com")
    expected = "książka:a book Last answer mark: False"
