import sys
import pygame
from constants import *
from game_logic import *
from game_board import *

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe - You v AI')
screen.fill(black)
draw_lines(screen)

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // square_size
            mouseY = event.pos[1] // square_size

            if available_square(mouseY, mouseX):  # Is the square available when I click on it?
                mark_square(mouseY, mouseX, player)
                if check_win(player):  # Check for win
                    game_over = True
                player = player % 2 + 1 # Mathematical way to turn a 2 into a 1 and vice versa

                if not game_over:
                    if best_move():
                        if check_win(2):  # Check to see if AI won
                            game_over = True
                        player = player % 2 + 1  # If not, player turn again

                if not game_over:
                    if is_board_full():
                        game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                screen.fill(black)
                draw_lines(screen)
                game_over = False
                player = 1

    if not game_over:
        draw_figures(screen, board)
    else:
        if check_win(1):
            draw_figures(screen, board, green)
            draw_lines(screen, green)
        elif check_win(2):
            draw_figures(screen, board, red)
            draw_lines(screen, red)
        else:
            draw_figures(screen, board, gray)
            draw_lines(screen, gray)
    
    pygame.display.update()