"""
Player classes for the poker game with enhanced visuals.
"""
from typing import List, Optional
from abc import ABC, abstractmethod

from .cards import Card
from .hand_evaluator import PokerHand


class Player(ABC):
    """Abstract base class for poker players."""
    
    def __init__(self, name: str, chips: int = 1000):
        """Initialize a player with name and starting chips."""
        self.name = name
        self.chips = chips
        self.hole_cards: List[Card] = []
        self.current_bet = 0
        self.folded = False
        self.all_in = False
    
    def receive_cards(self, cards: List[Card]) -> None:
        """Receive hole cards."""
        self.hole_cards = cards
    
    def bet(self, amount: int) -> int:
        """Make a bet. Returns the actual amount bet."""
        if amount > self.chips:
            # All-in
            actual_bet = self.chips
            self.all_in = True
        else:
            actual_bet = amount
        
        self.chips -= actual_bet
        self.current_bet += actual_bet
        return actual_bet
    
    def fold(self) -> None:
        """Fold the hand."""
        self.folded = True
    
    def reset_for_new_hand(self) -> None:
        """Reset player state for a new hand."""
        self.hole_cards = []
        self.current_bet = 0
        self.folded = False
        self.all_in = False
    
    def can_act(self) -> bool:
        """Check if player can take an action."""
        return not self.folded and not self.all_in
    
    def get_hand(self, community_cards: List[Card]) -> PokerHand:
        """Get the best poker hand using hole cards and community cards."""
        all_cards = self.hole_cards + community_cards
        return PokerHand(all_cards)
    
    @abstractmethod
    def make_decision(self, community_cards: List[Card], current_bet: int, pot_size: int) -> str:
        """Make a betting decision. Should return 'fold', 'call', 'raise', or 'check'."""
        pass
    
    @abstractmethod
    def get_raise_amount(self, min_raise: int, max_raise: int) -> int:
        """Get the amount to raise when raising."""
        pass


class HumanPlayer(Player):
    """Human player that takes input from the command line."""
    
    def make_decision(self, community_cards: List[Card], current_bet: int, pot_size: int) -> str:
        """Get decision from human input with enhanced visuals."""
        from .visuals import CardDisplay, Colors
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}{Colors.BG_BLUE}🎮 YOUR TURN! 🎮{Colors.RESET}")
        
        # Display hole cards beautifully
        print(CardDisplay.display_cards_with_shadow(self.hole_cards, "🃏 Your Hole Cards"))
        
        # Display community cards if any
        if community_cards:
            print(CardDisplay.display_cards_with_shadow(community_cards, "🌟 Community Cards"))
        
        # Display enhanced game info
        print(f"\n{Colors.CYAN}{Colors.BOLD}💰 Your chips: {Colors.GREEN}{self.chips:,}{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}💵 Pot size: {Colors.YELLOW}{pot_size:,}{Colors.RESET}")
        
        call_amount = current_bet - self.current_bet
        if call_amount > 0:
            print(f"{Colors.CYAN}{Colors.BOLD}📞 To call: {Colors.YELLOW}{call_amount:,}{Colors.RESET}")
        
        # Determine valid actions and display enhanced menu
        if current_bet > self.current_bet:
            valid_actions = ["fold", "call", "raise"]
        else:
            valid_actions = ["check", "raise"]
        
        print(CardDisplay.display_action_menu_deluxe(valid_actions, call_amount))
        
        while True:
            action = input(f"{Colors.BOLD}{Colors.MAGENTA}Your choice: {Colors.RESET}").lower().strip()
            
            if action in ['f', 'fold'] and 'fold' in valid_actions:
                return 'fold'
            elif action in ['c', 'call'] and 'call' in valid_actions:
                return 'call'
            elif action in ['k', 'check'] and 'check' in valid_actions:
                return 'check'
            elif action in ['r', 'raise'] and 'raise' in valid_actions:
                return 'raise'
            else:
                print(f"{Colors.RED}{Colors.BOLD}❌ Invalid action. Please try again.{Colors.RESET}")
    
    def get_raise_amount(self, min_raise: int, max_raise: int) -> int:
        """Get raise amount from human input."""
        from .visuals import Colors
        
        print(f"\n{Colors.BOLD}{Colors.YELLOW}📈 RAISE AMOUNT 📈{Colors.RESET}")
        print(f"Minimum raise: {Colors.GREEN}{min_raise}{Colors.RESET}")
        print(f"Maximum raise: {Colors.GREEN}{max_raise}{Colors.RESET}")
        
        while True:
            try:
                amount = int(input(f"{Colors.CYAN}Enter raise amount: {Colors.RESET}"))
                if min_raise <= amount <= max_raise:
                    return amount
                else:
                    print(f"{Colors.RED}❌ Amount must be between {min_raise} and {max_raise}{Colors.RESET}")
            except ValueError:
                print(f"{Colors.RED}❌ Please enter a valid number{Colors.RESET}")


class AIPlayer(Player):
    """Simple AI player with basic strategy."""
    
    def make_decision(self, community_cards: List[Card], current_bet: int, pot_size: int) -> str:
        """Make decision based on simple AI logic."""
        import random
        
        # Get hand strength (simplified)
        hand_strength = self._evaluate_hand_strength(community_cards)
        call_amount = current_bet - self.current_bet
        
        # Very weak hands - fold if there's a bet
        if hand_strength < 0.3 and call_amount > 0:
            return 'fold'
        
        # Strong hands - raise
        if hand_strength > 0.7:
            if random.random() < 0.6:  # 60% chance to raise with strong hand
                return 'raise'
        
        # Medium hands or conservative play
        if call_amount == 0:
            if random.random() < 0.3:  # 30% chance to bet with medium hand
                return 'raise'
            else:
                return 'check'
        else:
            if hand_strength > 0.4:
                return 'call'
            else:
                return 'fold'
    
    def get_raise_amount(self, min_raise: int, max_raise: int) -> int:
        """Get raise amount for AI."""
        import random
        
        # Prefer smaller raises
        if min_raise == max_raise:
            return min_raise
        
        range_size = max_raise - min_raise
        # 70% chance for smaller raise, 30% for larger
        if random.random() < 0.7:
            return min_raise + random.randint(0, range_size // 3)
        else:
            return min_raise + random.randint(range_size // 3, range_size)
    
    def _evaluate_hand_strength(self, community_cards: List[Card]) -> float:
        """Evaluate hand strength on a scale of 0-1."""
        if len(community_cards) < 5:
            # Pre-flop or early streets - simplified evaluation
            return self._evaluate_preflop_strength()
        
        # Post-flop evaluation
        try:
            hand = self.get_hand(community_cards)
            rank_value = hand.best_hand[0].numeric_value
            
            # Normalize hand rank to 0-1 scale
            return min(rank_value / 10.0, 1.0)
        except:
            return 0.3  # Default to medium strength if evaluation fails
    
    def _evaluate_preflop_strength(self) -> float:
        """Evaluate preflop hand strength."""
        if len(self.hole_cards) != 2:
            return 0.3
        
        card1, card2 = self.hole_cards
        rank1, rank2 = card1.rank.numeric_value, card2.rank.numeric_value
        
        # Pocket pairs
        if rank1 == rank2:
            if rank1 >= 10:  # TT, JJ, QQ, KK, AA
                return 0.9
            elif rank1 >= 7:  # 77, 88, 99
                return 0.7
            else:
                return 0.5
        
        # High cards
        if rank1 >= 12 or rank2 >= 12:  # King or Ace
            if rank1 >= 10 and rank2 >= 10:  # Both high cards
                return 0.8
            return 0.6
        
        # Suited connectors and decent cards
        if abs(rank1 - rank2) <= 2 and rank1 >= 7:
            return 0.5
        
        return 0.3
