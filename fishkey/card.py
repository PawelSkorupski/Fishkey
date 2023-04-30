class Card:
    """
    ## Card class.

    Atributes
    ---------
    mainWord : str
        a word that will be shown in the main window
    secondaryWord : str
        a word with ex. translation
    correctAnswers : int
        contains a number of correct answers
    incorrectAnswers : int
        contains a number of incorrect answers

    Methods
    -------
    normalize_input(input : str) -> str
        a method that changes all letters to lower case
        and removes ',' signs, blank spaces
    validate_answer(answer : str) -> bool
        returns True when the answer is correct
    mark(answer : str) -> bool
        returns True when the answer is correct,
        and changes correct and incorrect answer coutners
    clear_last_answers() -> None
        Clears correct and incorrect in a row counters.
        Can be used after closing session.
    calculate_next_bucket(current_bucket: int, max_bucket: int) -> int
        Calculates in which bucket card should be placed based on
        last answers.
        If user answered correctly 3 times in a row
        card is returns last bucket number, and the card is considered
        as "learned".
        If user gave wrong answer third time in a row, method returns 0,
        it means that the card will be placed at the beggining.
        Any other combination of answers, results in `current_bucket + 1`
        if last answer was correct, or `current_bucket - 1`
        if last answer was wrong.

    """

    def normalize_input(self, inputString: str) -> str:
        inputString = inputString.strip()
        inputString = inputString.lower()
        inputString = inputString.replace(",", "")
        return inputString

    def __init__(
        self,
        mainWord: str,
        secondaryWord: str,
        correct: int,
        incorrect: int,
        correctInRow: int,
        incorrectInRow: int,
        priority: int,
    ) -> None:
        self._mainWord = self.normalize_input(mainWord)
        self._secondaryWord = self.normalize_input(secondaryWord)
        self._correctAnswers = correct
        self._incorrectAnswers = incorrect
        # Ensuring no erorors while drawing random cards with priority
        # Priority has to be higher than 0.
        self._priority = max(1, priority)

        self._correctAnswersInRow = correctInRow
        self._incorrectAnswersInRow = incorrectInRow
        self._lastAnswerMark = None
        self._lastAnswer = ""

    def validate_answer(self, answer: str) -> bool:
        """
        Validates answer, returns true if parameter is
        the same as card seconary word. Does not change
        correct and incorrect answer counters.
        """
        answer = self.normalize_input(answer)
        return self._secondaryWord == answer

    def mark(self, answer) -> bool:
        """
        Marks answer, returns true or false based on the
        answer, and **changes** correct and incorrect answer counters.
        """
        self._lastAnswer = answer
        if self.validate_answer(answer):
            self._correctAnswers += 1
            self._correctAnswersInRow += 1
            self._incorrectAnswersInRow = 0
            self._lastAnswerMark = True
            return True
        else:
            self._incorrectAnswers += 1
            self._incorrectAnswersInRow += 1
            self._correctAnswersInRow = 0
            self._lastAnswerMark = False
            return False

    def clear_last_answers(self) -> None:
        """
        Clears correct and incorrect IN A ROW counters.
        """
        self._correctAnswersInRow = 0
        self._incorrectAnswersInRow = 0

    def calculate_next_bucket(
        self, current_bucket: int, max_bucket: int, consider_learned: int
    ) -> int:
        if self._correctAnswersInRow >= consider_learned:
            return max_bucket
        elif self._incorrectAnswersInRow >= consider_learned:
            return 0
        elif self._lastAnswerMark:
            return min(current_bucket + 1, max_bucket)
        else:
            return max(0, current_bucket - 1)

    def __str__(self):
        main = self._mainWord
        secondary = self._secondaryWord
        mark = self._lastAnswerMark
        return f"{main}:{secondary} Last answer mark: {mark}"

    @property
    def mainWord(self) -> str:
        return self._mainWord

    @property
    def secondaryWord(self) -> str:
        return self._secondaryWord

    @property
    def correctAnswers(self) -> int:
        return self._correctAnswers

    @property
    def incorrectAnswers(self) -> int:
        return self._incorrectAnswers

    @property
    def correctAnswersInRow(self) -> int:
        return self._correctAnswersInRow

    @property
    def incorrectAnswersInRow(self) -> int:
        return self._incorrectAnswersInRow

    @property
    def lastAnswerMark(self) -> bool:
        return self._lastAnswerMark

    @property
    def lastAnswer(self) -> str:
        return self._lastAnswer

    @property
    def priority(self) -> str:
        return self._priority

    @mainWord.setter
    def mainWord(self, newWord: str) -> None:
        self._mainWord = self.normalize_input(newWord)

    @secondaryWord.setter
    def secondaryWord(self, newWord: str) -> None:
        self._secondaryWord = self.normalize_input(newWord)

    @correctAnswers.setter
    def correctAnswers(self, newNumber: int) -> None:
        self._correctAnswers = newNumber

    @incorrectAnswers.setter
    def incorrectAnswers(self, newNumber: int) -> None:
        self._incorrectAnswers = newNumber

    @priority.setter
    def priority(self, newPriority: int) -> None:
        self._priority = newPriority
