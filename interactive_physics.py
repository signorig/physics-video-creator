"""
Interactive Physics Module - Static Equilibrium of a Body
Simulates a rigid body on an inclined plane with visible forces
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Slider
import numpy as np

class EquilibrioStaticoSimulator:
    def __init__(self):
        """Initialize the static equilibrium simulator"""
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        plt.subplots_adjust(bottom=0.35)
        
        # Physics parameters
        self.mass = 10  # kg
        self.angle = 30  # degrees
        self.mu_s = 0.5  # static friction coefficient
        self.g = 9.8  # gravity acceleration
        
        # Labels and text
        self.title = self.ax.set_title("Static Equilibrium of a Body on Inclined Plane", fontsize=14, fontweight='bold')
        
        # Sliders to control parameters
        self.setup_sliders()
        
        # Colors
        self.color_weight = 'red'
        self.color_normal = 'green'
        self.color_friction = 'blue'
        self.color_components = 'orange'
        
    def setup_sliders(self):
        """Create sliders to control parameters"""
        # Angle slider
        ax_angle = plt.axes([0.2, 0.25, 0.6, 0.03])
        self.slider_angle = Slider(ax_angle, 'Angle (degrees)', 0, 80, valinit=30, color='blue')
        self.slider_angle.on_changed(self.update)
        
        # Mass slider
        ax_mass = plt.axes([0.2, 0.20, 0.6, 0.03])
        self.slider_mass = Slider(ax_mass, 'Mass (kg)', 1, 50, valinit=10, color='red')
        self.slider_mass.on_changed(self.update)
        
        # Friction slider
        ax_friction = plt.axes([0.2, 0.15, 0.6, 0.03])
        self.slider_friction = Slider(ax_friction, 'Friction μ_s', 0, 1.0, valinit=0.5, color='green')
        self.slider_friction.on_changed(self.update)
        
        # Information text
        self.info_text = self.fig.text(0.1, 0.08, '', fontsize=10, family='monospace')
        self.equilibrium_text = self.fig.text(0.1, 0.02, '', fontsize=12, fontweight='bold', color='darkgreen')
    
    def update(self, val):
        """Update simulation when sliders change"""
        self.angle = self.slider_angle.val
        self.mass = self.slider_mass.val
        self.mu_s = self.slider_friction.val
        
        self.draw_simulation()
    
    def draw_simulation(self):
        """Draw the simulation with all forces"""
        self.ax.clear()
        
        # Angle in radians
        theta = np.radians(self.angle)
        
        # Force calculations
        weight = self.mass * self.g  # Weight in N
        normal_force = weight * np.cos(theta)  # Normal force
        component_parallel = weight * np.sin(theta)  # Parallel component
        friction_max = self.mu_s * normal_force  # Maximum friction
        
        # Determine if body is in equilibrium
        is_equilibrium = component_parallel <= friction_max
        
        # Draw the inclined plane
        self.draw_inclined_plane(theta)
        
        # Draw the body
        body_x = 5
        body_y = 5 * np.tan(theta) + 0.5
        self.draw_body(body_x, body_y, theta)
        
        # Draw forces
        force_scale = 0.01  # Scale for visualizing forces
        
        # Force application point (center of mass)
        force_origin = np.array([body_x, body_y])
        
        # 1. Weight (vertical downward)
        weight_vector = np.array([0, -weight * force_scale])
        self.draw_arrow(force_origin, weight_vector, self.color_weight, 'Weight (mg)', 3)
        
        # 2. Normal Force (perpendicular to plane)
        normal_direction = np.array([-np.sin(theta), np.cos(theta)])
        normal_vector = normal_direction * normal_force * force_scale
        self.draw_arrow(force_origin, normal_vector, self.color_normal, 'N (Normal)', 2.5)
        
        # 3. Friction (parallel to plane, opposite to motion)
        if component_parallel > 0:
            friction_direction = np.array([-np.cos(theta), -np.sin(theta)])
        else:
            friction_direction = np.array([np.cos(theta), np.sin(theta)])
        friction_force = min(component_parallel, friction_max)
        friction_vector = friction_direction * friction_force * force_scale
        self.draw_arrow(force_origin, friction_vector, self.color_friction, f'f = {friction_force:.2f} N', 2.5)
        
        # 4. Weight components (dashed lines)
        parallel_component = np.array([np.cos(theta), np.sin(theta)]) * component_parallel * force_scale
        perpendicular_component = np.array([-np.sin(theta), np.cos(theta)]) * (weight * np.cos(theta)) * force_scale
        
        self.ax.arrow(force_origin[0], force_origin[1], parallel_component[0], parallel_component[1],
                     head_width=0.2, head_length=0.1, fc=self.color_components, ec=self.color_components,
                     linestyle='--', linewidth=1.5, alpha=0.6)
        
        # Information text
        info_text = f"""
FORCE ANALYSIS
_______________________________________________________________
Mass (m):                   {self.mass:.1f} kg
Angle (θ):                  {self.angle:.1f}°
Static Friction Coefficient (μ_s): {self.mu_s:.2f}

FORCES:
_______________________________________________________________
Weight (W = mg):            {weight:.2f} N
Parallel Component:         {component_parallel:.2f} N
Perpendicular Component:    {weight * np.cos(theta):.2f} N
Normal Force (N):           {normal_force:.2f} N
Maximum Friction:           {friction_max:.2f} N
Actual Friction:            {min(component_parallel, friction_max):.2f} N
        """
        
        self.info_text.set_text(info_text)
        
        # Equilibrium text
        if is_equilibrium:
            equilibrium_info = f"✓ STATIC EQUILIBRIUM MAINTAINED (Friction ≥ Parallel Component)"
            color_eq = 'darkgreen'
        else:
            equilibrium_info = f"✗ BODY SLIPPING (Friction < Parallel Component) - Acceleration: {(component_parallel - friction_max) / self.mass:.2f} m/s²"
            color_eq = 'darkred'
        
        self.equilibrium_text.set_text(equilibrium_info)
        self.equilibrium_text.set_color(color_eq)
        
        # Axis configuration
        self.ax.set_xlim(-2, 14)
        self.ax.set_ylim(-2, 12)
        self.ax.set_aspect('equal')
        self.ax.grid(True, alpha=0.3)
        self.ax.set_xlabel('Distance (m)', fontsize=10)
        self.ax.set_ylabel('Height (m)', fontsize=10)
        self.ax.set_title(f"Static Equilibrium - θ={self.angle:.0f}°, m={self.mass:.0f}kg, μ_s={self.mu_s:.2f}", 
                         fontsize=14, fontweight='bold')
        
        # Legend
        self.ax.legend(loc='upper right', fontsize=9)
        
        plt.draw()
    
    def draw_inclined_plane(self, theta):
        """Draw the inclined plane"""
        x_plane = np.array([0, 12])
        y_plane = x_plane * np.tan(theta)
        self.ax.plot(x_plane, y_plane, 'k-', linewidth=3, label='Inclined Plane')
        
        # Shadow under the plane
        self.ax.fill_between(x_plane, y_plane, -1, alpha=0.1, color='gray')
    
    def draw_body(self, x, y, theta):
        """Draw the body as a rectangle"""
        from matplotlib.transforms import Affine2D
        
        # Body dimensions
        width = 1.0
        height = 0.5
        
        # Create rectangle
        rect = patches.Rectangle((x - width/2, y - height/2), width, height,
                                 linewidth=2, edgecolor='black', facecolor='lightblue', alpha=0.7)
        
        # Rotate rectangle
        transform = Affine2D().rotate_around(x, y, theta) + self.ax.transData
        rect.set_transform(transform)
        
        self.ax.add_patch(rect)
        
        # Center of mass
        self.ax.plot(x, y, 'ko', markersize=8, label='Center of Mass')
    
    def draw_arrow(self, origin, vector, color, label, linewidth=2):
        """Draw an arrow representing a force"""
        self.ax.arrow(origin[0], origin[1], vector[0], vector[1],
                     head_width=0.25, head_length=0.15, fc=color, ec=color,
                     linewidth=linewidth, label=label)
    
    def run(self):
        """Launch the interactive simulation"""
        print("\n=== STATIC EQUILIBRIUM SIMULATOR ===")
        print("Use the sliders to modify:")
        print("  - Inclination angle of the plane")
        print("  - Mass of the body")
        print("  - Static friction coefficient")
        print("\nObserve how the forces change!")
        print("====================================\n")
        
        self.draw_simulation()
        plt.show()

if __name__ == "__main__":
    simulator = EquilibrioStaticoSimulator()
    simulator.run()
