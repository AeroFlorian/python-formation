from enum import Enum
from collections import Counter


class Color(Enum):
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3
    CLUBS = 4


class Value(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class HandValues(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10


class Card:
    def __init__(self):
        self.color = None
        self.value = None


def has_number_of_occurences(counter, occurence):
    return len([x for x in counter.keys if counter[x] == occurence])


class Hand:
    def __init__(self):
        self.cards = []

    def compute_value(self):
        counter = Counter(self.cards)
        number_of_pairs = has_number_of_occurences(counter, 2)
        has_threes = has_number_of_occurences(counter, 3)
        has_fours = has_number_of_occurences(counter, 4)
