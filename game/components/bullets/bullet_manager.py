import pygame 
from game.utils.constants import SHIELD_TYPE

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    pygame.time.delay(1000)
                    game.death_count.update()
                    
                break
         
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    self.bullets.remove(bullet) 
                    game.enemy_manager.enemies.remove(enemy)
                    game.score.update()   
                    break
            
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
            
        for bullet in self.bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 2:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == "player" and len(self.bullets) < 5:
            self.bullets.append(bullet)
            
    def reset(self):
        self.bullets = []
        self.enemy_bullets = []