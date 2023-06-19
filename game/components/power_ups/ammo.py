import pygame

from game.components.power_ups.power_up import PowerUp
from game.utils.constants import AMMO, AMMO_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

class Ammo(PowerUp):
    def __init__(self):
        super().__init__(AMMO, AMMO_TYPE)