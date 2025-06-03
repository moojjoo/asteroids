# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    pygame.init()

    # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)



    while True:
        pygame.Surface.fill(
            screen, (0, 0, 0)
        )  # Fill the screen with black color       

        player.draw(screen)  # Draw the player after filling the screen

        pygame.display.flip()

        player.update(dt)

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
