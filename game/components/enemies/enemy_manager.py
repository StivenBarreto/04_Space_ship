from game.components.enemies.enemy import Enemy
from game.components.enemies.phantom_ship import EnemyPhantom
from game.components.enemies.tick import EnemyTick
import random

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
        
    def add_enemy(self):
        enemy_type = random.randint(1,2)
        if enemy_type == 1:
            tick = EnemyTick()
            phantom = EnemyPhantom()
            enemy = Enemy()
        else: 
            x_speed = 5
            y_speed = 2
            move_x_for = [50, 120]
            enemy = Enemy()
            tick = EnemyTick()
            phantom = EnemyPhantom()
            
        if len(self.enemies) < 2:
            self.enemies.append(enemy)
            self.enemies.append(phantom) 
            self.enemies.append(tick)           
            
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
     
    def reset(self):
         self.enemies = []       
