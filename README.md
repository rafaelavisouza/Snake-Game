## 🐍 Snake Game in Pygame

This is a simple project of the classic Snake Game implemented in Python using the Pygame library.

-----

### 🎮 About the Game

The objective of the game is to control the green snake to eat the red food that appears randomly on the screen. With each piece of food the snake eats, it grows, and the game speed increases. The game ends when the snake collides with the edges of the screen or with itself.

<img width="906" height="657" alt="Captura de tela de 2025-11-22 11-19-07" src="https://github.com/user-attachments/assets/e66632f7-32ff-4687-b5ae-f86f869c05b7" />


-----

### 💻 Requirements

To run this game, you need to have Python 3 and the Pygame library installed.

#### 1. Install Python

Make sure you have Python 3 installed on your system.

#### 2. Install Pygame

You can install Pygame using `pip`, the Python package manager:
```bash
pip install pygame
If you are using a virtual environment (venv), activate it before running the command above:

Bash
source venv/bin/activate
pip install pygame
```

-----


### 🕹️ Controls

The game is controlled by the keyboard arrow keys:

| Key | Action |
| :---: | :--- |
| **↑** | Move the snake UP |
| **↓** | Move the snake DOWN |
| **←** | Move the snake LEFT |
| **→** | Move the snake RIGHT |

-----

### ⚙️ Implementation Details

| Variable | Description |
| :--- | :--- |
| `dis_width`, `dis_height` | Game screen dimensions (800x600 pixels). |
| `snake_block` | Size of each snake block and food (10 pixels). |
| `snake_speed` | The initial speed of the snake (15 FPS), which increases every time the snake eats. |
| `length_of_snake` | The current length of the snake, which serves as the basis for calculating the score. |

The score is displayed on the Game Over screen and corresponds to length_of_snake - 1.
