# Physics Video Creator

Integrated educational application to create educational videos for YouTube.

## 📚 Description

**Physics Video Creator** is a complete tool for producing educational videos on physics topics. It integrates:

- 📊 **Slide Presenter** - Viewing and navigation of PowerPoint slides
- ⚙️ **Interactive Physics Simulator** - Educational app on static equilibrium with sliders
- 🎨 **Digital Whiteboard** - Freehand drawing for annotations
- 🎬 **Presentation Mode** - Integration of all elements

## 🎯 Case Study: Static Equilibrium

The application includes a complete simulator for the static equilibrium of a body on an inclined plane, with:

- Dynamic visualization of all forces (weight, normal, friction)
- Interactive sliders to control:
  - Angle of inclined plane (0-80°)
  - Mass of body (1-50 kg)
  - Coefficient of static friction (0-1.0)
- Automatic equilibrium analysis
- Acceleration calculation in case of slipping

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip

### Step 1: Clone the repository
```bash
git clone https://github.com/signorig/physics-video-creator.git
cd physics-video-creator
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Launch the application
```bash
python app_main.py
```

## 📖 Usage

### 1. Main Menu
On startup, you will see 4 options:

#### 📊 SLIDE PRESENTER
- View presentation slides
- Navigate with "Previous Slide" and "Next Slide" buttons
- Sample slides are pre-loaded in `sample_slides/`

#### ⚙️ PHYSICS SIMULATOR
- Opens an interactive Matplotlib application
- **Angle Slider**: Modify the plane's inclination (0-80°)
- **Mass Slider**: Modify the body's mass (1-50 kg)
- **Friction Slider**: Modify the static friction coefficient (0-1.0)
- Watch how forces change in real time
- The app automatically shows if the body is in static equilibrium

#### 🎨 DIGITAL WHITEBOARD
- Opens a Pygame window with a white whiteboard
- **Mouse**: Draw freely
- **Keys 1-4**: Change color (Black, Red, Blue, Green)
- **+/-**: Increase/Decrease brush thickness
- **C**: Clear everything
- **Q**: Exit

#### 🎬 PRESENTATION MODE
- Integrated layout with 2 panels
- **Left**: Slides with navigation controls
- **Right**: Buttons to launch simulator and whiteboard
- **Recommended use**: Use this mode to record video

## 📹 How to Record a Video

### Preparation
1. Launch the app: `python app_main.py`
2. Select "PRESENTATION MODE"
3. Open OBS Studio (https://obsproject.com/)

### OBS Studio Configuration
1. **Add Source** → **Window Capture** → Select Python window
2. **Audio**: Configure microphone for narration
3. **Layout**: Adjust resolution for YouTube (1920x1080 recommended)

### Recording
1. Start recording in OBS
2. Navigate through slides in the app
3. When needed, launch the physics simulator (appears above slides)
4. When needed, open the digital whiteboard for annotations
5. Explain while navigating
6. Stop recording when finished

### Post-Production
- Process video in an editor (DaVinci Resolve, Adobe Premiere, OpenShot)
- Add titles, background music, effects
- Export and upload to YouTube

## 📁 File Structure

```
physics-video-creator/
├── app_main.py              # Main application
├── interactive_physics.py    # Physics simulator
├── whiteboard.py            # Digital whiteboard
├── slides_manager.py        # Slide manager
├── requirements.txt         # Python dependencies
├── sample_slides/           # Sample slides folder
│   ├── slide_00.png
│   ├── slide_01.png
│   ├── slide_02.png
│   ├── slide_03.png
│   └── slide_04.png
└── README.md               # This file
```

## 🎓 Topics Covered

### Static Equilibrium
The sample slides cover:
1. Definition of static equilibrium
2. Forces on inclined plane (decomposition)
3. Coefficient of friction (static vs kinetic)
4. Equilibrium condition: μ_s ≥ tan(θ)
5. Practical applications

### Applied Physics
The simulator shows:
- ✓ Equilibrium maintained when: `f ≥ W·sin(θ)`
- ✗ Body slipping when: `f < W·sin(θ)`
- Slipping acceleration: `a = (W·sin(θ) - f) / m`

## 🛠️ Customization

### Adding Custom Slides
1. Prepare your slides as PNG/JPG images
2. Put files in a folder (e.g., `my_slides/`)
3. In `app_main.py`, modify:
   ```python
   self.slides_manager.load_slides_from_folder("my_slides/")
   ```

### Modifying Physics Parameters
Edit `interactive_physics.py`:
- `self.mass` = initial mass (kg)
- `self.angle` = initial angle (°)
- `self.mu_s` = initial friction coefficient
- Slider range in `setup_sliders()` functions

### Customizing the Whiteboard
Edit `whiteboard.py`:
- Custom colors in `self.color_*` section
- Default brush thickness: `self.brush_size`
- Window dimensions: `__init__` parameters

## 📊 Advanced Features

### Automatic Analysis
The simulator automatically calculates:
- Weight components (parallel and perpendicular)
- Normal force and maximum friction
- Equilibrium state
- Acceleration in case of slipping

### Physics Visualization
- Force vectors in scale
- Decomposed components (dashed line)
- Color coding for forces:
  - 🔴 Red = Weight
  - 🟢 Green = Normal Force
  - 🔵 Blue = Friction
  - 🟠 Orange = Components

## 🐛 Troubleshooting

### Simulator won't open
- Verify matplotlib is installed: `pip install matplotlib`
- Try launching from terminal to see errors: `python interactive_physics.py`

### Whiteboard not working
- Check Pygame: `pip install pygame`
- Make sure you have a display available

### Slides won't load
- Verify the `sample_slides/` folder exists
- Check read permissions on PNG files

## 📝 License

MIT License - Free for educational and commercial use

## 👨‍🏫 For Teachers

This tool was created to facilitate interactive teaching:

- **Engagement**: Students immediately see physics in action
- **Interactivity**: You can change parameters during the lesson
- **Recording**: Perfect for remote lessons and archives
- **Extensibility**: Easily adaptable to other physics topics

## 🤝 Contributions

You are welcome to suggest improvements! Examples:
- New physics simulators
- Additional slide themes
- Interface improvements
- Translations to other languages

---

**Created for modern and interactive physics education** 🎓
