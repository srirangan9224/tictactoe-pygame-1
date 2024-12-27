from constants import *
import pygame

class Static:
    @staticmethod
    def draw_board(screen):
        #draw horizontal lines
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
            )
        #draw vertical lines
        for i in range(1, BOARD_COLS):
            pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
            )
            
    @staticmethod        
    def square(pos):
        x,y = pos
        return (x // SQUARE_SIZE, y // SQUARE_SIZE)
    
    @staticmethod
    def center(square):
        x,y = square
        return ((x*SQUARE_SIZE+SQUARE_SIZE/2),(y*SQUARE_SIZE+SQUARE_SIZE/2))
    
    @staticmethod
    def draw_chip(screen,center,chip,chip_font):       
        if chip == CHIP_X:
            chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
            chip_x_rect = chip_x_surf.get_rect(center=center)
            screen.blit(chip_x_surf, chip_x_rect)

            
        elif chip == CHIP_O:
            chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)
            chip_o_rect = chip_o_surf.get_rect(center=center)
            screen.blit(chip_o_surf, chip_o_rect)   
            
        else:
            raise ValueError(f"Invalid chip type: {chip}. Expected 'x' or 'o'.")