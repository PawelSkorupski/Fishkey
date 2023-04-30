from card import Card
from file_rw import (
    EmptyBucketsError,
    IncorrectFileFormatError,
    NonExistantBucketError,
    import_cards,
    export_cards,
    statistics_data_file_name,
    generate_statistics_data,
    export_session_stats,
    import_session_stats,
    sort_cards,
    split_to_buckets,
    count_buckets_elements,
    count_cards_to_N_bucket,
    merge_buckets,
    draw_random_cards_priority,
)
import os
from unittest.mock import Mock
from pytest import raises


def test_importing_list():
    cardList = import_cards("tests/test_card_data.csv")
    card0, bucket = cardList[0]
    assert card0.mainWord == "szkoła"
    assert card0.incorrectAnswers == 0
    assert bucket == 1
    lastCard, bucket = cardList[-1]
    assert lastCard.mainWord == "tytoń"
    assert lastCard.secondaryWord == "tobacco"
    assert lastCard.correctAnswers == 0
    assert lastCard.incorrectAnswers == 3
    assert bucket == 5
    multipleWordCard, bucket = cardList[-4]
    assert multipleWordCard.mainWord == "zupa pomidorowa"
    assert multipleWordCard.secondaryWord == "tomato soup"
    assert multipleWordCard.correctAnswers == 0
    assert multipleWordCard.incorrectAnswers == 3
    assert bucket == 3


def test_importing_incorrect_data():
    with raises(IncorrectFileFormatError):
        import_cards("tests/incorrect_data.csv")


def test_export_cards():
    cardList = import_cards("tests/test_card_data.csv")
    test_file = "test_exp.csv"
    export_cards(test_file, cardList)
    exportedList = import_cards("test_exp.csv")
    for original, exported in zip(cardList, exportedList):
        oCard, oBucket = original
        eCard, eBucket = exported
        assert oCard.mainWord == eCard.mainWord
    os.remove(test_file)


def test_splitting():
    card1 = Card("word", "word", 1, 1, 1, 1, 5)
    card2 = Card("word", "word", 2, 1, 1, 1, 5)
    card3 = Card("word", "word", 1, 2, 1, 1, 5)
    card4 = Card("word", "word", 1, 2, 3, 1, 5)
    card5 = Card("word", "word", 1, 2, 3, 4, 8)
    card6 = Card("word", "word", 1, 2, 3, 4, 8)
    card7 = Card("word", "word", 1, 2, 4, 4, 9)
    cardList = [
        [card1, 3],
        [card2, 1],
        [card3, 5],
        [card4, 5],
        [card5, 4],
        [card6, 2],
        [card7, 2],
    ]
    buckets = split_to_buckets(cardList, 5)
    assert buckets[2][0] == card6
    assert buckets[1][0] == card2
    assert buckets[3][0] == card1


def test_splitting_bucket_error():
    card1 = Card("word", "word", 1, 1, 1, 1, 5)
    card2 = Card("word", "word", 1, 2, 1, 1, 2)
    cardList = [
        [card1, 3],
        [card2, 7],
    ]
    with raises(NonExistantBucketError):
        split_to_buckets(cardList, 5)


def test_random_cards_with_priority(monkeypatch):
    cardList = import_cards("tests/test_card_data.csv")
    setRandomList = [
        cardList[2][0],
        cardList[5][0],
        cardList[7][0],
        cardList[4][0],
    ]
    returnData = [
        cardList[2],
        cardList[5],
        cardList[7],
        cardList[2],
        cardList[2],
        cardList[4],
    ]
    testMock = Mock(side_effect=returnData)

    monkeypatch.setattr("file_rw.random.choices", testMock)
    randomList = draw_random_cards_priority(cardList, 4)
    for card in setRandomList:
        assert card in randomList


def test_random_cards_with_priority_random():
    cardList = import_cards("tests/test_card_data.csv")
    returnList = [card for card, _ in cardList if card.priority > 90]

    randomList = draw_random_cards_priority(cardList, 3)
    for card in returnList:
        assert card in randomList


def test_merge_buckets():
    cardList = import_cards("tests/test_card_data.csv")
    buckets = split_to_buckets(cardList, 10)
    newCardList = merge_buckets(buckets)

    for cardTupple in newCardList:
        assert cardTupple in cardList

    assert len(newCardList) == len(cardList)


def test_merge_empty_buckets():
    cardList = import_cards("tests/test_card_data.csv")
    buckets = split_to_buckets(cardList, 10)
    buckets = buckets[6:8]
    with raises(EmptyBucketsError):
        merge_buckets(buckets)


def test_count_buckets_elements():
    cardList = import_cards("tests/test_card_data.csv")
    buckets = split_to_buckets(cardList, 10)
    assert count_buckets_elements(buckets) == len(cardList)


def test_count_cards_to_N_bucket():
    card1 = Card("word", "other_word", 0, 0, 0, 0, 1)
    card2 = Card("word", "other_word", 0, 0, 0, 0, 2)
    card3 = Card("word", "other_word", 0, 0, 0, 0, 3)
    card4 = Card("word", "other_word", 0, 0, 0, 0, 4)
    card5 = Card("word", "other_word", 1, 2, 3, 4, 5)
    cardList = [
        [card1, 1],
        [card2, 3],
        [card3, 5],
        [card4, 3],
        [card5, 2],
    ]
    counter = count_cards_to_N_bucket(cardList, 3, 5)
    assert counter == 4


def test_sort_cards():
    card1 = Card("word", "other_word", 0, 0, 0, 0, 1)
    card2 = Card("word", "other_word", 0, 0, 0, 0, 2)
    card3 = Card("word", "other_word", 0, 0, 0, 0, 3)
    card4 = Card("word", "other_word", 0, 0, 0, 0, 4)
    cardList = [(card2, 0), (card4, 0), (card1, 0), (card3, 0)]
    newCardList = sort_cards(cardList)
    sortedList = [(card4, 0), (card3, 0), (card2, 0), (card1, 0)]
    assert newCardList == sortedList


def test_import_export_session_stats():
    stats = {
        "time": "test_time",
        "lastBucket": 3,
        "correctAnsweres": 5,
        "incorrectAnsweres": 3,
        "learned": 2,
    }
    test_file = "test_export.json"
    export_session_stats(test_file, stats)
    data = import_session_stats(test_file)
    newDict = {"1": stats}
    assert data == newDict
    os.remove(test_file)


def test_generate_statistics_data_exam():
    data = generate_statistics_data(True, True, 0, 3, 0, 0)
    assert data["exam"] is True
    assert data["finished"] is True
    assert data["lastBucket"] == 0
    assert data["correctAnswers"] == 3
    assert data["incorrectAnswers"] == 0
    assert data["learned"] == 0


def test_generate_statistics_data_session():
    data = generate_statistics_data(False, True, 4, 3, 5, 2)
    assert data["exam"] is False
    assert data["finished"] is True
    assert data["lastBucket"] == 4
    assert data["correctAnswers"] == 3
    assert data["incorrectAnswers"] == 5
    assert data["learned"] == 2


def test_statistics_data_file_name():
    statsFile = statistics_data_file_name("file_name.csv")
    assert statsFile == "file_name_stats.json"
    statsFile = statistics_data_file_name("iLike.csvfiles.csv")
    assert statsFile == "iLike.csvfiles_stats.json"

    previous = "C:\\Users\\UserName\\Documents\\Desktop\\iLovePipr.csv"
    expected = "C:\\Users\\UserName\\Documents\\Desktop\\iLovePipr_stats.json"

    statsFile = statistics_data_file_name(previous)
    assert statsFile == expected
