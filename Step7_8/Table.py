import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(Path(__file__).parent.parent))
from Step5_6.Deck import Deck, Hand, Card, CardValues, Color, HandValues

class Table:
    def __init__(self):
        self.hands = []
        self.deck = Deck()
        self.deck.fill_deck()

    def compute_best(self):
        hand_values = list(map(lambda x: x.compute_value(), self.hands))
        return sorted(hand_values)[-1]

    def pick_hands(self, number_of_hands):
        for i in range(number_of_hands):
            self.hands.append(Hand(list(self.deck.pick_cards(5))))