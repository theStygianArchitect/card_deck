"""See Description below.

Module Name: card.py

Description:
This module provides the implementation for a suite and rank enumeration and a `Card` class
used to represent individual playing cards. It forms the basis for card manipulation
and deck-related functionality. Within this module, you will find everything needed to
define suites, ranks, and the properties of individual cards.

Classes:
    - Suite: Enum class for card suites (Clubs, Diamonds, Hearts, Spades).
    - Rank: Enum class for card ranks (Ace to King).
    - Card: Represents a playing card, pairing a rank and a suite.

Usage:
Users can create and manipulate card objects using these classes for card-related operations.
"""

from enum import Enum

from card_deck.exceptions import InvalidCardRank
from card_deck.exceptions import InvalidCardSuite


class Suite(Enum):
    """An enumeration to represent the four suits in a standard deck of cards.

    Attributes:
        CLUBS (int): Represents the 'CLUBS' suite.
        DIAMONDS (int): Represents the 'DIAMONDS' suite.
        HEARTS (int): Represents the 'HEARTS' suite.
        SPADES (int): Represents the 'SPADES' suite.
    """
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __str__(self) -> str:
        return self.name


class Rank(Enum):
    """An enumeration to represent the ranks in a standard deck of cards.

    Attributes:
        ACE (int): Represents the 'Ace' rank with a value of 1.
        TWO to TEN (int): Represent numeric card_deck ranks with values from 2 to 10.
        JACK (int): Represents the 'Jack' rank with a value of 11.
        QUEEN (int): Represents the 'Queen' rank with a value of 12.
        KING (int): Represents the 'King' rank with a value of 13.
    """
    ACE = 1
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

    def __str__(self) -> str:
        return self.name


class Card:
    """A class to represent a playing card_deck, defined by its suite and rank.

    Attributes:
        suite (Suite): The suite of the card_deck (Clubs, Diamonds, Hearts, Spades).
        rank (Rank): The rank of the card_deck (Ace, 2-10, Jack, Queen, King).
    """

    def __init__(self, suite: Suite, rank: Rank):
        """Initialize a Card object with a specified suite and rank.

        Args:
            suite (Suite): An instance of the suite enum representing the card_deck's suite.
            rank (Rank): An instance of the Rank enum representing the card_deck's rank.
        """
        if suite in Suite:
            self.suite = suite
        else:
            raise InvalidCardSuite("Invalid card_deck suite")

        if rank in Rank:
            self.rank = rank
        else:
            raise InvalidCardRank("Invalid card_deck rank")

    def __repr__(self) -> str:
        """Return a string representation of the card_deck.

        Returns:
            str: A formatted string in the format '<Rank> of <suite>'.
        """
        return f"{self.rank} of {self.suite}"

    def get_suite(self) -> Suite:
        """Get the suite of the card_deck.

        Returns:
            Suite: The suite of the card_deck.
        """
        return self.suite

    def get_rank(self) -> Rank:
        """Get the rank of the card_deck.

        Returns:
            Rank: The rank of the card_deck.
        """
        return self.rank

    def set_suite(self, suite: Suite) -> Suite:
        """Set the suite of the card_deck.

        Args:
            suite (Suite): An instance of the suite enum representing the new suite.0

        Returns:
            Suite: The updated suite of the card_deck.

        Raises:
            InvalidCardSuite: If the provided suite is not a valid suite enum.
        """
        if suite in Suite:
            self.suite = suite
            return self.suite
        raise InvalidCardSuite("Invalid card_deck suite")

    def set_rank(self, rank: Rank) -> Rank:
        """Set the rank of the card_deck.

        Args:
            rank (Rank): An instance of the Rank enum representing the new rank.

        Returns:
            Rank: The updated rank of the card_deck.

        Raises:
            InvalidCardRank: If the provided rank is not a valid Rank enum.
        """
        if rank in Rank:
            self.rank = rank
            return self.rank
        raise InvalidCardRank("Invalid card_deck rank")
