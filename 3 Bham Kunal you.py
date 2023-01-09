
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
    col = index  % 8
    row = index // 8
    index = (row + 1) * 10 + col + 1
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
    return "".join(temp_board)

def find_next_move(board, player, depth):
    possible_move = possible_moves(board, player)
    if player == 'o':
        looking_min = True
    else:
        looking_min = False
    scores = []
    for move in possible_move:
        if looking_min:
            scores.append(max1(make_move(board, player, move), 'x', depth - 1))
        else:
            scores.append(min1(make_move(board, player, move), 'o', depth - 1))
    if looking_min:
        return possible_move[scores.index(min(scores))]
    else:
        return possible_move[scores.index(max(scores))]

def min1(board, player, depth):
    opp = "xo"["ox".index(player)]
    if depth == 0 or game_over(board):
        return score(board, player)
    if len(possible_moves(board, player)) == 0:
        return max1(board, opp, depth - 1)
    outcomes = []
    moves = possible_moves(board, player)
    for i in moves:
        new_board = make_move(board, player, i)
        outcomes.append(max1(new_board, opp, depth - 1))
    return min(outcomes)

def max1(board, player, depth):
    opp = "xo"["ox".index(player)]
    if depth == 0 or game_over(board):
        return score(board, player)
    if len(possible_moves(board, player)) == 0:
        return min1(board, opp, depth - 1)
    outcomes = []
    moves = possible_moves(board, player)
    for i in moves:
        new_board = make_move(board, player, i)
        outcomes.append(min1(new_board, opp, depth - 1))
    return max(outcomes)

def game_over(board):
    if len(possible_moves(board, 'o')) == 0:
        if len(possible_moves(board, 'x')) == 0:
            return True
    return False


def score(board, player):
    corner = [board[0], board[7], board[63], board[56]]
    corner_indexes = [0, 7, 63, 56]
    corners_dict = {
        0: {1, 8, 9},
        7: {6, 14, 15},
        56: {57, 48, 49},
        63: {62, 54, 55}
    }
    # adj_corner = [board[1], board[6], board[62], board[55], board[9], board[14], board[15], board[57], board[48], board[49], board[54], board[8]]
    
    if player =='x':
        multiplier = 1
    if player == 'o':
        multiplier = -1
    opp = "xo"["ox".index(player)]
    to_ret = 0
    if game_over(board):
        opp_count = board.count(opp)
        player_count = board.count(player)
        if opp_count ==  player_count:
            return 0
        if opp_count > player_count:
            return (-1000000000 * multiplier)   
        if player_count > opp_count:
            return (1000000000 * multiplier)
    corner_count = corner.count(player)
    adj_corner_count = 0
    opp_corner_count = corner.count(opp)
    opp_adj_corner_count = 0
    for i in corner_indexes:
        if board[i] == '.':
            for j in corners_dict[i]:
                if board[j] == player:
                    adj_corner_count += 1
                if board[j] == opp:
                    opp_adj_corner_count += 1

    to_ret = to_ret + (multiplier * ((corner_count * 1000) - (adj_corner_count * 100)) - (opp_corner_count * 1000) + (opp_adj_corner_count * 100) + len(possible_moves(board, player)) - len(possible_moves(board, opp)))
    return to_ret

# All your other functions
# print(score("oo.........................ox......xx.......x..................x", 'x'))

import sys
board = sys.argv[1]

player = sys.argv[2]

depth = 1

for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all

   print(find_next_move(board, player, depth))

   depth += 1

# class Strategy():

#    logging = True  # Optional

#    def best_strategy(self, board, player, best_move, still_running):


#        depth = 1

#        for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all

#            best_move.value = find_next_move(board, player, depth)

#            depth += 1