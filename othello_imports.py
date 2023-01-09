
i = 0
directions = [i - 11 , i - 10, i - 9, i - 1, i + 1, i + 9, i + 10, i + 11]
def convert_to_100(board):
    starting_board = ['?' for i in range(0,100)]
    for i,val in enumerate(board):
        row = i // 8
        col = i % 8
        starting_board[10 * (row + 1) + (col + 1)] = val
    return list(starting_board)
def convert_10_to_8(i):
    row = i // 10
    col = i % 10
    return 8 * (row - 1) + col - 1

def print_puzzle(board):
    for i in range(0,8):
        for j in range(0,8):
            print(board[i * 8 + j], end= "")
        print()  

def possible_moves(board, token):
    board = convert_to_100(board)
    opp = "xo"["ox".index(token)]
    token_spots = [i for i,val in enumerate(board) if val == token]
    possible_moves = set()
    for spot in token_spots:
        for direction in directions:
            next_index = spot + direction
            while board[next_index] == opp:
                if board[next_index + direction] == '.':
                    possible_moves.add(next_index + direction)
                next_index = next_index + direction
    converted_moves = list()
    for i in possible_moves:
        converted_moves.append(convert_10_to_8(i))
    return converted_moves

def make_move(board, token, index):
    # print(index)
    col = index  % 8
    row = index // 8
    # print(index)
    index = (row + 1) * 10 + col + 1
    # print(index)
    # input()
    # index = ((index // 8) + 1)* 10 + (index % 10) + 1
    board = convert_to_100(board)
    opp = "xo"["ox".index(token)]
    for direction in directions:
        temp_opp_moves = [index]
        temp_index = index + direction
        while board[temp_index] == opp:
            temp_opp_moves.append(temp_index)
            temp_index = temp_index + direction
        if (board[temp_index] == token):
            temp_opp_moves.append(temp_index)
            for i in temp_opp_moves:
                board[i] = token
    temp_board = []
    for i in board:
        if i != "?":
            temp_board.append(i)
    # for i in range(0,8):
    #     for j in range(0,8):
    #         print(temp_board[i * 8 + j], end= "")
    #     print()  
    return "".join(temp_board)
 
# temp_board = "xxoo.xox.....oox......oxo..ooxooo..oox.ox.xxx..oxoox...o.....xox"
# print_puzzle(temp_board)
# input()
# print()
# temp = (possible_moves(temp_board, 'x'))

# print(make_move(temp_board, 'x', temp[0]))