import pygame
from bird import Bird
from pipe import Pipe
from settings import WIDTH, HEIGHT, GRAVITY, GROUND_HEIGHT, PIPE_WIDTH

BASE_PIPE_GAP = 240   # starting gap
MIN_PIPE_GAP = 120    # smallest allowed gap
GAP_STEP = 20         # gap reduction per level
POINTS_PER_LEVEL = 5  # shrink gap every 5 points

class World:
    def __init__(self, sounds=None):
        """Initialize world with optional sounds"""
        self.sounds = sounds  # Store sounds from main.py
        
        # Create bird
        # FIX: Ensure sounds are passed to the Bird instance
        self.bird = Bird(50, HEIGHT // 2, sounds=sounds) 
        
        # Pipe management
        self.pipes = []
        self.pipe_spawn_timer = 0
        self.pipe_spawn_interval = 120  # Spawn every 2 seconds (120 frames @ 60 FPS)
        
        # Game state
        self.score = 0
        self.game_over = False
        self.playing = False
        
        # Difficulty (pipe gap)
        self.current_pipe_gap = BASE_PIPE_GAP
        
        # Spawn first pipe
        self.spawn_pipe()
    
    def spawn_pipe(self):
        """Create a new pipe on the right side"""
        new_pipe = Pipe.create_random_pipe(WIDTH, self.current_pipe_gap)
        self.pipes.append(new_pipe)
    
    def update(self, action=None):
        """Main game update logic"""
        if not self.playing:
            return
        
        # Handle input
        if action == "jump":
            self.bird.flap()
        
        # Apply gravity
        self.bird.apply_gravity(GRAVITY)
        
        # Update pipes
        for pipe in self.pipes:
            pipe.update()
        
        # Spawn new pipes
        self.pipe_spawn_timer += 1
        if self.pipe_spawn_timer >= self.pipe_spawn_interval:
            self.spawn_pipe()
            self.pipe_spawn_timer = 0
        
        # Remove off-screen pipes
        self.pipes = [p for p in self.pipes if not p.is_off_screen()]
        
        # Check collisions
        self.check_collisions()
        
        # Update score
        self.update_score()
    
    def check_collisions(self):
        """Check if bird hit pipes or ground"""
        # Hit ground
        if self.bird.rect.bottom >= HEIGHT - GROUND_HEIGHT:
            if self.sounds and 'die' in self.sounds:
                self.sounds['die'].play()
            self.game_over = True
            self.playing = False
            return
        
        # Hit ceiling
        if self.bird.rect.top <= 0:
            self.game_over = True
            self.playing = False
            return
        
        # Hit pipes
        for pipe in self.pipes:
            top_rect, bottom_rect = pipe.get_rect()
            if (self.bird.rect.colliderect(top_rect) or 
                self.bird.rect.colliderect(bottom_rect)):
                if self.sounds and 'hit' in self.sounds:
                    self.sounds['hit'].play()
                self.game_over = True
                self.playing = False
                return
    
    def update_score(self):
        """Add 1 point each time bird passes a pipe and adjust difficulty"""
        for pipe in self.pipes:
            pipe_center = pipe.x + PIPE_WIDTH // 2
            bird_center = self.bird.rect.centerx
            
            if not hasattr(pipe, 'scored'):
                pipe.scored = False
            
            if not pipe.scored and bird_center > pipe_center:
                self.score += 1
                pipe.scored = True
                # Play score sound (using 'hit' as point sound is unavailable)
                # FIX: Properly indent the sound playback to resolve SyntaxError
                if self.sounds and 'hit' in self.sounds: 
                    self.sounds['hit'].play()
            
            # Difficulty: shrink gap every POINTS_PER_LEVEL points
            level = self.score // POINTS_PER_LEVEL
            new_gap = BASE_PIPE_GAP - level * GAP_STEP
            self.current_pipe_gap = max(new_gap, MIN_PIPE_GAP)
    
    def restart(self):
        """Reset game for new play"""
        self.__init__(self.sounds)  # Pass sounds to new instance