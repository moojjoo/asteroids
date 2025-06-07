import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # If the asteroid is too small, it cannot be split
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        # Randomly choose an angle to  the velocity vector
        else:        
            random_angle = random.uniform(20, 50)
            # Create two new velocity vectors, rotated in opposite directions
            velocity1 = self.velocity.rotate(random_angle) * 1.2
            velocity2 = self.velocity.rotate(-random_angle) * 1.2

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create two new asteroids at the current position with the new radius
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1
            asteroid2.velocity = velocity2
            self.kill()  # Remove the current asteroid
        



        

