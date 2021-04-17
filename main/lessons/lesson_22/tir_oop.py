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

        # Добавил поля для ширины и высоты экрана, т.к. они дальше понадобятся для использования в других классах.
        # (для отрисовки прицела, цели)
        self.width = width
        self.height = height

        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.player = []
        self.targets = []
        self.hud_obj = []
        self.game_objects = []
        self.mouse_handlers = defaultdict(list)  # dct = {"нажали на мышку": [obj1, obj2],
        # "передвинули мышку": [handle_mouse, obj2]} - вместо obj будут функции-обработчики событий

    # функция, запускающая игру
    def start_game(self):
        pygame.mixer.music.load("music/Highway_to_Hell.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        while True:
            self.handle_events()

            self.game_objects = [*self.targets, *self.hud_obj, *self.player]

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

            # if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            #     for handler in self.mouse_handlers[event.type]:
            #         handler(event.type, event.pos)

            # Я разделил обработку событий мыши на два ветвления, так как мне необходимо было получить
            # номер кнопки, чтоб выстрел происходил ТОЛЬКО при нажатии левой кнопки мыши. А у событий
            # MOUSEMOTION и MOUSEBUTTONDOWN разные аттрибуты.
            if event.type == pygame.MOUSEMOTION:
                for handler in self.mouse_handlers[event.type]:
                    handler(event.type, event.pos)

            # мой вариант
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     for handler in self.mouse_handlers[event.type]:
            #         handler(event.type, event.pos, event.button)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for handler in self.mouse_handlers[event.type]:
                    handler(event.type, event.pos)


class Tir(Game):
    def __init__(self):
        super().__init__("TIR", 640, 400, (0, 0, 0), 60)
        self.score = 0
        self.scope = None
        self.target = None
        self.create_objects()

    def create_objects(self):
        self.create_scope()
        self.create_target()
        self.create_label()

    def create_scope(self):
        scope = Scope()

        self.mouse_handlers[pygame.MOUSEMOTION].append(scope.handle_mouse)
        self.mouse_handlers[pygame.MOUSEBUTTONDOWN].append(scope.handle_mouse)

        self.scope = scope
        self.player.append(self.scope)

    def create_target(self):
        target = Target(self.window_width, self.window_height, "DK.bmp")
        self.target = target
        # target с помощью list.insert помещаем перед объектом scope, чтоб прицел отрисовывался сверху обезьянки
        # self.game_objects.insert(0, self.target)
        self.targets.append(self.target)

    def create_label(self):
        text_obj = TextObject(
            0,
            0,
            lambda: f'Score: {self.score}',
            (175, 185, 195),
            'scootchover-sans.ttf',
            24
        )
        self.hud_obj.append(text_obj)

    def handle_shots(self):
        for target in self.targets:
            if self.scope.shot.colliderect(target.target_rect):
                self.score += 10
                # target.change_position()
                target.get_new_coords()

    def update(self):
        self.handle_shots()
        super().update()

    # def create_score(self):
    #     score = Score()
    #     self.score = score

    # Два нижних метода с декоратором @property под вопросом, сдаётся мне, что можно было обойтись без них
    # Двумя этими методами, я хотел "расшарить" ширину и высоту игрового экрана, чтоб они были доступны извне
    @property
    def window_width(self):
        return self.width

    @property
    def window_height(self):
        return self.height


class Scope:
    def __init__(self):
        self.red = random.randrange(1, 255)
        self.green = random.randrange(1, 255)
        self.blue = random.randrange(1, 255)
        self.line_color = self.red, self.green, self.blue
        self.x_scope_pos = 0
        self.y_scope_pos = 0
        self.scope_size = 20
        self.shoot_sound = pygame.mixer.Sound("weapons/awp.wav")
        self.shoot_sound.set_volume(0.05)

        self.shot = pygame.Rect(1000, 1000, 1, 1)

    # Добавил ещё один аргумент event_optional, в MOUSEMOTION - это будет соответствовать event.rel,
    # а в MOUSEBUTTONDOWN - event.button
    # def handle_mouse(self, event_type, event_pos, event_optional):
    def handle_mouse(self, event_type, event_pos):
        if event_type == pygame.MOUSEMOTION:
            self.x_scope_pos, self.y_scope_pos = event_pos

        elif event_type == pygame.MOUSEBUTTONDOWN:
            self.shoot()
            # self.shoot_sound.play()

    def shoot(self):
        self.shoot_sound.play()
        self.shot = pygame.Rect(self.x_scope_pos, self.y_scope_pos, 1, 1)

    def blit(self, surface):
        # горизонтальная линия
        pygame.draw.line(
            surface,
            self.line_color,
            (self.x_scope_pos - self.scope_size, self.y_scope_pos),
            (self.x_scope_pos + self.scope_size, self.y_scope_pos),
        )
        # вертикальная линия
        pygame.draw.line(
            surface,
            self.line_color,
            (self.x_scope_pos, self.y_scope_pos - self.scope_size),
            (self.x_scope_pos, self.y_scope_pos + self.scope_size),
        )

    def update(self):
        pass

    # Этим методом или свойством, я хочу передать координаты прицела во время выстрела.
    # @property
    # def shot(self):
    #     return self.x_scope_pos, self.y_scope_pos


class Target:
    def __init__(self, width, height, image) -> None:
        self.window_width = width
        self.window_height = height

        # self.target_img = pygame.image.load("DK.bmp")
        self.target_img = pygame.image.load(image)
        self.target_rect = self.target_img.get_rect()
        # self.target_rect.x = random.randint(0, self.window_width - 48)
        # self.target_rect.y = random.randint(0, self.window_height - 32)
        self.target_rect.x = random.randint(0, self.window_width - self.target_rect.w)
        self.target_rect.y = random.randint(0, self.window_height - self.target_rect.h)

    def blit(self, surface):
        surface.blit(self.target_img, self.target_rect)

    def update(self):
        # Добавлял, проверял, не понравилось )
        # self.target_rect.x = random.randint(0, 640 - 48)
        # self.target_rect.y = random.randint(0, 400 - 32)
        pass

    # Этим методом я хочу изменить координаты цели, после попадания в неё
    def get_new_coords(self):
        self.target_rect.x = random.randint(0, self.window_width - self.target_rect.w)
        self.target_rect.y = random.randint(0, self.window_height - self.target_rect.h)

    # # Этим свойством я хочу передать "хитбокс" цели
    # @property
    # def get_hitbox(self):
    #     return self.target_rect


# class Score:
#     def __init__(self) -> None:
#         self.score_obj = pygame.font.Font('scootchover-sans.ttf', 24)
#         self.score = 0

#     def blit(self, surface):
#         self.score_text = self.score_obj.render(f'Score: {score}', True, (160, 200, 50))
#         surface.blit(self.score_text, (0, 0))


class TextObject:
    def __init__(self, x, y, text_func, color, font_name, font_size):
        self.x = x
        self.y = y
        self.text_func = text_func
        self.color = color
        self.font = pygame.font.Font(font_name, font_size)
        self.text = self.get_surface(self.text_func())

    def get_surface(self, text):
        text_surface = self.font.render(text, True, self.color)
        return text_surface, text_surface.get_rect()

    def blit(self, surface):
        text_surface, text_rect = self.get_surface(self.text_func())
        surface.blit(text_surface, text_rect)

    def update(self):
        pass


if __name__ == "__main__":
    Tir().start_game()
