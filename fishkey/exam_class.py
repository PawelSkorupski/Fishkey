from session_class import Session
from file_read_write import (
    import_cards,
    draw_random_cards_priority,
    generate_statistics_data,
    seconds_to_minutes_and_seconds,
)


class NegativeTimeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Exam(Session):
    """
    ## Exam(Session) class.
    Works like Session but does not change cards buckets.

    Atributes:
    ----------

    correct_answers: int - number of correct answers in session

    incorrect_answers: int - number of incorrect answers in session

    number_of_cards: int - number of cards loaded in current session

    current_card_index: int - index of a current card in selected cards
    list

    current_card_{main_word, secondary_word, last_answer_mark, last_answer}
        - current card object parameters

    minutes_left: int - number of whole minutes left to do exam.

    seconds_left: int - number of whole seconds left to do exam.

    time_left_str: str - time left to do exam formated {minutes:seconds}
    For 1 minute and 2 seconds returns 1:02

    time_passed: bool - True if time for exam passed.
    """

    def __init__(self, fileLocation, numberOfCards: int, timePerCard: int):
        """
        # Arguments

        ## fileLocation - location of file.

        ## numberOfCards: int - number of cards to draw.

        ## timePerCard: int - time in seconds for one card.

        """
        self._fileLocation = fileLocation
        self._numberOfCards = numberOfCards

        # Counters
        self._correctAnswers = 0
        self._incorrectAnswers = 0
        self._learned = 0
        self._currentCardIndex = 0

        self._selectedCardList = []

        # Setting time counters
        if timePerCard <= 0:
            raise NegativeTimeError
        self._time_remaining = timePerCard * numberOfCards
        self._minute = 0
        self._second = 0
        self._time_passed = False

        self._cardList = import_cards(fileLocation)
        self._select_cards()

        self._currentCardObject = self._selectedCardList[0]

    def _select_cards(self):
        """
        Allows for monkeypatching.
        """
        self._selectedCardList = draw_random_cards_priority(
            self._cardList, self._numberOfCards
        )

    def update_time(self):
        """
        Updates exam time by one second.
        Should be called by interface every second.
        Implemented here to separate timer method,
        because it can be done diferently depending
        on QUI implementation.
        """
        # Decrement counter by 1
        if not self._time_passed:
            self._time_remaining -= 1

            timeTuple = seconds_to_minutes_and_seconds(self._time_remaining)

            self._minute, self._second = timeTuple
            if self._time_remaining == 0:
                self._time_passed = True

    def validate_current_card(self, userGuess: str) -> None:
        """
        Method that marks current card without changing bucket.
        """
        if self._currentCardObject.mark(userGuess):
            self._correctAnswers += 1
        else:
            self._incorrectAnswers += 1

    def mark_current_card(self, userGuess) -> None:
        """
        Overwrites mark_current_card to use
        validate_current_card insted.
        """
        if not self._time_passed:
            self.validate_current_card(userGuess)

    def _change_card(self, cardIndex: int) -> None:
        """
        Overwrites change_card - Session method,
        so it doesn't need buckets.
        """
        self._currentCardIndex = cardIndex
        self._currentCardObject = self._selectedCardList[cardIndex]

    def statistics(self) -> dict:
        """
        Overwrites statistics - Session method,
        to save correct exam information
        """
        isFinished = (
            self._correctAnswers + self._incorrectAnswers
            == self._numberOfCards
        )
        statistics = generate_statistics_data(
            True,
            isFinished,
            0,
            self._correctAnswers,
            self._incorrectAnswers,
            0,
        )
        return statistics

    def __str__(self):
        correct = self._correctAnswers
        incorrect = self._incorrectAnswers
        return f"Exam: Correct: {correct} Incorrect: {incorrect}"

    @property
    def time_passed(self) -> bool:
        """
        Returns information if time passed and no answers
        can be marked.
        """
        return self._time_passed

    @property
    def minutes_left(self):
        return self._minute

    @property
    def seconds_left(self):
        return self._second

    @property
    def time_left_str(self) -> str:
        """
        Returns string with formated time left to finish exam.
        """
        minutes, seconds = seconds_to_minutes_and_seconds(self._time_remaining)
        if seconds < 10:
            seconds = f"0{seconds}"
        return f"{minutes}:{seconds}"
