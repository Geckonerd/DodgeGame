import pygame
import math

class Player:
    def __init__(self):
        self.height = 110
        self.width = 50
        self.x_pos = 200
        self.y_pos = 390
        self.lives = 3
        # These three values are used in
        # regards to the ability to jump
        self.isJumping = False
        self.gravity = 0.001
        self.vel = 0.0

    # As jumping has some different behaviors compared to horizontal
    # movement, we'll calculate the Y position before doing the rest
    def moveVertical(self, key):
        if self.isJumping == False:
            if key[pygame.K_UP]:
                self.vel = 0.55
                self.isJumping = True

        else:
            self.y_pos -= self.vel
            self.vel -= self.gravity
            if self.y_pos + self.height >= 500:
                self.isJumping = False
                self.vel = 0

    
    # After getting the verical aspect of the character's position,
    # we'll apply any remaining horizontal changes then draw the character
    def moveHorizontal(self, game, character, moving, key):

        if key[pygame.K_LEFT] and self.x_pos>0:
            self.x_pos -= .2
            game.blit(pygame.transform.flip((moving), True, False), (self.x_pos, self.y_pos))
        elif key[pygame.K_RIGHT] and self.x_pos + self.width < 1000:
            self.x_pos += .2
            game.blit(moving, (self.x_pos, self.y_pos))
        else:
            game.blit(character, (self.x_pos, self.y_pos))

    # Check if the enemy and player have collided
    def collision(self, enemy):
        testX = 0
        testY = 0

        if enemy.x_pos < self.x_pos:
            testX = self.x_pos
        else:
            testX = self.x_pos + self.width
        
        if enemy.y_pos < self.y_pos:
            testY = self.y_pos
        else:
            testY = self.x_pos + self.height

        distX = enemy.x_pos - testX
        distY = enemy.y_pos - testY
        dist = math.sqrt((distX*distX) + (distY*distY))

        if (dist <= enemy.radius):
            return True
        return False