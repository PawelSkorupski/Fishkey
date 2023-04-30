from file_rw import import_session_stats
from statistics_methods import (
    total_correct_incorrect_answers,
    count_in_buckets,
    count_learned,
    count_exams,
    count_finished_sessions,
    average_exam_score,
    average_session_score,
)
from card import Card
import pytest


def prepareCardList():
    card1 = Card("word", "word", 1, 1, 1, 1, 5)
    card2 = Card("word", "word", 2, 1, 1, 1, 5)
    card3 = Card("word", "word", 1, 2, 1, 1, 5)
    card4 = Card("word", "word", 1, 2, 3, 1, 5)
    card5 = Card("word", "word", 1, 2, 3, 4, 8)
    card6 = Card("word", "word", 1, 2, 3, 4, 8)
    card7 = Card("word", "word", 1, 2, 4, 4, 9)
    cardList = [
        [card1, 5],
        [card2, 3],
        [card3, 5],
        [card4, 5],
        [card5, 4],
        [card6, 2],
        [card7, 2],
    ]
    return cardList


def test_count_learned():
    cardList = prepareCardList()
    assert count_learned(cardList, 5) == 3


def test_count_in_buckets():
    cardList = prepareCardList()
    counted = count_in_buckets(cardList, 5)
    base_counted = [0, 0, 2, 1, 1, 3]
    assert counted == base_counted


# @TODO Make this test!!
def test_total_correct_incorrect_answers():
    cardList = prepareCardList()
    ans = total_correct_incorrect_answers(cardList)
    correct, incorrect = ans
    assert correct == 8
    assert incorrect == 12
    pass


def test_count_exams():
    jsonData = import_session_stats("tests/stats_for_tests.json")
    assert count_exams(jsonData) == 2


def test_finished_sessions():
    jsonData = import_session_stats("tests/stats_for_tests.json")
    assert count_finished_sessions(jsonData) == 20


def sessionData():
    jsonData = {
        "1": {
            "exam": True,
            "lastBucket": 0,
            "correctAnswers": 3,
            "incorrectAnswers": 1,
            "learned": 0,
        },
        "2": {
            "exam": True,
            "lastBucket": 0,
            "correctAnswers": 10,
            "incorrectAnswers": 10,
            "learned": 0,
        },
        "3": {
            "exam": False,
            "finished": True,
            "lastBucket": 2,
            "correctAnswers": 9,
            "incorrectAnswers": 1,
            "learned": 0,
        },
        "4": {
            "exam": False,
            "finished": True,
            "lastBucket": 2,
            "correctAnswers": 5,
            "incorrectAnswers": 5,
            "learned": 0,
        },
        "5": {
            "exam": False,
            "finished": False,
            "lastBucket": 2,
            "correctAnswers": 7,
            "incorrectAnswers": 1,
            "learned": 0,
        },
    }
    return jsonData


def test_average_exam_score():
    jsonData = sessionData()
    average_score = average_exam_score(jsonData)
    assert average_score == pytest.approx(round((75 + 50) / 2, 2))


def test_average_session_score():
    jsonData = sessionData()
    average_score = average_session_score(jsonData)
    assert average_score == pytest.approx(round((90 + 50) / 2, 2))
