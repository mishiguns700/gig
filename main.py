import pygame
import sys
import random
import os
pygame.init()

cars = ["cop1.png", "car3.png", "car4.png", "car5.png", "car6.png"]
cars_r = ["cop1_r.png", "car.png", "car4_r.png", "car5_r.png", "car6_r.png"]

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


class Background(pygame.sprite.Sprite):
    def __init__(self, number, *args):
        self.image = load_image('fon.png').convert()
        self.rect = self.image.get_rect()
        self._layer = -10
        pygame.sprite.Sprite.__init__(self, *args)
        self.moved = 0
        self.number = number
        self.rect.y = -self.rect.height * self.number

    def update(self):
        self.rect.move_ip(0, 1)
        self.moved += -1

        if self.moved <= -self.rect.height:
            self.rect.y = -self.rect.height * self.number
            self.moved = 0


# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
all_sprites2_r = pygame.sprite.Group()
# создадим спрайт
sprite = pygame.sprite.Sprite()
Cars = pygame.sprite.Sprite()
Cars_r = pygame.sprite.Sprite()
# определим его вид
sprite.image = load_image("car.png")
a = random.choice(cars)
Cars.image = load_image(a)
a_r = random.choice(cars_r)
Cars_r.image = load_image(a_r)
# и размеры
Cars.rect = Cars.image.get_rect()
sprite.rect = sprite.image.get_rect()
Cars_r.rect = Cars_r.image.get_rect()
# добавим спрайт в группу
all_sprites2.add(Cars)
all_sprites.add(sprite)
all_sprites2_r.add(Cars_r)

r = random.choice([0, 1])
rr = random.choice([0, 1])

Cars.image = load_image(a)
if r == 1:
    Cars.rect.x = 330
    Cars.rect.y = -560
else:
    Cars.rect.x = 120
    Cars.rect.y = -560

Cars_r.image = load_image(a_r)
if rr == 1:
    Cars_r.rect.x = 550
    Cars_r.rect.y = -560
else:
    Cars_r.rect.x = 800
    Cars_r.rect.y = -560

sprite.rect.x = 550
sprite.rect.y = 720

right = False
left = False
group = pygame.sprite.LayeredUpdates()
Background(0, group)
Background(1, group)
clock = pygame.time.Clock()
counter, text = 0, '0'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
if __name__ == '__main__':
    running = True
    while running:
        group.draw(window)
        window.fill((0, 0, 0))
        group.update()
        group.draw(window)
        all_sprites.draw(window)
        all_sprites2.draw(window)
        all_sprites2_r.draw(window)
        window.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        r = random.choice([0, 1])
        rr = random.choice([0, 1])
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                counter += 1
                text = str(counter).rjust(3)
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
        hits_r = pygame.sprite.spritecollide(sprite, all_sprites2_r, False)
        if hits_r:
            pygame.quit()
        hits = pygame.sprite.spritecollide(sprite, all_sprites2, False)
        if hits:
            pygame.quit()

        if Cars_r.rect.y != 1024:
            Cars_r.rect.y += 2
        if Cars_r.rect.y == 1024:
            Cars_r.rect = Cars.image.get_rect()
            a_r = random.choice(cars_r)
            Cars_r.image = load_image(a_r)
            if rr == 1:
                Cars_r.rect.x = 550
                Cars_r.rect.y = -560
            else:
                Cars_r.rect.x = 800
                Cars_r.rect.y = -560

        if Cars.rect.y != 1024:
            Cars.rect.y += 3
        if Cars.rect.y == 1024:
            Cars.rect = Cars.image.get_rect()
            a = random.choice(cars)
            Cars.image = load_image(a)
            if r == 1:
                Cars.rect.x = 330
                Cars.rect.y = -560
            else:
                Cars.rect.x = 120
                Cars.rect.y = -560
            all_sprites2.draw(window)
        if sprite.rect.x == 850:
            right = False
        if sprite.rect.x == 70:
            left = False
        if right is True:
            sprite.rect.x += 3
            all_sprites.update()
        if left is True:
            sprite.rect.x -= 3
            all_sprites.update()
        all_sprites.update()
        pygame.display.update()
    pygame.display.flip()
    clock.tick(120)
    pygame.quit()
