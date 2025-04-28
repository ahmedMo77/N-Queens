import tkinter as tk
from tkinter import messagebox
import threading

# -------------- Game Logic --------------

class NQueensSolver:
    def __init__(self, size):
        """Initialize the N-Queens solver with board size."""
        self.size = size
        self.board = [-1] * size
        self.solutions = []
        self.cols = set()
        self.diag1 = set()
        self.diag2 = set()

    def is_safe(self, row, col):
        """Check if placing a queen at (row, col) is safe in O(1)."""
        return (col not in self.cols and
                (row + col) not in self.diag1 and
                (row - col) not in self.diag2)

    def solve(self, row=0, stop_after_first=False):
        """Solve N-Queens using backtracking."""
        if row == self.size:
            self.solutions.append(self.board.copy())
            return stop_after_first
        for col in range(self.size):
            if self.is_safe(row, col):
                self.board[row] = col
                self.cols.add(col)
                self.diag1.add(row + col)
                self.diag2.add(row - col)
                if self.solve(row + 1, stop_after_first):
                    return True
                self.board[row] = -1
                self.cols.remove(col)
                self.diag1.remove(row + col)
                self.diag2.remove(row - col)
        return False

# -------------- GUI Game --------------

class NQueensGame(tk.Frame):
    def __init__(self, master, size=8, is_manual=True):
        """Initialize the N-Queens game GUI."""
        super().__init__(master)
        self.master = master
        self.size = size
        self.is_manual = is_manual
        self.cell_size = 50
        self.board = [-1] * self.size
        self.current_solution = 0
        self.solver = NQueensSolver(self.size)
        self.create_widgets()

    def create_widgets(self):
        """Create the game widgets."""
        canvas_width = self.size * self.cell_size + 2
        canvas_height = self.size * self.cell_size + 2

        self.canvas = tk.Canvas(self.master, width=canvas_width, height=canvas_height,
                                bg="#f0f8ff", highlightthickness=0)
        self.canvas.pack(pady=20)

        btn_frame = tk.Frame(self.master, bg="#f0f8ff")
        btn_frame.pack(pady=10)

        self.reset_button = tk.Button(btn_frame, text="Reset", font=("Poppins", 12, "bold"),
                                    bg="#6fa8dc", fg="white", width=10, command=self.reset_board)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.solve_button = tk.Button(btn_frame, text="Solve", font=("Poppins", 12, "bold"),
                                    bg="#38ada9", fg="white", width=10, command=self.start_auto_solve)
        self.solve_button.pack(side=tk.LEFT, padx=5)

        self.back_button = tk.Button(btn_frame, text="Back to Menu", font=("Poppins", 12, "bold"),
                                    bg="#9b59b6", fg="white", width=12, command=self.back_to_menu)
        self.back_button.pack(side=tk.LEFT, padx=5)

        nav_frame = tk.Frame(self.master, bg="#f0f8ff")
        nav_frame.pack(pady=5)

        self.prev_button = tk.Button(nav_frame, text="Previous", font=("Poppins", 10),
                                    bg="#9b59b6", fg="white", command=self.show_prev_solution)
        self.prev_button.pack(side=tk.LEFT, padx=5)

        self.next_button = tk.Button(nav_frame, text="Next", font=("Poppins", 10),
                                    bg="#9b59b6", fg="white", command=self.show_next_solution)
        self.next_button.pack(side=tk.LEFT, padx=5)

        self.solution_label = tk.Label(nav_frame, text="Solution 0/0", font=("Poppins", 10), bg="#f0f8ff")
        self.solution_label.pack(side=tk.LEFT, padx=5)

        if not self.is_manual:
            self.solve_button.config(state="disabled")
            threading.Thread(target=self.auto_solve, daemon=True).start()
        else:
            self.canvas.bind("<Button-1>", self.place_queen)

        self.draw_board()

    def draw_board(self):
        """Draw the chessboard and queens."""
        self.canvas.delete("all")
        color1 = "#aad1e6"
        color2 = "#ffffff"
        for row in range(self.size):
            for col in range(self.size):
                x1, y1 = col * self.cell_size + 1, row * self.cell_size + 1
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                fill = color1 if (row + col) % 2 == 0 else color2
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="black")
                if self.board[row] == col:
                    self.canvas.create_text(x1 + self.cell_size / 2, y1 + self.cell_size / 2,
                                            text="♛", font=("Poppins", 24, "bold"), fill="black")

    def place_queen(self, event):
        """Handle manual queen placement."""
        col = (event.x - 1) // self.cell_size
        row = (event.y - 1) // self.cell_size
        if not (0 <= row < self.size and 0 <= col < self.size):
            return

        if self.board[row] == col:
            old_col = self.board[row]
            self.board[row] = -1
            self.solver.cols.remove(old_col)
            self.solver.diag1.remove(row + old_col)
            self.solver.diag2.remove(row - old_col)
        elif self.board[row] != -1 or not self.solver.is_safe(row, col):
            messagebox.showerror("Invalid Move", "Cannot place a queen here!")
            return
        else:
            self.board[row] = col
            self.solver.cols.add(col)
            self.solver.diag1.add(row + col)
            self.solver.diag2.add(row - col)

        self.draw_board()

        if all(self.board[r] != -1 for r in range(self.size)) and self.is_valid_solution():
            messagebox.showinfo("Congratulations", "You solved the N-Queens puzzle!")

    def is_valid_solution(self):
        """Check if the current board is a valid solution."""
        for row in range(self.size):
            col = self.board[row]
            self.solver.cols.remove(col)
            self.solver.diag1.remove(row + col)
            self.solver.diag2.remove(row - col)
            if not self.solver.is_safe(row, col):
                self.solver.cols.add(col)
                self.solver.diag1.add(row + col)
                self.solver.diag2.add(row - col)
                return False
            self.solver.cols.add(col)
            self.solver.diag1.add(row + col)
            self.solver.diag2.add(row - col)
        return True

    def reset_board(self):
        """Reset the board and solution state."""
        self.board = [-1] * self.size
        self.solver.solutions.clear()
        self.current_solution = 0
        self.solver.cols.clear()
        self.solver.diag1.clear()
        self.solver.diag2.clear()
        self.update_solution_label()
        self.prev_button.config(state="disabled")
        self.next_button.config(state="disabled")
        self.draw_board()

    def back_to_menu(self):
        """Return to the main menu."""
        for widget in self.master.winfo_children():
            widget.destroy()
        MainMenu(self.master)

    def start_auto_solve(self):
        """Start auto-solving in manual mode."""
        self.solve_button.config(state="disabled")
        threading.Thread(target=self.auto_solve, daemon=True).start()

    def auto_solve(self):
        """Solve the puzzle automatically with visualization."""
        self.solver.solve()
        if self.solver.solutions:
            self.current_solution = 0
            self.board = self.solver.solutions[0].copy()
            self.update_solution_label()
            self.prev_button.config(state="normal")
            self.next_button.config(state="normal")
            self.draw_board()
            messagebox.showinfo("Solved!", f"Found {len(self.solver.solutions)} solutions!")
        else:
            messagebox.showerror("Error", "No solution found!")
        self.solve_button.config(state="normal")

    def show_prev_solution(self):
        """Show the previous solution."""
        if self.solver.solutions and self.current_solution > 0:
            self.current_solution -= 1
            self.board = self.solver.solutions[self.current_solution].copy()
            self.draw_board()
            self.update_solution_label()

    def show_next_solution(self):
        """Show the next solution."""
        if self.solver.solutions and self.current_solution < len(self.solver.solutions) - 1:
            self.current_solution += 1
            self.board = self.solver.solutions[self.current_solution].copy()
            self.draw_board()
            self.update_solution_label()

    def update_solution_label(self):
        """Update the solution counter label."""
        total = len(self.solver.solutions)
        current = self.current_solution + 1
        self.solution_label.config(text=f"Solution {current}/{total}")

# -------------- Main Menu --------------

class MainMenu(tk.Frame):
    def __init__(self, master):
        """Initialize the main menu."""
        super().__init__(master)
        self.master = master
        self.master.configure(bg="#f0f8ff")
        self.create_widgets()

    def validate_spin_input(self, value):
        """Validate Spinbox input in real-time."""
        if value == "":
            return True
        try:
            val = int(value)
            return 4 <= val <= 15
        except ValueError:
            return False

    def create_widgets(self):
        """Create the main menu widgets."""
        title = tk.Label(self.master, text="👑 N Queens Puzzle",
                         font=("Poppins", 32, "bold"), bg="#f0f8ff", fg="#3c6382")
        title.pack(pady=(60, 20))

        spin_frame = tk.Frame(self.master, bg="#f0f8ff")
        spin_frame.pack(pady=(0, 20))

        tk.Label(spin_frame, text="Select Number of Queens:",
                 font=("Poppins", 14), bg="#f0f8ff", fg="#3c6382").pack(side=tk.LEFT)

        self.queen_count = tk.StringVar(value="8")
        validate_cmd = (self.master.register(self.validate_spin_input), '%P')
        spin = tk.Spinbox(spin_frame, from_=4, to=15, textvariable=self.queen_count,
                          font=("Poppins", 14), width=5, validate="key", validatecommand=validate_cmd)
        spin.pack(side=tk.LEFT, padx=10)

        btn_frame = tk.Frame(self.master, bg="#f0f8ff")
        btn_frame.pack()

        tk.Button(btn_frame, text="Play Manually", font=("Poppins", 14, "bold"),
                  bg="#38ada9", fg="white", width=15, command=self.start_manual).pack(side=tk.LEFT, padx=10)

        tk.Button(btn_frame, text="Auto Solve", font=("Poppins", 14, "bold"),
                  bg="#9b59b6", fg="white", width=15, command=self.start_auto).pack(side=tk.LEFT, padx=10)

    def start_manual(self):
        """Start the manual game."""
        size = int(self.queen_count.get())
        for widget in self.master.winfo_children():
            widget.destroy()
        NQueensGame(self.master, size=size, is_manual=True)

    def start_auto(self):
        """Start the auto-solve game."""
        size = int(self.queen_count.get())
        for widget in self.master.winfo_children():
            widget.destroy()
        NQueensGame(self.master, size=size, is_manual=False)

# -------------- Main Loop --------------

if __name__ == "__main__":
    root = tk.Tk()
    root.title("N-Queens Puzzle Game")
    root.geometry("700x700")
    MainMenu(root)
    root.mainloop()
