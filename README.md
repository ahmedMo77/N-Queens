   # N-Queens Puzzle Game

**Project Name**: N-Queens Puzzle Game

**Project Description**:  
The N-Queens Puzzle Game is an interactive application that allows users to solve the classic N-Queens problem, both manually and automatically. The game visualizes the board with queens represented as chess pieces (`♛`). Users can choose to place queens manually and check for validity or use an AI-based algorithm to solve the puzzle automatically, displaying all possible solutions. The game is built using Python and Tkinter for the graphical interface and backtracking as the core AI algorithm for solving the puzzle.

## Features

- **Manual Mode**: Users can place queens on the board and check if the configuration is valid.
- **Auto-Solve Mode**: The algorithm solves the puzzle automatically and visualizes the solutions step-by-step.
- **Multiple Solutions**: Displays all possible solutions to the N-Queens puzzle.
- **Graphical User Interface (GUI)**: An interactive chessboard interface built with Tkinter.
- **Reset and Navigation**: Users can reset the board, navigate between solutions, and return to the main menu.

## Technologies Used

- **Programming Language**: Python 3.x
- **GUI Framework**: Tkinter library for GUI
- **AI Algorithm**: Backtracking Algorithm for solving the N-Queens puzzle
- **Project Type**: Interactive Puzzle Game with Graphical Interface

## AI Algorithm

This project uses the **Backtracking Algorithm** to solve the N-Queens problem. The backtracking technique is a form of recursion where the algorithm builds a solution incrementally and backtracks as soon as it detects an invalid state. The key steps include:

1. Place a queen in the first row and try to place it in different columns.
2. For each row, check if placing a queen in a specific column is valid (i.e., it doesn’t conflict with already placed queens).
3. If a valid configuration is found, proceed to the next row.
4. If a conflict is found or all columns are tried, backtrack to the previous row and try the next column.
5. The process continues until all queens are placed on the board.

The algorithm also visualizes all possible solutions to the N-Queens problem, allowing the user to see how the puzzle can be solved in multiple ways.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/ahmedMo77/N-Queens-puzzle.git
   cd N-Queens-puzzle

