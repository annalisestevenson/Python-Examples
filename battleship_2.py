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

def random_row(board):  # generate the random ship location (in the list keys)
    rand_numb = randint(2, len(board[0]))
    return rand_numb

def random_col(board):
    rand_numb = randint(2, len(board))  # generate the random ship column (in the outer lists)
    return rand_numb

def start_game(board_one, board_two):   # each time the players decides to play again, start with a fresh slate
    del board_one[:]
    del board_two[:]
    print "Let's play Battleship!"
    print "Turn 1"
    build_board_large(board_large)
    build_board_small(board_small)
    show_board(board_one, board_two)
    ship_col_large = random_col(board_large) - 1
    ship_row_large = random_row(board_large) - 1
    ship_col_small = random_col(board_small) - 1
    ship_row_small = random_row(board_small) - 1
    print ship_row_large
    print ship_col_large
    print ship_row_small
    print ship_row_small
    return {
        'ship_col_large': ship_col_large,
        'ship_row_large': ship_row_large,
        'ship_col_small': ship_col_small,
        'ship_row_small': ship_row_small
    }

ship_points = start_game(board_large, board_small)  # assign the new ship locations to the new dictionary "ship_points"

def player_turns(total_turns):
    if total_turns % 2 == 0:  # alternate between player turns by checking for odd numbers
        player_turn = player_two
        return player_turn
    else:
        player_turn = player_one
        return player_turn

def best_out_of(win_state, total_turns=0, player=player_one):   # check the game statistics
    play_again = ""
    if player["wins"] >= 2:     # check who won best out of 3
        print "%s wins best out of 3" % (player["name"])
    elif player["lose"] >= 2:
        print "%s lost best out of 3" % (player["name"])
    elif win_state == 1:    # check if someone won the current game
        print "%s wins this game!" % (player["name"])
        play_again = str(raw_input("Would you like to play again?"))
    elif win_state == 0 and total_turns == 6:
        play_again = str(raw_input("This match was a draw. Would you like to play again? "))
    elif win_state != 6 and total_turns == 6:
        play_again = str(raw_input("Would you like to play again?"))
    if play_again == "yes":
        return play_again
    else:
        exit()

def input_check(ship_row, ship_col, player, board, win_state):  # check/handle the players guesses of the ship points
    while True:
        try:
            guess_row = int(raw_input("Guess Row:"))
            guess_col = int(raw_input("Guess Col:"))
        except ValueError:
            print "Enter a number only."
            continue
        else:
            break
    if guess_row == ship_row and guess_col == ship_col:
        global ship_points
        win_state = 1  # notes that someone has won the current game
        player["wins"] += 1  # add a win to the current player
        print "Congratulations! You sunk my battleship!"
        if best_out_of(win_state) == "yes":
            ship_points = start_game(board_large, board_small)
            return ship_points
    elif player == player_two:  # check the current player to then correlate with the correct board size
        if (guess_row < 0 or guess_row > 3) or (guess_col < 0 or guess_col > 3):
            print "Oops, that's not even in the ocean."
        elif board[guess_row - 1][guess_col - 1] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row - 1][guess_col - 1] = "X"
        show_board(board_large, board_small)
    elif player == player_one:  # check the current player to then correlate with the correct board size
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print "Oops, that's not even in the ocean."
        elif board[guess_row - 1][guess_col - 1] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row - 1][guess_col - 1] = "X"
            win_state = 0
        show_board(board_large, board_small)
    return win_state


for games in range(3):
    games += 1  # 3 games total
    for turns in range(6):  # 6 turns total = 3 turns for each player
        total_turns += 1
        if player_turns(total_turns) == player_one:
            print "It's player Ones's turn"
            input_check(
                ship_points['ship_row_large'],
                ship_points['ship_col_large'],
                player_one, board_large, win_state_change
            )
        elif player_turns(total_turns) == player_two:
            print "It's player Two's turn"
            input_check(
                ship_points['ship_row_small'],
                ship_points['ship_col_small'],
                player_two, board_small, win_state_change
            )
        if total_turns == 6:
            if best_out_of(win_state_change, total_turns) == "yes":
                ship_points = start_game(board_large, board_small)
                continue
            else:
                break
    if games == 6:
            print "The game has ended."
        #   print "Wins: %s" % (player_one[entry])
            exit()
