# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

board_state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

print(*board_state, sep="\n")

print('What would you like to pick:')
player_x_pick = input()

print(board_state[1][1])