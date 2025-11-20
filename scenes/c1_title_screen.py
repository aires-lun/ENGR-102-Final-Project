import pygame
from .scene_template import Scene

class title_screen(Scene):
    def __init__(self):
        super().__init__(None, "intro")

    def process_input(self, events):
        super().process_input(events)
        
        for e in events:
            if e.type == pygame.KEYDOWN:
                self.switch_to("intro")

    def render(self, screen):
        super().render(screen)
        text = self.font.render("Press any key to start", True, (255,255,255))
        screen.blit(text, (100,100))
<<<<<<< HEAD
###frfrrf
=======


#this is another test
#this is a test to see if github works for dnyanesh
>>>>>>> e1b0ef017526a5a5866fc6ee61c5639cb04c13ff
