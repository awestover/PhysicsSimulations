# libraries
from functions import *
from pprint import pprint

num_games = 1#10**2
moves_to_win = []

for game in range(0, num_games):

    # initialize the boards
    boards = [[], [], [], []]
    n = 10
    ships = [[], []]  # player, computer 5 ship 4 ship 3 ship 3 ship 2 ship

    ship_types = {
        '5ship': 5,
        '4ship': 4,
        '3ship1': 3,
        '3ship2': 3,
        '2ship2': 2
    }

    ships_left = [5, 4, 3, 3, 2]


    for i in range(0, 2):
        for j in range(0, 5):
            ships[i].append([])

    # initialize board
    for k in range(0, len(boards)):
        for i in range(0, n):
            boards[k].append([])
            for j in range(0, n):
                boards[k][i].append('N')

    pdb.set_trace()

    boards, ships = place_ships_randomly_cc(boards, ships, n, ships_left)

    ct = 0
    while game_over(boards, n) == "no":
        computer_move(boards, ships_left=ships_left)

        pdb.set_trace()
        pprint(boards)
        ct += 1

    moves_to_win.append(total_moves_made(boards, n, 1))



avg_moves_to_win = 0
for i in range(0, len(moves_to_win)):
    avg_moves_to_win += moves_to_win[i]
avg_moves_to_win /= len(moves_to_win)

print("Moves to win statistics")
print("average " + str(avg_moves_to_win))
print("max " + str(max(moves_to_win)))
print("min " + str(min(moves_to_win)))
