import pygame
import os


class Music:
    IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
    
    def update(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(IMG_DIR, "Sonido/intro.ogg"))
        pygame.mixer.music.play(1)