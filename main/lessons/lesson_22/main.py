# Занятие 22 - Pygame
import pygame
import random
import sys


def main():
    # включение модуля pygame
    pygame.init()

    WIDTH, HEIGHT = 640, 400
    BG_COLOR = (0, 0, 0)
    score = 0

    # surface - поверхность
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("-= T I R =-")
    clock = pygame.time.Clock()  # Frame Per Second
    pygame.mouse.set_visible(False)

    # RGB (Red, Green, Blue)
    red = random.randrange(1, 255)
    green = random.randrange(1, 255)
    blue = random.randrange(1, 255)
    line_color = red, green, blue
    x_scope_pos = 0
    y_scope_pos = 0
    scope_size = 20

    # Обезьяна
    target_img = pygame.image.load("DK.bmp")
    target_rect = target_img.get_rect()
    target_rect.x = random.randint(0, WIDTH - 48)
    target_rect.y = random.randint(0, HEIGHT - 32)

    # Объект звука выстрела
    shoot_sound = pygame.mixer.Sound("weapons/awp.wav")
    shoot_sound.set_volume(0.05)

    # Музыка
    pygame.mixer.music.load('music/Highway_to_Hell.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    # Текст очков
    score_obj = pygame.font.Font('scootchover-sans.ttf', 24)

    while True:
        # закрываем окно
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                x_scope_pos, y_scope_pos = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    shot = pygame.Rect(x_scope_pos, y_scope_pos, 1, 1)
                    if shot.colliderect(target_rect):
                        score += 10
                        target_rect.x = random.randint(0, WIDTH - 48)
                        target_rect.y = random.randint(0, HEIGHT - 32)
                    shoot_sound.play()

        surface.fill(BG_COLOR)

        surface.blit(target_img, target_rect)

        # рисуем прицел
        # pygame.draw.line(surface, linecolor, (x_scope_pos - scope_size, y_scope_pos), (x_scope_pos + scope_size, y_scope_pos))  # Рисуем горизонтальную линию
        # pygame.draw.line(surface, linecolor, (x_scope_pos, y_scope_pos - scope_size), (x_scope_pos, y_scope_pos + scope_size))  # Рисуем вертикальную линию
        pygame.draw.line(
            surface, line_color, (x_scope_pos - scope_size, y_scope_pos), (x_scope_pos + scope_size, y_scope_pos)
        )  # горизонтальная линия
        pygame.draw.line(
            surface, line_color, (x_scope_pos, y_scope_pos - scope_size), (x_scope_pos, y_scope_pos + scope_size)
        )  # вертикальная линия

        score_text = score_obj.render(f'Score: {score}', True, (160, 200, 50))
        surface.blit(score_text, (0, 0))

        pygame.display.update()  # Обновляет все положения всех игровых объектов на экране
        clock.tick(60)  # FPS 60


if __name__ == "__main__":
    main()
