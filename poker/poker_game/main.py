"""
Main entry point for the poker game with enhanced visuals.
"""
import os
from .game import PokerGame
from .visuals import PokerArt, Colors


def main():
    """Main function to start the poker game."""
    try:
        # Clear screen
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Show welcome screen
        print(PokerArt.title_banner())
        print(f"""
{Colors.BOLD}{Colors.CYAN}Welcome to the most exciting poker experience in your terminal!{Colors.RESET}

{Colors.YELLOW}� Game Features:{Colors.RESET}
  • Full Texas Hold'em with all betting rounds
  • Smart AI opponents with realistic strategies  
  • Beautiful ASCII card displays
  • Colorful interface with emojis
  • Professional poker hand evaluation

{Colors.GREEN}🚀 Ready to test your poker skills?{Colors.RESET}
""")
        
        # Get player name
        player_name = input(f"{Colors.BOLD}{Colors.CYAN}Enter your poker name: {Colors.RESET}").strip()
        if not player_name:
            player_name = "Player"
        
        print(f"\n{Colors.GREEN}Welcome to the table, {Colors.BOLD}{player_name}{Colors.RESET}{Colors.GREEN}! 🎉{Colors.RESET}")
        
        # Get number of AI opponents
        while True:
            try:
                num_ai = input(f"\n{Colors.CYAN}Number of AI opponents (1-5) [{Colors.YELLOW}3{Colors.CYAN}]: {Colors.RESET}").strip()
                if not num_ai:
                    num_ai = 3
                else:
                    num_ai = int(num_ai)
                
                if 1 <= num_ai <= 5:
                    break
                else:
                    print(f"{Colors.RED}❌ Please enter a number between 1 and 5{Colors.RESET}")
            except ValueError:
                print(f"{Colors.RED}❌ Please enter a valid number{Colors.RESET}")
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}🎮 Starting game with {num_ai} AI opponents...{Colors.RESET}")
        print(f"{Colors.CYAN}💰 Everyone starts with 1000 chips{Colors.RESET}")
        print(f"{Colors.YELLOW}🎯 Blinds: 10/20{Colors.RESET}")
        
        input(f"\n{Colors.BOLD}Press Enter to deal the first hand... 🃏{Colors.RESET}")
        
        # Start the game
        game = PokerGame(player_name, num_ai)
        game.play_game()
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BOLD}{Colors.MAGENTA}Thanks for playing poker! Come back soon! 👋{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}An error occurred: {e}{Colors.RESET}")
        print(f"{Colors.MAGENTA}Thanks for playing! 👋{Colors.RESET}")


if __name__ == "__main__":
    main()
