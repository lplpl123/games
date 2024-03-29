# 工具和游戏主控
import pygame
import random
import os

class Game:
    def __init__(self, state_dict, start_state):
        self.screen = pygame.display.get_surface() # 获取到游戏框架
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed() # 键盘按下的状态的元组
        self.state_dict = state_dict
        self.state = self.state_dict[start_state] # main_menu

    def update(self):
        if self.state.finished:
            game_info = self.state.game_info
            next_state = self.state.next
            self.state.finished = False
            self.state = self.state_dict[next_state]
            self.state.start(game_info)
        self.state.update(self.screen, self.keys)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            self.update()
            pygame.display.update()
            self.clock.tick(60)

def load_graphics(path, accept = ('.jpg', '.png', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic) # 分割了文件名和扩展名
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics

def get_image(sheet, x, y, width, height, colorkey, scale):
    # 创建了一个名叫image的图层
    image = pygame.Surface((width, height))
    # sheet为title_screen
    image.blit(sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
    return image