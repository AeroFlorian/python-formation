import pytest
from Deck import Deck, Hand, Card, CardValues, Color, HandValues
import random


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
