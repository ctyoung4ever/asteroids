import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():

    # initialize game
    pygame.init()

    # set screen vars and print
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # create empty groups, one updateable and one drawable, one for asteroids
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # add player class to the two sprite groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    # FPS setting (called in game loop)
    clock = pygame.time.Clock()
    dt = 0.0


    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # game loop (exits when user exits the window from the quit if statement)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # needs to be before the display.flip()
        updatable.update(dt)
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
