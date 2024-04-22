import pygame

# Инициализация Pygame
pygame.init()

# Получение списка доступных шрифтов
fonts = pygame.font.get_fonts()

# Вывод списка шрифтов
for font in fonts:
    print(font)

# Завершаем Pygame
pygame.quit()