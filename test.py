import pytest
from pokertypes import *
import random


def setup_module():
    pass


def teardown_module():
    pass


def test_framework():
    assert True


def test_hand_high_card():
    cards = [Card(CardValues.TWO, Color.SPADES),
             Card(CardValues.THREE, Color.SPADES),
             Card(CardValues.FOUR, Color.DIAMONDS),
             Card(CardValues.FIVE, Color.SPADES),
             Card(CardValues.SEVEN, Color.SPADES)]

    hand = Hand(cards)
    assert (hand.compute_value() == (HandValues.HIGH_CARD, Card(CardValues.SEVEN, Color.SPADES)))


def test_hand_pair():
    cards = [Card(CardValues.TWO, Color.SPADES),
             Card(CardValues.TWO, Color.DIAMONDS),
             Card(CardValues.FOUR, Color.DIAMONDS),
             Card(CardValues.FIVE, Color.SPADES),
             Card(CardValues.SEVEN, Color.SPADES)]

    hand = Hand(cards)
    assert (hand.compute_value() == (HandValues.PAIR, [CardValues.TWO.value], Card(CardValues.SEVEN, Color.SPADES)))


def test_hand_two_pair():
    cards = [Card(CardValues.TWO, Color.SPADES),
             Card(CardValues.TWO, Color.DIAMONDS),
             Card(CardValues.FOUR, Color.DIAMONDS),
             Card(CardValues.FOUR, Color.SPADES),
             Card(CardValues.SEVEN, Color.SPADES)]

    hand = Hand(cards)
    assert (hand.compute_value() == (
        HandValues.TWO_PAIR, [CardValues.TWO.value, CardValues.FOUR.value], Card(CardValues.SEVEN, Color.SPADES)))


def test_hand_three_of_a_kind():
    cards = [Card(CardValues.TWO, Color.SPADES),
             Card(CardValues.TWO, Color.DIAMONDS),
             Card(CardValues.TWO, Color.HEARTS),
             Card(CardValues.FIVE, Color.SPADES),
             Card(CardValues.SEVEN, Color.SPADES)]

    hand = Hand(cards)
    assert (hand.compute_value() == (
        HandValues.THREE_OF_A_KIND, CardValues.TWO.value))


def test_hand_straight():
    cards = [Card(CardValues.TWO, Color.SPADES),
             Card(CardValues.THREE, Color.SPADES),
             Card(CardValues.FOUR, Color.DIAMONDS),
             Card(CardValues.FIVE, Color.SPADES),
             Card(CardValues.SIX, Color.SPADES)]

    hand = Hand(cards)
    assert (hand.compute_value() == (HandValues.STRAIGHT, Card(CardValues.SIX, Color.SPADES)))


def test_hand_flush():
    cards = [Card(CardValues.TWO, Color.SPADES),
             Card(CardValues.THREE, Color.SPADES),
             Card(CardValues.FOUR, Color.SPADES),
             Card(CardValues.FIVE, Color.SPADES),
             Card(CardValues.SEVEN, Color.SPADES)]

    hand = Hand(cards)
    assert (hand.compute_value() == (HandValues.FLUSH, Card(CardValues.SEVEN, Color.SPADES)))


def test_hand_full_house():
    cards = [Card(CardValues.TWO, Color.SPADES),
             Card(CardValues.TWO, Color.DIAMONDS),
             Card(CardValues.TWO, Color.HEARTS),
             Card(CardValues.FIVE, Color.SPADES),
             Card(CardValues.FIVE, Color.HEARTS)]

    hand = Hand(cards)
    assert (hand.compute_value() == (HandValues.FULL_HOUSE, CardValues.TWO.value))


def test_hand_four_of_a_kind():
    cards = [Card(CardValues.TWO, Color.SPADES),
             Card(CardValues.TWO, Color.DIAMONDS),
             Card(CardValues.TWO, Color.HEARTS),
             Card(CardValues.TWO, Color.CLUBS),
             Card(CardValues.FIVE, Color.HEARTS)]

    hand = Hand(cards)
    assert (hand.compute_value() == (HandValues.FOUR_OF_A_KIND, CardValues.TWO.value))


def test_hand_straight_flush():
    cards = [Card(CardValues.TWO, Color.SPADES),
             Card(CardValues.THREE, Color.SPADES),
             Card(CardValues.FOUR, Color.SPADES),
             Card(CardValues.FIVE, Color.SPADES),
             Card(CardValues.SIX, Color.SPADES)]

    hand = Hand(cards)
    assert (hand.compute_value() == (HandValues.STRAIGHT_FLUSH, Card(CardValues.SIX, Color.SPADES)))


def test_fill_deck():
    deck = Deck()
    deck.fill_deck()
    assert (len(deck.cards) == 52)


def test_pick_one_card():
    deck = Deck()
    deck.fill_deck()
    card = deck.pick_card()
    assert (len(deck.cards) == 51)


def test_pick_cards():
    deck = Deck()
    deck.fill_deck()
    cards_to_take = deck.pick_cards(5)
    # verify pick_cards is a generator
    assert (len(deck.cards) == 52)
    card_list = list(cards_to_take)
    assert (len(card_list) == 5 and len(deck.cards) == 47)


def test_pick_too_many_cards():
    deck = Deck()
    deck.fill_deck()
    cards_to_take = deck.pick_cards(53)
    # verify pick_cards is a generator
    assert (len(deck.cards) == 52)
    card_list = []
    try:
        card_list = list(cards_to_take)
        assert False
    except IndexError:
        assert (len(card_list) == 0 and len(deck.cards) == 0)


def test_pick_4_cards_with_seed_0():
    deck = Deck()
    deck.fill_deck()
    random.seed(0)
    cards = list(deck.pick_cards(5))
    hand = Hand(cards)
    assert (hand.compute_value() == (HandValues.HIGH_CARD, Card(CardValues.KING, Color.HEARTS)))


def test_pick_4_cards_with_seed_10():
    deck = Deck()
    deck.fill_deck()
    random.seed(10)
    cards = list(deck.pick_cards(5))
    hand = Hand(cards)
    assert (hand.compute_value() == (HandValues.PAIR, [CardValues.FOUR.value], Card(CardValues.QUEEN, Color.DIAMONDS)))


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
    assert (best_hand == (HandValues.TWO_PAIR, [CardValues.SIX.value, CardValues.ACE.value], Card(CardValues.ACE, Color.SPADES)))
