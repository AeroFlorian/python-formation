import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(Path(__file__).parent.parent))
from Step3_4.Hand import Hand, Card, CardValues, Color, HandValues
import random

class Deck:
    def __init__(self):
        self.cards = []

    def fill_deck(self):
        self.cards = []
        for color in Color:
            for value in CardValues:
                self.cards.append(Card(color=color, val=value))

    def pick_card(self):
        if len(self.cards) == 0:
            raise IndexError
        j = random.randint(0, len(self.cards) - 1)
        card = self.cards.pop(j)
        return card

    def pick_cards(self, number_of_cards):
        i = 0
        while i < number_of_cards:
            card = self.pick_card()
            yield card
            i = i + 1