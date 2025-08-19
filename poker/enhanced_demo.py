#!/usr/bin/env python3
"""
Enhanced visual demo showcasing the beautiful poker game features.
"""
import time
from poker_game.cards import Card, Rank, Suit, Deck
from poker_game.visuals import PokerArt, CardDisplay, Colors, print_with_sparkle_effect, clear_screen_with_effect
from poker_game.hand_evaluator import PokerHand

def spectacular_demo():
    """Demonstrate the enhanced poker game with stunning visuals."""
    
    # 1. Animated Title Sequence
    print("🎬 Starting Enhanced Visual Demo...")
    time.sleep(1)
    PokerArt.animated_title()
    time.sleep(2)
    
    clear_screen_with_effect()
    print(PokerArt.title_banner())
    print(PokerArt.poker_table_deluxe())
    
    print_with_sparkle_effect("Welcome to the most beautiful poker game!")
    print_with_sparkle_effect("Let's explore the enhanced features...")
    
    time.sleep(2)
    
    # 2. Enhanced Card Display Demo
    clear_screen_with_effect()
    print(f"{Colors.BOLD}{Colors.YELLOW}🃏 STUNNING CARD DISPLAYS 🃏{Colors.RESET}")
    print("=" * 70)
    
    deck = Deck()
    hole_cards = [
        Card(Rank.ACE, Suit.SPADES),
        Card(Rank.KING, Suit.HEARTS)
    ]
    
    print(CardDisplay.display_cards_with_shadow(hole_cards, "💎 Premium Hole Cards"))
    
    time.sleep(2)
    
    community = [
        Card(Rank.ACE, Suit.DIAMONDS),
        Card(Rank.KING, Suit.CLUBS),
        Card(Rank.QUEEN, Suit.HEARTS)
    ]
    
    print()
    print(CardDisplay.display_cards_with_shadow(community, "🌟 Beautiful Community Cards"))
    
    time.sleep(3)
    
    # 3. Animated Betting Rounds
    clear_screen_with_effect()
    print(f"{Colors.BOLD}{Colors.CYAN}🎯 DYNAMIC BETTING ROUNDS 🎯{Colors.RESET}")
    print("=" * 70)
    
    PokerArt.loading_animation("Shuffling deck", 1.5)
    print(PokerArt.betting_round_header_deluxe("🎲 PRE-FLOP"))
    time.sleep(1)
    
    PokerArt.loading_animation("Dealing the flop", 1.5)
    print(PokerArt.betting_round_header_deluxe("🃏 FLOP", community))
    time.sleep(1)
    
    # Add turn card
    turn_community = community + [Card(Rank.JACK, Suit.SPADES)]
    PokerArt.loading_animation("Dealing the turn", 1.0)
    print(PokerArt.betting_round_header_deluxe("🎯 TURN", turn_community))
    time.sleep(1)
    
    # Add river card
    river_community = turn_community + [Card(Rank.TEN, Suit.DIAMONDS)]
    PokerArt.loading_animation("Dealing the river", 1.0)
    print(PokerArt.betting_round_header_deluxe("🌊 RIVER", river_community))
    
    time.sleep(3)
    
    # 4. Enhanced Action Menu
    clear_screen_with_effect()
    print(f"{Colors.BOLD}{Colors.GREEN}🎮 INTERACTIVE MENUS 🎮{Colors.RESET}")
    print("=" * 70)
    
    print(CardDisplay.display_pot_info_deluxe(2450, 150))
    print()
    print(CardDisplay.display_action_menu_deluxe(["fold", "call", "raise"], 150))
    
    time.sleep(3)
    
    # 5. Hand Evaluation Showcase
    clear_screen_with_effect()
    print(f"{Colors.BOLD}{Colors.MAGENTA}🏆 HAND EVALUATION SYSTEM 🏆{Colors.RESET}")
    print("=" * 70)
    
    # Create a royal flush for demo
    royal_cards = [
        Card(Rank.ACE, Suit.HEARTS),
        Card(Rank.KING, Suit.HEARTS),
        Card(Rank.QUEEN, Suit.HEARTS),
        Card(Rank.JACK, Suit.HEARTS),
        Card(Rank.TEN, Suit.HEARTS),
        Card(Rank.TWO, Suit.SPADES),
        Card(Rank.THREE, Suit.CLUBS)
    ]
    
    royal_hand = PokerHand(royal_cards)
    
    print(CardDisplay.display_cards_with_shadow(royal_cards[:2], "🃏 Your Hole Cards"))
    print()
    print(CardDisplay.display_cards_with_shadow(royal_cards[2:7], "🌟 Community Cards"))
    print()
    print(f"{Colors.BOLD}{Colors.YELLOW}✨ Result: {royal_hand} ✨{Colors.RESET}")
    
    time.sleep(3)
    
    # 6. Winner Celebration
    clear_screen_with_effect()
    print(f"{Colors.BOLD}{Colors.YELLOW}🎊 WINNER CELEBRATION 🎊{Colors.RESET}")
    print("=" * 70)
    
    print(PokerArt.winner_celebration_deluxe("You", 5000))
    
    time.sleep(3)
    
    # 7. Final Summary
    clear_screen_with_effect()
    print(PokerArt.title_banner())
    
    print(f"\n{Colors.BOLD}{Colors.GREEN}🎉 ENHANCED FEATURES SUMMARY 🎉{Colors.RESET}")
    print("=" * 70)
    
    features = [
        "✨ Animated title sequences and transitions",
        "🎨 Beautiful ASCII cards with shadow effects",
        "🌈 Rich color schemes using only Python built-ins",
        "🎯 Dynamic betting round headers with sparkles",
        "💫 Loading animations and progress indicators",
        "🎮 Enhanced interactive menus with styling",
        "🏆 Spectacular winner celebrations",
        "💎 Professional casino atmosphere",
        "⚡ Smooth visual effects and timing",
        "🎊 Dramatic showdown presentations"
    ]
    
    for i, feature in enumerate(features):
        print(f"  {feature}")
        time.sleep(0.3)
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}🚀 All created with pure Python - no external dependencies! 🚀{Colors.RESET}")
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}Ready to play the most beautiful poker game in your terminal?{Colors.RESET}")
    print(f"{Colors.YELLOW}Run: ./play.sh or poetry run poker{Colors.RESET}")
    
    print(PokerArt.poker_table_deluxe())

if __name__ == "__main__":
    spectacular_demo()
