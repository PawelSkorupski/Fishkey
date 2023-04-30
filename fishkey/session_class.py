from file_read_write import (
    import_cards,
    export_cards,
    split_to_buckets,
    count_cards_to_N_bucket,
    merge_buckets,
    export_session_stats,
    statistics_data_file_name,
    generate_statistics_data,
)
from configuration import consider_learned


class Session:
    """
    ## Session class.

    Atributes:
    ----------

    correct_answers: int - number of correct answers in session

    incorrect_answers: int - number of incorrect answers in session

    number_of_cards: int - number of cards loaded in current session

    learned: int - number of cards learned in current session ->
    Number of cards that got to the last bucket because of the correct
    answer in current session.

    current_card_index: int - index of a current card in selected cards
    list

    current_card_{main_word, secondary_word, last_answer_mark, last_answer}
        - current card object parameters
    """

    def __init__(self, fileLocation, bucketsTotal, lastBucket):
        self._fileLocation = fileLocation
        self._numberOfBuckets = bucketsTotal
        self._lastBucket = lastBucket

        # Counters
        self._correctAnswers = 0
        self._incorrectAnswers = 0
        self._learned = 0
        self._currentCardIndex = 0

        self._cardList = import_cards(self._fileLocation)

        self._importedBuckets = split_to_buckets(
            self._cardList, self._numberOfBuckets
        )

        self._buckets = self._importedBuckets[0:self._lastBucket + 1]

        self._numberOfCards = count_cards_to_N_bucket(
            self._cardList, self._lastBucket, self._numberOfBuckets
        )

        self._selectedCardList = merge_buckets(self._buckets)
        cardTuple = self._selectedCardList[0]
        self._currentCardObject, self._currentBucket = cardTuple

    def _change_card(self, cardIndex: int) -> None:
        """
        Changes current card object to a card from selectedCardList
        of cardIndex element

        Arguments:
        ----------

        cardIndex: int - selectedCardList list index. Must be in range
        from 0 to numberOfCards

        """
        self._currentCardIndex = cardIndex
        self._currentCardObject, self._currentBucket = self._selectedCardList[
            cardIndex
        ]

    def move_to_next_previous_card(self, forward: bool) -> None:
        """
        Changes currentCardIndex to next or previous number,
        and calls change_card method to change current card object.
        Makes not to go out of bound of selectedCardList.
        """
        if forward:
            self._currentCardIndex = min(
                self._currentCardIndex + 1, self._numberOfCards - 1
            )
        else:
            self._currentCardIndex = max(self._currentCardIndex - 1, 0)
        self._change_card(self._currentCardIndex)

    def _current_card_next_bucket(self) -> int:
        """
        Gets next bucket of current card object.
        """
        nextBucket = self._currentCardObject.calculate_next_bucket(
            self._currentBucket, self._numberOfBuckets, consider_learned
        )
        return nextBucket

    def _change_current_card_bucket(self):
        """
        Changes current card bucket to next bucket.
        Checks if the card was just learned.
        Saves new bucket to cardList.
        """
        currentBucket = self._currentBucket
        nextBucket = self._current_card_next_bucket()

        if currentBucket == nextBucket and nextBucket == self._numberOfBuckets:
            self._learned += 1

        cardListIndex = self._cardList.index(
            [self._currentCardObject, self._currentBucket]
        )
        self._cardList[cardListIndex][1] = nextBucket
        self._currentBucket = nextBucket

    def mark_current_card(self, userGuess) -> None:
        """
        Marks current card object and changes correct and
        incorrect answers counter.
        """
        if self._currentCardObject.mark(userGuess):
            self._correctAnswers += 1
        else:
            self._incorrectAnswers += 1

        self._change_current_card_bucket()

    def statistics(self) -> dict:
        isFinished = (
            self._correctAnswers + self._incorrectAnswers
            == self._numberOfCards
        )
        statistics = generate_statistics_data(
            False,
            isFinished,
            self._lastBucket,
            self._correctAnswers,
            self._incorrectAnswers,
            self._learned,
        )
        return statistics

    def save_statistics(self):
        statsFileLocation = statistics_data_file_name(self._fileLocation)
        statistics = self.statistics()
        export_session_stats(statsFileLocation, statistics)

    def save_session(self):
        export_cards(self._fileLocation, self._cardList)

    def completion_level_string(self) -> str:
        """
        Returns a string with current card index/number of cards.
        Level of session copletion.
        """
        return f"{self._currentCardIndex + 1}/{self._numberOfCards}"

    def session_completed(self) -> bool:
        """
        Returns true if current session is completed.
        All cards have been completed.
        """
        cards_done = self._correctAnswers + self._incorrectAnswers
        return cards_done == self._numberOfCards

    def __str__(self):
        correct = self._correctAnswers
        incorrect = self._incorrectAnswers
        return f"Session: Correct: {correct} Incorrect: {incorrect}"

    @property
    def correct_answers(self) -> int:
        """
        Session correct answers counter.
        """
        return self._correctAnswers

    @property
    def incorrect_answers(self) -> int:
        """
        Session incorrect answers counter.
        """
        return self._incorrectAnswers

    @property
    def number_of_cards(self) -> int:
        """
        Number of cards in current session.
        """
        return self._numberOfCards

    @property
    def learned(self) -> int:
        """
        Number of learned cards in current session.
        """
        return self._learned

    @property
    def current_card_index(self) -> int:
        return self._currentCardIndex

    @property
    def current_card_main_word(self) -> str:
        return self._currentCardObject.mainWord

    @property
    def current_card_secondary_word(self) -> str:
        return self._currentCardObject.secondaryWord

    @property
    def current_card_last_answer_mark(self) -> bool:
        return self._currentCardObject.lastAnswerMark

    @property
    def current_card_last_answer(self) -> str:
        return self._currentCardObject.lastAnswer
