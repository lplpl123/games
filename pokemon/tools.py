import pygame
import sys
from source.components.player import Player
from states.world01 import World01


class Game:
    def __init__(self):
        # todo 要把哪些是需要加载的，统一先加载在一个list数据库里面
        self.world01 = World01()
        self.player = Player()
        # 控制fps
        self.clock = pygame.time.Clock()

        pygame.init()
        self.screen = pygame.display.set_mode((240, 160))
        pygame.display.set_caption('pokemon')

        self.game_window = self.screen.get_rect()
        self.game_map_all = pygame.Surface((self.world01.map_rect.width, self.world01.map_rect.height))

    def run(self):
        # run
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        second = self.game_window.x + self.game_window.width / 2
                        if self.player.character_rect.centerx > second:
                            self.game_window.x += 10
                    self.player.update(event.key)
            # 控制为30fps
            self.clock.tick(30)
            # 绘制背景图片
            self.game_map_all.blit(self.world01.map, self.game_window, self.game_window)  # todo
            self.player.draw_on_map(self.game_map_all)
            self.screen.blit(self.game_map_all, (0, 0), self.game_window)
            pygame.display.flip()

# 这个函数的作用是把图片和白板粘在一处
def get_image(load_image):
    image = pygame.Surface((20, 25))  # 用来画人物的画板
    # 在画板绘制人物
    image.blit(load_image, (0, 0), (5, 5, 20, 25))
    image.set_colorkey((0, 80, 159))
    return image