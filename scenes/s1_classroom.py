import pygame
from .scene_template import Scene

class classroom(Scene):
    def __init__(self):
        # Initialize the scene to follow and the duration of the current scene 
        super().__init__(180, "playground")
        
        # Initial player position (x, y)
        self.player_pos = pygame.math.Vector2(100, 100)
        self.player_collision_box = pygame.Rect(self.player_pos.x, self.player_pos.y, 50, 50)
        self.player_speed = self.save["bA_speed"]
        
        # Initialize collision boxes
        self.collision_boxes = [                                                                                
            pygame.Rect(211, 160, 233, 54)                                                                                                                                                                                                                                                                                                                                                        )
        ]

    
    def process_input(self, events):
        super().process_input(events)                                                                                               

    def update(self, dt):
        super().update(dt)

        new_rect = self.player_collision_box.copy()

        new_rect.x += self.movement.x * self.player_speed * dt
        new_rect.y += self.movement.y * self.player_speed * dt

        if not any(new_rect.colliderect(box) for box in self.collision_boxes):
            self.player_collision_box = new_rect
            self.player_pos.update(self.player_collision_box.x, self.player_collision_box.y)

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
            (self.player_pos.x, self.player_pos.y, 50, 50)
        )

        # Draw UI text
        text = self.font.render("Classroom", True, (255,255,255))
        screen.blit(text, (20, 20))
        
        self.display_counters(screen)
