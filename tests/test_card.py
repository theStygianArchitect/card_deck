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


@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_card_initialization(suite: Suite, rank: Rank) -> None:
    """Test the initialization of a Card object with valid suite and rank values.
    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - The suite of the created card matches the input suite.
        - The rank of the created card matches the input rank.
        - The string representation of the card is in the format '<Rank> of <Suite>'.

    Returns:
        None
    """
    card = Card(suite, rank)
    assert card.suite == suite
    assert card.rank == rank
    assert repr(card) == f"{rank} of {suite}"


# @pytest.mark.parametrize("suite", list(Suite))
@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
def test_invalid_card_initialization_suite(rank: Rank) -> None:
    """Test the initialization of a Card object with an invalid suite.
    Args:
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - Raises an InvalidCardSuite exception when the suite is invalid.

    Returns:
        None
    """
    with pytest.raises(InvalidCardSuite):
        Card("InvalidSuit", rank)


@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_invalid_card_initialization_rank(suite: Suite) -> None:
    """Test the initialization of a Card object with an invalid rank.
    Args:
        suite (Suite): A valid suite from the Suite enum.

    Asserts:
        - Raises an InvalidCardRank exception when the rank is invalid.

    Returns:
        None
    """
    with pytest.raises(InvalidCardRank):
        Card(suite, "InvalidRank")


@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_get_suite(suite: Suite, rank: Rank) -> None:
    """Test the get_suite method of the Card class.
    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - The suite of the card matches its name representation.

    Returns:
        None
    """
    card = Card(suite, rank)
    assert str(card.suite.name) == suite.name


@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_get_rank(suite: Suite, rank: Rank) -> None:
    """Test the get_rank method of the Card class.
    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - The rank of the card matches its name representation.

    Returns:
        None
    """
    card = Card(suite, rank)
    assert str(card.rank.name) == rank.name


@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_set_suite_valid(suite: Suite, rank: Rank) -> None:
    """Test setting a valid suite for a Card object using the set_suite method.
    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - The suite of the card is updated correctly to the new suite.

    Returns:
        None
    """
    card = Card(suite, rank)
    temp_suite = Suite.SPADES
    if suite.name == "SPADES":
        temp_suite = Suite.CLUBS
    card.suite = temp_suite

    assert card.suite == temp_suite


@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_set_rank_valid(suite: Suite, rank: Rank) -> None:
    """Test setting a valid rank for a Card object using the set_rank method.
    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - The rank of the card is updated correctly to the new rank.

    Returns:
        None
    """
    card = Card(suite, rank)
    temp_rank = Rank.KING
    if rank.name == "KING":
        temp_rank = Rank.ACE
    card.rank = temp_rank

    assert card.rank == temp_rank


@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_set_suite_invalid(suite: Suite, rank: Rank) -> None:
    """Test setting an invalid suite for a Card object using the set_suite method.
    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - Raises an InvalidCardSuite exception when an invalid suite is set.

    Returns:
        None
    """
    card = Card(suite, rank)
    with pytest.raises(InvalidCardSuite):
        card.suite = "InvalidSuite"


@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_set_rank_invalid(suite: Suite, rank: Rank) -> None:
    """Test setting an invalid rank for a Card object using the set_rank method.
    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - Raises an InvalidCardRank exception when an invalid rank is set.

    Returns:
        None
    """
    card = Card(suite, rank)
    with pytest.raises(InvalidCardRank):
        card.rank = "InvalidRank"


@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_del_suite(suite: Suite, rank: Rank) -> None:
    """Test deleting the suite attribute of a Card object.
    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - Raises an AttributeError when attempting to delete the suite attribute.

    Returns:
        None
    """
    card = Card(suite, rank)
    with pytest.raises(AttributeError):
        del card.suite


@pytest.mark.parametrize("rank", list(Rank))  # type: ignore
@pytest.mark.parametrize("suite", list(Suite))  # type: ignore
def test_del_rank(suite: Suite, rank: Rank) -> None:
    """Test deleting the rank attribute of a Card object.
    Args:
        suite (Suite): A valid suite from the Suite enum.
        rank (Rank): A valid rank from the Rank enum.

    Asserts:
        - Raises an AttributeError when attempting to delete the rank attribute.

    Returns:
        None
    """
    card = Card(suite, rank)
    with pytest.raises(AttributeError):
        del card.rank
