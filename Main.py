import pygame
'''
Sudoku Rules:
Cannot have the same numbers in the same square of 3 by 3
Cannot have the same numbers in the same column and row
Numbers from 1-9 are inputed
Each box, column, and row is equal to 45
'''
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sudoku by Monica Phann")

clock = pygame.time.Clock()

width = screen.get_width()
height = screen.get_height()
#Line Positioning using .Vector2 which is x and y
center_screen = pygame.Vector2(width/ 2, height / 2)

#Left Line
vert_left_top = pygame.Vector2(width/3,0)
vert_left_bottom = pygame.Vector2(width/3,height)

#Right Line
vert_right_top = pygame.Vector2((width/3)*2,0)
vert_right_bottom = pygame.Vector2((width/3)*2,height)

#Top Line
horz_left_top = pygame.Vector2(0,(height/3))
horiz_right_top = pygame.Vector2(width,(height/3))

#Bottom Line
horz_left_bottom = pygame.Vector2(0,(height/3)*2)
horz_right_bottom = pygame.Vector2(width,(height/3)*2)


black_color = (0,0,0)

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    #Draws two vertical lines
    pygame.draw.line(screen,black_color, vert_left_top, vert_left_bottom,10)
    pygame.draw.line(screen,black_color, vert_right_top, vert_right_bottom,10)

    #Draws two horizontal lines
    pygame.draw.line(screen,black_color,horz_left_top,horiz_right_top,10)
    pygame.draw.line(screen,black_color,horz_left_bottom,horz_right_bottom,10)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key & pygame.K_x:
                print("x was pressed")
            if event.key & pygame.K_o:
                    print("o was pressed")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()
