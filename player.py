import pygame
import constants
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Turn left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Turn right
            self.rotate(dt)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
