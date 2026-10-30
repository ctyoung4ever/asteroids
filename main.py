import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
def main():

    # initialize game
    pygame.init()

    # set screen vars and print
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # FPS setting (called in game loop)
    clock = pygame.time.Clock()
    dt = 0.0


    # game loop (exits when user exits the window from the quit if statement)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    

if __name__ == "__main__":
    main()
