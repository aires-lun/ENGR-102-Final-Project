import pygame
from .scene_template import Scene

class classroom(Scene):
    def __init__(self):
        # Initialize the scene to follow and the duration of the current scene 
        super().__init__(180, "playground")
        # Initial player position (x, y)
        self.player_pos = pygame.math.Vector2(100, 100)
        
        self.player_speed = self.save["bA_speed"]
    
    def process_input(self, events):
        super().process_input(events)

    def update(self, dt):
        super().update(dt)
        self.player_pos += self.movement * self.player_speed * dt
        

    def render(self, screen):
        super().render(screen)
        
        # Load background for classroom
        background_image = pygame.image.load("assets/classroom_temp.png").convert_alpha()
        background_image = pygame.transform.scale(background_image, (800, 600))
        screen.blit(background_image, (0, 0))

        # Draw player
        pygame.draw.rect(
            screen,
            (200, 50, 50),
            (self.player_pos.x, self.player_pos.y, 50, 50)
        )

        # Draw UI text
        text = self.font.render("Classroom", True, (255,255,255))
        screen.blit(text, (20, 20))
