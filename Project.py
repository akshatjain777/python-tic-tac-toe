import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        # Creating a new board with all '-'
        self.board = [['-' for j in range(3)] for i in range(3)]

    def select_random_player(self):
        # Assigning chance to one of the two player randomly
        return random.randint(0, 1)

    def select_spot(self, row, col, player):
        self.board[row][col] = player

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

    def show_board(self):
        # Used to show the active board
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def get_input(self, player):
        # Getting input from user
        allowed_values = [1, 2, 3]  # allowed row and column values
        try:
            row = int(input(f'Enter row number to fix spot: '))
            col = int(input(f'Enter column number to fix spot: '))

            if row not in allowed_values or col not in allowed_values:  # checking if values is allowed or not
                print('Not a valid value')
                return self.get_input(player)
            # Checking if spot is not already taken
            elif self.board[row - 1][col - 1] != '-':
                print('Spot already taken, please select another spot')
                return self.get_input(player)
            else:
                return row, col
        except:
            print('Not a valid value')
            return self.get_input(player)

    def start(self):
        # Creating the board
        self.create_board()

        # Selecting player randomly
        player = 'X' if self.select_random_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")
            self.show_board()
            # Taking input from user
            row, col = self.get_input(player)

            # Selecting the spot
            self.select_spot(row - 1, col - 1, player)

            # Checking if any player won
            if self.check_win():
                print(f"Player {player} won!")
                break

            # Checking if match is draw
            if self.check_filled():
                print("Match Draw!")
                break

            # Change Player
            player = 'X' if player == 'O' else 'O'

        # Show final board
        print()
        self.show_board()


# Start the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
