"""
Modulo di Fisica Interattivo - Equilibrio Statico di un Corpo
Simula un corpo rigido su un piano inclinato con forze visibili
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Slider
import numpy as np

class EquilibrioStaticoSimulator:
    def __init__(self):
        """Inizializza il simulatore di equilibrio statico"""
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        plt.subplots_adjust(bottom=0.35)
        
        # Parametri fisici
        self.mass = 10  # kg
        self.angle = 30  # gradi
        self.mu_s = 0.5  # coefficiente attrito statico
        self.g = 9.8  # accelerazione gravita
        
        # Etichette e testi
        self.title = self.ax.set_title("Equilibrio Statico di un Corpo su Piano Inclinato", fontsize=14, fontweight='bold')
        
        # Slider per controllare parametri
        self.setup_sliders()
        
        # Colori
        self.color_weight = 'red'
        self.color_normal = 'green'
        self.color_friction = 'blue'
        self.color_components = 'orange'
        
    def setup_sliders(self):
        """Crea gli slider per controllare i parametri"""
        # Slider angolo
        ax_angle = plt.axes([0.2, 0.25, 0.6, 0.03])
        self.slider_angle = Slider(ax_angle, 'Angolo (°)', 0, 80, valinit=30, color='blue')
        self.slider_angle.on_changed(self.update)
        
        # Slider massa
        ax_mass = plt.axes([0.2, 0.20, 0.6, 0.03])
        self.slider_mass = Slider(ax_mass, 'Massa (kg)', 1, 50, valinit=10, color='red')
        self.slider_mass.on_changed(self.update)
        
        # Slider attrito
        ax_friction = plt.axes([0.2, 0.15, 0.6, 0.03])
        self.slider_friction = Slider(ax_friction, 'Attrito μ_s', 0, 1.0, valinit=0.5, color='green')
        self.slider_friction.on_changed(self.update)
        
        # Testo informazioni
        self.info_text = self.fig.text(0.1, 0.08, '', fontsize=10, family='monospace')
        self.equilibrium_text = self.fig.text(0.1, 0.02, '', fontsize=12, fontweight='bold', color='darkgreen')
    
    def update(self, val):
        """Aggiorna la simulazione quando i slider cambiano"""
        self.angle = self.slider_angle.val
        self.mass = self.slider_mass.val
        self.mu_s = self.slider_friction.val
        
        self.draw_simulation()
    
    def draw_simulation(self):
        """Disegna la simulazione con tutte le forze"""
        self.ax.clear()
        
        # Angolo in radianti
        theta = np.radians(self.angle)
        
        # Calcoli delle forze
        weight = self.mass * self.g  # Peso in N
        normal_force = weight * np.cos(theta)  # Forza normale
        component_parallel = weight * np.sin(theta)  # Componente parallela
        friction_max = self.mu_s * normal_force  # Attrito massimo
        
        # Determina se il corpo è in equilibrio
        is_equilibrium = component_parallel <= friction_max
        
        # Disegna il piano inclinato
        self.draw_inclined_plane(theta)
        
        # Disegna il corpo
        body_x = 5
        body_y = 5 * np.tan(theta) + 0.5
        self.draw_body(body_x, body_y, theta)
        
        # Disegna le forze
        force_scale = 0.01  # Scala per visualizzare le forze
        
        # Punto di applicazione delle forze (centro del corpo)
        force_origin = np.array([body_x, body_y])
        
        # 1. Peso (verticale verso il basso)
        weight_vector = np.array([0, -weight * force_scale])
        self.draw_arrow(force_origin, weight_vector, self.color_weight, 'Peso (mg)', 3)
        
        # 2. Forza Normale (perpendicolare al piano)
        normal_direction = np.array([-np.sin(theta), np.cos(theta)])
        normal_vector = normal_direction * normal_force * force_scale
        self.draw_arrow(force_origin, normal_vector, self.color_normal, 'N (Normale)', 2.5)
        
        # 3. Attrito (parallelo al piano, opposto al moto)
        if component_parallel > 0:
            friction_direction = np.array([-np.cos(theta), -np.sin(theta)])
        else:
            friction_direction = np.array([np.cos(theta), np.sin(theta)])
        friction_force = min(component_parallel, friction_max)
        friction_vector = friction_direction * friction_force * force_scale
        self.draw_arrow(force_origin, friction_vector, self.color_friction, f'f = {friction_force:.2f} N', 2.5)
        
        # 4. Componenti del peso (linee tratteggiate)
        parallel_component = np.array([np.cos(theta), np.sin(theta)]) * component_parallel * force_scale
        perpendicular_component = np.array([-np.sin(theta), np.cos(theta)]) * (weight * np.cos(theta)) * force_scale
        
        self.ax.arrow(force_origin[0], force_origin[1], parallel_component[0], parallel_component[1],
                     head_width=0.2, head_length=0.1, fc=self.color_components, ec=self.color_components,
                     linestyle='--', linewidth=1.5, alpha=0.6)
        
        # Testo informazioni
        info_text = f"""
ANALISI DELLE FORZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Massa (m):           {self.mass:.1f} kg
Angolo (θ):          {self.angle:.1f}°
Coefficiente attrito (μ_s): {self.mu_s:.2f}

FORZE:
─────────────────────────────
Peso (W = mg):       {weight:.2f} N
Componente ∥:        {component_parallel:.2f} N
Componente ⊥:        {weight * np.cos(theta):.2f} N
Forza Normale (N):   {normal_force:.2f} N
Attrito massimo:     {friction_max:.2f} N
Attrito effettivo:   {min(component_parallel, friction_max):.2f} N
        """
        
        self.info_text.set_text(info_text)
        
        # Testo equilibrio
        if is_equilibrium:
            equilibrium_info = f"✓ EQUILIBRIO STATICO MANTENUTO (Attrito ≥ Componente parallela)"
            color_eq = 'darkgreen'
        else:
            equilibrium_info = f"✗ CORPO SCIVOLA (Attrito < Componente parallela) - Accelerazione: {(component_parallel - friction_max) / self.mass:.2f} m/s²"
            color_eq = 'darkred'
        
        self.equilibrium_text.set_text(equilibrium_info)
        self.equilibrium_text.set_color(color_eq)
        
        # Configurazione assi
        self.ax.set_xlim(-2, 14)
        self.ax.set_ylim(-2, 12)
        self.ax.set_aspect('equal')
        self.ax.grid(True, alpha=0.3)
        self.ax.set_xlabel('Distanza (m)', fontsize=10)
        self.ax.set_ylabel('Altezza (m)', fontsize=10)
        self.ax.set_title(f"Equilibrio Statico - θ={self.angle:.0f}°, m={self.mass:.0f}kg, μ_s={self.mu_s:.2f}", 
                         fontsize=14, fontweight='bold')
        
        # Legenda
        self.ax.legend(loc='upper right', fontsize=9)
        
        plt.draw()
    
    def draw_inclined_plane(self, theta):
        """Disegna il piano inclinato"""
        x_plane = np.array([0, 12])
        y_plane = x_plane * np.tan(theta)
        self.ax.plot(x_plane, y_plane, 'k-', linewidth=3, label='Piano inclinato')
        
        # Ombra sotto il piano
        self.ax.fill_between(x_plane, y_plane, -1, alpha=0.1, color='gray')
    
    def draw_body(self, x, y, theta):
        """Disegna il corpo come un rettangolo"""
        from matplotlib.transforms import Affine2D
        
        # Dimensioni del corpo
        width = 1.0
        height = 0.5
        
        # Crea il rettangolo
        rect = patches.Rectangle((x - width/2, y - height/2), width, height,
                                 linewidth=2, edgecolor='black', facecolor='lightblue', alpha=0.7)
        
        # Ruota il rettangolo
        transform = Affine2D().rotate_around(x, y, theta) + self.ax.transData
        rect.set_transform(transform)
        
        self.ax.add_patch(rect)
        
        # Centro di massa
        self.ax.plot(x, y, 'ko', markersize=8, label='Centro di massa')
    
    def draw_arrow(self, origin, vector, color, label, linewidth=2):
        """Disegna una freccia rappresentante una forza"""
        self.ax.arrow(origin[0], origin[1], vector[0], vector[1],
                     head_width=0.25, head_length=0.15, fc=color, ec=color,
                     linewidth=linewidth, label=label)
    
    def run(self):
        """Avvia la simulazione interattiva"""
        print("\n=== SIMULATORE EQUILIBRIO STATICO ===")
        print("Usa gli slider per modificare:")
        print("  - Angolo del piano inclinato")
        print("  - Massa del corpo")
        print("  - Coefficiente di attrito statico")
        print("\nOsserva come cambiano le forze!")
        print("====================================\n")
        
        self.draw_simulation()
        plt.show()

if __name__ == "__main__":
    simulator = EquilibrioStaticoSimulator()
    simulator.run()
