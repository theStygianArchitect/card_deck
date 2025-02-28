"""The initializer module for the card package, providing core components for a deck of cards.

Module Name: __init__.py

This module acts as the initializer for the package. It provides access to the core
components of the card module, including the `Card`, `Rank`, and `Suit` classes.
These classes enable the structure and functionality required to work with a deck
of cards, including ranks, suits, and card representations.

Classes:
    Card: Represents a playing card with a specific rank and suit.
    Rank: Enum class to define the ranks (Ace to King) of playing cards.
    Suit: Enum class to define the suits (Clubs, Diamonds, Hearts, Spades) of playing cards.

Usage:
    Import this module to use the card system for card manipulation and functionality.
"""

from .card import Card
from .card import Rank
from .card import Suite

__all__ = [
    "Card",
    "Rank",
    "Suite"
]
