import math
import random
import pygame

#Consists
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Background
background = pygame.image.load('background.png')

#Caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png')

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY =   PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64)) # 64 is the size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf' , 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesaasbold.ttf' , 64)

def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("score :" + str(score_value), True, (57, 126, 237))
    screen.blit(score, (x, y))

def game_over_text():
    # Display the hame over text
    over_text = over_font.render("GAME OVER", True, (57, 126, 237))
    screen.blit(over_text, (200, 250))

def player(x, y):
    # Draw an enemy on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))

    