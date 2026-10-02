"""
MAIN INTEGRATED APPLICATION
Physics Video Creator - Complete system for educational videos

This software integrates:
- Slide Management
- Interactive Physics Simulator (Static Equilibrium)
- Digital Whiteboard
- Unified interface for creating educational videos
"""

import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import threading
import sys
import os

# Import custom modules
from slides_manager import SlidesManager
from interactive_physics import EquilibrioStaticoSimulator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class PhysicsVideoCreator:
    def __init__(self, root):
        """Initialize the main application"""
        self.root = root
        self.root.title("Physics Video Creator - Static Equilibrium")
        self.root.geometry("1600x900")
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Slide manager
        self.slides_manager = SlidesManager()
        self.slides_manager.load_slides_from_folder()
        
        # Application state
        self.current_view = "menu"
        self.physics_window = None
        
        # Create main layout
        self.create_main_layout()
        
        print("\n" + "="*60)
        print("🎬 PHYSICS VIDEO CREATOR")
        print("="*60)
        print("Interactive educational application for creating videos")
        print("Topic: Static Equilibrium of a Body")
        print("Created by: Prof. Signorini")
        print("="*60 + "\n")
    
    def create_main_layout(self):
        """Create the main application layout"""
        # Main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # HEADER
        self.create_header()
        
        # MAIN CONTENT (changes based on view)
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # FOOTER
        self.create_footer()
        
        # Show main menu
        self.show_menu()
    
    def create_header(self):
        """Create application header"""
        header_frame = ttk.Frame(self.main_frame, relief=tk.SUNKEN, height=100)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Main title
        title_label = ttk.Label(header_frame, text="🎬 Physics Video Creator - Static Equilibrium", 
                                font=("Arial", 20, "bold"))
        title_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Subtitle
        subtitle_label = ttk.Label(header_frame, text="Educational tool to create teaching videos",
                                   font=("Arial", 12), foreground="gray")
        subtitle_label.pack(side=tk.LEFT, padx=20)
        
        # Creator attribution
        creator_label = ttk.Label(header_frame, text="Created by: Prof. Signorini",
                                 font=("Arial", 10, "italic"), foreground="darkblue")
        creator_label.pack(side=tk.RIGHT, padx=20, pady=10)
    
    def create_footer(self):
        """Create application footer"""
        footer_frame = ttk.Frame(self.main_frame, relief=tk.SUNKEN)
        footer_frame.pack(fill=tk.X, pady=(10, 0))
        
        footer_label = ttk.Label(footer_frame, text="Select a mode to get started →", 
                                font=("Arial", 10), foreground="darkblue")
        footer_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.status_label = ttk.Label(footer_frame, text="Ready", font=("Arial", 10))
        self.status_label.pack(side=tk.RIGHT, padx=10, pady=5)
    
    def clear_content(self):
        """Clear the content frame"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_menu(self):
        """Show main menu"""
        self.clear_content()
        self.current_view = "menu"
        
        # Title
        title = ttk.Label(self.content_frame, text="Choose a working mode:", 
                         font=("Arial", 16, "bold"))
        title.pack(pady=20)
        
        # Frame with buttons
        buttons_frame = ttk.Frame(self.content_frame)
        buttons_frame.pack(pady=40, fill=tk.BOTH, expand=True)
        
        # Button 1: Slides
        self.create_menu_button(
            buttons_frame,
            "📊 SLIDE PRESENTER",
            "View and manage presentation slides",
            self.show_slides_view,
            0, 0
        )
        
        # Button 2: Physics Simulator
        self.create_menu_button(
            buttons_frame,
            "⚙️ PHYSICS SIMULATOR",
            "Interactive app: Static equilibrium with sliders",
            self.show_physics_view,
            0, 1
        )
        
        # Button 3: Whiteboard
        self.create_menu_button(
            buttons_frame,
            "🎨 DIGITAL WHITEBOARD",
            "Whiteboard for drawing and annotating explanations",
            self.show_whiteboard,
            1, 0
        )
        
        # Button 4: Presentation Mode
        self.create_menu_button(
            buttons_frame,
            "🎬 PRESENTATION MODE",
            "Integrates Slides + Simulator + Whiteboard",
            self.show_presentation_mode,
            1, 1
        )
        
        self.status_label.config(text="Main menu")
    
    def create_menu_button(self, parent, title, description, command, row, col):
        """Create a main menu button"""
        button_frame = ttk.LabelFrame(parent, text=title, padding=20)
        button_frame.grid(row=row, column=col, padx=20, pady=20, sticky="nsew", 
                         ipadx=20, ipady=20)
        
        # Description text
        desc_label = ttk.Label(button_frame, text=description, 
                              font=("Arial", 11), foreground="gray", wraplength=250)
        desc_label.pack(pady=10)
        
        # Button
        btn = ttk.Button(button_frame, text="Open →", command=command)
        btn.pack(pady=10)
        
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
    
    def show_slides_view(self):
        """Show slide presentation view"""
        self.clear_content()
        self.current_view = "slides"
        
        # Controls
        controls_frame = ttk.Frame(self.content_frame)
        controls_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(controls_frame, text="◀ Back", command=self.show_menu).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(controls_frame, text="SLIDE PRESENTER", font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=20)
        
        self.slide_info_label = ttk.Label(controls_frame, text="", font=("Arial", 10))
        self.slide_info_label.pack(side=tk.RIGHT, padx=10)
        
        # Frame for slide
        slide_frame = ttk.LabelFrame(self.content_frame, text="Current Slide", padding=10)
        slide_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.slide_canvas = tk.Canvas(slide_frame, bg="white", height=500)
        self.slide_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Navigation controls
        nav_frame = ttk.Frame(self.content_frame)
        nav_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(nav_frame, text="◀ Previous Slide", 
                  command=self.prev_slide).pack(side=tk.LEFT, padx=5)
        ttk.Button(nav_frame, text="Next Slide ▶", 
                  command=self.next_slide).pack(side=tk.LEFT, padx=5)
        
        # Show first slide
        self.display_slide()
        
        self.status_label.config(text="Slide View")
    
    def display_slide(self):
        """Display current slide"""
        slide_image = self.slides_manager.get_current_slide()
        
        if slide_image is not None:
            # Convert from BGR (OpenCV) to RGB
            slide_image_rgb = cv2.cvtColor(slide_image, cv2.COLOR_BGR2RGB)
            
            # Resize to fit canvas
            height = 500
            aspect_ratio = slide_image_rgb.shape[1] / slide_image_rgb.shape[0]
            width = int(height * aspect_ratio)
            
            slide_image_resized = cv2.resize(slide_image_rgb, (width, height))
            
            # Convert for Tkinter
            pil_image = Image.fromarray(slide_image_resized)
            photo = ImageTk.PhotoImage(pil_image)
            
            # Show on canvas
            self.slide_canvas.delete("all")
            self.slide_canvas.create_image(
                self.slide_canvas.winfo_width()//2,
                self.slide_canvas.winfo_height()//2,
                image=photo
            )
            self.slide_canvas.image = photo
            
            # Update info
            self.slide_info_label.config(text=self.slides_manager.get_slide_info())
    
    def next_slide(self):
        """Go to next slide"""
        self.slides_manager.next_slide()
        self.display_slide()
    
    def prev_slide(self):
        """Go to previous slide"""
        self.slides_manager.previous_slide()
        self.display_slide()
    
    def show_physics_view(self):
        """Show physics simulator"""
        self.clear_content()
        self.current_view = "physics"
        
        # Controls
        controls_frame = ttk.Frame(self.content_frame)
        controls_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(controls_frame, text="◀ Back", command=self.show_menu).pack(side=tk.LEFT, padx=5)
        ttk.Label(controls_frame, text="STATIC EQUILIBRIUM SIMULATOR", 
                 font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=20)
        
        # Message
        msg = ttk.Label(self.content_frame, 
                       text="The simulator opens in a separate window...\nUse the sliders to modify parameters and observe how forces change!",
                       font=("Arial", 11), foreground="darkblue")
        msg.pack(pady=20)
        
        # Launch button
        ttk.Button(self.content_frame, text="🚀 Launch Simulator", 
                  command=self.launch_physics_simulator).pack(pady=20)
        
        self.status_label.config(text="Physics Simulator (ready)")
    
    def launch_physics_simulator(self):
        """Launch the physics simulator"""
        # Launch in separate thread to not block UI
        thread = threading.Thread(target=self._run_physics_sim, daemon=True)
        thread.start()
        self.status_label.config(text="Physics Simulator (running)")
    
    def _run_physics_sim(self):
        """Thread for simulator"""
        simulator = EquilibrioStaticoSimulator()
        simulator.run()
    
    def show_whiteboard(self):
        """Show digital whiteboard"""
        self.clear_content()
        self.current_view = "whiteboard"
        
        # Controls
        controls_frame = ttk.Frame(self.content_frame)
        controls_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(controls_frame, text="◀ Back", command=self.show_menu).pack(side=tk.LEFT, padx=5)
        ttk.Label(controls_frame, text="DIGITAL WHITEBOARD", 
                 font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=20)
        
        # Message
        msg = ttk.Label(self.content_frame, 
                       text="The whiteboard opens in a separate window (Pygame)...\nCommands: Mouse to draw, C to clear, Q to exit",
                       font=("Arial", 11), foreground="darkblue")
        msg.pack(pady=20)
        
        # Launch button
        ttk.Button(self.content_frame, text="🎨 Open Whiteboard", 
                  command=self.launch_whiteboard).pack(pady=20)
        
        self.status_label.config(text="Digital Whiteboard (ready)")
    
    def launch_whiteboard(self):
        """Launch the digital whiteboard"""
        from whiteboard import Whiteboard
        
        thread = threading.Thread(target=self._run_whiteboard, daemon=True)
        thread.start()
        self.status_label.config(text="Digital Whiteboard (running)")
    
    def _run_whiteboard(self):
        """Thread for whiteboard"""
        from whiteboard import Whiteboard
        whiteboard = Whiteboard()
        whiteboard.run()
    
    def show_presentation_mode(self):
        """Show integrated presentation mode"""
        self.clear_content()
        self.current_view = "presentation"
        
        # Controls
        controls_frame = ttk.Frame(self.content_frame)
        controls_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(controls_frame, text="◀ Main Menu", command=self.show_menu).pack(side=tk.LEFT, padx=5)
        ttk.Label(controls_frame, text="🎬 PRESENTATION MODE", 
                 font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=20)
        
        # Main frame with 2 columns
        main_split = ttk.PanedWindow(self.content_frame, orient=tk.HORIZONTAL)
        main_split.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # LEFT: Slides
        left_frame = ttk.LabelFrame(main_split, text="📊 SLIDES", padding=10)
        main_split.add(left_frame, weight=1)
        
        self.pres_slide_canvas = tk.Canvas(left_frame, bg="white", height=400)
        self.pres_slide_canvas.pack(fill=tk.BOTH, expand=True)
        
        left_controls = ttk.Frame(left_frame)
        left_controls.pack(fill=tk.X, pady=10)
        
        ttk.Button(left_controls, text="◀", command=self.pres_prev_slide).pack(side=tk.LEFT, padx=2)
        ttk.Button(left_controls, text="▶", command=self.pres_next_slide).pack(side=tk.LEFT, padx=2)
        self.pres_slide_info = ttk.Label(left_controls, text="")
        self.pres_slide_info.pack(side=tk.LEFT, padx=10)
        
        # RIGHT: Control panel
        right_frame = ttk.LabelFrame(main_split, text="⚙️ CONTROLS", padding=10)
        main_split.add(right_frame, weight=1)
        
        # Simulator section
        ttk.Label(right_frame, text="Physics Simulator:", font=("Arial", 11, "bold")).pack(anchor=tk.W, pady=10)
        ttk.Button(right_frame, text="🚀 Launch Simulator", 
                  command=self.launch_physics_simulator).pack(fill=tk.X, pady=5)
        
        # Whiteboard section
        ttk.Label(right_frame, text="Digital Whiteboard:", font=("Arial", 11, "bold")).pack(anchor=tk.W, pady=(20, 10))
        ttk.Button(right_frame, text="🎨 Open Whiteboard", 
                  command=self.launch_whiteboard).pack(fill=tk.X, pady=5)
        
        # Info section
        ttk.Label(right_frame, text="Slide Info:", font=("Arial", 11, "bold")).pack(anchor=tk.W, pady=(20, 10))
        info_text = ttk.Label(right_frame, 
                             text="In this mode you can:\n\n1. Navigate slides\n2. Launch physics simulator\n3. Open whiteboard\n\nPerfect for recording with OBS Studio!",
                             font=("Arial", 10), foreground="darkblue", justify=tk.LEFT)
        info_text.pack(anchor=tk.W, pady=10)
        
        # Show first slide
        self.pres_display_slide()
        
        self.status_label.config(text="Presentation Mode")
    
    def pres_display_slide(self):
        """Show slide in presentation panel"""
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
        """Next slide in presentation mode"""
        self.slides_manager.next_slide()
        self.pres_display_slide()
    
    def pres_prev_slide(self):
        """Previous slide in presentation mode"""
        self.slides_manager.previous_slide()
        self.pres_display_slide()
    
    def run(self):
        """Launch the application"""
        self.root.mainloop()

def main():
    """Startup function"""
    root = tk.Tk()
    app = PhysicsVideoCreator(root)
    app.run()

if __name__ == "__main__":
    main()
