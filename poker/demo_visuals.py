#!/usr/bin/env python3
"""
Demo of the enhanced visual poker game.
"""
import time
from poker_game.cards import Card, Rank, Suit, Deck
from poker_game.visuals import PokerArt, CardDisplay, Colors, print_with_delay
from poker_game.hand_evaluator import PokerHand

def demo_enhanced_poker():
    """Demonstrate the enhanced poker game visuals."""
    print(PokerArt.title_banner())
    print(PokerArt.poker_table())
    
    print_with_delay(f"\n{Colors.BOLD}{Colors.CYAN}🎮 Welcome to the Enhanced Poker Experience! 🎮{Colors.RESET}")
    print_with_delay(f"Let's see what makes this poker game special...\n")
    
    # Demo 1: Beautiful Card Display
    print(f"{Colors.BOLD}{Colors.YELLOW}🃏 Beautiful ASCII Cards 🃏{Colors.RESET}")
    print("=" * 50)
    
    deck = Deck()
    hole_cards = [deck.deal_card(), deck.deal_card()]
    community = [deck.deal_card(), deck.deal_card(), deck.deal_card()]
    
    print(CardDisplay.display_cards_horizontal(hole_cards, "Your Hole Cards:"))
    print()
    print(CardDisplay.display_cards_horizontal(community, "Community Cards (Flop):"))
    
    print_with_delay("", 2)
    
    # Demo 2: Betting Round Headers
    print(f"\n{Colors.BOLD}{Colors.YELLOW}🎯 Dynamic Betting Round Headers 🎯{Colors.RESET}")
    print("=" * 50)
    
    print(PokerArt.betting_round_header("🎲 PRE-FLOP"))
    time.sleep(1)
    print(PokerArt.betting_round_header("🃏 FLOP", community))
    time.sleep(1)
    
    # Add turn and river cards
    turn_card = deck.deal_card()
    river_card = deck.deal_card()
    all_community = community + [turn_card, river_card]
    
    print(PokerArt.betting_round_header("🎯 TURN", community + [turn_card]))
    time.sleep(1)
    print(PokerArt.betting_round_header("🌊 RIVER", all_community))
    
    print_with_delay("", 2)
    
    # Demo 3: Action Menu
    print(f"\n{Colors.BOLD}{Colors.YELLOW}🎮 Interactive Action Menu 🎮{Colors.RESET}")
    print("=" * 50)
    print(CardDisplay.display_action_menu(["fold", "call", "raise"], 75))
    
    print_with_delay("", 2)
    
    # Demo 4: Hand Evaluation
    print(f"\n{Colors.BOLD}{Colors.YELLOW}🏆 Hand Evaluation System 🏆{Colors.RESET}")
    print("=" * 50)
    
    # Create a strong hand for demo
    royal_flush_cards = [
        Card(Rank.ACE, Suit.HEARTS),
        Card(Rank.KING, Suit.HEARTS),
        Card(Rank.QUEEN, Suit.HEARTS),
        Card(Rank.JACK, Suit.HEARTS),
        Card(Rank.TEN, Suit.HEARTS),
        Card(Rank.TWO, Suit.SPADES),
        Card(Rank.THREE, Suit.CLUBS)
    ]
    
    royal_hand = PokerHand(royal_flush_cards)
    print(CardDisplay.display_cards_horizontal(royal_flush_cards[:2], "Royal Flush Hole Cards:"))
    print()
    print(CardDisplay.display_cards_horizontal(royal_flush_cards[2:7], "Community Cards:"))
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}🎉 Result: {royal_hand} 🎉{Colors.RESET}")
    
    print_with_delay("", 2)
    
    # Demo 5: Winner Banner
    print(f"\n{Colors.BOLD}{Colors.YELLOW}🏆 Winner Celebration 🏆{Colors.RESET}")
    print("=" * 50)
    print(PokerArt.winner_banner("You", 2500))
    
    print_with_delay("", 2)
    
    # Demo 6: Showdown
    print(f"\n{Colors.BOLD}{Colors.YELLOW}🎊 Showdown Display 🎊{Colors.RESET}")
    print("=" * 50)
    print(PokerArt.showdown_banner())
    
    print_with_delay("", 1)
    
    print(f"\n{Colors.BOLD}{Colors.GREEN}🎉 Enhanced Features Summary: 🎉{Colors.RESET}")
    print(f"  {Colors.CYAN}✨ Colorful ANSI terminal output{Colors.RESET}")
    print(f"  {Colors.CYAN}🎨 Beautiful ASCII card displays{Colors.RESET}")
    print(f"  {Colors.CYAN}🎯 Dynamic betting round headers{Colors.RESET}")
    print(f"  {Colors.CYAN}🎮 Interactive action menus{Colors.RESET}")
    print(f"  {Colors.CYAN}🏆 Dramatic winner celebrations{Colors.RESET}")
    print(f"  {Colors.CYAN}🎊 Exciting showdown presentations{Colors.RESET}")
    print(f"  {Colors.CYAN}⏱️  Timed delays for dramatic effect{Colors.RESET}")
    
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}Ready to play the most visual poker game in your terminal? 🚀{Colors.RESET}")
    print(f"{Colors.YELLOW}Run: ./play.sh or poetry run poker{Colors.RESET}")

if __name__ == "__main__":
    demo_enhanced_poker()
