# -*- coding:utf-8 -*-
import pygame
import sys
import random
import os

class Snake():
    def __init__(self):
        pygame.init()
        self.x_min = 0
        self.x_max = 1000
        self.y_min = 0
        self.y_max = 500
        self.offset = 20
        self.radius = 10

        self.background_color = [255, 255, 255]
        self.background_music = 'bgm.mp3'
        self.default_color = [0, 0, 0]
        pygame.display.set_caption('Greedy snake')
        self.screen = pygame.display.set_mode([self.x_max, self.y_max])
        self.screen.fill(self.background_color)

        self.directions = {pygame.K_UP : [0, -20], pygame.K_DOWN : [0, 20], pygame.K_LEFT : [-20, 0], pygame.K_RIGHT : [20, 0]}
        self.direction = self.directions[pygame.K_DOWN]
        self.snake = [[50, 10], [30, 10], [10, 10]]
        self.tail = self.snake[-1]
        self.food_number = 0
        self.score = 0
        self.food_position = None

    def food(self):
        if self.food_number == 0:
            self.food_number = 1
            self.food_position = [10 + random.randint(self.x_min, self.x_max / self.offset) * self.offset, 10 + random.randint(self.y_min, self.y_max / self.offset) * self.offset]
            color = [random.randint(1, 255) for i in range(0, 3)]
            pygame.draw.circle(self.screen, color, self.food_position, self.radius, self.radius)

    def move(self):
        for node in self.snake:
            pygame.draw.circle(self.screen, self.default_color, node, self.radius, self.radius)
        pygame.display.flip()

        self.tail = self.snake[-1]
        pygame.draw.circle(self.screen, self.background_color, self.tail, self.radius, self.radius)

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = self.snake[i - 1][:]
        self.snake[0][0] = (self.snake[0][0] + self.direction[0]) % self.x_max
        self.snake[0][1] = (self.snake[0][1] + self.direction[1]) % self.y_max
        self.eat_food()

    def turn(self, key):
        self.direction = self.directions[key]

    def display_score(self):
        pygame.draw.rect(self.screen, [110, 110, 110], [self.x_max - 100, 0, 100, 40], 0)
        font_color = self.default_color
        text = pygame.font.Font(None, 25).render('Score %d' % self.score, True, font_color)
        rect = text.get_rect()
        rect.topleft = (self.x_max - 100, 10)
        self.screen.blit(text, rect)

    def eat_food(self):
        if self.snake[0][0] == self.food_position[0] and self.snake[0][1] == self.food_position[1]:
            self.food_number = 0
            self.score += 1
            self.snake.append(self.tail)

    def draw_lines(self):
        for x in range(0, self.x_max, self.offset):
            pygame.draw.line(self.screen, [0, 255, 0], (x, 0), (x, self.y_max))
        for y in range(0, self.y_max, self.offset):
            pygame.draw.line(self.screen, [0, 255, 0], (0, y), (self.x_max, y))

    def play_background_music(self):
        if os.path.exists(self.background_music):
            pygame.mixer.music.load(self.background_music)
            pygame.mixer.music.play(0)

    def game(self):
        self.play_background_music()
        while True:
            self.draw_lines()
            self.display_score()
            self.food()
            self.move()
            pygame.time.Clock().tick(3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in self.directions.keys():
                        self.turn(event.key)

            pygame.display.flip()

if __name__ == "__main__":
    snake = Snake()
    snake.game()
