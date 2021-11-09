import pytest
from Hand import Card, CardValues, Color, Hand, HandValues


def setup_module():
    pass


def teardown_module():
    pass


def test_card_hand_has_1_attribute():
    hand = Hand([])
    attributes = {'cards': []}
    assert (attributes == hand.__dict__)


def test_hand_has_2_methods():
    hand = Hand([])
    methods_attributes = [x for x in dir(hand) if x[0] != '_' and not (x in hand.__dict__)]
    methods_wanted = ['compute_value', 'pick_card_with_value']
    assert (methods_attributes == methods_wanted)


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
