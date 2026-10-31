# ssignment
from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame

# Create a new class called Asteroid in a new file called asteroid.py that inherits from CircleShape.
class Asteroid(CircleShape):

# Give it a constructor with this signature, and inside it call the parent CircleShape constructor so the sprite is initialized correctly:
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    # override the draw method (polymorphism) to draw the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

# Override the update() method so that it moves in a straight line at constant speed. On each frame, it should add (self.velocity * dt) to its position 
# (get self.velocity from its parent class, CircleShape).
    def update(self, dt):
        self.position += self.velocity * dt
# In main.py before the game loop starts, create a new empty pygame.sprite.Group for the asteroids.

# Like we did with the Player class, set the static containers field of the Asteroid class to the new asteroids group, as well as the updatable and drawable groups. This ensures that every instance of the Asteroid class is automatically added to these groups upon creation.

# Asteroid.containers = (asteroids, updatable, drawable)