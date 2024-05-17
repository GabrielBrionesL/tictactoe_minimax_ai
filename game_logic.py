import numpy as np

board = np.zeros((3, 3))

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full(check_board=board):
    for row in range(3):
        for col in range(3):
            if check_board[row][col] == 0:
                return False
    return True

def check_win(player, check_board=board):
    for col in range(3):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True
    for row in range(3):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True
    if check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player:
        return True
    return False

def minimax(minimax_board, depth, is_maximizing):
    if check_win(2, minimax_board):
        return float('inf')  # Best thing that can happen
    elif check_win(1, minimax_board):
        return float('-inf')  # Worst thing that can happen
    elif is_board_full(minimax_board):
        return 0  # Draw/Neutral
    
    if is_maximizing:  
        best_score = -1000
        for row in range(3):
            for col in range(3):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)  # What would the opponent do?
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:  # Pretends to be the player
        best_score = 1000
        for row in range(3):
            for col in range(3):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)  # What would the AI do?
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)  # Change max to min here
        return best_score

def best_move():
    best_score = -1000
    move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = 2  # Change == to = here
                score = minimax(board, 0, False) # Evaluates the possibilities of the opponent
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col) # Position AI should play

    if move != (-1, -1):
        mark_square(move[0], move[1], 2)
        return True
    return False

def restart_game():
    global board
    board = np.zeros((3, 3))
