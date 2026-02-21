Flappy Bird: Modular Python Engine
A physics-based 2D side-scroller built with Python and Pygame, featuring a modular architecture and a dynamic difficulty scaling algorithm.

🛠 Technical Engineering Highlights
Pygame Framework: Leverages the Pygame library for sprite management, hardware-accelerated rendering, and real-time event handling.

Object-Oriented Architecture: The project follows a strict Separation of Concerns (SoC) pattern, with distinct classes for game entities (Bird, Pipe) and environment management (World).

Dynamic Difficulty Scaling: Implemented a linear difficulty curve in world.py that reduces the obstacle gap as the player's score increases, balancing player engagement with challenge.

Collision Optimization: Utilizes optimized hitbox logic by shrinking the bird’s collision rectangle to 70% of its visual size, enhancing the user experience by making near-misses feel intentional rather than frustrating.

Centralized Configuration: All game constants, asset paths, and physics parameters are managed via settings.py for high maintainability and rapid prototyping.

📂 Project Structure
main.py: The entry point for the game loop, event handling, and rendering.

world.py: Manages the high-level game state, including pipe spawning, scoring, and level progression.

bird.py: Handles sprite animation frames, vertical physics (gravity/velocity), and collision logic.

pipe.py: Controls the generation and movement of obstacles.

settings.py: A configuration hub for screen dimensions, colors, and game constants.

assets/: Contains localized audio and sprite animation frames.

🚀 How to Run
Clone the repository:

Bash
git clone https://github.com/rizwanahmed109-beep/flappy-bird-python.git
Install dependencies:

Bash
pip install pygame
Execute the game:

Bash
python main.py