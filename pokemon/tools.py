import pygame


# 这个函数的作用是把图片和白板粘在一处
def get_image(load_image):
    image = pygame.Surface((20, 25))  # 用来画人物的画板
    # 在画板绘制人物
    image.blit(load_image, (0, 0), (5, 5, 20, 25))
    image.set_colorkey((0, 80, 159))
    return image