from Table import Table, Deck, Hand, Card, CardValues, Color, HandValues
import random


def test_table_pick_1_hand():
    table = Table()
    table.pick_hands(1)
    assert (len(table.hands) == 1)
    assert (len(table.deck.cards) == 47)


def test_table_pick_2_hands_compare():
    table = Table()
    random.seed(10)
    table.pick_hands(2)

    assert (len(table.hands) == 2)
    assert (len(table.deck.cards) == 42)
    best_hand = table.compute_best()
    assert (best_hand == (HandValues.PAIR, [CardValues.FOUR.value], Card(CardValues.QUEEN, Color.DIAMONDS)))


def test_table_pick_4_hands_compare():
    table = Table()
    random.seed(10)
    table.pick_hands(4)

    assert (len(table.hands) == 4)
    assert (len(table.deck.cards) == 32)
    best_hand = table.compute_best()
    assert (best_hand == (HandValues.TWO_PAIR, [CardValues.SIX.value, CardValues.ACE.value], Card(CardValues.EIGHT, Color.CLUBS)))