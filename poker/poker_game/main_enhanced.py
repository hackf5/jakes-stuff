#!/usr/bin/env python3
"""
Enhanced Beautiful Poker Game - Main Entry Point
No external dependencies - pure Python beauty!
"""
import time
import sys
from .game import PokerGame
from .visuals import PokerArt, Colors, clear_screen_with_effect, print_with_sparkle_effect

def get_enhanced_player_setup():
    """Get player name and AI count with enhanced visuals."""
    clear_screen_with_effect()
    print(PokerArt.title_banner())
    print(f"\n{Colors.BOLD}{Colors.CYAN}🎯 PLAYER SETUP 🎯{Colors.RESET}")
    print("=" * 50)
    
    # Get player name
    player_name = input(f"\n{Colors.YELLOW}Enter your poker name: {Colors.CYAN}").strip()
    if not player_name:
        player_name = "Player"
    
    print(f"\n{Colors.GREEN}Welcome to the table, {Colors.BOLD}{player_name}{Colors.RESET}{Colors.GREEN}! 🎉{Colors.RESET}")
    
    # Get AI count
    while True:
        try:
            num_ai = input(f"\n{Colors.CYAN}Number of AI opponents (1-5) [{Colors.YELLOW}3{Colors.CYAN}]: {Colors.RESET}").strip()
            if not num_ai:
                num_ai = 3
            else:
                num_ai = int(num_ai)
            
            if 1 <= num_ai <= 5:
                return player_name, num_ai
            else:
                print(f"{Colors.RED}❌ Please enter a number between 1 and 5{Colors.RESET}")
                time.sleep(1.5)
        except ValueError:
            print(f"{Colors.RED}❌ Please enter a valid number{Colors.RESET}")
            time.sleep(1.5)

def enhanced_welcome_sequence():
    """Display an enhanced welcome sequence."""
    clear_screen_with_effect()
    
    # Animated title
    PokerArt.animated_title()
    time.sleep(2)
    
    clear_screen_with_effect()
    print(PokerArt.title_banner())
    print(PokerArt.poker_table_deluxe())
    
    welcome_messages = [
        "🌟 Welcome to the most beautiful poker game in your terminal!",
        "✨ Enhanced with stunning visuals and smooth animations",
        "🎨 Created with pure Python - no external dependencies",
        "🚀 Get ready for an unforgettable gaming experience!"
    ]
    
    for msg in welcome_messages:
        print_with_sparkle_effect(msg)
        time.sleep(1)
    
    print(f"\n{Colors.YELLOW}Press Enter to begin your poker journey...{Colors.RESET}")
    input()

def main():
    """Main game entry point with enhanced visuals."""
    try:
        # Enhanced welcome sequence
        enhanced_welcome_sequence()
        
        # Get player setup with style
        player_name, num_ai = get_enhanced_player_setup()
        
        # Loading animation
        clear_screen_with_effect()
        PokerArt.loading_animation("Setting up your poker table", 2.0)
        
        # Create and start the game
        game = PokerGame(player_name, num_ai)
        game.play_game()
        
    except KeyboardInterrupt:
        clear_screen_with_effect()
        print(f"\n{Colors.BOLD}{Colors.YELLOW}🎭 Thanks for playing! Come back soon! 🎭{Colors.RESET}")
        print(PokerArt.poker_table_deluxe())
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}❌ An error occurred: {e}{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
