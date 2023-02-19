import pygame
import sys
import os
pygame.init()

width, height = 1024, 1024
window = pygame.display.set_mode((width, height))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()

# создадим спрайт
sprite = pygame.sprite.Sprite()
bg_img = pygame.sprite.Sprite()
# определим его вид
sprite.image = load_image("car.png")
bg_img.image = load_image("fon.png")
# и размеры
bg_img.rect = bg_img.image.get_rect()
sprite.rect = sprite.image.get_rect()
# добавим спрайт в группу
all_sprites.add(bg_img)
all_sprites.add(sprite)

sprite.rect.x = 550
sprite.rect.y = 580

right = False
left = False

if __name__ == '__main__':
    running = True
    while running:
        all_sprites.draw(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_LEFT:
                    left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_LEFT:
                    left = False
        if sprite.rect.x == 780:
            right = False
        if sprite.rect.x == -20:
            left = False
        if right is True:
            sprite.rect.x += 10
            all_sprites.update()
        if left is True:
            sprite.rect.x -= 10
            all_sprites.update()
        all_sprites.update()
        pygame.display.update()
    pygame.display.flip()
    pygame.quit()
