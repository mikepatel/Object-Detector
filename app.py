"""


"""
################################################################################
# Imports
import pygame


################################################################################
# Main
if __name__ == "__main__":
    pygame.init()

    # set up drawing window
    screen = pygame.display.set_mode(size=[500, 500])

    running = True

    while running:
        # close window button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # done
    pygame.quit()
