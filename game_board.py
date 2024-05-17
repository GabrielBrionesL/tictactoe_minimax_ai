import pygame
from constants import *

def draw_lines(screen, color=white):
    for i in range(1, board_rows):
        pygame.draw.line(screen, color, (0, square_size * i), (width, square_size * i), line_width)
        pygame.draw.line(screen, color, (square_size * i, 0), (square_size * i, height), line_width)

def draw_figures(screen, board, color=white):
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, (int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)), circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, (col * square_size + square_size // 4, row * square_size + square_size // 4), (col * square_size + 3 * square_size // 4, row * square_size + 3 * square_size // 4), cross_width)
                pygame.draw.line(screen, color, (col * square_size + square_size // 4, row * square_size + 3 * square_size // 4), (col * square_size + 3 * square_size // 4, row * square_size + square_size // 4), cross_width)
