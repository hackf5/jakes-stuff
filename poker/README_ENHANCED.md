# 🎰 Beautiful Command Line Poker 🎰

**The most stunning Texas Hold'em poker experience in your terminal!**

## ✨ Enhanced Visual Features ✨

### 🎨 **Pure Python Beauty** - *No External Dependencies!*
- **Spectacular ASCII Art** with animated sequences
- **Rich Color Schemes** using ANSI escape codes  
- **Shadow Effects** on cards and UI elements
- **Sparkle Animations** for text displays
- **Professional Casino Atmosphere** with deluxe table graphics

### 🃏 **Enhanced Card System**
- **Colorized Cards** with suit-specific colors (♥️ red, ♠️ black, etc.)
- **Shadow Effects** that make cards pop off the screen
- **Artistic Borders** with professional styling
- **Community Card Displays** with elegant layouts

### 🎯 **Dynamic Game Flow**
- **Animated Title Sequences** with typewriter effects
- **Loading Animations** with progress indicators
- **Enhanced Betting Rounds** with sparkle headers
- **Winner Celebrations** with confetti animations
- **Smooth Transitions** between game states

### 🎮 **Interactive Experience**
- **Enhanced Menus** with professional styling
- **Pot Information Displays** with visual flair
- **Action Confirmations** with animation feedback
- **Chip Count Displays** with currency formatting
- **Error Messages** with gentle animations

## 🚀 **Game Features**

### 🏆 **Complete Texas Hold'em Implementation**
- **Full Betting Rounds**: Pre-flop, Flop, Turn, River
- **Professional Hand Evaluation**: 7-card evaluation system
- **Smart AI Opponents**: Realistic betting strategies and bluffing
- **Blind Management**: Small/big blind rotation
- **Pot Management**: Side pots and all-in scenarios

### 🎯 **Advanced Poker Logic**
- **Hand Rankings**: Royal Flush through High Card
- **Tie Breaking**: Proper kicker evaluation
- **Betting Actions**: Check, Call, Raise, Fold, All-in
- **Position Management**: Dealer button rotation
- **Multi-player Support**: 2-8 players

## 📦 Installation & Setup

### Using Poetry (Recommended)
```bash
# Clone the repository
git clone <your-repo-url>
cd poker

# Install dependencies
poetry install

# Run the game
poetry run poker

# Or run the enhanced demo
poetry run python enhanced_demo.py
```

### Direct Python Execution
```bash
# Run the enhanced main
python3 -m poker_game.main_enhanced

# Run the spectacular demo
python3 enhanced_demo.py

# Run the original version
python3 -m poker_game.main
```

## 🎬 **Visual Demo**

Run the enhanced demo to see all the stunning features in action:

```bash
python3 enhanced_demo.py
```

This showcases:
- 🎭 Animated title sequences
- 🃏 Beautiful card displays with shadows
- 🎯 Dynamic betting round animations
- 🎮 Interactive menu systems
- 🏆 Hand evaluation demonstrations
- 🎊 Winner celebration effects

## 🎪 **Game Controls**

### During Your Turn:
- **F** - Fold your hand 🙅‍♂️
- **C** - Call the current bet 📞
- **R** - Raise the bet 📈
- **A** - Go All-in 🚀 (when available)

### Game Flow:
- **Enter** - Continue to next action
- **Y/N** - Continue to next hand
- **Ctrl+C** - Exit gracefully

## 🏗️ **Project Structure**

```
poker/
├── poker_game/
│   ├── __init__.py
│   ├── cards.py           # Enhanced card system with ASCII art
│   ├── hand_evaluator.py  # Comprehensive hand evaluation
│   ├── player.py          # Human & AI player implementations
│   ├── game.py            # Main game orchestration
│   ├── visuals.py         # 🎨 Enhanced visual effects system
│   ├── main.py            # Original entry point
│   └── main_enhanced.py   # ✨ Enhanced beautiful entry point
├── tests/
│   └── test_*.py          # Comprehensive test suite
├── enhanced_demo.py       # 🎬 Spectacular feature demo
├── play.sh               # Quick launch script
├── pyproject.toml        # Poetry configuration
└── README.md             # This file
```

## 🔧 **Technical Highlights**

### 🎨 **Visual System** (`visuals.py`)
- **PokerArt Class**: Animated ASCII art and table graphics
- **CardDisplay Class**: Enhanced card rendering with shadows
- **Colors Class**: ANSI color code management
- **Animation Functions**: Loading bars, sparkle effects, transitions

### 🃏 **Card System** (`cards.py`)
- **Enhanced ASCII Cards**: Colorized with suit-specific styling
- **Shadow Effects**: Professional card presentation
- **Deck Management**: Shuffling with visual feedback

### 🧠 **AI System** (`player.py`)
- **Realistic Strategy**: Hand strength evaluation
- **Bluffing Logic**: Probability-based deception
- **Position Awareness**: Betting position considerations

### 🎯 **Game Engine** (`game.py`)
- **State Management**: Clean game flow handling
- **Betting Logic**: Complex multi-player scenarios
- **Visual Integration**: Seamless animation coordination

## 🎊 **What Makes This Special**

### ✨ **No External Dependencies**
Everything is built with **pure Python stdlib**:
- ANSI escape codes for colors
- Time module for animations  
- Random module for deck shuffling
- Built-in string formatting for layouts

### 🎨 **Professional Visual Design**
- **Casino-quality** table graphics
- **Smooth animations** with perfect timing
- **Color psychology** - reds for hearts/diamonds, etc.
- **Typography effects** with borders and shadows

### 🚀 **Performance Optimized**
- **Efficient rendering** with minimal screen updates
- **Smart animation timing** for smooth experience
- **Memory conscious** card and game state management

## 🎭 **Screenshots in Text**

```
╔═══════════════════════════════════════════════════════════════════╗
║                    🎰 TEXAS HOLD'EM POKER 🎰                     ║
║                        Command Line Casino                        ║
╚═══════════════════════════════════════════════════════════════════╝

═════ 🃏 Your Hole Cards ═════

┌─────────┐ ┌─────────┐
│A        │ │K        │
│         │ │         │
│    ♠    │ │    ♥    │
│         │ │         │
│       A │ │       K │
└─────────┘ └─────────┘
  ░ ░       ░ ░

┌─────────────────────────────────────────────────────────────────────┐
│                       🎮 YOUR MOVE! 🎮                             │
│                                                                     │
│  (F)old 🙅‍♂️ │ (C)all 50 📞 │ (R)aise 📈  │
└─────────────────────────────────────────────────────────────────────┘
```

## 🏆 **Contributing**

Feel free to enhance this beautiful poker experience:
- 🎨 Add more visual effects
- 🧠 Improve AI strategies  
- 🎯 Add tournament modes
- 📊 Include statistics tracking

## 📜 **License**

MIT License - Feel free to use and enhance this beautiful poker game!

---

**🎊 Enjoy the most beautiful command-line poker experience ever created! 🎊**

*Created with ❤️ using pure Python - no external dependencies required!*
