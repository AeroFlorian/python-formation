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


def has_number_of(counter, number):
    return len([x for x in counter.keys if counter[x] == number])


def take_value(card):
    return card.value


def take_number_of(counter, number):
    return [x for x in counter.keys if counter[x] == number][0]


def take_pairs(counter):
    return [x for x in counter.keys if counter[x] == 2]


class Hand:
    def __init__(self):
        self.cards = []

    def compute_value(self):
        self.cards.sort(key=take_value)
        values = [v.value for v in self.cards]
        counter = Counter(values)
        number_of_pairs = has_number_of(counter, 2)
        has_threes = has_number_of(counter, 3)
        has_fours = has_number_of(counter, 4)
        is_color = len(Counter([v.color for v in self.cards])) == 1
        is_straight = all(values[i + 1] == values[i] + 1 for i in range(len(values) - 1))
        highest_card = self.cards[-1]
        if is_straight and is_color:
            if highest_card.value == Value.ACE:
                return HandValues.ROYAL_FLUSH
            return HandValues.STRAIGHT_FLUSH, highest_card
        if has_fours:
            return HandValues.FOUR_OF_A_KIND, take_number_of(counter, 4)
        if has_threes and number_of_pairs == 1:
            return HandValues.FULL_HOUSE, take_number_of(counter, 3)
        if is_color:
            return HandValues.FLUSH, highest_card
        if is_straight:
            return HandValues.STRAIGHT, highest_card
        if has_threes:
            return HandValues.THREE_OF_A_KIND, take_number_of(counter, 3)
        if number_of_pairs == 2:
            return HandValues.TWO_PAIR, take_pairs(counter), highest_card
        if number_of_pairs == 1:
            return HandValues.PAIR, take_pairs(counter), highest_card
        return HandValues.HIGH_CARD, highest_card
