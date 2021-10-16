import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# initialize the game
pygame.init()

# Load all images
b_bishop = pygame.transform.scale(pygame.image.load('.\Images\\b_bishop_png_128px.png'), (50, 50))
w_bishop = pygame.transform.scale(pygame.image.load('.\Images\\w_bishop_png_128px.png'), (50, 50))
b_king = pygame.transform.scale(pygame.image.load('.\Images\\b_king_png_128px.png'), (50, 50))
w_king = pygame.transform.scale(pygame.image.load('.\Images\\w_king_png_128px.png'), (50, 50))
b_queen = pygame.transform.scale(pygame.image.load('.\Images\\b_queen_png_128px.png'), (50, 50))
w_queen = pygame.transform.scale(pygame.image.load('.\Images\\w_queen_png_128px.png'), (50, 50))
b_rook = pygame.transform.scale(pygame.image.load('.\Images\\b_rook_png_128px.png'), (50, 50))
w_rook = pygame.transform.scale(pygame.image.load('.\Images\\w_rook_png_128px.png'), (50, 50))
b_pawn = pygame.transform.scale(pygame.image.load('.\Images\\b_pawn_png_128px.png'), (50, 50))
w_pawn = pygame.transform.scale(pygame.image.load('.\Images\\w_pawn_png_128px.png'), (50, 50))
b_knight = pygame.transform.scale(pygame.image.load('.\Images\\b_knight_png_128px.png'), (50, 50))
w_knight = pygame.transform.scale(pygame.image.load('.\Images\\w_knight_png_128px.png'), (50, 50))



# Defin width and height
Height = 600
Width = 600

#  Set title
pygame.display.set_caption('Chess')

# Define screen with width and height variables
screen = pygame.display.set_mode((Height, Width))

# Define game in main loop
running = True
while running:
    # loop through every game event
    for event in pygame.event.get():
        # Check if event is keydown
        if event.type == KEYDOWN:
            # if key is escape then we are done
            if event.key == K_ESCAPE:
                running = False
        # Check if close button is pressed        
        if event.type == pygame.QUIT:
            running = False
    
    # Draw chess board
    size = 75
    colours = [(255, 255, 255), (0, 0, 0,)]
    n = 8
    for row in range(n):
        c_index = row % 2
        for col in range(n):
            square = (col*size, row*size, size, size)
            screen.fill(colours[c_index], square)
            c_index = (c_index + 1) % 2
            
    # Draw black pieces onto the board
    piece_index = ['r1', 'n1', 'b1', 'k', 'q', 'b2', 'n2', 'r2']
    screen.blit(b_bishop, (13+75*(piece_index.index('b1')), 10))
    screen.blit(b_rook, (13+75*(piece_index.index('r1')), 10))
    screen.blit(b_knight, (13+75*(piece_index.index('n1')), 10))
    screen.blit(b_king, (13+75*(piece_index.index('k')), 10))
    screen.blit(b_queen, (13+75*(piece_index.index('q')), 10))
    screen.blit(b_bishop, (13+75*(piece_index.index('b2')), 10))
    screen.blit(b_rook, (13+75*(piece_index.index('r2')), 10))
    screen.blit(b_knight, (13+75*(piece_index.index('n2')), 10))
    for i in range(8):
        screen.blit(b_pawn, ((13+75*i), 85))
        
    # Draw white piece on the board
    screen.blit(w_bishop, (13+75*(piece_index.index('b1')), 10+(7*75)))
    screen.blit(w_rook, (13+75*(piece_index.index('r1')), 10+(7*75)))
    screen.blit(w_knight, (13+75*(piece_index.index('n1')), 10+(7*75)))
    screen.blit(w_king, (13+75*(piece_index.index('k')), 10+(7*75)))
    screen.blit(w_queen, (13+75*(piece_index.index('q')), 10+(7*75)))
    screen.blit(w_bishop, (13+75*(piece_index.index('b2')), 10+(7*75)))
    screen.blit(w_rook, (13+75*(piece_index.index('r2')), 10+(7*75)))
    screen.blit(w_knight, (13+75*(piece_index.index('n2')), 10+(7*75)))
    for i in range(8):
        screen.blit(w_pawn, ((13+75*i), 85+(75 * 5)))
    

    #refresh the screen every loop iteration
    pygame.display.update()
    
    
pygame.quit()
            
        