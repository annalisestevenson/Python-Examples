""" A somewhat odd game of battleship that expands upon the battleship game demonstrated in codeacademy
"""


from random import randint

board_large = []
board_small = []

def build_board_large(board):
    for item in range(5):
        board.append(["O"] * 5)

def build_board_small(board):
    for item in range(3):
        board.append(["O"] * 3)

def show_board(board_one, board_two):
    print "Board One"
    for row in board_one:
        print " ".join(row)
    print "Board Two"
    for row in board_two:
        print " ".join(row)

build_board_large(board_large)
build_board_small(board_small)

def random_row(board):
    rand_numb = randint(1, len(board[0]) - 1)
    return rand_numb

def random_col(board):
    rand_numb = randint(1, len(board) - 1)
    return rand_numb


ship_col_large = random_col(board_large)
ship_row_large = random_row(board_large)
ship_col_small = random_col(board_small)
ship_row_small = random_row(board_small)

def start_game():
    print "Let's play Battleship!"
    print "Turn 1"
    show_board(board_large, board_small)
    print ship_row_large
    print ship_col_large
    print ship_row_small
    print ship_row_small

def best_out_of(player, win_state_change):
    play_again = ""
    if player["wins"] >= 2:
        print "%s win best out of 3" % (player["name"])
    elif player["lose"] >= 2:
        print "%s lost best out of 3" % (player["name"])
    elif win_state_change == 1:
        print "%s wins this game!" % (player["name"])
        play_again = str(raw_input("Would you like to play again?"))
    elif win_state_change == 0:
        play_again = str(raw_input("This match was a draw. Would you like to play again? "))
    if play_again == "yes":
        start_game()
    else:
        exit()

def input_check(ship_row, ship_col, player, board):
    while True:
        try:
            guess_row = int(raw_input("Guess Row:")) - 1
            guess_col = int(raw_input("Guess Col:")) - 1
        except ValueError:
            print "Enter a number only."
            continue
        else:
            break
    if guess_row == ship_row and guess_col == ship_col:
        win_state_change = 1  # notes that someone has won the current game
        player["wins"] += 1  # add a win to the current player
        print "Congratulations! You sunk my battleship!"
        best_out_of(player, win_state_change)
    else:
        if player == player_two:  # check the current player to correlate with the correct board size
            if (guess_row < 0 or guess_row > 2) or (guess_col < 0 or guess_col > 2):
                print "Oops, that's not even in the ocean."
            elif board[guess_row][guess_col] == "X":
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
        elif player == player_one:  # check the current player to correlate with the correct board size
            if (guess_row < 0 or guess_row >= 5) or (guess_col < 0 or guess_col >= 5):
                print "Oops, that's not even in the ocean."
            elif board[guess_row][guess_col] == "X":
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
        show_board(board_large, board_small)

total_turns = 0

def player_turns(total_turns):
    if total_turns % 2 == 0:  # alternate between player turns by checking for odd numbers
        player_turn = player_two
        return player_turn
    else:
        player_turn = player_one
        return player_turn

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
start_game()

for games in range(3):
    games += 1  # 3 games total
    for turns in range(6):  # 6 turns total = 3 turns for each player
        total_turns += 1
        if player_turns(total_turns) == player_one:
            print "It's player Ones's turn"
            input_check(ship_row_large, ship_col_large, player_one, board_large)
        elif player_turns(total_turns) == player_two:
            print "It's player Two's turn"
            input_check(ship_row_small, ship_col_small, player_two, board_small)
        if total_turns == 6:
            print "Game Over"
            exit()
            # for entry in player_one:
            #     print entry
            #     print "Wins: %s" % (player_one[entry])
