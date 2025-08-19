"""
Visual utilities for the poker game using only Python built-ins.
Enhanced beautiful ASCII art and animations without external dependencies.
"""
import time
import os
import random
from typing import List
from .cards import Card


class Colors:
    """ANSI color codes for beautiful terminal output."""
    # Standard colors
    RED = "\033[91m"
    GREEN = "\033[92m" 
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    GRAY = "\033[90m"
    
    # Background colors
    BG_RED = "\033[101m"
    BG_GREEN = "\033[102m"
    BG_YELLOW = "\033[103m"
    BG_BLUE = "\033[104m"
    BG_MAGENTA = "\033[105m"
    BG_CYAN = "\033[106m"
    
    # Styles
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    
    # Reset
    RESET = "\033[0m"


class PokerArt:
    """Enhanced ASCII art for the poker game."""
    
    @staticmethod
    def animated_title() -> None:
        """Display an animated title sequence."""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Animated casino entrance
        frames = [
            f"""{Colors.YELLOW}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║                    🎰 WELCOME TO THE CASINO 🎰                      ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}""",
            
            f"""{Colors.CYAN}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                        ✨ LIGHTS FLASHING ✨                        ║
    ║                    � WELCOME TO THE CASINO �                      ║
    ║                        💎 DIAMONDS SPARKLING 💎                     ║
    ╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}""",
            
            f"""{Colors.MAGENTA}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                          🌟 VIP ENTRANCE 🌟                         ║
    ║                    🎰 WELCOME TO THE CASINO 🎰                      ║
    ║                          🎊 PREMIUM POKER 🎊                        ║
    ╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}"""
        ]
        
        for frame in frames:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(frame)
            time.sleep(0.8)
    
    @staticmethod
    def title_banner() -> str:
        """Return the main title banner with enhanced styling."""
        return f"""{Colors.BOLD}{Colors.YELLOW}{Colors.BG_BLUE}
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                     � TEXAS HOLD'EM POKER �                           ║
║                         💎 Command Line Casino 💎                        ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.GREEN}{Colors.BOLD}               ★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ★
               ★                 PREMIUM POKER EXPERIENCE                 ★  
               ★ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ★{Colors.RESET}"""
    
    @staticmethod
    def poker_table_deluxe() -> str:
        """Return an enhanced poker table with beautiful styling."""
        return f"""{Colors.GREEN}{Colors.BOLD}
                         ╭─────────────────────────────────────╮
                      ╭──┴─────────────────────────────────────┴──╮
                   ╭──┴─────────────────────────────────────────────┴──╮
                ╭──┴───────────────────────────────────────────────────┴──╮
             ╭──┴─────────────────────────────────────────────────────────┴──╮
          ╭──┴───────────────────────────────────────────────────────────────┴──╮
       ╭──┴─────────────────────────────────────────────────────────────────────┴──╮
    ╭──┴───────────────────────────────────────────────────────────────────────────┴──╮
   ╱                                                                                   ╲
  ╱                          {Colors.YELLOW}💰 PREMIUM POKER TABLE 💰{Colors.GREEN}                          ╲
 ╱                              {Colors.CYAN}🃏 High Stakes Action 🃏{Colors.GREEN}                              ╲
╱                                {Colors.MAGENTA}♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣{Colors.GREEN}                                ╲
╲                              {Colors.YELLOW}🎯 Professional Gaming 🎯{Colors.GREEN}                              ╱
 ╲                              {Colors.RED}💎 Casino Quality 💎{Colors.GREEN}                                ╱
  ╲                                                                                   ╱
   ╲─────────────────────────────────────────────────────────────────────────────────╱
    ╲─────────────────────────────────────────────────────────────────────────────╱
       ╲───────────────────────────────────────────────────────────────────────╱
          ╲─────────────────────────────────────────────────────────────────╱
             ╲───────────────────────────────────────────────────────────╱
                ╲─────────────────────────────────────────────────────╱
                   ╲───────────────────────────────────────────────╱
                      ╲─────────────────────────────────────────╱
                         ╲─────────────────────────────────╱{Colors.RESET}"""
    
    @staticmethod
    def hand_separator_animated() -> None:
        """Display an animated hand separator."""
        separator_frames = [
            f"""{Colors.CYAN}
╔═════════════════════════════════════════════════════════════════════════════╗
║                              🃏 NEW HAND 🃏                               ║
╚═════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}""",
            
            f"""{Colors.MAGENTA}
╔═════════════════════════════════════════════════════════════════════════════╗
║                           ✨ 🃏 NEW HAND 🃏 ✨                            ║
╚═════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}""",
            
            f"""{Colors.YELLOW}
╔═════════════════════════════════════════════════════════════════════════════╗
║                        🌟 ✨ 🃏 NEW HAND 🃏 ✨ 🌟                         ║
╚═════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}"""
        ]
        
        for frame in separator_frames:
            print(frame)
            time.sleep(0.3)
    
    @staticmethod
    def betting_round_header_deluxe(round_name: str, community_cards: List[Card] = None) -> str:
        """Return an enhanced betting round header."""
        # Create sparkle effects
        sparkles = "✨ ⭐ ✨ ⭐ ✨"
        
        if community_cards:
            cards_display = " ".join(str(card) for card in community_cards)
            return f"""{Colors.BOLD}{Colors.BLUE}{Colors.BG_CYAN}
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                    {sparkles}                    │
│                            {round_name.center(20)}                            │
│                        {cards_display.center(25)}                        │
│                    {sparkles}                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}"""
        else:
            return f"""{Colors.BOLD}{Colors.BLUE}{Colors.BG_CYAN}
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                    {sparkles}                    │
│                            {round_name.center(20)}                            │
│                    {sparkles}                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}"""
    
    @staticmethod
    def winner_celebration_deluxe(winner_name: str, amount: int) -> str:
        """Return an elaborate winner celebration."""
        celebration = f"""{Colors.BOLD}{Colors.YELLOW}{Colors.BG_GREEN}
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     🎊 🎉 🏆 🥇 CONGRATULATIONS! 🥇 🏆 🎉 🎊                                ║
║                                                                               ║
║                            🌟 WINNER! 🌟                                    ║
║                              {winner_name.center(15)}                              ║
║                                                                               ║
║                     💰 Wins {amount:,} chips! 💰                           ║
║                                                                               ║
║     💎 ✨ 🎯 🎰 FANTASTIC PLAY! 🎰 🎯 ✨ 💎                               ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}"""
        
        return celebration
    
    @staticmethod
    def loading_animation(message: str, duration: float = 2.0) -> None:
        """Display a beautiful loading animation."""
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        start_time = time.time()
        
        while time.time() - start_time < duration:
            for frame in frames:
                if time.time() - start_time >= duration:
                    break
                print(f"\r{Colors.CYAN}{Colors.BOLD}{frame} {message}...{Colors.RESET}", end="", flush=True)
                time.sleep(0.1)
        
        print(f"\r{Colors.GREEN}{Colors.BOLD}✓ {message} complete!{Colors.RESET}")


class CardDisplay:
    """Enhanced card display utilities using only built-ins."""
    
    @staticmethod
    def enhanced_card_art(card: Card) -> List[str]:
        """Return enhanced ASCII art for a single card."""
        rank_display = card.rank.display.ljust(2)
        suit_char = card.suit.symbol
        color = card.suit.color
        reset = Colors.RESET
        
        # Add card border styling
        border_color = Colors.BOLD + Colors.WHITE
        
        return [
            f"{border_color}┌─────────┐{reset}",
            f"{border_color}│{color}{rank_display:<2}{reset}{border_color}       │{reset}",
            f"{border_color}│         │{reset}",
            f"{border_color}│    {color}{suit_char}{reset}{border_color}    │{reset}",
            f"{border_color}│         │{reset}",
            f"{border_color}│       {color}{rank_display:>2}{reset}{border_color}│{reset}",
            f"{border_color}└─────────┘{reset}"
        ]
    
    @staticmethod
    def display_cards_with_shadow(cards: List[Card], title: str = "") -> str:
        """Display cards with beautiful shadow effects."""
        if not cards:
            return ""
        
        # Get enhanced card art
        card_lines = [CardDisplay.enhanced_card_art(card) for card in cards]
        
        result = []
        if title:
            # Enhanced title with decorations
            title_line = f"{Colors.BOLD}{Colors.CYAN}{'═' * 5} {title} {'═' * 5}{Colors.RESET}"
            result.append(title_line)
            result.append("")
        
        # Display cards with shadow effect
        for line_idx in range(7):
            line = ""
            shadow_line = ""
            
            for card_idx, card_art in enumerate(card_lines):
                line += card_art[line_idx]
                # Add shadow effect
                if line_idx > 0:
                    shadow_line += f"{Colors.GRAY}░{Colors.RESET}"
                
                if card_idx < len(card_lines) - 1:
                    line += " "
                    if line_idx > 0:
                        shadow_line += " "
            
            result.append(line)
            # Add shadow line below each card line (except the first)
            if line_idx > 0 and line_idx == 6:
                shadow_padding = "  "
                result.append(shadow_padding + shadow_line)
        
        return "\n".join(result)
    
    @staticmethod
    def display_hand_summary_deluxe(player_name: str, hole_cards: List[Card], chips: int, current_bet: int = 0) -> str:
        """Display enhanced player hand summary."""
        cards_str = " ".join(str(card) for card in hole_cards)
        
        # Add status indicators
        chip_status = "💰" if chips > 500 else "🪙" if chips > 100 else "🔴"
        
        return f"""{Colors.BOLD}{Colors.CYAN}{Colors.BG_BLUE}
┌─────────────────────────────────────────────────────────────────────┐
│ {chip_status} {player_name:<20} │ 🃏 Cards: {cards_str:<15} │ 💎 Chips: {str(chips):>6} │
│ 💸 Current Bet: {str(current_bet):>6} │ 🎯 Status: {"Active" if chips > 0 else "Out":<8} │              
└─────────────────────────────────────────────────────────────────────┘{Colors.RESET}"""
    
    @staticmethod
    def display_pot_info_deluxe(pot_size: int, current_bet: int) -> str:
        """Display enhanced pot information with animations."""
        pot_icon = "💰" if pot_size > 500 else "🪙"
        bet_icon = "📈" if current_bet > 50 else "💵"
        
        return f"""{Colors.BOLD}{Colors.YELLOW}{Colors.BG_GREEN}
┌─────────────────────────────────────────────────────────────────────┐
│                        {pot_icon} POT INFORMATION {pot_icon}                      │
│                                                                     │
│              🏆 Total Pot: {str(pot_size):>8} chips                      │
│              {bet_icon} Current Bet: {str(current_bet):>8} chips                    │
│                                                                     │
│                    💎 Stakes are rising! 💎                        │
└─────────────────────────────────────────────────────────────────────┘{Colors.RESET}"""
    
    @staticmethod
    def display_action_menu_deluxe(valid_actions: List[str], call_amount: int = 0) -> str:
        """Display enhanced action menu with beautiful styling."""
        action_items = []
        
        if "fold" in valid_actions:
            action_items.append(f"{Colors.RED}{Colors.BOLD}(F)old 🙅‍♂️{Colors.RESET}")
        if "call" in valid_actions:
            action_items.append(f"{Colors.GREEN}{Colors.BOLD}(C)all {call_amount} 📞{Colors.RESET}")
        if "check" in valid_actions:
            action_items.append(f"{Colors.GREEN}{Colors.BOLD}Chec(K) ✋{Colors.RESET}")
        if "raise" in valid_actions:
            action_items.append(f"{Colors.YELLOW}{Colors.BOLD}(R)aise 📈{Colors.RESET}")
        
        action_text = " │ ".join(action_items)
        
        return f"""{Colors.BOLD}{Colors.MAGENTA}{Colors.BG_CYAN}
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│                       🎮 YOUR MOVE! 🎮                             │
│                                                                     │
│                        Choose wisely...                            │
│                                                                     │
│  {action_text.center(65)}  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘{Colors.RESET}"""


def print_with_sparkle_effect(text: str, delay: float = 0.5) -> None:
    """Print text with a sparkle effect animation."""
    sparkles = ["✨", "⭐", "🌟", "💫", "⭐", "✨"]
    
    for i in range(3):
        sparkle = sparkles[i % len(sparkles)]
        print(f"\r{sparkle} {text} {sparkle}", end="", flush=True)
        time.sleep(delay / 3)
    
    print(f"\r{text}")


def clear_screen_with_effect() -> None:
    """Clear screen with a beautiful transition effect."""
    # Create a wipe effect
    for i in range(5):
        print("░" * (20 + i * 10))
        time.sleep(0.1)
    
    os.system('clear' if os.name == 'posix' else 'cls')
