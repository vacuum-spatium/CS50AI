"""
Tic Tac Toe Player
"""

import math
import copy
from random import randrange

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if sum(x.count(X) for x in board) == sum(x.count(O) for x in board):
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_actions = set()
    for ii in range(3):
        for jj in range(3):
            if board[ii][jj] == EMPTY:
                all_actions.add((ii,jj))
    if len(all_actions) == 0:
        all_actions.add((0,0))             
    return all_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if action not in actions(board):
        raise "Action not legal"
    else:
        new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    check_diag1 = set()
    check_diag2 = set()
    for ii in range(3):
        check_diag1.add(board[ii][ii])
        check_diag2.add(board[-ii+2][ii]) 
        check_row = set()
        check_column = set()       
        for jj in range(3):
            check_row.add(board[ii][jj])
            check_column.add(board[jj][ii])
        if len(check_row) == 1 and EMPTY not in check_row:
            return check_row.pop()
        if len(check_column) == 1 and EMPTY not in check_column:
            return check_column.pop()
    if len(check_diag1) == 1 and EMPTY not in check_diag1:
        return check_diag1.pop()
    if len(check_diag2) == 1 and EMPTY not in check_diag2:
        return check_diag2.pop()
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if sum(x.count(EMPTY) for x in board) == 0 or winner(board) != None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """    
    victor = winner(board)
    if victor == X:
        return 1
    elif victor == O:
        return -1
    return 0   


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    optimal = tuple()

    if player(board) == X:

        # if first move, all move choices equally good so pick one at random
        if sum(x.count(EMPTY) for x in board) == 9:
            return (randrange(3),randrange(3))

        # check for win state on next move
        for val in actions(board):
            new_board = result(board, val)
            if terminal(new_board):
                if utility(new_board) == 1:
                    return val

        # if no win state on next move search possible moves
        util = -math.inf 
        for val in actions(board):
            new_board = result(board, val)
            if terminal(new_board):
                util_check = utility(new_board)
            else:
                util_check = utility_find(new_board)
            if util_check > util:
                util = util_check
                optimal = val

            if util == 1:
                return optimal
        
    else:

        # check for win state on next move
        for val in actions(board):
            new_board = result(board, val)
            if terminal(new_board):
                if utility(new_board) == -1:
                    return val

        # if no win state on next move search possible moves
        util = math.inf            
        for val in actions(board):
            new_board = result(board, val)
            if terminal(new_board):
                util_check = utility(new_board)
            else:
                util_check = utility_find(new_board)
            if util_check < util:
                util = util_check
                optimal = val
            if util == -1:
                return optimal
 
    return optimal

def utility_find(board):

    if player(board) == X:

        # check for win state on next move
        for val in actions(board):
            new_board = result(board, val)
            if terminal(new_board):
                if utility(new_board) == 1:
                    return 1

        # if no win state on next move search possible moves
        util = -math.inf    
        for val in actions(board):
            new_board = result(board, val)
            if terminal(new_board):
                util_check = utility(new_board)
            else:
                util_check = utility_find(new_board)
            if util_check > util:
                util = util_check
            if util == 1:
                return util
        return util
        
    else:

        # check for win state on next move
        for val in actions(board):
            new_board = result(board, val)
            if terminal(new_board):
                if utility(new_board) == -1:
                    return -1

        # if no win state on next move search possible moves
        util = math.inf            
        for val in actions(board):
            new_board = result(board, val)
            if terminal(new_board):
                util_check = utility(new_board)
            else:
                util_check = utility_find(new_board)
            if util_check < util:
                util = util_check
            if util == -1:
                return util
        return util