# DodgeGame.py
# A simple game using pygame
import pygame
from Player import Player
from Enemy import Enemy

pygame.init()

# Set up the general game
game = pygame.display.set_mode((1000,500))
pygame.display.set_caption("DodgeGame")
Icon = pygame.image.load("Icon.png")
pygame.display.set_icon(Icon)
background = (0, 128, 0)
running = True

# set up the player character
player = Player()
character = pygame.image.load("Stationary.png")
moving = pygame.image.load("Moving.png")

# set up the enemy
enemy = Enemy()
vel = 0.1

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game.fill(background)
    
    # aside from the background, the bulk of the game happens
    # only while the player character is alive
    if player.lives > 0:

        # Handling player character behavior before showing it
        key = pygame.key.get_pressed()
        player.moveVertical(key)
        player.moveHorizontal(game, character, moving, key)

        # This is checking if the enemy has reached the end
        # If it has, it will be deleted 
        if enemy.x_pos > 0:
            enemy.x_pos -= vel
            pygame.draw.circle(game, (255,0,0),[enemy.x_pos,enemy.y_pos], enemy.radius, 0)
        else:
            enemy.x_pos = 950
            vel += 0.02

        # After the ball has moved, we'll check
        # collision between player and object
        if player.collision(enemy) == True:
            enemy.x_pos = 950
            player.lives -= 1

        if player.lives == 0:
            character = pygame.transform.rotate(character, 90)
    # If the player has 0 lives, nothing else needs to happen
    # It just displays a dead character
    else:
        game.blit(character, (player.x_pos, 450))

    pygame.display.update()