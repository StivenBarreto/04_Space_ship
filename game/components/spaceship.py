import pygame
import os
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_TYPE
from game.components.bullets.bullet import Bullet


class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect() 
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.has_power_up = False
        self.power_time_up = 0
        self.power_up_type = DEFAULT_TYPE
        
    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager, game)
      
    def shoot(self, bullet_manager, game):    
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet, game)
        
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x = self.rect.x - 10
        else:
            self.rect.x = SCREEN_WIDTH
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x = self.rect.x + 10
        else:
            self.rect.x = 0
    
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y = self.rect.y - 10
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y = self.rect.y + 10
            
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))  
        
    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
            
    def set_image(self, size=(40,60),image=SPACESHIP):
          self.image = image
          self.image = pygame.transform.scale(self.image, size)