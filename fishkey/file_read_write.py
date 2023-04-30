import os
import csv
import json
import random
from card import Card
from datetime import datetime


class EmptyBucketsError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class IncorrectFileFormatError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NonExistantBucketError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


"""
    "CardTuple" is really a 2 element list containing card object and
    a number of designated bucket. "Tuple" in name used to differentiate
    from `cardList`.
"""
cardTuple = tuple[Card, int]
cardTupleList = list[cardTuple]
bucketList = list[list[Card]]


def import_cards(fileLocation: str) -> cardTupleList:
    """
    Method that reads in from comma spearated csv file.
    Returns list containing tuples: (card, bucket)
    File format:

    [main word], [secondary word], [correct], [incorrect],
    [correctInRow], [incorrectInRow], [priority], [bucket]

    Arguments
    ---------
    fileLocation : str

    """
    cardList = []
    with open(fileLocation, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            try:
                (
                    mainWord,
                    secondaryWord,
                    correct,
                    incorrect,
                    correctInRow,
                    incorrectInRow,
                    priority,
                    bucket,
                ) = row
            except ValueError as e:
                raise IncorrectFileFormatError(e)
            correct = int(correct)
            incorrect = int(incorrect)
            correctInRow = int(correctInRow)
            incorrectInRow = int(incorrectInRow)
            priority = int(priority)
            bucket = int(bucket)
            card = Card(
                mainWord,
                secondaryWord,
                correct,
                incorrect,
                correctInRow,
                incorrectInRow,
                priority,
            )
            cardWithBucket = [card, bucket]
            cardList.append(cardWithBucket)
    if len(cardList) == 0:
        raise IncorrectFileFormatError
    return cardList


def export_cards(fileLocation: str, cardList: cardTupleList) -> None:
    """
    Method that saves to comma spearated csv file.
    File format:

    [main word], [secondary word], [correct], [incorrect],
    [correctInRow], [incorrectInRow], [priority], [bucket]

    Arguments
    ---------
    fileLocation : str
    """
    with open(fileLocation, "w", encoding="utf-8", newline="") as file:
        cardList = sort_cards(cardList)
        writer = csv.writer(file)
        for cardTupple in cardList:
            card, bucket = cardTupple
            mainWord = card.mainWord
            secondaryWord = card.secondaryWord
            correct = card.correctAnswers
            incorrect = card.incorrectAnswers
            correctInRow = card.correctAnswersInRow
            incorrectInRow = card.incorrectAnswersInRow
            priority = card.priority
            row = [
                mainWord,
                secondaryWord,
                correct,
                incorrect,
                correctInRow,
                incorrectInRow,
                priority,
                bucket,
            ]
            writer.writerow(row)


def statistics_data_file_name(fileLocation: str) -> str:
    """
    Generates correct statistics data file location.
    Changes .csv at the end of a file to _stats.json

    Ex. For file "data_en_pl.cvs" correct file name with
    statistic data is "data_en_pl_stats.json"
    """
    fileLocation, ext = os.path.splitext(fileLocation)
    return fileLocation + "_stats.json"


def generate_statistics_data(
    isExam: bool,
    isFinished: bool,
    lastBucket: int,
    correctAnswers: int,
    incorrectAnswers: int,
    learned: int,
) -> dict:
    """
    Method that takes statistics about session or exam,
    return dictionary with formated data.
    """
    statistics = {}
    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    statistics["exam"] = isExam
    statistics["finished"] = isFinished
    statistics["date_and_time"] = date_string
    statistics["lastBucket"] = lastBucket
    statistics["correctAnswers"] = correctAnswers
    statistics["incorrectAnswers"] = incorrectAnswers
    statistics["learned"] = learned

    return statistics


def export_session_stats(fileLocation: str, stats: dict) -> None:
    try:
        with open(fileLocation, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            size = len(json_data)
            json_data[str(size + 1)] = stats
    except FileNotFoundError:
        json_data = {"1": stats}
    with open(fileLocation, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4)


def import_session_stats(fileLocation: str) -> dict:
    with open(fileLocation, "r", encoding="utf-8") as file:
        json_data = json.load(file)
        return json_data


def sort_cards(cardList: cardTupleList) -> cardTupleList:
    """
    Sorts cards based on card priority.

    Arguments
    ---------
    cardList : cardTupleList

    """
    return sorted(
        cardList, key=lambda cardTuple: cardTuple[0].priority, reverse=True
    )


def split_to_buckets(cardList, numberOfBuckets: int) -> bucketList:
    """
    Splits cards to buckets; depending on cardTuple second element.

    Aguments:
    ---------

    cardList - list containing tupples (Card, bucketNumber)
    """
    buckets = []
    for number in range(numberOfBuckets + 1):
        buckets.append([])

    for cardTuple in cardList:
        card, bucket = cardTuple
        if bucket > numberOfBuckets:
            raise NonExistantBucketError
        buckets[bucket].append(card)
    return buckets


def count_buckets_elements(bucketsList: bucketList) -> int:
    """
    Method counting all cards inside of bucket lists.

    Arguments:
    ----------

    bucketsList : bucketList - list containting buckets [lists].
    """
    counter = 0
    for bucket in bucketsList:
        counter += len(bucket)
    return counter


def count_cards_to_N_bucket(
    cardList: cardTupleList, Nbucket: int, maxBucket
) -> int:
    buckets = split_to_buckets(cardList, maxBucket)
    buckets = buckets[0:Nbucket + 1]
    return count_buckets_elements(buckets)


def merge_buckets(bucketsList: bucketList) -> cardTupleList:
    """
    Method that merges bucketList to one cardList of cardTupples.

    Arguments:
    ----------

    bucketsList : bucketList - list containting buckets [lists].
    """
    cardList = []
    for bucketId, bucket in enumerate(bucketsList):
        for card in bucket:
            cardList.append([card, bucketId])
    if len(cardList) == 0:
        raise EmptyBucketsError
    return cardList


def draw_random_cards_priority(
    cardList: cardTupleList, numberOfCards: int
) -> list[Card]:
    """
    Returns a random list of cards, size: numberOfCards.
    Card priority is taken into consideration while drawing cards.
    Returned list doesn't have multiples.


    Arguments:
    ----------

    cardList : cardTupleList

    numberOfCards : int - number of cards to draw.
    """
    randomCardSet = set([])
    cardList = [card for card, bucket in cardList]
    priorityList = [card.priority for card in cardList]
    while len(randomCardSet) != numberOfCards:
        randomCard = random.choices(cardList, priorityList)
        randomCardSet.add(randomCard[0])
    return list(randomCardSet)


def seconds_to_minutes_and_seconds(timeInSeconds) -> tuple[int, int]:
    minutes = timeInSeconds // 60
    seconds = timeInSeconds % 60

    return (minutes, seconds)
