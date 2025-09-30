import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
# from asteroidfield import AsteroidField

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt): 
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            randomAngle = random.uniform(20, 50)
            firstvector = self.velocity.rotate(randomAngle)
            secondvector = self.velocity.rotate(-1 * randomAngle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            asteroidOne = Asteroid(self.position.x, self.position.y, newRadius)
            asteroidTwo = Asteroid(self.position.x, self.position.y, newRadius)
            asteroidOne.velocity += firstvector * 1.2
            asteroidTwo.velocity += secondvector * 1.2

    