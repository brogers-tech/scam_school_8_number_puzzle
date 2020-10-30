#The puzzle in scam stuff
#Place the numbers 1 - 8 on the board such that
#no numbers are touching their sequential neighbors
#The board is as follows
#       ___
#      |   |
#  -------------
# |    |   |    |
# |-------------|
# |    |   |    |
#  -------------
#      |   |
#       ---

board = [[None, 0, None],[0, 0, 0],[0, 0, 0], [None, 0, None]]
positions = ((0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 1))

def validate_n_neighbor(board, position, value):
    row = position[0]
    col = position[1]
    nvalue = board[row - 1][col] if row - 1 >= 0 else None
    if nvalue != None and nvalue != 0:
        return abs(value - nvalue) > 1
    return True

def validate_ne_neighbor(board, position, value):
    row = position[0]
    col = position[1]
    nevalue = board[row - 1][col + 1] if row - 1 >= 0 and col + 1 < len(board[row]) else None
    if nevalue != None and nevalue != 0:
        return abs(value - nevalue) > 1
    return True
   
def validate_e_neighbor(board, position, value):
    row = position[0]
    col = position[1]
    evalue = board[row][col + 1] if col + 1 < len(board[row]) else None
    if evalue != None and evalue != 0:
        return abs(value - evalue) > 1
    return True

def validate_se_neighbor(board, position, value):
    row = position[0]
    col = position[1]
    sevalue = board[row + 1][col + 1] if row + 1 < len(board) and col + 1 < len(board[row])  else None
    if sevalue != None and sevalue != 0:
        return abs(value - sevalue) > 1
    return True

def validate_s_neighbor(board, position, value):
    row = position[0]
    col = position[1]
    svalue = board[row + 1][col] if row + 1 < len(board) else None
    if svalue != None and svalue != 0:
        return abs(value - svalue) > 1
    return True

def validate_sw_neighbor(board, position, value):
    row = position[0]
    col = position[1]
    swvalue = board[row + 1][col - 1] if row + 1 < len(board) and col >= 0 else None
    if swvalue != None and swvalue != 0:
        return abs(value - swvalue) > 1
    return True

def validate_w_neighbor(board, position, value):
    row = position[0]
    col = position[1]
    wvalue = board[row][col - 1] if col - 1 >= 0 else None
    if wvalue != None and wvalue != 0:
        return abs(value - wvalue) > 1
    return True

def validate_nw_neighbor(board, position, value):
    row = position[0]
    col = position[1]
    nwvalue = board[row - 1][col - 1] if row - 1 >= 0 and col - 1 >= 0 else None
    if nwvalue != None and nwvalue != 0:
        return abs(value - nwvalue) > 1
    return True

def validate_not_in(board, value):
    for b in board:
        if value in b:
            return False
    return True

def is_valid(board, position, value):
    valid = [
       validate_e_neighbor(board, position, value),
       validate_n_neighbor(board, position, value),
       validate_ne_neighbor(board, position, value),
       validate_nw_neighbor(board, position, value),
       validate_s_neighbor(board, position, value),
       validate_se_neighbor(board, position, value),
       validate_sw_neighbor(board, position, value),
       validate_w_neighbor(board, position, value),
       validate_not_in(board, value)
    ]
    return all(valid)

def solve(board, positions, index):
    if index >= len(positions):
        return True
    position = positions[index]
    (row, col) = position
    solved = False
    for i in range(1, 9):
        valid = is_valid(board, position, i)
        if valid:
            board[row][col] = i 
            solved = solve(board, positions, index + 1)
            if solved:
                break
            else:
                board[row][col] = 0
    else:
        return False
    
    return solved

def print_board(board):
    print('     ---')
    for (i, b) in enumerate(board):
        if i == 0 or i == 3:
            print(f"    | {b[1]} |")
        else:
            if i == 1:
                print('', '-' * 11)
            print('| ' + ' | '.join(map(str, b)) + ' |')
            print('', '-' * 11)
    print('     ---')

solve(board, positions, 0)
print_board(board)















