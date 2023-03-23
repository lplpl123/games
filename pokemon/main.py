import pygame
import sys


# 初始化
pygame.init()
# 设置主屏窗口
screen = pygame.display.set_mode((240, 160))
pygame.display.set_caption('pokemon')
# 加载地图
map = pygame.image.load('./data/graphic/maps/map01.png')
# 加载人物
character_image = pygame.image.load('./data/graphic/characters/character01.png')
# todo 要把哪些是需要加载的，统一先加载在一个list数据库里面
# 控制fps
clock = pygame.time.Clock()
# run
while True:
    site = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            site[1] -= 1
        if event.type == pygame.K_DOWN:
            site[1] += 1
        if event.type == pygame.K_LEFT:
            site[0] -= 1
        if event.type == pygame.K_RIGHT:
            site[0] += 1
    # 控制为30fps
    clock.tick(30)
    # 绘制背景图片
    screen.blit(map, (0, 0)) # todo
    # 绘制人物
    screen.blit(character_image, (50, 50), (5, 5, 20, 25))
    pygame.display.flip()
