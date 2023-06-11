import pygame
import sys
import random
import time
import math
from enum import Enum


class Scene(Enum):
    MAIN_MENU = 0
    GAME = 1
    GAME_OVER = 2

    def draw(self):
        pass


class Game():
    def __init__(self):
        pass

    def draw(self):
        pass


class GameOver():
    def __init__(self):
        pass

    def draw(self):
        pass


class StateManager:
    def __init__(self, screen):
        self.screen = screen
        self.main_menu = MainMenu()
        self.game = Game()
        self.game_over = GameOver()
        self.current_scene = Scene.MAIN_MENU
        # images...
        # sounds...

    def set_scene(self, scene):
        self.current_scene = scene

    def get_event(self, event: pygame.event):
        pass

    def draw(self):
        if self.current_scene == Scene.MAIN_MENU:
            self.main_menu.draw()
        elif self.current_scene == Scene.GAME:
            self.game.draw()
        elif self.current_scene == Scene.GAME_OVER:
            self.game_over.draw()

    pass


class Tank:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.size = 32
        self.x = x
        self.y = y
        self.angle = 0
        self.image = image_filename

    def draw(self):
        rotated = pygame.transform.rotate(self.image, 90 - self.angle)
        centered_rect = rotated.get_rect(center=(self.x - self.size // 2, self.y - self.size // 2))
        self.screen.blit(rotated, centered_rect)

    def rotate_by(self, amount: int):
        self.angle += amount

    def move(self, amount: int):
        x = math.cos(math.radians(self.angle))
        y = math.sin(math.radians(self.angle))
        self.x += x * amount
        self.y += y * amount


class Turret:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.size = 32
        self.x = x
        self.y = y
        self.angle = 0
        self.image = image_filename

    def draw(self):
        rotated = pygame.transform.rotate(self.image, -90 - self.angle)
        centered_rect = rotated.get_rect(center=(self.x - self.size // 2, self.y - self.size // 2))
        self.screen.blit(rotated, centered_rect)

    def rotate_by(self, amount: int):
        self.angle += amount

    def move(self, amount: int):
        x = math.cos(math.radians(self.angle))
        y = math.sin(math.radians(self.angle))
        self.x += x * amount
        self.y += y * amount


class Fire:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.size = 32
        self.x = x
        self.y = y
        self.angle = 0
        self.image = image_filename

    def draw(self):
        rotated = pygame.transform.rotate(self.image, self.angle)
        centered_rect = rotated.get_rect(center=(self.x - self.size // 2, self.y - self.size // 2))
        self.screen.blit(rotated, centered_rect)

    def rotate_by(self, amount: int):
        self.angle += amount

    def move(self, amount: int):
        x = math.cos(math.radians(self.angle))
        y = math.sin(math.radians(self.angle))
        self.x += x * amount
        self.y += y * amount


def main():
    pygame.init()

    pygame.display.set_caption("Tank Tower Defense")
    screen = pygame.display.set_mode((640, 480))

    clock = pygame.time.Clock()
    tank_turret = pygame.image.load("Tank_Turret.png")
    tank_base = pygame.image.load("Tank_Base.png")
    fire_bullet = pygame.image.load("Fire.png")
    tank = Tank(screen, (screen.get_width() // 2), (screen.get_height() // 2), tank_base)
    turret = Turret(screen, (screen.get_width() // 2), (screen.get_height() // 2), tank_turret)
    fire = Fire(screen, (screen.get_width() // 2), (screen.get_height() // 2), fire_bullet)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

        clock.tick(60)
        screen.fill((255, 255, 255))
        tank.draw()
        turret.draw()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            tank.rotate_by(2)
            turret.rotate_by(2)
        if pressed_keys[pygame.K_LEFT]:
            tank.rotate_by(-2)
            turret.rotate_by(-2)
        if pressed_keys[pygame.K_UP]:
            tank.move(1)
            turret.move(1)

        if pressed_keys[pygame.K_a]:
            turret.rotate_by(-2)
        if pressed_keys[pygame.K_d]:
            turret.rotate_by(2)

        if pressed_keys[pygame.K_SPACE]:
            fire.angle = turret.angle.__invert__() - 90

        turret.x = tank.x
        turret.y = tank.y



main()
