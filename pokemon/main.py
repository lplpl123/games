import pygame


# 初始化
pygame.init()
# 设置主屏窗口
screen = pygame.display.set_mode((240, 160))
# 设置窗口标题
pygame.display.set_caption('pokemon')
# 设置背景
# bg = pygame.image.load("./maps/map01.png") # todo

clock = pygame.time.Clock()
# run
while True:
    # 控制为30fps
    clock.tick(30)
    # 绘制背景图片
    # screen.blit(bg, (0, 0)) # todo
    pygame.display.flip()
