import pygame


# ��������������ǰ�ͼƬ�Ͱװ�ճ��һ��
def get_image(load_image):
    image = pygame.Surface((20, 25))  # ����������Ļ���
    # �ڻ����������
    image.blit(load_image, (0, 0), (5, 5, 20, 25))
    image.set_colorkey((0, 80, 159))
    return image