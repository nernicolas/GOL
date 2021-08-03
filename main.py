import pygame, pygame_gui, pygame_menu
import life


# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [600,800]
screen = pygame.display.set_mode(WINDOW_SIZE)
# Set title of screen
pygame.display.set_caption("Game_Of_Life")


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


to_update = False
# -------- Main Program Loop -----------
def start(done=False,to_update=False):
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 5
    HEIGHT = 5
    # This sets the margin between each cell
    MARGIN = 1

    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.

    grid = [[0 for i in range(100)] for j in range(100)]

    # Set row 1, cell 5 to one. (Remember rows and
    # column numbers start at zero.)
    grid[1][5] = 1

    actual_cells = life.alive_cells_from_grid(grid)
    print(actual_cells)

    k=0
    gen=0
    pop=0
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one or zero
                try:
                    grid[row][column] = 1 - grid[row][column]
                    print("Click ", pos, "Grid coordinates: ", row, column)
                except:
                    pass
            elif  pygame.mouse.get_pressed()[0]:
                pos = event.pos
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one or zero
                try:
                    grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)
                except:
                    pass
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    to_update= True
                elif event.key == pygame.K_s:
                    to_update= False
                elif event.key == pygame.K_ESCAPE:
                    done =True
                    break
        if to_update:
            if k == 0:
                actual_cells = life.alive_cells_from_grid(grid)
                pop = len(actual_cells)
                grid, actual_cells = life.update(grid, actual_cells)
                k+=1
            else:
                grid, actual_cells = life.update(grid, actual_cells)
            pop = len(actual_cells)
            gen += 1

        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        for row in range(100):
            for column in range(100):
                color = BLACK
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        pygame.draw.line(screen,GREEN,[0,(WIDTH+MARGIN)*99+2*MARGIN],[WIDTH*10000,(WIDTH+MARGIN)*99+2*MARGIN] )
        generation_text = pygame.font.SysFont(None,24)
        generation_text = generation_text.render("generation :"+str(gen), True, GREEN)
        population_text = pygame.font.SysFont(None, 24)
        population_text = population_text.render("population :" + str(pop), True, GREEN)
        screen.blit(generation_text,(20,(WIDTH+MARGIN)*101+2*MARGIN))
        screen.blit(population_text,(20,(WIDTH+MARGIN)*104+2*MARGIN))


        # Limit to 60 frames per second
        clock.tick(90)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
menu = pygame_menu.Menu(600, 600, 'Game Of Life',
                       theme=pygame_menu.themes.THEME_DARK)

menu.add.button('Play', start)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
pygame.quit()


