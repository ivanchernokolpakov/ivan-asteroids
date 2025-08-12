from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity *dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius > ASTEROID_MIN_RADIUS:
             rand_angle = random.uniform(20,50)
             split_a_ang = self.velocity.rotate(rand_angle)
             split_b_ang = self.velocity.rotate(-rand_angle)
             new_radius = self.radius - ASTEROID_MIN_RADIUS
             split_a = Asteroid(self.position.x, self.position.y, new_radius)
             split_b = Asteroid(self.position.x, self.position.y, new_radius)
             split_a.velocity = split_a_ang *1.2
             split_b.velocity = split_b_ang *1.2
