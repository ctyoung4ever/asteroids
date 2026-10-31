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


    def update(self, dt):
        self.position += self.velocity * dt
