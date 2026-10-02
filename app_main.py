"""
APPLICAZIONE PRINCIPALE INTEGRATA
Physics Video Creator - Sistema completo per video didattici

Questo software integra:
- Gestione Slide
- Simulatore Fisica Interattivo (Equilibrio Statico)
- Lavagna Digitale
- Interfaccia unificata per creare video educativi
"""

import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import threading
import sys
import os

# Import dei moduli custom
from slides_manager import SlidesManager
from interactive_physics import EquilibrioStaticoSimulator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class PhysicsVideoCreator:
    def __init__(self, root):
        """Inizializza l'applicazione principale"""
        self.root = root
        self.root.title("Physics Video Creator - Equilibrio Statico")
        self.root.geometry("1600x900")
        
        # Stile
        style = ttk.Style()
        style.theme_use('clam')
        
        # Gestore slide
        self.slides_manager = SlidesManager()
        self.slides_manager.load_slides_from_folder()
        
        # Stato dell'app
        self.current_view = "menu"
        self.physics_window = None
        
        # Crea il layout principale
        self.create_main_layout()
        
        print("\n" + "="*60)
        print("🎬 PHYSICS VIDEO CREATOR")
        print("="*60)
        print("Applicazione didattica interattiva per video educativi")
        print("Tema: Equilibrio Statico di un Corpo")
        print("="*60 + "\n")
    
    def create_main_layout(self):
        """Crea il layout principale dell'app"""
        # Frame principale
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # HEADER
        self.create_header()
        
        # CONTENUTO PRINCIPALE (cambia in base alla vista)
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # FOOTER
        self.create_footer()
        
        # Mostra il menu iniziale
        self.show_menu()
    
    def create_header(self):
        """Crea l'intestazione dell'app"""
        header_frame = ttk.Frame(self.main_frame, relief=tk.SUNKEN, height=80)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        title_label = ttk.Label(header_frame, text="🎬 Physics Video Creator - Equilibrio Statico", 
                                font=("Arial", 20, "bold"))
        title_label.pack(side=tk.LEFT, padx=20, pady=15)
        
        subtitle_label = ttk.Label(header_frame, text="Strumento didattico per creare video educativi",
                                   font=("Arial", 12), foreground="gray")
        subtitle_label.pack(side=tk.LEFT, padx=20)
    
    def create_footer(self):
        """Crea il footer dell'app"""
        footer_frame = ttk.Frame(self.main_frame, relief=tk.SUNKEN)
        footer_frame.pack(fill=tk.X, pady=(10, 0))
        
        footer_label = ttk.Label(footer_frame, text="Seleziona una modalità per iniziare →", 
                                font=("Arial", 10), foreground="darkblue")
        footer_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.status_label = ttk.Label(footer_frame, text="Pronto", font=("Arial", 10))
        self.status_label.pack(side=tk.RIGHT, padx=10, pady=5)
    
    def clear_content(self):
        """Pulisce il frame del contenuto"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_menu(self):
        """Mostra il menu principale"""
        self.clear_content()
        self.current_view = "menu"
        
        # Titolo
        title = ttk.Label(self.content_frame, text="Scegli una modalità di lavoro:", 
                         font=("Arial", 16, "bold"))
        title.pack(pady=20)
        
        # Frame con i bottoni
        buttons_frame = ttk.Frame(self.content_frame)
        buttons_frame.pack(pady=40, fill=tk.BOTH, expand=True)
        
        # Bottone 1: Slide
        self.create_menu_button(
            buttons_frame,
            "📊 SLIDE PRESENTER",
            "Visualizza e gestisci le slide della presentazione",
            self.show_slides_view,
            0, 0
        )
        
        # Bottone 2: Simulatore Fisica
        self.create_menu_button(
            buttons_frame,
            "⚙️ SIMULATORE FISICA",
            "App interattiva: Equilibrio statico con slider",
            self.show_physics_view,
            0, 1
        )
        
        # Bottone 3: Lavagna
        self.create_menu_button(
            buttons_frame,
            "🎨 LAVAGNA DIGITALE",
            "Lavagna per disegnare e annotare spiegazioni",
            self.show_whiteboard,
            1, 0
        )
        
        # Bottone 4: Modalità Presentazione
        self.create_menu_button(
            buttons_frame,
            "🎬 MODALITÀ PRESENTAZIONE",
            "Integra Slide + Simulatore + Lavagna",
            self.show_presentation_mode,
            1, 1
        )
        
        self.status_label.config(text="Menu principale")
    
    def create_menu_button(self, parent, title, description, command, row, col):
        """Crea un bottone del menu principale"""
        button_frame = ttk.LabelFrame(parent, text=title, padding=20)
        button_frame.grid(row=row, column=col, padx=20, pady=20, sticky="nsew", 
                         ipadx=20, ipady=20)
        
        # Testo descrizione
        desc_label = ttk.Label(button_frame, text=description, 
                              font=("Arial", 11), foreground="gray", wraplength=250)
        desc_label.pack(pady=10)
        
        # Bottone
        btn = ttk.Button(button_frame, text="Apri →", command=command)
        btn.pack(pady=10)
        
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
    
    def show_slides_view(self):
        """Mostra la visualizzazione delle slide"""
        self.clear_content()
        self.current_view = "slides"
        
        # Controlli
        controls_frame = ttk.Frame(self.content_frame)
        controls_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(controls_frame, text="◀ Indietro", command=self.show_menu).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(controls_frame, text="SLIDE PRESENTER", font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=20)
        
        self.slide_info_label = ttk.Label(controls_frame, text="", font=("Arial", 10))
        self.slide_info_label.pack(side=tk.RIGHT, padx=10)
        
        # Frame per la slide
        slide_frame = ttk.LabelFrame(self.content_frame, text="Slide Attuale", padding=10)
        slide_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.slide_canvas = tk.Canvas(slide_frame, bg="white", height=500)
        self.slide_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Controlli navigazione
        nav_frame = ttk.Frame(self.content_frame)
        nav_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(nav_frame, text="◀ Slide Precedente", 
                  command=self.prev_slide).pack(side=tk.LEFT, padx=5)
        ttk.Button(nav_frame, text="Slide Successiva ▶", 
                  command=self.next_slide).pack(side=tk.LEFT, padx=5)
        
        # Mostra la prima slide
        self.display_slide()
        
        self.status_label.config(text="Visualizzazione Slide")
    
    def display_slide(self):
        """Visualizza la slide corrente"""
        slide_image = self.slides_manager.get_current_slide()
        
        if slide_image is not None:
            # Converti da BGR (OpenCV) a RGB
            slide_image_rgb = cv2.cvtColor(slide_image, cv2.COLOR_BGR2RGB)
            
            # Resize per adattare al canvas
            height = 500
            aspect_ratio = slide_image_rgb.shape[1] / slide_image_rgb.shape[0]
            width = int(height * aspect_ratio)
            
            slide_image_resized = cv2.resize(slide_image_rgb, (width, height))
            
            # Converti per Tkinter
            pil_image = Image.fromarray(slide_image_resized)
            photo = ImageTk.PhotoImage(pil_image)
            
            # Mostra su canvas
            self.slide_canvas.delete("all")
            self.slide_canvas.create_image(
                self.slide_canvas.winfo_width()//2,
                self.slide_canvas.winfo_height()//2,
                image=photo
            )
            self.slide_canvas.image = photo
            
            # Aggiorna info
            self.slide_info_label.config(text=self.slides_manager.get_slide_info())
    
    def next_slide(self):
        """Passa alla slide successiva"""
        self.slides_manager.next_slide()
        self.display_slide()
    
    def prev_slide(self):
        """Torna alla slide precedente"""
        self.slides_manager.previous_slide()
        self.display_slide()
    
    def show_physics_view(self):
        """Mostra il simulatore di fisica"""
        self.clear_content()
        self.current_view = "physics"
        
        # Controlli
        controls_frame = ttk.Frame(self.content_frame)
        controls_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(controls_frame, text="◀ Indietro", command=self.show_menu).pack(side=tk.LEFT, padx=5)
        ttk.Label(controls_frame, text="SIMULATORE EQUILIBRIO STATICO", 
                 font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=20)
        
        # Messaggio
        msg = ttk.Label(self.content_frame, 
                       text="Il simulatore si apre in una finestra separata...\nUsa gli slider per modificare i parametri e osserva come cambiano le forze!",
                       font=("Arial", 11), foreground="darkblue")
        msg.pack(pady=20)
        
        # Bottone per lanciare
        ttk.Button(self.content_frame, text="🚀 Avvia Simulatore", 
                  command=self.launch_physics_simulator).pack(pady=20)
        
        self.status_label.config(text="Simulatore Fisica (pronto)")
    
    def launch_physics_simulator(self):
        """Lancia il simulatore di fisica"""
        # Avvia in thread separato per non bloccare l'UI
        thread = threading.Thread(target=self._run_physics_sim, daemon=True)
        thread.start()
        self.status_label.config(text="Simulatore Fisica (in esecuzione)")
    
    def _run_physics_sim(self):
        """Thread per il simulatore"""
        simulator = EquilibrioStaticoSimulator()
        simulator.run()
    
    def show_whiteboard(self):
        """Mostra la lavagna digitale"""
        self.clear_content()
        self.current_view = "whiteboard"
        
        # Controlli
        controls_frame = ttk.Frame(self.content_frame)
        controls_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(controls_frame, text="◀ Indietro", command=self.show_menu).pack(side=tk.LEFT, padx=5)
        ttk.Label(controls_frame, text="LAVAGNA DIGITALE", 
                 font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=20)
        
        # Messaggio
        msg = ttk.Label(self.content_frame, 
                       text="La lavagna si apre in una finestra separata (Pygame)...\nComandi: Mouse per disegnare, C per cancellare, Q per uscire",
                       font=("Arial", 11), foreground="darkblue")
        msg.pack(pady=20)
        
        # Bottone per lanciare
        ttk.Button(self.content_frame, text="🎨 Apri Lavagna", 
                  command=self.launch_whiteboard).pack(pady=20)
        
        self.status_label.config(text="Lavagna Digitale (pronta)")
    
    def launch_whiteboard(self):
        """Lancia la lavagna digitale"""
        from whiteboard import Whiteboard
        
        thread = threading.Thread(target=self._run_whiteboard, daemon=True)
        thread.start()
        self.status_label.config(text="Lavagna Digitale (in esecuzione)")
    
    def _run_whiteboard(self):
        """Thread per la lavagna"""
        from whiteboard import Whiteboard
        whiteboard = Whiteboard()
        whiteboard.run()
    
    def show_presentation_mode(self):
        """Mostra la modalità presentazione integrata"""
        self.clear_content()
        self.current_view = "presentation"
        
        # Controlli
        controls_frame = ttk.Frame(self.content_frame)
        controls_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(controls_frame, text="◀ Menu Principale", command=self.show_menu).pack(side=tk.LEFT, padx=5)
        ttk.Label(controls_frame, text="🎬 MODALITÀ PRESENTAZIONE", 
                 font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=20)
        
        # Frame principale con 2 colonne
        main_split = ttk.PanedWindow(self.content_frame, orient=tk.HORIZONTAL)
        main_split.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # SINISTRA: Slide
        left_frame = ttk.LabelFrame(main_split, text="📊 SLIDE", padding=10)
        main_split.add(left_frame, weight=1)
        
        self.pres_slide_canvas = tk.Canvas(left_frame, bg="white", height=400)
        self.pres_slide_canvas.pack(fill=tk.BOTH, expand=True)
        
        left_controls = ttk.Frame(left_frame)
        left_controls.pack(fill=tk.X, pady=10)
        
        ttk.Button(left_controls, text="◀", command=self.pres_prev_slide).pack(side=tk.LEFT, padx=2)
        ttk.Button(left_controls, text="▶", command=self.pres_next_slide).pack(side=tk.LEFT, padx=2)
        self.pres_slide_info = ttk.Label(left_controls, text="")
        self.pres_slide_info.pack(side=tk.LEFT, padx=10)
        
        # DESTRA: Pannello di controllo
        right_frame = ttk.LabelFrame(main_split, text="⚙️ CONTROLLI", padding=10)
        main_split.add(right_frame, weight=1)
        
        # Sezione Simulatore
        ttk.Label(right_frame, text="Simulatore Fisica:", font=("Arial", 11, "bold")).pack(anchor=tk.W, pady=10)
        ttk.Button(right_frame, text="🚀 Avvia Simulatore", 
                  command=self.launch_physics_simulator).pack(fill=tk.X, pady=5)
        
        # Sezione Lavagna
        ttk.Label(right_frame, text="Lavagna Digitale:", font=("Arial", 11, "bold")).pack(anchor=tk.W, pady=(20, 10))
        ttk.Button(right_frame, text="🎨 Apri Lavagna", 
                  command=self.launch_whiteboard).pack(fill=tk.X, pady=5)
        
        # Sezione Info
        ttk.Label(right_frame, text="Info Slide:", font=("Arial", 11, "bold")).pack(anchor=tk.W, pady=(20, 10))
        info_text = ttk.Label(right_frame, 
                             text="In questa modalità puoi:\n\n1. Navigare le slide\n2. Lanciare il simulatore di fisica\n3. Aprire la lavagna\n\nPerfetto per registrare il video con OBS Studio!",
                             font=("Arial", 10), foreground="darkblue", justify=tk.LEFT)
        info_text.pack(anchor=tk.W, pady=10)
        
        # Mostra la prima slide
        self.pres_display_slide()
        
        self.status_label.config(text="Modalità Presentazione")
    
    def pres_display_slide(self):
        """Mostra la slide nel pannello presentazione"""
        slide_image = self.slides_manager.get_current_slide()
        
        if slide_image is not None:
            slide_image_rgb = cv2.cvtColor(slide_image, cv2.COLOR_BGR2RGB)
            height = 350
            aspect_ratio = slide_image_rgb.shape[1] / slide_image_rgb.shape[0]
            width = int(height * aspect_ratio)
            
            slide_image_resized = cv2.resize(slide_image_rgb, (width, height))
            pil_image = Image.fromarray(slide_image_resized)
            photo = ImageTk.PhotoImage(pil_image)
            
            self.pres_slide_canvas.delete("all")
            self.pres_slide_canvas.create_image(
                self.pres_slide_canvas.winfo_width()//2,
                self.pres_slide_canvas.winfo_height()//2,
                image=photo
            )
            self.pres_slide_canvas.image = photo
            
            self.pres_slide_info.config(text=self.slides_manager.get_slide_info())
    
    def pres_next_slide(self):
        """Slide successiva in modalità presentazione"""
        self.slides_manager.next_slide()
        self.pres_display_slide()
    
    def pres_prev_slide(self):
        """Slide precedente in modalità presentazione"""
        self.slides_manager.previous_slide()
        self.pres_display_slide()
    
    def run(self):
        """Avvia l'applicazione"""
        self.root.mainloop()

def main():
    """Funzione di avvio"""
    root = tk.Tk()
    app = PhysicsVideoCreator(root)
    app.run()

if __name__ == "__main__":
    main()
