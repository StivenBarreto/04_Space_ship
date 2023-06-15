from game.components.enemies.enemy import Enemy
import random
# from game.components.enemies.phantom_ship import EnemyPhantom
# from game.components.enemies.tick import EnemyTick

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
        
    def add_enemy(self):
        if len(self.enemies) < 2:
            enemy = Enemy()
            # phantom = EnemyPhantom()
            # tick = EnemyTick()
            self.enemies.append(enemy)
            # self.enemies.append(phantom) 
            # self.enemies.append(tick)           
            
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
