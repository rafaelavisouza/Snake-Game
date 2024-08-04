import pygame
import sys
import time
import random

pygame.init()  # Inicializar programa

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Tela
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game")  # Título

clock = pygame.time.Clock()

snake_block = 10  # Tamanho do bloco

font_style = pygame.font.SysFont(None, 50)

# Pontuação
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Mensagem de game over
def game_over_screen(score):
    dis.fill(black)  # Tela preta
    game_over_font = pygame.font.SysFont(None, 75)  # Fonte
    game_over_Surf = game_over_font.render("Your score is : " + str(score), True, white)  # Mensagem
    game_over_Rect = game_over_Surf.get_rect()  # Retângulo
    game_over_Rect.midtop = (dis_width / 2, dis_height / 4)  # Posição
    dis.blit(game_over_Surf, game_over_Rect)  # Desenha na tela o retângulo
    pygame.display.flip()  # Atualiza a tela
    pygame.time.wait(1500)  # 1.5s

# Mostrar pontuação
def gameLoop():
    game_over = False
    x1, y1 = dis_width / 2, dis_height / 2
    x1_change, y1_change = 0, 0
    snake_List = []
    snake_speed = 15
    length_of_snake = 1
    foodx, foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0, round(
        random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP:
                    x1_change, y1_change = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change, y1_change = 0, snake_block

        # A cobra sair da tela, o jogo acaba
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_List.append(snake_head)

        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_over = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0, round(
                random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            snake_speed = 15 + length_of_snake

        clock.tick(snake_speed)

    game_over_screen(length_of_snake - 1)
    pygame.quit()
    quit()

gameLoop()
