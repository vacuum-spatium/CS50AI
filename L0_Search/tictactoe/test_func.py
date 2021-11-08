import tictactoe as tt

def print_board(board):
    for val in board:
        print(val)
    print("------------")    
        
board = tt.initial_state()
# player = tt.player(board)
# actions = tt.actions(board)
# result = tt.result(board, actions.pop())

# print(result)


# winner = tt.winner(board)
# terminal = tt.terminal(board)
# util = tt.utility(board)

new_board = tt.result(board, tt.minimax(board))
print_board(new_board)

new_board = tt.result(new_board, (1,1))
print_board(new_board)

new_board = tt.result(new_board, tt.minimax(new_board))
print_board(new_board)



# tt.minimax(board)

# print(winner)
# print(terminal)
# print(util)