"""
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
    """
    An enumeration to represent the four suits in a standard deck of cards.
    
    Attributes:
        Clubs (int): Represents the 'Clubs' suite.
        Diamonds (int): Represents the 'Diamonds' suite.
        Hearts (int): Represents the 'Hearts' suite.
        Spades (int): Represents the 'Spades' suite.
    """
    Clubs = 1
    Diamonds = 2
    Hearts = 3
    Spades = 4

    def __str__(self):
        return self.name


class Rank(Enum):
    """
    An enumeration to represent the ranks in a standard deck of cards.

    Attributes:
        Ace (int): Represents the 'Ace' rank with a value of 1.
        Two to Ten (int): Represent numeric card_deck ranks with values from 2 to 10.
        Jack (int): Represents the 'Jack' rank with a value of 11.
        Queen (int): Represents the 'Queen' rank with a value of 12.
        King (int): Represents the 'King' rank with a value of 13.
    """
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

    def __str__(self):
        return self.name

class Card:
    """
    A class to represent a playing card_deck, defined by its suite and rank.

    Attributes:
        suite (Suite): The suite of the card_deck (Clubs, Diamonds, Hearts, Spades).
        rank (Rank): The rank of the card_deck (Ace, 2-10, Jack, Queen, King).
    """

    def __init__(self, suite: Suite, rank: Rank):
        """
        Initialize a Card object with a specified suite and rank.
        
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
        

    def __repr__(self):
        """
        Return a string representation of the card_deck.
        
        Returns:
            str: A formatted string in the format '<Rank> of <suite>'.
        """
        return f"{self.rank} of {self.suite}"

    def get_suite(self) -> Suite:
        """
        Get the suite of the card_deck.
        
        Returns:
            Suite: The suite of the card_deck.
        """
        return self.suite

    def get_rank(self) -> Rank:
        """
        Get the rank of the card_deck.
        
        Returns:
            Rank: The rank of the card_deck.
        """
        return self.rank

    def set_suite(self, suite: Suite) -> Suite:
        """
        Set the suite of the card_deck.
    
        Args:
            suite (Suite): An instance of the suite enum representing the new suite.
    
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
        """
        Set the rank of the card_deck.
    
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
