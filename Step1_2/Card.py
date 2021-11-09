#!/usr/bin/env python3
from enum import Enum


class Color(Enum):
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3
    CLUBS = 4


class CardValues(Enum):
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


class Card:
    def __init__(self, val, color):
        self.val = val
        self.color = color

    def __repr__(self):
        return "{} {}".format(self.val, self.color)

    def __eq__(self, other):
        return self.color == other.color and self.val == other.val
