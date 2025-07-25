# 🎮 TicTacToe Game
A classic TicTacToe game implementation in Python featuring human vs computer gameplay with clean object-oriented design.

# ✨ Features
- Interactive Gameplay: Play against a computer opponent
- Clean Console Interface: Visual board representation with numbered positions
- Smart Game Logic: Automatic win detection and tie handling
- Object-Oriented Design: Modular code structure with separate player classes
- Input Validation: Robust error handling for user inputs

# 🚀 How to Play

- The game displays a numbered board (0-8) showing available positions
- Players take turns placing their markers (X or O)
- Enter a number (0-8) corresponding to your desired position
- The first player to get three markers in a row, column, or diagonal wins
- If all squares are filled without a winner, it's a tie

- Board Layout
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

# 🛠️ Installation & Setup

Clone this repository:

```
git clone https://github.com/yourusername/tictactoe-game.git
cd tictactoe-game
```

Make sure you have Python 3.x installed on your system
Run the game:

```
python game.py
```

# 🎯 Game Components
## TicTacToe Class (game.py)

- Board Management: Handles the 3x3 game board
- Move Validation: Ensures moves are legal
- Win Detection: Checks for winning conditions (rows, columns, diagonals)
- Game Flow: Manages turn-based gameplay

## Player Classes (player.py)

- Player: Base class for all player types
- HumanPlayer: Handles human input with validation
- RandomComputerPlayer: AI opponent that makes random valid moves

# 🤖 Computer AI
The computer opponent uses a random strategy, selecting randomly from all available moves. This provides unpredictable gameplay while ensuring all moves are valid.
