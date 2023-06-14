from game.components.enemies.enemy import Enemy
from game.components.enemies.phantom_ship import EnemyPhantom
from game.components.enemies.tick import EnemyTick

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)
        
    def add_enemy(self):
        if len(self.enemies) < 10:
            enemy = Enemy()
            phantom = EnemyPhantom()
            tick = EnemyTick()
            self.enemies.append(enemy)
            self.enemies.append(phantom) 
            self.enemies.append(tick)           
            
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
