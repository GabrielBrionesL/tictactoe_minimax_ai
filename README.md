# Tic Tac Toe - You vs AI

This is a simple Tic Tac Toe game where you can play against an AI. The game uses the minimax algorithm for the AI to make optimal moves.

## Features

- Play Tic Tac Toe against a computer AI
- AI uses the minimax algorithm to ensure optimal play
- Simple and intuitive graphical interface using Pygame
- Color-coded game outcomes
  - Green for player win
  - Red for AI win
  - Gray for draw
- Reset the game with the 'R' key

## Getting Started

### Prerequisites

- Python 3.x
- Pygame
- NumPy

### Installation

1. Clone the repository
2. Install the required packages
3. Run the main game file

### How to Play
- Click on a square to make your move.
- The AI will automatically make its move after yours.
- The game will announce the winner by changing the color of the lines:
    - Green lines indicate the player has won.
    - Red lines indicate the AI has won.
    - Gray lines indicate a draw.
- Press the 'R' key to restart the game.

## Project Structure

├── constants.py     # Contains game constants like colors and dimensions
├── drawing.py       # Functions for drawing the game board and figures
├── game_logic.py    # Game logic including move validation and the minimax algorithm
├── main.py          # Main game loop and event handling
└── README.md        # Project documentation
