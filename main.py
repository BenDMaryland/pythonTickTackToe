
board_state = [['0A', '1B', '2C'], ['3D', '4E', '5F'], ['6G', '7H', '8I']]
#board_state = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

print(*board_state, sep="\n")

def input_handler():
    print('What would you like to pick:')
    number_as_string = input()
    return int(number_as_string)

def position_parser(user_input):
    y = 0
    remainder = user_input % 3

    if user_input > 2:
        y = 1
        if user_input > 5:
            y = 2
    return y, remainder


for i in range(9):
    number_as_int = input_handler()
    nums = position_parser(number_as_int)
    y = nums[0]
    x = nums[1]
    print(board_state[y][x])

    '''
    if board_state[y][remainder] == '-':
        board_state[y][remainder] = 'x'
    print(*board_state, sep="\n")
    '''
