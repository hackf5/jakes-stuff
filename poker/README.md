# 🎰 Command Line Poker 🎰

A **stunning, fully-featured Texas Hold'em poker game** written in Python that runs in your terminal! Experience casino-quality poker with beautiful ASCII art, colorful interfaces, and smooth gameplay.

## ✨ Visual Features

🎨 **Spectacular ASCII Art**
- Beautiful card displays with suits and colors
- Elegant poker table visualization
- Dynamic betting round headers
- Celebration banners and animations

🌈 **Colorful Terminal Experience**
- Red hearts and diamonds, black clubs and spades
- Color-coded player actions and game states
- Highlighted important information
- Professional casino atmosphere

🎮 **Interactive Visual Interface**
- Clear action menus with visual cues
- Real-time game state displays
- Smooth transitions between game phases
- Dramatic timing and visual effects

## 🃏 Game Features

✨ **Full Texas Hold'em Implementation**
- Complete betting rounds (pre-flop, flop, turn, river)
- Proper hand evaluation and ranking (including Royal Flush, Straight Flush, etc.)
- Multiple AI opponents with realistic strategies
- Chip management and pot calculation
- Blinds system and all-in mechanics

🧠 **Smart AI Opponents**
- AI players with varying strategies
- Hand strength evaluation
- Realistic betting patterns
- Dynamic difficulty scaling

🎯 **Professional Gameplay**
- Standard Texas Hold'em rules
- Complete hand rankings system
- Betting rounds with proper validation
- Tournament-style chip management

## 🎨 Visual Examples

### Beautiful ASCII Card Display
```
Your Hole Cards:

┌─────────┐ ┌─────────┐
│A        │ │K        │
│         │ │         │
│    ♠    │ │    ♥    │
│         │ │         │
│       A │ │       K │
└─────────┘ └─────────┘
```

### Dynamic Betting Round Headers
```
┌─────────────────────────────────────────────────────────────────────┐
│                          🃏 FLOP                                   │
│                     A♠ K♥ Q♦                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Interactive Action Menu
```
┌─────────────────────────────────────────────────────────────┐
│                      🎮 YOUR ACTION 🎮                      │
│                                                             │
│                    (F)old | (C)all 50 | (R)aise                    │
└─────────────────────────────────────────────────────────────┘
```

### Winner Celebration
```
╔═════════════════════════════════════════════════════════════════════╗
║                          🎉 WINNER! 🎉                             ║
║                            Player                            ║
║                        Wins 1500 chips!                        ║
╚═════════════════════════════════════════════════════════════════════╝
```

## Installation

### Quick Start (Recommended)

```bash
cd poker
./play.sh
```

### Manual Installation

```bash
cd poker
poetry install
poetry run poker
```

## 🎮 Visual Demo

Want to see the visual features before playing? Run the demo:

```bash
cd poker
poetry run python demo_visuals.py
```

## How to Play

1. **Starting the Game**: Run `./play.sh` or `poetry run poker`
2. **Enter Your Name**: Type your player name when prompted
3. **Choose Opponents**: Select 1-5 AI opponents
4. **Game Actions**:
   - `f` or `fold` - Fold your hand
   - `c` or `call` - Call the current bet
   - `k` or `check` - Check (when no bet to call)
   - `r` or `raise` - Raise the bet

## Game Rules

This implements standard Texas Hold'em poker:

- Each player gets 2 hole cards (private)
- 5 community cards are dealt in stages (flop: 3, turn: 1, river: 1)
- Players make the best 5-card hand from their 2 hole cards + 5 community cards
- Standard poker hand rankings apply
- Betting rounds occur before the flop, after the flop, turn, and river
- Players start with 1000 chips
- Small blind: 10 chips, Big blind: 20 chips

## Hand Rankings (High to Low)

1. **Royal Flush** - A, K, Q, J, 10 all same suit
2. **Straight Flush** - 5 consecutive cards, same suit
3. **Four of a Kind** - 4 cards of same rank
4. **Full House** - 3 of a kind + pair
5. **Flush** - 5 cards of same suit
6. **Straight** - 5 consecutive cards
7. **Three of a Kind** - 3 cards of same rank
8. **Two Pair** - 2 different pairs
9. **Pair** - 2 cards of same rank
10. **High Card** - Highest card wins

## Example Gameplay

```
🃏 Welcome to Texas Hold'em Poker! 🃏
Starting with 3 players
Small blind: 10, Big blind: 20

==================================================
HAND #1
==================================================
AI 1 posts small blind: 10
AI 2 posts big blind: 20

--- PRE-FLOP ---

Player's turn:
Your hole cards: A♠ K♥
Community cards: 
Your chips: 1000
Current bet to call: 20
Pot size: 30
Actions: (f)old, (c)all, (r)aise
Choose your action: c

--- FLOP: A♦ K♠ 2♣ ---
...
```

## Technical Details

- **Language**: Python 3.12+
- **Dependencies**: No external dependencies (uses only Python standard library)
- **Architecture**: Modular design with separate classes for cards, players, game logic, and hand evaluation
- **Hand Evaluation**: Comprehensive 7-card evaluation system (2 hole + 5 community cards)

## Project Structure

```
poker/
├── poker_game/
│   ├── __init__.py
│   ├── main.py          # Game entry point
│   ├── cards.py         # Card and Deck classes
│   ├── game.py          # Main game logic
│   ├── player.py        # Human and AI player classes
│   └── hand_evaluator.py # Poker hand evaluation
├── tests/
├── pyproject.toml
├── README.md
└── play.sh             # Easy launcher script
```

Enjoy the game! 🃏🎉
