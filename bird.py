import pygame
import os
from settings import BIRD_ANIMATION_FOLDER, BIRD_FRAME_SIZE, BIRD_ANIMATION_SPEED, BIRD_FLAP_SPEED

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, sounds=None):
        super().__init__()
        
        # Store sounds if provided
        self.sounds = sounds
        
        # Load all animation frames
        self.frames = []
        try:
            # FIX: Use direct file names for Android stability
            # Assumes 4 frames: bird-0.png to bird-3.png
            FRAME_COUNT = 4 
            frame_files = [f"bird-{i}.png" for i in range(FRAME_COUNT)]
            
            print(f"Loading {len(frame_files)} bird animation frames...")
            
            for frame_file in frame_files:
                frame_path = os.path.join(BIRD_ANIMATION_FOLDER, frame_file)
                frame = pygame.image.load(frame_path).convert_alpha()
                frame = pygame.transform.scale(frame, BIRD_FRAME_SIZE)
                self.frames.append(frame)
            
            print(f"Successfully loaded {len(self.frames)} frames!")
        except Exception as e:
            print(f"ERROR: Could not load bird animation: {e}")
            print("Make sure animation frames are in", BIRD_ANIMATION_FOLDER)
            self.frames = []
        
        # Animation state
        self.current_frame = 0
        self.animation_speed = BIRD_ANIMATION_SPEED
        self.animation_counter = 0
        
        # Set initial image
        if self.frames:
            self.image = self.frames[0]
        else:
            self.image = pygame.Surface(BIRD_FRAME_SIZE)
            self.image.fill((255, 200, 50))
        
        # Create rect with SMALLER hitbox (70% of actual width/height)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.width = int(self.rect.width * 0.7)  # 70% of actual width
        self.rect.height = int(self.rect.height * 0.7)  # 70% of actual height
        
        # Physics
        self.velocity_y = 0
        self.alive = True
    
    def flap(self):
        """Make the bird jump"""
        self.velocity_y = BIRD_FLAP_SPEED
        # Play flap sound if available
        if hasattr(self, 'sounds') and self.sounds and 'flap' in self.sounds:
            self.sounds['flap'].play()
    
    def apply_gravity(self, gravity):
        """Add gravity to bird's vertical movement"""
        self.velocity_y += gravity
        
        # Cap maximum falling speed
        if self.velocity_y > 10:
            self.velocity_y = 10
        
        self.rect.y += self.velocity_y
    
    def update(self):
        """Update animation frames"""
        if self.frames:
            self.animation_counter += self.animation_speed
            if self.animation_counter >= 1:
                self.animation_counter = 0
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = self.frames[self.current_frame]