import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_SHOOT_SPEED
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot



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
    shots = pygame.sprite.Group()

    # add player class to the two sprite groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

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

        # iterate over all objects in asteroids. If any collide with player, print message
        for i in asteroids:
            if i.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        for i in asteroids:
            for x in shots:
                if x.collides_with(i):
                    log_event("asteroid_shot")
                    x.kill()
                    i.kill()

        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
