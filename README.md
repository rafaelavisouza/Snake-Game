## 🐍 Snake Game em Pygame

Este é um projeto simples do clássico jogo da cobra (Snake Game) implementado em **Python** utilizando a biblioteca **Pygame**.

-----

### 🎮 Sobre o Jogo

O objetivo do jogo é controlar a cobra verde para comer a comida vermelha que aparece aleatoriamente na tela. A cada pedaço de comida que a cobra come, ela cresce e a velocidade do jogo aumenta. O jogo termina quando a cobra colide com as bordas da tela ou consigo mesma.

<img width="906" height="657" alt="Captura de tela de 2025-11-22 11-19-07" src="https://github.com/user-attachments/assets/e66632f7-32ff-4687-b5ae-f86f869c05b7" />


-----

### 💻 Requisitos

Para rodar este jogo, você precisa ter o **Python 3** e a biblioteca **Pygame** instalados.

#### 1\. Instalar Python

Certifique-se de ter o Python 3 instalado no seu sistema.

#### 2\. Instalar Pygame

Você pode instalar o Pygame usando o `pip`, o gerenciador de pacotes do Python:

```bash
pip install pygame
```

Se estiver usando um ambiente virtual (`venv`), ative-o antes de executar o comando acima:

```bash
source venv/bin/activate
pip install pygame
```

-----


### 🕹️ Controles

O jogo é controlado pelas **teclas de seta** do teclado:

| Tecla | Ação |
| :---: | :--- |
| **↑** | Mover a cobra para **CIMA** |
| **↓** | Mover a cobra para **BAIXO** |
| **←** | Mover a cobra para **ESQUERDA** |
| **→** | Mover a cobra para **DIREITA** |

-----

### ⚙️ Detalhes da Implementação

| Variável | Descrição |
| :--- | :--- |
| `dis_width`, `dis_height` | Dimensões da tela de jogo (800x600 pixels). |
| `snake_block` | Tamanho de cada bloco da cobra e da comida (10 pixels). |
| `snake_speed` | A velocidade inicial da cobra (15 FPS), que aumenta a cada vez que a cobra come. |
| `length_of_snake` | O tamanho atual da cobra, que serve como base para calcular a pontuação. |

A pontuação é exibida na tela de **Game Over** e corresponde a `length_of_snake - 1`.
