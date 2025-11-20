import pygame
from save_manager import load_save, save_data

class Scene:
    """This is the parent class for all scenes, it is like a template.
    """
    
    def __init__(self, duration = None, next_scene_key = None):
        """Default constructor. It sets the initial values for the scene like initial position.

        Parameters:
            duration (float): Time the scene should last in seconds (real time). Defaults to None.
            next_scene_key (string): The key for the scene to follow after the current scene. Defaults to None.
        """
        self.next_scene = self
        self.timer = 0.0
        self.duration = duration
        self.default_next_scene = next_scene_key
        self.font = pygame.font.Font(None, 36)
        self.save = load_save()
        
    def save_game(self):
        """When called, saves the game data to the file "save.json".
        """
        save_data(self.save)

    def process_input(self, events):
        """This function detects and defines how input should be processed.

        Parameters:
            events (List[Event]): A list of events that pygame registers at an instant of time.
        """
        self.movement = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()  # continuous input
        if keys[pygame.K_LEFT]:
            self.movement.x = -1
        if keys[pygame.K_RIGHT]:
            self.movement.x = 1
        if keys[pygame.K_UP]:
            self.movement.y = -1
        if keys[pygame.K_DOWN]:
            self.movement.y = 1
    
    def update(self, dt):
        """This function handles the game logic on what should be updated. It should move objects, animate sprites, check for collisions,
        update timers, update counters, etc.

        Parameters:
            dt (float): The time step (in seconds) taken before updating data again
        """
        # Update the timer
        if self.duration is not None:
            self.timer += dt
            if self.timer >= self.duration and self.default_next_scene:
                self.switch_to(self.default_next_scene)
                
        # Normalize movement speed
        if self.movement.length_squared() > 0:
            self.movement = self.movement.normalize()
            
    def render(self, screen):
        """This function is what draws the whole frame to the screen. It does not handle any game logic, it purely draws the pixels to the
        screen without changing anything, completely visual.

        Parameters:
            screen (Surface): The window that displays the game.
        """
        screen.fill((0,0,0))   # Clears the screen

    def display_counters(self, screen):
        WHITE = (255, 255, 255)
        SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
        padding = 10
        line1_surface = self.font.render(f"Buyers: {self.save["buyers"]}", True, WHITE)
        line1_rect = line1_surface.get_rect()
        line1_rect.topright = (SCREEN_WIDTH - padding, padding)
        screen.blit(line1_surface, line1_rect)

        line2_surface = self.font.render(f"Cash: {self.save["money"]}", True, WHITE)
        line2_rect = line2_surface.get_rect()
        line2_rect.topright = line1_rect.bottomright
        line2_rect.top += padding
        screen.blit(line2_surface, line2_rect)

        line3_surface = self.font.render(f"Candy: {self.save["candy"]}", True, WHITE)
        line3_rect = line3_surface.get_rect()
        line3_rect.topright = line2_rect.bottomright
        line3_rect.top += padding
        screen.blit(line3_surface, line3_rect)
    
    def switch_to(self, next_scene_key):
        """This function is used to change what the next scene should be. It is simple enough that it is not overloaded in the individual
        scenes and is defined in the parent class SceneTemplate.

        Parameters:
            next_scene_key (string): The key to the next scene to switch to.
        """
        self.next_scene = next_scene_key