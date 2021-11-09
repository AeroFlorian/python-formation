import pytest
from Card import Card, CardValues, Color


def setup_module():
    pass


def teardown_module():
    pass


def test_framework():
    assert True


def test_card_has_2_attributes():
    card = Card(color=Color.SPADES, val=CardValues.ACE)
    attributes = {'color': Color.SPADES, 'val': CardValues.ACE}
    assert (attributes == card.__dict__)
