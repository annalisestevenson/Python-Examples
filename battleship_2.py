__author__ = 'Shawn Daniel'
""" A somewhat odd and primitive game of battleship that expands upon the battleship game as demonstrated in
    Codeacademy's Python lesson 19/19
"""


from random import randint

board_large = []
board_small = []
player_one = {
    "name": "Player 1",
    "wins": 0,
    "lose": 0
}
player_two = {
    "name": "Player 2",
    "wins": 0,
    "lose": 0
}
total_turns = 0
win_state_change = 0


def build_board_large(board):   # create a 5 x 5 board
    for item in range(5):
        board.append(["O"] * 5)


def build_board_small(board):   # create a 3 x 3 board
    for item in range(3):
        board.append(["O"] * 3)


def show_board(board_one, board_two):   # make the lists look more like a simple battleship graph
    print "Board One"
    for row in board_one:
        print " ".join(row)
    print "Board Two"
    for row in board_two:
        print " ".join(row)


def start_game(board_one, board_two):   # each time the players decides to play again, start again from a fresh slate
    print "Let's play Battleship!"
    print "Turn 1"
    del board_one[:]
    del board_two[:]
    build_board_large(board_one)
    build_board_small(board_two)
    show_board(board_one, board_two)
    ship_col_large = (lambda x: randint(1, len(x)))(board_one)
    ship_row_large = (lambda x: randint(1, len(x[0])))(board_one)
    ship_col_small = (lambda x: randint(1, len(x)))(board_two)
    ship_row_small = (lambda x: randint(1, len(x[0])))(board_two)
    print "Board 1 ship column: " + str(ship_row_large)
    print "Board 1 ship row: " + str(ship_col_large)
    print "Board 2 ship column: " + str(ship_row_small)
    print "Board 2 ship row: " + str(ship_col_small)
    return {
        'ship_col_large': ship_col_large,
        'ship_row_large': ship_row_large,
        'ship_col_small': ship_col_small,
        'ship_row_small': ship_row_small
    }

ship_points = start_game(board_large, board_small)  # assign the new ship locations to the new dictionary


def player_turns():
    if total_turns % 2 == 0:  # alternate between player turns by checking for odd numbers
        return player_two
    else:
        return player_one


def best_out_of(win_state, player):   # check the game statistics
    play_again = ""
    if win_state == 1 and player["wins"] < 2:  # check if player one the current game
        print "%s wins this game!" % (player["name"])
        play_again = str(raw_input("Would you like to play again?"))
        if play_again == "yes":
            return play_again
        else:
            exit()
    elif win_state == 0 and total_turns == 6:
        play_again = str(raw_input("This match was a draw. Would you like to play again? "))
    elif win_state != 0 and total_turns == 6:
        play_again = str(raw_input("Would you like to play again?"))
    elif player["wins"] >= 2:     # check who won best out of 3
        print "%s wins best out of 3" % (player["name"])
    elif player["lose"] >= 2:
        print "%s lost best out of 3" % (player["name"])
    else:
        return play_again
    return play_again


def input_check(ship_row, ship_col, player, board):  # check/handle the players guesses of the ship points
    global ship_points
    global total_turns
    global win_state_change
    guess_col = 0
    guess_row = 0
    while True:
        try:
            guess_row = int(raw_input("Guess Row:")) - 1
            guess_col = int(raw_input("Guess Col:")) - 1
        except ValueError:
            print "Enter a number only."
            continue
        else:
            break
    match = guess_row == ship_row - 1 and guess_col == ship_col - 1
    not_on_small_board = (guess_row < 0 or guess_row > 2) or (guess_col < 0 or guess_col > 2)
    not_on_large_board = (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4)
    if match:
        win_state_change = 1  # notes that someone has won the current game
        player["wins"] += 1  # add a win to the current player
        print "Congratulations! You sunk my battleship!"
        if best_out_of(win_state_change, player) == "yes":
            total_turns = 0    # reset / start over from player one again
            ship_points = start_game(board_large, board_small)
    elif not match and player == player_two:  # check the current player to then correlate with the correct board size
        if not_on_small_board:
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        win_state_change = 0
        show_board(board_large, board_small)
    elif not match and player == player_one:  # check the current player to then correlate with the correct board size
        if not_on_large_board:
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        win_state_change = 0
        show_board(board_large, board_small)
    else:
        return win_state_change


for games in range(3):
    games += 1  # 3 games total
    for turns in range(6):  # 6 turns total = 3 turns for each player
        total_turns += 1
        if player_turns() == player_one:
            print "It's player Ones's turn"
            input_check(
                ship_points['ship_row_large'],
                ship_points['ship_col_large'],
                player_one, board_large
            )
        elif player_turns() == player_two:
            print "It's player Two's turn"
            input_check(
                ship_points['ship_row_small'],
                ship_points['ship_col_small'],
                player_two, board_small
            )
        else:
            break
        if total_turns == 6 and player_turns() == player_one:
            if best_out_of(win_state_change, player_one) == "yes":  # check if player wants to play again
                ship_points = {}
                ship_points = start_game(board_large, board_small)
                continue
        elif total_turns == 6 and player_turns() == player_two:
            if best_out_of(win_state_change, player_two) == "yes":
                ship_points = {}
                ship_points = start_game(board_large, board_small)
                continue
        elif total_turns == 6 and best_out_of(win_state_change, player_two) != "yes":
            break
        else:
            continue
    if games == 3:
            print "The game has ended."
        #   print "Wins: %s" % (player_one[entry])
            exit()
    else:
        continue
