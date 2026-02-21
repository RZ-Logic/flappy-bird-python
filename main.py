# main.py
import pygame
import sys
import os
from settings import WIDTH, HEIGHT, FPS, GROUND_HEIGHT
from world import World

# Initialize mixer BEFORE pygame.init()
pygame.mixer.init(44100, -16, 2, 512)  # MP3 support

class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Load sounds INSIDE __init__
        self.sounds = {
            'flap': pygame.mixer.Sound(os.path.join("assets/sounds", "flap.ogg")),
            'hit': pygame.mixer.Sound(os.path.join("assets/sounds", "hit.ogg")),
            'die': pygame.mixer.Sound(os.path.join("assets/sounds", "die.ogg"))
        }
        # Set volume (0.0 to 1.0)
        for sound in self.sounds.values():
            sound.set_volume(0.6)
        
        # Pass sounds to world
        self.world = World(self.sounds)
    
    def handle_events(self):
        """Process user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.world.playing and not self.world.game_over:
                        self.world.playing = True
                    elif self.world.playing:
                        self.world.update(action="jump")
                if event.key == pygame.K_r:
                    self.world.restart()
    
    def update(self):
        """Update game state"""
        self.world.update()
        self.world.bird.update()
    
    def draw(self):
        """Render everything"""
        # Sky gradient background
        for y in range(HEIGHT):
            color_value = int(200 + (y / HEIGHT) * 55)  # 200 to 255
            pygame.draw.line(self.screen, (135, 206, color_value), (0, y), (WIDTH, y))
        
        # Draw pipes
        for pipe in self.world.pipes:
            pipe.draw(self.screen)
        
        # Draw bird
        self.screen.blit(self.world.bird.image, self.world.bird.rect)
        
        # Draw ground
        pygame.draw.rect(self.screen, (139, 69, 19), (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.world.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        
        # Game over screen
        if self.world.game_over:
            game_over_text = font.render("GAME OVER! Press R to restart", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            self.screen.blit(game_over_text, text_rect)
        
        # Start screen
        if not self.world.playing and not self.world.game_over:
            start_text = font.render("Press SPACE to start", True, (0, 0, 0))
            text_rect = start_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            self.screen.blit(start_text, text_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
