from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random

# Create a new class called Asteroid in a new file called asteroid.py that inherits from CircleShape.
class Asteroid(CircleShape):

# Give it a constructor with this signature, and inside it call the parent CircleShape constructor so the sprite is initialized correctly:
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    # override the draw method (polymorphism) to draw the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        self.position += self.velocity * dt

    # add split method
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_number = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_number)
        vector2 = self.velocity.rotate(-random_number)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2


# Otherwise, we need to spawn 2 new asteroids like so:
# Create two new Asteroid objects at the current asteroid position with the new radius.
# Set the first's .velocity to the first new vector, but make it move faster by scaling it up (multiplying) by 1.2.
# Do the same for the second asteroid, but with the second new vector.
# In the game loop in main.py, replace asteroid.kill() with asteroid.split().
# Run the game and shoot some asteroids
