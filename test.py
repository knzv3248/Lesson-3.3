import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра "Тир"')
icon = pygame.image.load("image/targetSmall.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("image/TargetApple.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
if max(background_color) > 255/2:
    text_color = (0, 0, 0)
else:
    text_color = (255, 255, 255)

running = True
n_shooting = 0
n_target = 0
text_shooting = "Число выстрелов: 0"
text_hit = "Число попаданий: 0"
font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 14)

while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            n_shooting += 1
            text_shooting = "Число выстрелов: " + str(n_shooting)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                n_target += 1
                text_hit = "Число попаданий: " + str(n_target)
                print(text_hit)
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Обновляем текст
    out_text = text_shooting + "  " + text_hit
    text_surface = font.render(out_text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (10, 10)
    screen.blit(text_surface, text_rect)

    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()