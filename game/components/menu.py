import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    
    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        
    def handle_event_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            if event.type == pygame.KEYDOWN:
                game.run()
    
    def update(self, game):
        pygame.display.update()
        self.handle_event_on_menu(game)
    
    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        
    def update_message(self, message, screen):
        lines = message.split("\n")
        for i,line in enumerate(lines):
            
            text = self.font.render(line, True,(0,0,0))
            text_rect = self.text.get_rect()
            text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + (i * 40))
            screen.blit(text, text_rect)
        
    def reset_screen_collor(self, screen):
        screen.fill((255, 255, 255))