import pygame
import sys
import os
pygame.init()

width, height = 1024, 1024
window = pygame.display.set_mode((width, height))
bg_img = pygame.image.load('fon.png')
bg_img = pygame.transform.scale(bg_img, (width, height))


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
# определим его вид
sprite.image = load_image("car.png")
# и размеры
sprite.rect = sprite.image.get_rect()
# добавим спрайт в группу
all_sprites.add(sprite)

sprite.rect.x = 550
sprite.rect.y = 800

if __name__ == '__main__':
    running = True
    all_sprites.draw(bg_img)
    while running:
        window.blit(bg_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    sprite.rect.x -= 10
                    all_sprites.update()
                if event.key == pygame.K_d:
                    sprite.rect.x += 10
                    all_sprites.update()
        all_sprites.update()
        pygame.display.update()
    pygame.display.flip()
    pygame.quit()
