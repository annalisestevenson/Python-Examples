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

def check_rand(numb):
    if numb < 0:
        numb += 1
    return numb

def random_row(board):
    rand_numb = randint(0, len(board[0]) - 1)
    check_rand(rand_numb)
    return rand_numb

def random_col(board):
    rand_numb = randint(0, len(board) - 1)
    check_rand(rand_numb)
    return rand_numb


ship_col_large = random_col(board_large)
ship_row_large = random_row(board_large)
ship_col_small = random_col(board_small)
ship_row_small = random_row(board_small)


print "Let's play Battleship!"
print "Turn 1"
show_board(board_large, board_small)
print ship_row_large
print ship_col_large
print ship_row_small
print ship_row_small

def best_out_of(player):
    wins = player["wins"]
    loses = player["loses"]
    if wins >= 2:
        print "%s win best out of 3" % (player)
        player = "win"
        return player
    elif loses >= 2:
        print "%s lost best out of 3" % (player)
        player = "lose"
        return player
    elif wins or loses < 1:
        play_again = str(raw_input("Would you like to play again? "))
        return play_again

def player_turns(total_turns):
    if total_turns % 2 == 0:
        return True
    else:
        return False

player_one = {
    "name": "",
    "wins": 0,
    "loses": 0
}
player_two = {
    "name": "",
    "wins": 0,
    "loses": 0
}

for games in range(3):
    games += 1
    total_turns = 0
    player = 1
    for turns in range(6):
        total_turns += 1
        player_turns(total_turns)
        if player_turns(total_turns) == False:
            print "It's player Ones's turn"
            try:
                guess_row_large = int(raw_input("Guess Row:")) - 1
                guess_col_large = int(raw_input("Guess Col:")) - 1
            except ValueError:
                print "Enter a number only."
                continue
            if guess_row_large == ship_row_large and guess_col_large == ship_col_large:
                player_one["wins"] += 1
                print "Congratulations! You sunk my battleship!"
                show_board(board_large, board_small)
            else:
                if (guess_row_large < 0 or guess_row_large > 4) or (guess_col_large < 0 or guess_col_large > 4):
                    print "Oops, that's not even in the ocean."
                elif board_large[guess_row_large][guess_col_large] == "X":
                    print "You guessed that one already."
                else:
                    print "You missed my battleship!"
                    board_large[guess_row_large][guess_col_large] = "X"
                print total_turns + 1
                show_board(board_large, board_small)
        elif player_turns(total_turns) == True:
            print "It's player Two's turn"
            try:
                guess_row_small = int(raw_input("Guess Row:")) - 1
                guess_col_small = int(raw_input("Guess Col:")) - 1
            except ValueError:
                print "Enter a number only."
                continue
            if guess_row_small == ship_row_small and guess_col_small == ship_col_small:
                player_two["wins"] += 1
                print "Congratulations! You sunk my battleship!"
                show_board(board_large, board_small)
            else:
                if (guess_row_small < 0 or guess_row_small > 2) or (guess_col_small < 0 or guess_col_small > 2):
                    print "Oops, that's not even in the ocean."
                elif board_small[guess_row_small][guess_col_small] == "X":
                    print "You guessed that one already."
                else:
                    print "You missed my battleship!"
                    board_small[guess_row_small][guess_col_small] = "X"
                print total_turns + 1
                show_board(board_large, board_small)

        if total_turns == 6:
            print "Game Over"
            if player_turns(total_turns) == False:
                player_one["loses"] += 1
                loses = player_one["loses"]
                wins = player_one["wins"]
                print "In total, player one lost %s times and won %s times" % (loses, wins)
                best_out_of(player_one)
            elif player_turns(total_turns) == True:
                player_two["loses"] += 1
                loses = player_two["loses"]
                wins = player_two["wins"]
                print "In total, player two lost %s times and won %s times" % (loses, wins)
                best_out_of(player_two)
