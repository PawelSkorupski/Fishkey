from card import Card
from file_read_write import split_to_buckets

cardTuple = list[Card, int]
cardTupleList = list[cardTuple]
bucketList = list[list[Card]]


class NotEnoughDataToDisplayError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def count_learned(cardList: cardTupleList, maxBucket: int) -> int:
    """
    Method that returns a number of cards in the last bucket -> learned.

    Arguments
    ---------

    cardList - list containing tupples (Card, bucketNumber)

    maxBucket - a number of biggest bucket.
    """
    counter = 0
    for card, bucket in cardList:
        if bucket == maxBucket:
            counter += 1
    return counter


def count_in_buckets(cardList: cardTupleList, maxBucket: int) -> list[int]:
    """
    Returns a dictionary with numbers of cards in specific buckets.

    Arguments
    ---------

    cardList - list containing tupples (Card, bucketNumber)

    maxBucket - a number of biggest bucket.
    """
    counter = [0 for _ in range(0, maxBucket + 1)]
    buckets = split_to_buckets(cardList, maxBucket)
    for bucketNumber, bucket in enumerate(buckets):
        counter[bucketNumber] = len(bucket)
    if counter == [0 for _ in range(0, maxBucket + 1)]:
        raise NotEnoughDataToDisplayError
    return counter


def total_correct_incorrect_answers(cardList: cardTupleList) -> list:
    """
    Method that returns a tuple with sum of correct and incorrect answers
    taken from all cards in list.

    Arguments
    ---------

    cardList - list containing tupples (Card, bucketNumber)
    """
    correctAnswersCounter = 0
    incorrectAnswersCounter = 0
    for card, bucket in cardList:
        correctAnswersCounter += card.correctAnswers
        incorrectAnswersCounter += card.incorrectAnswers
    if correctAnswersCounter == 0 and incorrectAnswersCounter == 0:
        raise NotEnoughDataToDisplayError
    return [correctAnswersCounter, incorrectAnswersCounter]


def count_exams(jsonData: dict) -> int:
    """
    Method counting all exams inside of session save file.

    Arguments
    ---------

    jsonData: dict - dictionary with sessions and exams save data.
    """

    counter = 0
    for element in jsonData:
        if jsonData[element]["exam"] is True:
            counter += 1
    if counter == 0:
        raise NotEnoughDataToDisplayError
    return counter


def count_finished_sessions(jsonData: dict) -> int:
    """
    Method counting all finished sessions inside of session save file.

    Arguments
    ---------

    jsonData: dict - dictionary with sessions and exams save data.
    """
    counter = 0
    for element in jsonData:
        if (
            jsonData[element]["exam"] is False
            and jsonData[element]["finished"] is True
        ):
            counter += 1
    if counter == 0:
        raise NotEnoughDataToDisplayError
    return counter


def average_exam_score(jsonData: dict) -> float:
    """
    Method calculating average exam score from all exams stored
    inside of session save file. Returns score in precentages.

    Arguments
    ---------

    jsonData: dict - dictionary with sessions and exams save data.
    """
    scoreList = []
    for element in jsonData:
        if jsonData[element]["exam"] is True:
            correct = jsonData[element]["correctAnswers"]
            incorrect = jsonData[element]["incorrectAnswers"]
            if correct + incorrect == 0:
                raise NotEnoughDataToDisplayError
            scoreList.append(correct / (correct + incorrect))
    if len(scoreList) == 0:
        raise NotEnoughDataToDisplayError
    return round((sum(scoreList) / len(scoreList)) * 100, 2)


def average_session_score(jsonData: dict) -> float:
    """
    Method calculating average session score from finished sessions
    stored inside of session save file. Returns score in precentages.

    Arguments
    ---------

    jsonData: dict - dictionary with sessions and exams save data.
    """
    scoreList = []
    for element in jsonData:
        if (
            jsonData[element]["exam"] is False
            and jsonData[element]["finished"] is True
        ):
            correct = jsonData[element]["correctAnswers"]
            incorrect = jsonData[element]["incorrectAnswers"]
            scoreList.append(correct / (correct + incorrect))
    if len(scoreList) == 0:
        raise NotEnoughDataToDisplayError
    return round((sum(scoreList) / len(scoreList)) * 100, 2)
