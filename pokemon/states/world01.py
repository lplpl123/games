import pygame


class World01:
    def __init__(self):
        self.load_map()

    def load_map(self):
        # 加载地图
        self.map = pygame.image.load('./data/graphic/maps/map01.png')
        self.map_rect = self.map.get_rect()
