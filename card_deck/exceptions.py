"""
Module Name: exceptions.py

Description:
This module defines custom exception classes for use in the 'card_deck' system.
These exceptions handle errors related to invalid cards, card ranks, suites, and
deck definitions. It includes base exception classes and specific exceptions for
different types of errors encountered in card and deck management.

Classes:
    - CardDeckException: Base exception for all card_deck errors.
    - CardDeckValueError: Exception for invalid card_deck values.
    - CardDeckTypeError: Exception for invalid card_deck types.
    - InvalidCard: Exception for invalid card definitions.
    - InvalidCardRank: Exception for invalid ranks of cards.
    - InvalidCardSuite: Exception for invalid suites of cards.
    - InvalidDeck: Exception for invalid deck definitions.
"""


# Base card_deck_exceptions
class CardDeckException(Exception):
    """
    Base exception class for all card_deck deck-related exceptions.
    """
    pass


class CardDeckValueError(ValueError):
    """
    Exception raised for invalid card_deck deck values.
    """
    pass


class CardDeckTypeError(TypeError):
    """
    Exception raised for invalid card_deck deck types.
    """
    pass


# Card card_deck_exceptions
class InvalidCard(CardDeckException):
    """
    Exception raised for invalid card_deck definitions.
    """
    pass


class InvalidCardRank(CardDeckValueError):
    """
    Exception raised for invalid card_deck ranks.
    """
    pass


class InvalidCardSuite(CardDeckTypeError):
    """
    Exception raised for invalid card_deck suites.
    """
    pass


# Deck card_deck_exceptions
class InvalidDeck(CardDeckException):
    """
    Exception raised for invalid deck definitions.
    """
    pass
