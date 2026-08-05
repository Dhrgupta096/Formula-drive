# Dhruv's F1 Playground — 3D Interactive WebGL Simulator

An interactive, high-fidelity 3D tabletop Formula 1 model kit, customizer, and arcade driving simulation. Built using Three.js, GSAP animations, and Rapier physics.

🎮 **[PLAY LIVE NOW ON GITHUB PAGES](https://dhrgupta096.github.io/Formula-drive/)**

---

## Features

### 🔧 Kit Mode (Interactive Assembly)
*   **Blueprint Workbench**: Components are laid out on a blueprint cutting mat as individual model parts.
*   **Part Inspection**: Hovering over parts highlights them and displays their names.
*   **Smooth Assembly**: Seamless 3D animations that transition components from their disassembled state into the assembled chassis.

### 🎨 Studio Mode (Customizer)
*   **Livery Color customizer**: Update the main chassis colors with metallic paint swatches.
*   **Compound Picker**: Swap between soft (red), medium (yellow), and hard (white) tire compounds.
*   **Pedestal Orbit**: Free camera Orbit Controls to inspect the assembled car from any angle.

### 🏎️ Drive Mode (Arcade Driving Simulator)
*   **Physics Simulator**: Responsive keyboard steering, acceleration, reversing, and handbrake-drifting physics.
*   **Exhaust Particles & Drifting Sparks**: Smoke and sparks emit from rear tires during high-speed drifts.
*   **Dynamic Skid Marks**: Realistic tire tracks are rendered dynamically on the cutting mat surface.
*   **Speedometer HUD**: Real-time speed tracking, gear shifting indicator, and drift points score accumulator.
*   **Mobile Support**: Fully responsive layout with virtual on-screen joystick controllers for phone viewports.

---

## Technical Architecture

*   **Render Engine**: [Three.js](https://threejs.org/) (WebGL) with ACES Filmic Tone Mapping and shadow-mapped spotlighting.
*   **3D Assets**: Optimized low-poly glTF model kit compiled with Draco mesh compression.
*   **Physics Engine**: [Rapier 3D Physics](https://rapier.rs/) compiled with inline WebAssembly.
*   **Motion & Easing**: [GSAP (GreenSock)](https://greensock.com/) ScrollTrigger for view transition interpolations.

---

## Running Locally

To run this simulation on your local computer:

1. Clone this repository:
   ```bash
   git clone https://github.com/Dhrgupta096/Formula-drive.git
   cd Formula-drive
   ```

2. Start a local web server (for example, using Python):
   ```bash
   python3 -m http.server 8008
   ```

3. Open your browser and go to:
   **[http://localhost:8008](http://localhost:8008)**

---

## License & Credits

*   Built with the **Three.js** and **Rapier.js** communities.
*   Designed and curated by **Dhruv Gupta**.
