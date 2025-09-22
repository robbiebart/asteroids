import pygame
from constants import *

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while SCREEN_HEIGHT != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # pygame.Surface.fill(screen, (0,0,0))
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()