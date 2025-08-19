"""
Main poker game implementation with enhanced visuals.
"""
from typing import List, Optional, Tuple
import time
import os

from .cards import Card, Deck
from .player import Player, HumanPlayer, AIPlayer
from .hand_evaluator import PokerHand
from .visuals import PokerArt, CardDisplay, Colors, print_with_sparkle_effect, clear_screen_with_effect


class PokerGame:
    """Texas Hold'em poker game."""
    
    def __init__(self, player_name: str = "Player", num_ai_players: int = 3):
        """Initialize the poker game."""
        self.deck = Deck()
        self.community_cards: List[Card] = []
        self.pot = 0
        self.current_bet = 0
        self.small_blind = 10
        self.big_blind = 20
        self.dealer_position = 0
        
        # Create players
        self.players: List[Player] = [HumanPlayer(player_name)]
        for i in range(num_ai_players):
            self.players.append(AIPlayer(f"AI {i+1}"))
        
        self.active_players: List[Player] = []
    
    def play_game(self) -> None:
        """Main game loop with enhanced visuals."""
        # Enhanced animated intro
        PokerArt.animated_title()
        time.sleep(1)
        
        clear_screen_with_effect()
        print(PokerArt.title_banner())
        print(PokerArt.poker_table_deluxe())
        
        print_with_sparkle_effect(f"🎮 Welcome to the premium poker experience! 🎮")
        print_with_sparkle_effect(f"Players: {len(self.players)}")
        print_with_sparkle_effect(f"Blinds: {Colors.YELLOW}{self.small_blind}/{self.big_blind}{Colors.RESET}")
        print_with_sparkle_effect(f"Starting chips: {Colors.GREEN}1000{Colors.RESET} per player")
        
        time.sleep(2)
        
        hand_number = 1
        while len([p for p in self.players if p.chips > 0]) > 1:
            clear_screen_with_effect()
            PokerArt.hand_separator_animated()
            print(f"{Colors.BOLD}{Colors.WHITE}💎 HAND #{hand_number} 💎{Colors.RESET}")
            
            self.play_hand()
            hand_number += 1
            
            # Remove players with no chips
            self.players = [p for p in self.players if p.chips > 0]
            
            # Update dealer position
            self.dealer_position = (self.dealer_position + 1) % len(self.players)
            
            # Check if human player is still in the game
            human_player = next((p for p in self.players if isinstance(p, HumanPlayer)), None)
            if not human_player:
                print(f"\n{Colors.RED}{Colors.BOLD}💸 You're eliminated! Thanks for playing! 💸{Colors.RESET}")
                break
            
            if len(self.players) == 1:
                print(PokerArt.winner_celebration_deluxe(self.players[0].name, self.players[0].chips))
                break
            
            # Show chip counts
            self._display_chip_counts()
            
            # Ask if player wants to continue
            print(f"\n{Colors.CYAN}Continue to next hand? (y/n): {Colors.RESET}", end="")
            if input().lower().strip() != 'y':
                break
        
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}🎊 Thanks for playing at our premium casino! �{Colors.RESET}")
        print(PokerArt.poker_table_deluxe())
    
    def play_hand(self) -> None:
        """Play a single hand of poker."""
        # Reset for new hand
        self.deck.reset()
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        
        for player in self.players:
            player.reset_for_new_hand()
        
        self.active_players = [p for p in self.players if p.chips > 0]
        
        if len(self.active_players) < 2:
            return
        
        # Post blinds
        self._post_blinds()
        
        # Deal hole cards
        self._deal_hole_cards()
        
        # Pre-flop betting round
        print(PokerArt.betting_round_header_deluxe("🎲 PRE-FLOP"))
        if self._betting_round():
            return
        
        # Deal the flop
        if len([p for p in self.active_players if not p.folded]) > 1:
            PokerArt.loading_animation("Dealing the flop", 1.5)
            self._deal_flop()
            print(PokerArt.betting_round_header_deluxe("🃏 FLOP", self.community_cards[:3]))
            print(CardDisplay.display_cards_with_shadow(self.community_cards[:3], "🌟 Community Cards 🌟"))
            if self._betting_round():
                return
        
        # Deal the turn
        if len([p for p in self.active_players if not p.folded]) > 1:
            PokerArt.loading_animation("Dealing the turn", 1.0)
            self._deal_turn()
            print(PokerArt.betting_round_header_deluxe("🎯 TURN", self.community_cards))
            print(CardDisplay.display_cards_with_shadow(self.community_cards, "🌟 Community Cards 🌟"))
            if self._betting_round():
                return
        
        # Deal the river
        if len([p for p in self.active_players if not p.folded]) > 1:
            PokerArt.loading_animation("Dealing the river", 1.0)
            self._deal_river()
            print(PokerArt.betting_round_header_deluxe("🌊 RIVER", self.community_cards))
            print(CardDisplay.display_cards_with_shadow(self.community_cards, "🌟 Final Community Cards 🌟"))
            if self._betting_round():
                return
        
        # Showdown
        self._showdown()
    
    def _post_blinds(self) -> None:
        """Post small and big blinds."""
        num_players = len(self.active_players)
        if num_players < 2:
            return
        
        # Small blind
        sb_pos = (self.dealer_position + 1) % num_players
        sb_player = self.active_players[sb_pos]
        sb_amount = sb_player.bet(self.small_blind)
        self.pot += sb_amount
        self.current_bet = sb_amount
        print(f"{Colors.BLUE}{sb_player.name}{Colors.RESET} posts small blind: {Colors.YELLOW}{sb_amount}{Colors.RESET}")
        
        # Big blind
        bb_pos = (self.dealer_position + 2) % num_players
        bb_player = self.active_players[bb_pos]
        bb_amount = bb_player.bet(self.big_blind)
        self.pot += bb_amount
        self.current_bet = bb_amount
        print(f"{Colors.BLUE}{bb_player.name}{Colors.RESET} posts big blind: {Colors.YELLOW}{bb_amount}{Colors.RESET}")
    
    def _deal_hole_cards(self) -> None:
        """Deal hole cards to all players."""
        for player in self.active_players:
            hole_cards = [self.deck.deal_card(), self.deck.deal_card()]
            player.receive_cards(hole_cards)
    
    def _deal_flop(self) -> None:
        """Deal the flop (3 community cards)."""
        self.deck.deal_card()  # Burn card
        for _ in range(3):
            self.community_cards.append(self.deck.deal_card())
    
    def _deal_turn(self) -> None:
        """Deal the turn (4th community card)."""
        self.deck.deal_card()  # Burn card
        self.community_cards.append(self.deck.deal_card())
    
    def _deal_river(self) -> None:
        """Deal the river (5th community card)."""
        self.deck.deal_card()  # Burn card
        self.community_cards.append(self.deck.deal_card())
    
    def _betting_round(self) -> bool:
        """Conduct a betting round. Returns True if hand ends early."""
        # Reset current bets for this round
        for player in self.active_players:
            player.current_bet = 0
        self.current_bet = 0
        
        acting_players = [p for p in self.active_players if p.can_act()]
        if len(acting_players) <= 1:
            return True
        
        # Determine starting position
        if len(self.community_cards) == 0:  # Pre-flop
            start_pos = (self.dealer_position + 3) % len(self.active_players)
        else:  # Post-flop
            start_pos = (self.dealer_position + 1) % len(self.active_players)
        
        last_raiser_pos = None
        current_pos = start_pos
        actions_this_round = 0
        
        while True:
            player = self.active_players[current_pos]
            
            if player.can_act():
                action = self._player_action(player)
                actions_this_round += 1
                
                if action == "raise":
                    last_raiser_pos = current_pos
                elif action == "fold":
                    # Check if only one player remains
                    remaining = [p for p in self.active_players if not p.folded]
                    if len(remaining) == 1:
                        print(PokerArt.winner_celebration_deluxe(remaining[0].name, self.pot))
                        remaining[0].chips += self.pot
                        return True
            
            # Move to next player
            current_pos = (current_pos + 1) % len(self.active_players)
            
            # Check if betting round is complete
            if self._is_betting_round_complete(current_pos, start_pos, last_raiser_pos, actions_this_round):
                break
        
        return False
    
    def _player_action(self, player: Player) -> str:
        """Handle a single player's action with enhanced visuals."""
        call_amount = self.current_bet - player.current_bet
        
        # Display enhanced game state
        print(CardDisplay.display_pot_info_deluxe(self.pot, self.current_bet))
        print(f"\n{Colors.BOLD}{Colors.CYAN}🎯 {player.name}'s Turn 🎯{Colors.RESET}")
        print(f"💰 Chips: {Colors.GREEN}{player.chips}{Colors.RESET} | 💸 Bet this round: {Colors.YELLOW}{player.current_bet}{Colors.RESET}")
        
        decision = player.make_decision(self.community_cards, self.current_bet, self.pot)
        
        if decision == "fold":
            player.fold()
            print(f"{Colors.RED}{Colors.BOLD}{player.name} folds 🙅‍♂️{Colors.RESET}")
            return "fold"
        
        elif decision == "check":
            print(f"{Colors.GREEN}{Colors.BOLD}{player.name} checks ✋{Colors.RESET}")
            return "check"
        
        elif decision == "call":
            actual_bet = player.bet(call_amount)
            self.pot += actual_bet
            print(f"{Colors.GREEN}{Colors.BOLD}{player.name} calls {actual_bet} 📞{Colors.RESET}")
            if actual_bet < call_amount:
                print(f"{Colors.MAGENTA}{Colors.BOLD}🚀 {player.name} is ALL-IN! 🚀{Colors.RESET}")
            return "call"
        
        elif decision == "raise":
            min_raise = max(self.current_bet * 2 - player.current_bet, self.current_bet + self.big_blind - player.current_bet)
            max_raise = player.chips
            
            if min_raise > max_raise:
                # Can't raise, treat as call
                actual_bet = player.bet(call_amount)
                self.pot += actual_bet
                print(f"{Colors.GREEN}{Colors.BOLD}{player.name} calls {actual_bet} (insufficient chips to raise) 📞{Colors.RESET}")
                return "call"
            
            raise_amount = player.get_raise_amount(min_raise, max_raise)
            actual_bet = player.bet(raise_amount)
            self.pot += actual_bet
            self.current_bet = player.current_bet
            print(f"{Colors.YELLOW}{Colors.BOLD}{player.name} raises to {self.current_bet}! 📈{Colors.RESET}")
            
            if actual_bet < raise_amount:
                print(f"{Colors.MAGENTA}{Colors.BOLD}🚀 {player.name} is ALL-IN! 🚀{Colors.RESET}")
            
            return "raise"
        
        return "check"
    
    def _is_betting_round_complete(self, current_pos: int, start_pos: int, last_raiser_pos: Optional[int], actions: int) -> bool:
        """Check if the betting round is complete."""
        acting_players = [p for p in self.active_players if p.can_act()]
        
        if len(acting_players) <= 1:
            return True
        
        # Everyone has had a chance to act
        if actions < len(acting_players):
            return False
        
        # Check if all acting players have matching bets
        for player in acting_players:
            if player.current_bet < self.current_bet and not player.all_in:
                return False
        
        return True
    
    def _showdown(self) -> None:
        """Determine the winner and distribute chips."""
        remaining_players = [p for p in self.active_players if not p.folded]
        
        if len(remaining_players) == 1:
            winner = remaining_players[0]
            print(PokerArt.winner_celebration_deluxe(winner.name, self.pot))
            winner.chips += self.pot
            return
        
        print(PokerArt.showdown_banner())
        print(CardDisplay.display_cards_with_shadow(self.community_cards, "🌟 Final Community Cards 🌟"))
        print()
        
        # Evaluate all hands with enhanced display
        hand_evaluations = []
        for player in remaining_players:
            hand = player.get_hand(self.community_cards)
            hand_evaluations.append((player, hand))
            
            # Show player's cards and hand
            print(f"{Colors.BOLD}{Colors.CYAN}🎯 {player.name}:{Colors.RESET}")
            print(CardDisplay.display_cards_with_shadow(player.hole_cards, "  🃏 Hole Cards"))
            print(f"  {Colors.YELLOW}{Colors.BOLD}✨ Best Hand: {hand} ✨{Colors.RESET}\n")
        
        # Find the winner(s)
        best_hand = max(hand_evaluations, key=lambda x: (x[1].best_hand[0].numeric_value, x[1].best_hand[1]))
        winners = [player for player, hand in hand_evaluations 
                  if hand.compare(best_hand[1]) == 0]
        
        # Distribute pot
        winnings_per_player = self.pot // len(winners)
        remainder = self.pot % len(winners)
        
        for i, winner in enumerate(winners):
            winnings = winnings_per_player + (1 if i < remainder else 0)
            winner.chips += winnings
            if len(winners) == 1:
                print(PokerArt.winner_celebration_deluxe(winner.name, winnings))
                print(f"{Colors.BOLD}{Colors.GREEN}🏆 Winning hand: {best_hand[1]} 🏆{Colors.RESET}")
            else:
                print(f"{Colors.BOLD}{Colors.YELLOW}🤝 {winner.name} ties and wins {winnings:,} chips! 🤝{Colors.RESET}")
        
        time.sleep(2)
    
    def _display_chip_counts(self) -> None:
        """Display current chip counts."""
        print(f"\n{Colors.BOLD}{Colors.CYAN}💰 CHIP COUNTS 💰{Colors.RESET}")
        print("┌" + "─" * 40 + "┐")
        for player in self.players:
            status = "💀" if player.chips == 0 else "💰"
            color = Colors.RED if player.chips == 0 else Colors.GREEN
            print(f"│ {status} {color}{player.name:<15}{Colors.RESET}: {player.chips:>8} chips │")
        print("└" + "─" * 40 + "┘")
