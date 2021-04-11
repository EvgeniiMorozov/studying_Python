import pygame
import random
import sys
from collections import defaultdict


class Game:
    def __init__(self, caption, width, height, background, frame_rate):
        pygame.init()
        self.caption = caption
        self.background = background
        self.frame_rate = frame_rate
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(self.caption)
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.game_objects = []
        self.mouse_handlers = defaultdict(list)  # dct = {"нажали на мышку": [obj1, obj2],
                            # "передвинули мышку": [handle_mouse, obj2]} - вместо obj будут функции-обработчики событий

    # функция, запускающая игру
    def start_game(self):
        pygame.mixer.music.load('music/Highway_to_Hell.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        while True:
            self.handle_events()

            self.surface.fill(self.background)
            self.update()
            self.blit(self.surface)

            pygame.display.update()
            self.clock.tick(self.frame_rate)

    # Обновление положения всех игровых объектов
    def update(self):
        for obj in self.game_objects:
            obj.update()

    # Отображение всех игровых объектов
    def blit(self, surface):
        for obj in self.game_objects:
            obj.blit(surface)

    # Обработчик всех игровых событий
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
                for handler in self.mouse_handlers[event.type]:
                    handler(event.type, event.pos)


class Tir(Game):
    def __init__(self):
        super().__init__('TIR', 640, 400, (0, 0, 0), 60)
        self.score = 0
        self.scope = None
        self.create_objects()

    def create_objects(self):
        self.create_scope()

    def create_scope(self):
        scope = Scope()

        self.mouse_handlers[pygame.MOUSEMOTION].append(scope.handle_mouse)

        self.scope = scope
        self.game_objects.append(self.scope)


class Scope:
    def __init__(self):
        self.red = random.randrange(1, 255)
        self.green = random.randrange(1, 255)
        self.blue = random.randrange(1, 255)
        self.line_color = self.red, self.green, self.blue
        self.x_scope_pos = 0
        self.y_scope_pos = 0
        self.scope_size = 20

    def handle_mouse(self, event_type, event_pos):
        if event_type == pygame.MOUSEMOTION:
            self.x_scope_pos, self.y_scope_pos = event_pos

    def blit(self, surface):
        pygame.draw.line(
            surface,
            self.line_color,
            (self.x_scope_pos - self.scope_size, self.y_scope_pos),
            (self.x_scope_pos + self.scope_size, self.y_scope_pos)
        )  # горизонтальная линия
        pygame.draw.line(
            surface,
            self.line_color,
            (self.x_scope_pos, self.y_scope_pos - self.scope_size),
            (self.x_scope_pos, self.y_scope_pos + self.scope_size)
        )  # вертикальная линия

    def update(self):
        pass


if __name__ == '__main__':
    Tir().start_game()
