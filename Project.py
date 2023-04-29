from tkinter import Tk, Button, messagebox, Label, font, Frame
import random


class TicTacToe:

    def __init__(self):
        self.board = []
        self.player = '-'
        self.display = None
        self.root = None

    def create_board(self):
        # Creating a new board with all '-'
        self.board = [['-' for j in range(3)] for i in range(3)]
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title("Tic Tac Toe")
        display_frame = Frame(master=self.root)
        grid_frame = Frame(master=self.root)
        self.player = 'X' if self.select_random_player() == 1 else 'O'
        self.display = Label(
            master=display_frame,
            text=f"{self.player}'s turn",
            font=font.Font(size=28, weight="bold"),
        )

        b1 = Button(grid_frame, text="-", font=("Helvetica", 20), height=3,
                    width=6, bg="white", command=lambda: self.select_spot(1, 1, b1))
        b2 = Button(grid_frame, text="-", font=("Helvetica", 20), height=3,
                    width=6, bg="white", command=lambda: self.select_spot(1, 2, b2))
        b3 = Button(grid_frame, text="-", font=("Helvetica", 20), height=3,
                    width=6, bg="white", command=lambda: self.select_spot(1, 3, b3))
        b4 = Button(grid_frame, text="-", font=("Helvetica", 20), height=3,
                    width=6, bg="white", command=lambda: self.select_spot(2, 1, b4))
        b5 = Button(grid_frame, text="-", font=("Helvetica", 20), height=3,
                    width=6, bg="white", command=lambda: self.select_spot(2, 2, b5))
        b6 = Button(grid_frame, text="-", font=("Helvetica", 20), height=3,
                    width=6, bg="white", command=lambda: self.select_spot(2, 3, b6))
        b7 = Button(grid_frame, text="-", font=("Helvetica", 20), height=3,
                    width=6, bg="white", command=lambda: self.select_spot(3, 1, b7))
        b8 = Button(grid_frame, text="-", font=("Helvetica", 20), height=3,
                    width=6, bg="white", command=lambda: self.select_spot(3, 2, b8))
        b9 = Button(grid_frame, text="-", font=("Helvetica", 20), height=3,
                    width=6, bg="white", command=lambda: self.select_spot(3, 3, b9))
        b1.grid(row=1, column=1)
        b2.grid(row=1, column=2)
        b3.grid(row=1, column=3)
        b4.grid(row=2, column=1)
        b5.grid(row=2, column=2)
        b6.grid(row=2, column=3)
        b7.grid(row=3, column=1)
        b8.grid(row=3, column=2)
        b9.grid(row=3, column=3)

        self.display.pack()
        display_frame.pack()
        grid_frame.pack()
        self.root.mainloop()

    def select_random_player(self):
        # Assigning chance to one of the two player randomly
        return random.randint(0, 1)

    def select_spot(self, row, col, button):
        allowed_values = [1, 2, 3]  # allowed row and column values
        try:
            if row not in allowed_values or col not in allowed_values:  # checking if values is allowed or not
                messagebox.showerror("Tic Tac Toe", "Not a valid value")
            # Checking if spot is not already taken
            elif self.board[row - 1][col - 1] != '-':
                messagebox.showerror("Tic Tac Toe",
                                     'Spot already taken, please select another spot')
            else:
                button["text"] = self.player
                button["state"] = "disabled"
                self.board[row - 1][col - 1] = self.player

                if self.check_win():
                    messagebox.showinfo(
                        "Tic Tac Toe", f"Player {self.player} won!")
                    self.root.destroy()
                    return

                # Checking if match is draw
                if self.check_filled():
                    messagebox.showinfo(
                        "Tic Tac Toe", f"Match Draw!")
                    self.root.destroy()
                    return

                self.player = 'X' if self.player == 'O' else 'O'
                self.display["text"] = f"{self.player}'s turn"
        except:
            messagebox.showerror("Tic Tac Toe", "Not a valid value")

    def check_win(self):
        win_parameters = (
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        )

        for win_param in win_parameters:
            # Checking if all the values in win param is same and not '-'
            row = set([self.board[row][col] for row, col in win_param])
            if len(row) == 1 and list(row)[0] != '-':
                return True

    def check_filled(self):
        # Check if the board is completely filled
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def start(self):
        # Creating the board
        self.create_board()


# Start the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
