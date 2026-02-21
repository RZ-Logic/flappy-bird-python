# pipe.py

import pygame
import random
from settings import WIDTH, HEIGHT, PIPE_WIDTH, PIPE_GAP, PIPE_SPEED, GROUND_HEIGHT

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, gap_y, gap_size):
        super().__init__()
        self.x = x
        self.gap_y = gap_y
        self.pipe_speed = PIPE_SPEED
        self.scored = False
        self.gap_size = gap_size  # store current gap for this pipe

    def update(self):
        """Move pipe to the left"""
        self.x += self.pipe_speed

    def draw(self, surface):
        """Draw metallic-style pipes using this pipe's gap_size"""
        gap = self.gap_size

        # TOP PIPE
        pygame.draw.rect(surface, (46, 125, 50), (self.x, 0,      PIPE_WIDTH, self.gap_y))
        pygame.draw.rect(surface, (16, 60, 20),  (self.x, self.gap_y - 15, PIPE_WIDTH, 15))
        pygame.draw.line(surface, (129, 199, 132), (self.x + 3, 10),
                         (self.x + 3, self.gap_y - 15), 3)
        pygame.draw.line(surface, (27, 94, 32), (self.x + PIPE_WIDTH - 3, 10),
                         (self.x + PIPE_WIDTH - 3, self.gap_y - 15), 2)

        # BOTTOM PIPE
        bottom_y = self.gap_y + gap
        bottom_height = HEIGHT - GROUND_HEIGHT - bottom_y

        pygame.draw.rect(surface, (46, 125, 50), (self.x, bottom_y, PIPE_WIDTH, bottom_height))
        pygame.draw.rect(surface, (16, 60, 20),  (self.x, bottom_y, PIPE_WIDTH, 15))
        pygame.draw.line(surface, (129, 199, 132), (self.x + 3, bottom_y + 15),
                         (self.x + 3, bottom_y + bottom_height), 3)
        pygame.draw.line(surface, (27, 94, 32), (self.x + PIPE_WIDTH - 3, bottom_y + 15),
                         (self.x + PIPE_WIDTH - 3, bottom_y + bottom_height), 2)

    def is_off_screen(self):
        """Check if pipe has left the screen"""
        return self.x < -PIPE_WIDTH

    def get_rect(self):
        """Hitboxes that match visual pipes and current gap"""
        gap = self.gap_size

        top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.gap_y)

        bottom_y = self.gap_y + gap
        bottom_height = HEIGHT - GROUND_HEIGHT - bottom_y
        bottom_rect = pygame.Rect(self.x, bottom_y, PIPE_WIDTH, bottom_height)

        return top_rect, bottom_rect

    @staticmethod
    def create_random_pipe(x, gap_size):
        """Generate a pipe with random gap position and given gap size"""
        min_gap_y = 80
        max_gap_y = HEIGHT - GROUND_HEIGHT - gap_size - 80
        gap_y = random.randint(min_gap_y, max_gap_y)
        return Pipe(x, gap_y, gap_size)
