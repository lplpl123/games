import pygame
import tools


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_images()

    def run(self):
        pass

    def load_images(self):
        # 加载人物
        self.character_image = pygame.image.load('./data/graphic/characters/character01.png')
        self.image = tools.get_image(self.character_image)
        self.character_rect = self.image.get_rect()
        # 小智的初始位置
        self.character_rect.x = 100
        self.character_rect.y = 80

    def update(self, direction):
        if direction == pygame.K_UP and self.character_rect.y > 0:  # todo 但是这里做的还不够好，因为人物距离屏幕边缘可能有一点距离
            self.character_rect.y -= 10
        # if direction == pygame.K_DOWN and self.character_rect.y < 130:  # 屏幕高减人物高
        #     self.character_rect.y += 10
        # if direction == pygame.K_LEFT and self.character_rect.x > 0:
        #     self.character_rect.x -= 10
        if direction == pygame.K_RIGHT and self.character_rect.x < 220:
            self.character_rect.x += 10

    def draw_on_map(self, screen):
        # 在世界地图上绘制人物
        screen.blit(self.image, self.character_rect)
