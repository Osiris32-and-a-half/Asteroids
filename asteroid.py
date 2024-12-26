import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
    def draw(self, screen):
        pygame.draw.circle(screen,
                           pygame.Color("white"),
                           self.position,
                           self.radius,
                           2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_left = Asteroid(self.position.x, self.position.y, new_radius)
        new_right = Asteroid(self.position.x, self.position.y, new_radius)
        
        new_left.velocity = self.velocity.rotate(-angle) * 1.2
        new_right.velocity = self.velocity.rotate(angle) * 1.2