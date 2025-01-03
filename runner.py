from board import Board 
from constants import *
import pygame
import sys
from static import Static

if __name__ == "__main__":
    pygame.init()
    
    screen = pygame.display.set_mode((HEIGHT,WIDTH))
    pygame.display.set_caption("tic-tac-toe")
    
    game_over = False
    game_started = False
    finished = False
    winner = None
    
    screen_font = pygame.font.Font(None, SCREEN_FONT)
    button_font = pygame.font.Font(None, BUTTON_FONT)
    chip_font = pygame.font.Font(None, CHIP_FONT)
    
    BOARD = Board()
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                square = Static.square(event.pos)
                if game_started and BOARD.is_valid(square[0],square[1]):
                    center = Static.center(square)
                    turn = CHIP_O
                    if BOARD.turn() == True:
                        turn = CHIP_X
                    BOARD.mark_square(square[0],square[1],turn)
                    
                
                if not game_started and play_button.collidepoint(event.pos):
                    game_started = True
                    
                if game_started and finished and replay_button.collidepoint(event.pos):
                    BOARD.initialize_board()
                    game_started = True
                    finished = False
        
        if not game_started and not finished:
            
            screen.fill(START_COLOR)

            # display welcome message
            welcome = screen_font.render("Welcome To TIC-TAC-TOE",0,TEXT_COLOR)
            welcome_rect = welcome.get_rect(center=(WIDTH/2,HEIGHT/4))
            screen.blit(welcome,welcome_rect)
            
            # play button display
            play_button = pygame.Rect(BUTTON_X,BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
            play_text = button_font.render("play",0,BUTTON_TEXT)
            play_text_rect = play_text.get_rect()
            play_text_rect.center = play_button.center
            pygame.draw.rect(screen,BUTTON_COLOR,play_button)
            screen.blit(play_text,play_text_rect)
            
        elif game_started and not finished:
            screen.fill(BG_COLOR)
            Static.draw_board(screen)
            for row in range(BOARD_ROWS):
                for col in range(BOARD_COLS):
                    if BOARD.board[row][col] != '-':
                        center = Static.center((row,col))
                        Static.draw_chip(screen,center,BOARD.board[row][col],chip_font)
                        
            if BOARD.check_if_winner(CHIP_X):
                winner = CHIP_X
                finished = True
                
            elif BOARD.check_if_winner(CHIP_O):
                winner = CHIP_O
                finished = True
                
            if BOARD.board_is_full():
                winner = None
                finished = True
                        
        elif game_started and finished:
            
            screen.fill(START_COLOR)
            
            if winner == CHIP_X:
                winner = screen_font.render(f"                {CHIP_X} WON",0,TEXT_COLOR)
            elif winner == CHIP_O:
                winner = screen_font.render(f"                {CHIP_O} WON",0,TEXT_COLOR)
            elif winner == None:
                winner = screen_font.render("              No One Won",0,TEXT_COLOR)       
                
                
            winner_rect = welcome.get_rect(center=(WIDTH/2,HEIGHT/4))
            screen.blit(winner,winner_rect)
            
             # replay button display
            replay_button = pygame.Rect(BUTTON_X,BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
            replay_text = button_font.render("replay",0,BUTTON_TEXT)
            replay_text_rect = replay_text.get_rect()
            replay_text_rect.center = replay_button.center
            pygame.draw.rect(screen,BUTTON_COLOR,replay_button)
            screen.blit(replay_text,replay_text_rect)
            
            
            
            
            
        pygame.display.flip()
    