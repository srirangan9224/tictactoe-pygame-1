# Tic-Tac-Toe

This is a simple implementation of the classic Tic-Tac-Toe game using Python and the Pygame library.

## Features

- **Two-player mode**: Play against another human player.
- **Graphical interface**: Interactive GUI built with Pygame.
- **Win and draw detection**: Automatically identifies game outcomes.

## Requirements

- Python 3.6 or higher
- Pygame library

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/srirangan9224/tictactoe-pygame-1.git

2. **install requirements.txt**:

    ```bash
    pip install -r requirements.txt

    (or)

    pip3 install -r requirements.txt

## File Descriptions

Here's a breakdown of the files included in this project and their purposes:

### `runner.py`
- **Purpose**: The main script that initializes and runs the game.
- **Key Features**:
  - Handles the game loop, including drawing the board and checking for win/draw conditions.
  - Manages user input and updates the game state accordingly.

### `board.py`
- **Purpose**: Contains the `Board` class, which represents the Tic-Tac-Toe game board.
- **Key Features**:
  - Maintains the current state of the board.
  - Provides methods to check for valid moves, determine the winner, and reset the game.

### `constants.py`
- **Purpose**: Defines constant values used throughout the project.
- **Key Features**:
  - Stores dimensions, colors, and other configuration details for easy customization.

### `ttt.py`
- **Purpose**: Implements core game logic for Tic-Tac-Toe.
- **Key Features**:
  - Manages player turns.
  - Detects win conditions and handles game state transitions.

### `static.py`
- **Purpose**: Handles static assets such as images and sounds (if used).
- **Key Features**:
  - Loads and manages game resources to enhance user experience.