import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

AMMO = pygame.image.load(os.path.join(IMG_DIR, 'Other/Gun.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))


DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
AMMO_TYPE = 'ammo'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
SPACESHIP_AMMO = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/space_ammo.png")) 
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_player.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
PHANTOM = pygame.image.load(os.path.join(IMG_DIR, "Enemy/phantom.png"))
TICK = pygame.image.load(os.path.join(IMG_DIR, "Enemy/tick.png"))

FONT_STYLE = 'freesansbold.ttf'

#Musica 
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(IMG_DIR, "Sonido/intro.ogg"))
pygame.mixer.music.play(-1)

