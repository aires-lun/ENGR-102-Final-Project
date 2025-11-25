import pygame
from .scene_template import Scene

class classroom(Scene):
    def __init__(self):
        # Initialize the scene to follow and the duration of the current scene 
        super().__init__(180, "playground")
        
        # Initial player position (x, y)
        self.player_pos = pygame.math.Vector2(600, 400)
        self.player_collision_box = pygame.Rect(self.player_pos.x, self.player_pos.y, 25, 25)
        self.player_speed = self.save["bA_speed"]
        
        # Initialize collision boxes
        self.collision_boxes = [
            # Top wall
            pygame.Rect(0, 0, 1280, 196),
            # Bottom wall
            pygame.Rect(0, 577, 1280, 143),
            
            # Misc Objects:
            pygame.Rect(0, 196, 11, 20),
            pygame.Rect(13, 338, 113, 71),
            pygame.Rect(315, 338, 61, 71),
            
            # Small Desks
            pygame.Rect(210, 160, 235, 58),
            pygame.Rect(712, 263, 44, 100),
            pygame.Rect(873, 263, 44, 100),
            pygame.Rect(712, 406, 44, 100),
            pygame.Rect(873, 406, 44, 100),
            # Large Desk
            pygame.Rect(1033, 275, 87, 217),
            
            # Game window boundaries are below
            pygame.Rect(-1, 0, 1, 720),
            pygame.Rect(0, -1, 1280, 1),
            pygame.Rect(1280, 0, 1, 720),
            pygame.Rect(0, 720, 1280, 1),
        ]

    
    def process_input(self, events):
        super().process_input(events)                                                                                               

    def update(self, dt):
        super().update(dt)
        super().move(dt)


    def render(self, screen):
        super().render(screen)
        
        # Load background for classroom
        background_image = pygame.image.load("assets/classroom.png").convert_alpha()
        background_image = pygame.transform.scale(background_image, screen.get_size())
        screen.blit(background_image, (0, 0))

        # Draw player
        pygame.draw.rect(
            screen,
            (200, 50, 50),
            (self.player_pos.x, self.player_pos.y, 25, 25)
        )

        # Draw UI text
        text = self.font.render("Classroom", True, (255,255,255))
        screen.blit(text, (20, 20))
        
        self.display_counters(screen)
