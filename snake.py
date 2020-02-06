__author__ = "WmBansbach"
#-------------------------------------------------------
#   Snake game made from scratch
#-------------------------------------------------------

import pygame
import random
import sys

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)


def drawApple():
    # returns a tuple of random numbers within the screen's boundaries
    return (random.randint(0, width - 10), random.randint(0, height - 10))

if __name__ == "__main__":

    # Window params
    height = 300
    width = 400
    fps = 30


    # Vars for current head position, starting in the middle of the screen
    head_x, head_y = width / 2, height / 2

    # Vars for change in vector
    head_change_x = 0
    head_change_y = 0

    
    snake = []                  # List of lists containing previous head positions [[head_x, head_y], [head_x, head_y]]
    apple_loc = drawApple()     # Apple's current location
    level = 1                   # Level counter
    game_end = False            # Flag for games end
    

    pygame.init()   
    game_display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("SNAKEE")
    game_clock = pygame.time.Clock()
    
    font = pygame.font.SysFont("arial", 18)
    
    while not game_end:
        # Filling screen every frame to remove previous head position
        game_display.fill(white)
        game_display.blit(font.render("Level: " + str(level), True, black), (15, 5))

        # Place apple
        apple = pygame.draw.circle(game_display, red, apple_loc, 5)

        # Place snake head
        snake_head = pygame.Rect((head_x, head_y), (10, 10))
        pygame.draw.rect(game_display, black, snake_head)

        # Place body parts
        if level > 1:
            for i in range(level):
                snake_body = pygame.Rect((snake[len(snake)- i - 1][0], snake[len(snake) - i - 1][1]), (10, 10))
                pygame.draw.rect(game_display, green, snake_body)
    
        pygame.display.update()

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   game_end = True
                # Apple reset
                if event.key == pygame.K_r:
                    apple_loc = drawApple()
                
                if event.key == pygame.K_UP:
                    head_change_y = -10
                    head_change_x = 0
                    
                if event.key == pygame.K_DOWN:
                    head_change_y = 10
                    head_change_x = 0
                    
                if event.key == pygame.K_LEFT:
                    head_change_x = -10
                    head_change_y = 0
                    
                if event.key == pygame.K_RIGHT:
                    head_change_x = 10
                    head_change_y = 0
        
        # Update head position      
        head_x += head_change_x
        head_y += head_change_y

        # Board boundaries
        if head_x > width or head_x < 0 or head_y > height or head_y < 0:
            game_end = True

        # EATTT
        if snake_head.colliderect(apple):
            level += 1
            apple_loc = drawApple()

        # Create new list with current head position
        head_list = []
        head_list.append(head_x)
        head_list.append(head_y)

        # Check for collisions with the body list (snake),
        # being sure to exclude locations not within the current level
        if head_list in snake[len(snake) - level:] and level > 1:
            game_end = True

        # Add current head to body list
        snake.append(head_list)

        # Control the size of body list
        if len(snake) > level:
            del snake[0]

        game_clock.tick(fps)
        
    
    pygame.quit()  
    sys.exit()
