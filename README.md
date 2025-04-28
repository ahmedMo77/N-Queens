# N-Queens Puzzle Game

The N-Queens Puzzle Game is a graphical application where users can manually place queens on a chessboard to solve the classic N-Queens problem, or they can have the solution automatically computed and visualized. This project is built using Python and Tkinter for the graphical interface and provides both manual and automatic modes.

## Features

- **Manual Mode**: Allows players to place queens on the board and check if the current configuration is valid.
- **Auto-Solve Mode**: Solves the puzzle automatically and visualizes the solutions step-by-step.
- **Multiple Solutions**: Displays all possible solutions to the N-Queens puzzle.
- **Graphical User Interface**: Interactive chessboard with queens represented as chess pieces (`♛`).
- **Reset and Navigation**: Users can reset the board, navigate between solutions, and go back to the main menu.

## Project Structure

The project consists of the following classes:

- **`NQueensSolver`**: Contains the logic for solving the N-Queens problem using backtracking.
- **`NQueensGame`**: The GUI class that manages the game interface and user interactions.
- **`MainMenu`**: The main menu that allows users to select the size of the board and choose between manual or auto-solve modes.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python, no need to install separately)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/n-queens-puzzle.git
   cd n-queens-puzzle
