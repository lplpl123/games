import pygame
import sys
import tools


def pokemon_init():
    # 初始化
    pygame.init()
    pygame.display.set_caption('pokemon')

pokemon_init()
screen = pygame.display.set_mode((240, 160))
# 加载地图
map = pygame.image.load('./data/graphic/maps/map01.png')
# 加载人物
character_image = pygame.image.load('./data/graphic/characters/character01.png')
image = tools.get_image(character_image)
character_rect = image.get_rect()
# 小智的初始位置
character_rect.x = 100
character_rect.y = 80
# todo 要把哪些是需要加载的，统一先加载在一个list数据库里面
# 控制fps
clock = pygame.time.Clock()
# run
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                character_rect.y -= 10
            if event.key == pygame.K_DOWN:
                character_rect.y += 10
            if event.key == pygame.K_LEFT:
                character_rect.x -= 10
            if event.key == pygame.K_RIGHT:
                character_rect.x += 10
    # 控制为30fps
    clock.tick(30)
    # 绘制背景图片
    screen.blit(map, (0, 0)) # todo
    # 在世界地图上绘制人物
    screen.blit(image, character_rect)
    pygame.display.flip()
