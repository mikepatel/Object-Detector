"""


"""
################################################################################
# Imports
import pygame


################################################################################
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RADIUS = 7
DRAW = False
LAST_POS = (0, 0)


################################################################################
# roundline
def roundline(surface, color, start, end, radius=1):
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    distance = max(abs(dx), abs(dy))

    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(surface, color, (x, y), radius)


# crope
def crope(original):
    cropped = pygame.Surface((SCREEN_WIDTH-5, SCREEN_HEIGHT-5))
    cropped.blit(original, (0, 0), (0, 0, SCREEN_WIDTH-5, SCREEN_HEIGHT-5))
    return cropped


# show output image
def show_output_image(image):
    surface = pygame.pixelcopy.make_surface(image)
    surface = pygame.transform.rotate(surface, -270)
    surface = pygame.transform.flip(surface, 0, 1)
    screen.blit(surface, (SCREEN_WIDTH+2, 0))


################################################################################
# Main
if __name__ == "__main__":
    pygame.init()

    # set up drawing window
    screen = pygame.display.set_mode(size=[SCREEN_WIDTH, SCREEN_HEIGHT])

    running = True
    points = []

    while running:
        for event in pygame.event.get():
            # close window button
            if event.type == pygame.QUIT:
                running = False

            # draw using mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.circle(screen, WHITE, event.pos, RADIUS)
                DRAW = True

            # continue drawing
            if event.type == pygame.MOUSEMOTION:
                if DRAW:
                    pygame.draw.circle(screen, WHITE, event.pos, RADIUS)
                    roundline(screen, WHITE, event.pos, LAST_POS, RADIUS)
                LAST_POS = event.pos

            # stop drawing
            if event.type == pygame.MOUSEBUTTONUP:
                DRAW = False

            pygame.display.flip()

    # done
    pygame.quit()
