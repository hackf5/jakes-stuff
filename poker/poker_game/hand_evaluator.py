"""
Hand evaluation for poker hands.
"""
from collections import Counter
from enum import Enum
from typing import List, Tuple, Optional

from .cards import Card, Rank, Suit


class HandRank(Enum):
    """Poker hand rankings from weakest to strongest."""
    HIGH_CARD = (1, "High Card")
    PAIR = (2, "Pair")
    TWO_PAIR = (3, "Two Pair")
    THREE_OF_A_KIND = (4, "Three of a Kind")
    STRAIGHT = (5, "Straight")
    FLUSH = (6, "Flush")
    FULL_HOUSE = (7, "Full House")
    FOUR_OF_A_KIND = (8, "Four of a Kind")
    STRAIGHT_FLUSH = (9, "Straight Flush")
    ROYAL_FLUSH = (10, "Royal Flush")
    
    def __init__(self, numeric_value: int, display: str):
        self.numeric_value = numeric_value
        self.display = display


class PokerHand:
    """Represents a poker hand with cards and evaluation."""
    
    def __init__(self, cards: List[Card]):
        """Initialize with a list of cards."""
        if len(cards) != 7:
            raise ValueError("Poker hand must have exactly 7 cards (2 hole + 5 community)")
        self.cards = sorted(cards, key=lambda c: c.rank.numeric_value, reverse=True)
        self.best_hand = self._find_best_hand()
    
    def _find_best_hand(self) -> Tuple[HandRank, List[int]]:
        """Find the best 5-card hand from the 7 available cards."""
        from itertools import combinations
        
        best_rank = HandRank.HIGH_CARD
        best_tiebreakers = []
        
        # Check all possible 5-card combinations
        for combo in combinations(self.cards, 5):
            rank, tiebreakers = self._evaluate_hand(list(combo))
            if rank.numeric_value > best_rank.numeric_value or (rank.numeric_value == best_rank.numeric_value and tiebreakers > best_tiebreakers):
                best_rank = rank
                best_tiebreakers = tiebreakers
        
        return best_rank, best_tiebreakers
    
    def _evaluate_hand(self, cards: List[Card]) -> Tuple[HandRank, List[int]]:
        """Evaluate a 5-card hand and return rank and tiebreakers."""
        cards = sorted(cards, key=lambda c: c.rank.numeric_value, reverse=True)
        ranks = [card.rank.numeric_value for card in cards]
        suits = [card.suit for card in cards]
        rank_counts = Counter(ranks)
        
        is_flush = len(set(suits)) == 1
        is_straight = self._is_straight(ranks)
        
        # Check for royal flush
        if is_straight and is_flush and ranks[0] == 14:  # Ace high
            return HandRank.ROYAL_FLUSH, [14]
        
        # Check for straight flush
        if is_straight and is_flush:
            return HandRank.STRAIGHT_FLUSH, [ranks[0]]
        
        # Check for four of a kind
        if 4 in rank_counts.values():
            four_kind = [rank for rank, count in rank_counts.items() if count == 4][0]
            kicker = [rank for rank, count in rank_counts.items() if count == 1][0]
            return HandRank.FOUR_OF_A_KIND, [four_kind, kicker]
        
        # Check for full house
        if 3 in rank_counts.values() and 2 in rank_counts.values():
            three_kind = [rank for rank, count in rank_counts.items() if count == 3][0]
            pair = [rank for rank, count in rank_counts.items() if count == 2][0]
            return HandRank.FULL_HOUSE, [three_kind, pair]
        
        # Check for flush
        if is_flush:
            return HandRank.FLUSH, ranks
        
        # Check for straight
        if is_straight:
            return HandRank.STRAIGHT, [ranks[0]]
        
        # Check for three of a kind
        if 3 in rank_counts.values():
            three_kind = [rank for rank, count in rank_counts.items() if count == 3][0]
            kickers = sorted([rank for rank, count in rank_counts.items() if count == 1], reverse=True)
            return HandRank.THREE_OF_A_KIND, [three_kind] + kickers
        
        # Check for two pair
        pairs = [rank for rank, count in rank_counts.items() if count == 2]
        if len(pairs) == 2:
            pairs.sort(reverse=True)
            kicker = [rank for rank, count in rank_counts.items() if count == 1][0]
            return HandRank.TWO_PAIR, pairs + [kicker]
        
        # Check for one pair
        if len(pairs) == 1:
            pair = pairs[0]
            kickers = sorted([rank for rank, count in rank_counts.items() if count == 1], reverse=True)
            return HandRank.PAIR, [pair] + kickers
        
        # High card
        return HandRank.HIGH_CARD, ranks
    
    def _is_straight(self, ranks: List[int]) -> bool:
        """Check if the ranks form a straight."""
        ranks = sorted(set(ranks), reverse=True)
        if len(ranks) != 5:
            return False
        
        # Check for regular straight
        if ranks[0] - ranks[4] == 4:
            return True
        
        # Check for wheel straight (A-2-3-4-5)
        if ranks == [14, 5, 4, 3, 2]:
            return True
        
        return False
    
    def __str__(self) -> str:
        """String representation of the hand."""
        rank, tiebreakers = self.best_hand
        return f"{rank.display}"
    
    def compare(self, other: 'PokerHand') -> int:
        """Compare this hand with another. Returns 1 if this hand wins, -1 if other wins, 0 for tie."""
        my_rank, my_tiebreakers = self.best_hand
        other_rank, other_tiebreakers = other.best_hand
        
        if my_rank.numeric_value > other_rank.numeric_value:
            return 1
        elif my_rank.numeric_value < other_rank.numeric_value:
            return -1
        else:
            # Same hand rank, compare tiebreakers
            for my_tb, other_tb in zip(my_tiebreakers, other_tiebreakers):
                if my_tb > other_tb:
                    return 1
                elif my_tb < other_tb:
                    return -1
            return 0
