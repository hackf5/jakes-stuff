"""
Card and Deck classes for the poker game.
"""
import random
from enum import Enum
from typing import List, NamedTuple


class Suit(Enum):
    """Card suits with colors."""
    HEARTS = ("♥", "\033[91m")    # Red
    DIAMONDS = ("♦", "\033[91m")  # Red
    CLUBS = ("♣", "\033[90m")     # Dark gray
    SPADES = ("♠", "\033[90m")    # Dark gray
    
    def __init__(self, symbol: str, color: str):
        self.symbol = symbol
        self.color = color


class Rank(Enum):
    """Card ranks with numeric values for comparison."""
    TWO = (2, "2")
    THREE = (3, "3")
    FOUR = (4, "4")
    FIVE = (5, "5")
    SIX = (6, "6")
    SEVEN = (7, "7")
    EIGHT = (8, "8")
    NINE = (9, "9")
    TEN = (10, "10")
    JACK = (11, "J")
    QUEEN = (12, "Q")
    KING = (13, "K")
    ACE = (14, "A")
    
    def __init__(self, numeric_value: int, display: str):
        self.numeric_value = numeric_value
        self.display = display


class Card(NamedTuple):
    """A playing card with rank and suit."""
    rank: Rank
    suit: Suit
    
    def __str__(self) -> str:
        return f"{self.suit.color}{self.rank.display}{self.suit.symbol}\033[0m"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def simple_str(self) -> str:
        """Return a simple string representation without colors."""
        return f"{self.rank.display}{self.suit.symbol}"
    
    def ascii_card(self) -> List[str]:
        """Return enhanced ASCII art representation of the card."""
        rank_display = self.rank.display.ljust(2)
        suit_char = self.suit.symbol
        color = self.suit.color
        reset = "\033[0m"
        border_color = "\033[1m\033[97m"  # Bold white
        
        # Enhanced card with beautiful borders and styling
        return [
            f"{border_color}┌─────────┐{reset}",
            f"{border_color}│{color}{rank_display:<2}{reset}{border_color}       │{reset}",
            f"{border_color}│         │{reset}",
            f"{border_color}│    {color}{suit_char}{reset}{border_color}    │{reset}",
            f"{border_color}│         │{reset}",
            f"{border_color}│       {color}{rank_display:>2}{reset}{border_color}│{reset}",
            f"{border_color}└─────────┘{reset}"
        ]


class Deck:
    """A deck of playing cards."""
    
    def __init__(self):
        """Initialize a full deck of 52 cards."""
        self.cards: List[Card] = []
        self.reset()
    
    def reset(self) -> None:
        """Reset the deck to a full 52-card deck and shuffle."""
        self.cards = [Card(rank, suit) for rank in Rank for suit in Suit]
        self.shuffle()
    
    def shuffle(self) -> None:
        """Shuffle the deck."""
        random.shuffle(self.cards)
    
    def deal_card(self) -> Card:
        """Deal one card from the top of the deck."""
        if not self.cards:
            raise ValueError("Cannot deal from an empty deck")
        return self.cards.pop()
    
    def cards_remaining(self) -> int:
        """Return the number of cards remaining in the deck."""
        return len(self.cards)
