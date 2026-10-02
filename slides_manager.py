"""
Modulo Gestione Slide
Permette di caricare e visualizzare slide PowerPoint o immagini
"""

import os
import cv2
import numpy as np
from pathlib import Path
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SlidesManager:
    def __init__(self):
        """Inizializza il gestore delle slide"""
        self.slides = []
        self.current_slide_index = 0
        self.slide_folder = "sample_slides"
        
        # Crea cartella sample se non esiste
        if not os.path.exists(self.slide_folder):
            os.makedirs(self.slide_folder)
            self.create_sample_slides()
    
    def create_sample_slides(self):
        """Crea slide di esempio per la fisica"""
        sample_slides_data = [
            {
                "title": "EQUILIBRIO STATICO",
                "subtitle": "Condizioni di equilibrio di un corpo rigido",
                "content": [
                    "• Un corpo è in equilibrio statico quando:",
                    "  - La somma delle forze = 0",
                    "  - La somma dei momenti = 0",
                    "",
                    "• Condizione matematica:",
                    "  ΣF = 0  →  Il corpo non si muove",
                    "  ΣM = 0  →  Il corpo non ruota"
                ]
            },
            {
                "title": "FORZE AGENTI SU UN PIANO INCLINATO",
                "subtitle": "Analisi delle componenti",
                "content": [
                    "Forze principali:",
                    "1. PESO (W = mg) - verticale verso il basso",
                    "   - Componente ∥: W·sin(θ)",
                    "   - Componente ⊥: W·cos(θ)",
                    "",
                    "2. FORZA NORMALE (N) - ⊥ al piano",
                    "   - Reazione del piano",
                    "",
                    "3. ATTRITO (f) - ∥ al piano",
                    "   - Oppone il movimento"
                ]
            },
            {
                "title": "COEFFICIENTE DI ATTRITO",
                "subtitle": "Attrito statico vs dinamico",
                "content": [
                    "Attrito Statico (μ_s):",
                    "• Forza che impedisce il movimento",
                    "• f_s ≤ μ_s · N",
                    "• Dipende dalle superfici",
                    "",
                    "Attrito Dinamico (μ_k):",
                    "• Forza che si oppone al movimento",
                    "• f_k = μ_k · N",
                    "• Solitamente μ_k < μ_s",
                    "",
                    "Valori tipici: μ_s = 0.5 - 1.5"
                ]
            },
            {
                "title": "CONDIZIONE DI EQUILIBRIO",
                "subtitle": "Su un piano inclinato",
                "content": [
                    "Per l'EQUILIBRIO STATICO:",
                    "",
                    "Lungo il piano:",
                    "  f ≥ W·sin(θ)",
                    "  μ_s·N ≥ W·sin(θ)",
                    "  μ_s·W·cos(θ) ≥ W·sin(θ)",
                    "  μ_s ≥ tan(θ)",
                    "",
                    "Perpendicolare al piano:",
                    "  N = W·cos(θ)"
                ]
            },
            {
                "title": "APPLICAZIONI PRATICHE",
                "subtitle": "Esempi della vita quotidiana",
                "content": [
                    "1. Auto su strada in salita",
                    "   - Accelera: componente parallela > attrito",
                    "   - Frena: attrito equilibra la gravità",
                    "",
                    "2. Scatola su un tavolo inclinato",
                    "   - Non scivola se μ_s·cos(θ) ≥ sin(θ)",
                    "",
                    "3. Scala appoggiata al muro",
                    "   - Equilibrio di momenti e forze",
                    "",
                    "4. Frenata di un'auto in salita"
                ]
            }
        ]
        
        # Crea immagini PNG per le slide
        for idx, slide_data in enumerate(sample_slides_data):
            self.create_slide_image(idx, slide_data)
    
    def create_slide_image(self, slide_number, data):
        """Crea un'immagine PNG per una slide"""
        width, height = 1280, 720
        image = Image.new('RGB', (width, height), color='white')
        
        # Sfondo con gradiente (simulato)
        pixels = image.load()
        for y in range(height):
            # Gradiente blu chiaro
            blue_value = int(220 + (y / height) * 35)
            for x in range(width):
                pixels[x, y] = (220, 230, blue_value)
        
        # Usa PIL ImageDraw
        from PIL import ImageDraw, ImageFont
        
        draw = ImageDraw.Draw(image)
        
        # Font
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
            subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
            content_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
        except:
            # Fallback a font di default
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
        
        # Titolo
        draw.text((50, 50), data["title"], fill='darkblue', font=title_font)
        
        # Sottotitolo
        draw.text((50, 130), data["subtitle"], fill='navy', font=subtitle_font)
        
        # Linea
        draw.line([(50, 170), (1230, 170)], fill='darkblue', width=3)
        
        # Contenuto
        y_pos = 200
        for line in data["content"]:
            draw.text((70, y_pos), line, fill='black', font=content_font)
            y_pos += 45
        
        # Numero slide
        slide_text = f"Slide {slide_number + 1}"
        draw.text((1100, 680), slide_text, fill='gray', font=content_font)
        
        # Salva
        filename = os.path.join(self.slide_folder, f"slide_{slide_number:02d}.png")
        image.save(filename)
        print(f"✓ Creata: {filename}")
    
    def load_slides_from_folder(self, folder_path=None):
        """Carica tutte le slide da una cartella"""
        if folder_path is None:
            folder_path = self.slide_folder
        
        self.slides = []
        
        # Estensioni supportate
        image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
        
        # Carica tutte le immagini
        for file in sorted(os.listdir(folder_path)):
            if os.path.splitext(file)[1].lower() in image_extensions:
                file_path = os.path.join(folder_path, file)
                self.slides.append(file_path)
        
        print(f"\n✓ Caricate {len(self.slides)} slide da {folder_path}")
        return self.slides
    
    def get_current_slide(self):
        """Ritorna l'immagine della slide corrente"""
        if not self.slides:
            return None
        
        slide_path = self.slides[self.current_slide_index]
        return cv2.imread(slide_path)
    
    def next_slide(self):
        """Passa alla slide successiva"""
        if self.slides:
            self.current_slide_index = (self.current_slide_index + 1) % len(self.slides)
            return self.current_slide_index
    
    def previous_slide(self):
        """Torna alla slide precedente"""
        if self.slides:
            self.current_slide_index = (self.current_slide_index - 1) % len(self.slides)
            return self.current_slide_index
    
    def jump_to_slide(self, index):
        """Salta a una slide specifica"""
        if 0 <= index < len(self.slides):
            self.current_slide_index = index
            return self.current_slide_index
        return None
    
    def get_slide_info(self):
        """Ritorna informazioni sulla slide corrente"""
        if not self.slides:
            return "Nessuna slide caricata"
        
        total = len(self.slides)
        current = self.current_slide_index + 1
        filename = os.path.basename(self.slides[self.current_slide_index])
        
        return f"Slide {current}/{total}: {filename}"

if __name__ == "__main__":
    manager = SlidesManager()
    manager.load_slides_from_folder()
    print(f"\n{manager.get_slide_info()}")
