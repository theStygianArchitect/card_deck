"""See Description below.

Module Name: test_card.py

Description:
This module contains test cases for validating the functionality of the Card class and its related components such as
Rank and Suite enums and the custom exceptions (InvalidCardRank, InvalidCardSuite). It uses the pytest framework for
defining and executing parameterized tests, ensuring robust verification of behaviors like initialization, setting,
and getting of card attributes, as well as exception handling for invalid inputs.

Key Features:
- Tests for valid and invalid initialization of the Card class.
- Verification of the Card class methods like get_suite(), get_rank(), set_suite(), and set_rank().
- Handling of edge cases to ensure proper exception raising for InvalidCardRank and InvalidCardSuite.

Dependencies:
- pytest
- card_deck.Card
- card_deck.Rank
- card_deck.Suite
- card_deck.exceptions.InvalidCardRank
- card_deck.exceptions.InvalidCardSuite
"""

import pytest

from card_deck import Card
from card_deck import Rank
from card_deck import Suite
from card_deck.exceptions import InvalidCardRank
from card_deck.exceptions import InvalidCardSuite


@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
def test_card_initialization(suite: Suite, rank: Rank):
    """
    Test the initialization of a Card object with valid suite and rank values.

    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - The suite of the created card matches the input suite.
        - The rank of the created card matches the input rank.
        - The string representation of the card is in the format '<Rank> of <Suite>'.
    """
    card = Card(suite, rank)
    assert card.suite == suite
    assert card.rank == rank
    assert repr(card) == f"{rank} of {suite}"


# @pytest.mark.parametrize("suite", list(Suite))
@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
def test_invalid_card_initialization_suite(rank: Rank):
    """
    Test the initialization of a Card object with an invalid suite.

    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - Raises an InvalidCardSuite exception when the suite is invalid.
    """
    with pytest.raises(InvalidCardSuite):
        Card("InvalidSuit", rank)


@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_invalid_card_initialization_rank(suite: Suite):
    """
    Test the initialization of a Card object with an invalid rank.

    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - Raises an InvalidCardRank exception when the rank is invalid.
    """
    with pytest.raises(InvalidCardRank):
        Card(suite, "InvalidRank")


@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
def test_get_suite(suite: Suite, rank: Rank):
    """
    Test the get_suite method of the Card class.

    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - The suite of the card matches its name representation.
    """
    card = Card(suite, rank)
    assert str(card.get_suite()) == suite.name


@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
def test_get_rank(suite: Suite, rank: Rank):
    """
    Test the get_rank method of the Card class.

    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - The rank of the card matches its name representation.
    """
    card = Card(suite, rank)
    assert str(card.get_rank()) == rank.name


@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
def test_set_suite_valid(suite: Suite, rank: Rank):
    """
    Test setting a valid suite for a Card object using the set_suite method.

    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - The suite of the card is updated correctly to the new suite.
    """
    card = Card(suite, rank)
    temp_suite = Suite.SPADES
    if suite.name == "SPADES":
        temp_suite = Suite.CLUBS
    card.set_suite(temp_suite)

    assert card.suite == temp_suite


@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
def test_set_rank_valid(suite: Suite, rank: Rank):
    """
    Test setting a valid rank for a Card object using the set_rank method.

    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - The rank of the card is updated correctly to the new rank.
    """
    card = Card(suite, rank)
    temp_rank = Rank.KING
    if rank.name == "KING":
        temp_rank = Rank.ACE
    card.set_rank(temp_rank)

    assert card.rank == temp_rank


@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
def test_set_suite_invalid(suite: Suite, rank: Rank):
    """
    Test setting an invalid suite for a Card object using the set_suite method.

    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - Raises an InvalidCardSuite exception when an invalid suite is set.
    """
    card = Card(suite, rank)
    with pytest.raises(InvalidCardSuite):
        card.set_suite("InvalidSuite")


@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
def test_set_rank_invalid(suite: Suite, rank: Rank):
    """
    Test setting an invalid rank for a Card object using the set_rank method.

    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - Raises an InvalidCardRank exception when an invalid rank is set.
    """
    card = Card(suite, rank)
    with pytest.raises(InvalidCardRank):
        card.set_rank("InvalidRank")
