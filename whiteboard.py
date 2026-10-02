"""
Modulo Lavagna Digitale Interattiva
Permette di disegnare a mano libera su uno sfondo bianco
"""

import pygame
import sys
from pygame.locals import *

class Whiteboard:
    def __init__(self, width=1000, height=700):
        """Inizializza la lavagna digitale"""
        self.width = width
        self.height = height
        self.running = True
        
        # Inizializza Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Lavagna Digitale - Equilibrio Statico")
        self.clock = pygame.time.Clock()
        
        # Colori
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 200, 0)
        self.GRAY = (200, 200, 200)
        
        # Proprietà del disegno
        self.drawing = False
        self.brush_color = self.BLACK
        self.brush_size = 3
        self.last_pos = None
        
        # Surface per il disegno
        self.canvas = pygame.Surface((self.width, self.height))
        self.canvas.fill(self.WHITE)
        
        # Font per bottoni e testo
        self.font = pygame.font.Font(None, 24)
        
    def handle_events(self):
        """Gestisce gli eventi di input"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                return
            
            if event.type == MOUSEBUTTONDOWN:
                self.drawing = True
                self.last_pos = event.pos
            
            if event.type == MOUSEBUTTONUP:
                self.drawing = False
                self.last_pos = None
            
            if event.type == MOUSEMOTION and self.drawing:
                self.draw_line(self.last_pos, event.pos)
                self.last_pos = event.pos
            
            if event.type == KEYDOWN:
                if event.key == K_c:  # Cancella
                    self.canvas.fill(self.WHITE)
                elif event.key == K_1:  # Nero
                    self.brush_color = self.BLACK
                elif event.key == K_2:  # Rosso
                    self.brush_color = self.RED
                elif event.key == K_3:  # Blu
                    self.brush_color = self.BLUE
                elif event.key == K_4:  # Verde
                    self.brush_color = self.GREEN
                elif event.key == K_PLUS or event.key == K_EQUALS:
                    self.brush_size = min(self.brush_size + 2, 20)
                elif event.key == K_MINUS:
                    self.brush_size = max(self.brush_size - 2, 1)
                elif event.key == K_q:  # Esci
                    self.running = False
    
    def draw_line(self, start_pos, end_pos):
        """Disegna una linea tra due punti"""
        if start_pos and end_pos:
            pygame.draw.line(self.canvas, self.brush_color, start_pos, end_pos, self.brush_size)
    
    def draw_ui(self):
        """Disegna l'interfaccia utente"""
        # Barra dei colori e comandi
        ui_height = 50
        pygame.draw.rect(self.screen, self.GRAY, (0, 0, self.width, ui_height))
        
        # Testo istruzioni
        instructions = [
            f"C=Cancella | 1=Nero | 2=Rosso | 3=Blu | 4=Verde | +/- Spessore:{self.brush_size} | Q=Esci"
        ]
        
        for i, text in enumerate(instructions):
            text_surface = self.font.render(text, True, self.BLACK)
            self.screen.blit(text_surface, (10, 10 + i * 25))
        
        # Disegna bottoni colore
        button_y = 10
        colors_buttons = [
            (self.BLACK, "N", 60),
            (self.RED, "R", 100),
            (self.BLUE, "B", 140),
            (self.GREEN, "G", 180),
        ]
        
        for color, label, x in colors_buttons:
            pygame.draw.rect(self.screen, color, (x, button_y, 30, 30))
            pygame.draw.rect(self.screen, self.BLACK, (x, button_y, 30, 30), 2)
    
    def render(self):
        """Renderizza il frame"""
        self.screen.fill(self.WHITE)
        self.screen.blit(self.canvas, (0, 50))
        self.draw_ui()
        pygame.display.flip()
    
    def run(self):
        """Loop principale della lavagna"""
        print("\n=== LAVAGNA DIGITALE ===")
        print("Comandi:")
        print("  Mouse: Disegna")
        print("  C: Cancella tutto")
        print("  1: Colore Nero")
        print("  2: Colore Rosso")
        print("  3: Colore Blu")
        print("  4: Colore Verde")
        print("  +/-: Aumenta/Diminuisci spessore")
        print("  Q: Esci")
        print("========================\n")
        
        while self.running:
            self.handle_events()
            self.render()
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    whiteboard = Whiteboard()
    whiteboard.run()
