#!/usr/bin/env python3
"""
Test the visual components of the poker game.
"""
from poker_game.cards import Card, Rank, Suit
from poker_game.visuals import CardDisplay, PokerArt, Colors

print("🎨 Testing Visual Components 🎨")
print("=================================")

# Test title banner
print(PokerArt.title_banner())

# Test card display
ace_spades = Card(Rank.ACE, Suit.SPADES)
king_hearts = Card(Rank.KING, Suit.HEARTS)
cards = [ace_spades, king_hearts]

print("\n📇 Card Display Test:")
print(CardDisplay.display_cards_horizontal(cards, "Sample Hand:"))

# Test betting round header
print("\n" + PokerArt.betting_round_header("🃏 FLOP", cards))

# Test action menu
print("\n" + CardDisplay.display_action_menu(["fold", "call", "raise"], 50))

print(f"\n{Colors.GREEN}✅ Visual components working!{Colors.RESET}")
