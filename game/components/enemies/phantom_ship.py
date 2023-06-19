import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import PHANTOM, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

class EnemyPhantom(Sprite):
    Y_POS = 30
    X_POS_LIST =[50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    SPEED_X = 5
    SPEED_Y = 0
    MOD_X = {0: 'left', 1:'right'}
    
    def __init__(self):
        self.image = PHANTOM
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]
        self.rect.y = self.Y_POS
        self.type = 'enemy'
        
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOD_X[random.randint(0,1)]
        self.move_x_for = random.randint(50,110)
        self.index = 0 
        self.shooting_time = random.randint(40,60)
        self.shooting_time= pygame.time.get_ticks()+500
        self.shoot_num = 0
        
    
    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH -40):
            self.movement_x = 'left'
        elif(self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            
        if self.index >= self.move_x_for:
            self.index = 0
            
    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager, game)
        
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
    
    def shoot(self, bullet_manager, game):
        current_time = pygame.time.get_ticks()
        round_time = round((self.shooting_time - pygame.time.get_ticks())/1000)
        
        if round_time <= 0:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet, game)
            self.shoot_num += 1
            self.shooting_time = pygame.time.get_ticks()+2000
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))