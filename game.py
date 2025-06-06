import os
import pygame
from models import GameObject
#set the screen surfuce

from utils import load_sprite

class SpaceRocks:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self._init_pygame()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT)) #screen is made
        self.background = load_sprite("space", False)
        self.spaceship = GameObject(
            (400, 300), load_sprite("spaceship"), (0, 0)
        )
        self.asteroid = GameObject(
            (400, 300), load_sprite("asteroid"), (1, 0)
        )


    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Rock shooter")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()


    def _process_game_logic(self):
        self.spaceship.move()
        self.asteroid.move()


    def _draw(self):
        self.screen.blit(self.background, (0,0))
        #self.screen.fill((0, 0, 255))
        self.spaceship.draw(self.screen)
        self.asteroid.draw(self.screen)        
        pygame.display.flip()



##################################################################################################

#set working directory 
os.chdir(os.path.dirname(os.path.realpath(__file__)))

space_rocks = SpaceRocks()
space_rocks.main_loop()

