# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

board_state = [['0A', '1B', '2C'], ['3D', '4E', '5F'], ['6G', '7H', '8I']]


print(*board_state, sep="\n")

for i in range(9):
    print('What would you like to pick:')
    number_as_string = input()
    number_as_int = int(number_as_string)

    y=0
    remainder = number_as_int % 3

    if number_as_int > 2:
        y=1
        if number_as_int > 5:
            y=2

    print(board_state[y][remainder])