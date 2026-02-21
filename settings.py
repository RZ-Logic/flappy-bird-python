# settings.py
import pygame

SOUNDS_FOLDER = "assets/sounds"

# Screen dimensions
WIDTH = 1280
HEIGHT = 720
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Game settings
GRAVITY = 0.5
BIRD_FLAP_SPEED = -10
PIPE_SPEED = -5
PIPE_WIDTH = 50
PIPE_GAP = 240
GROUND_HEIGHT = 100


# Bird Animation
BIRD_ANIMATION_FOLDER = "assets/bird"
BIRD_FRAME_SIZE = (60, 60)  # Adjust size if needed
BIRD_ANIMATION_SPEED = 0.08  # Change frames every X updates (lower = faster)