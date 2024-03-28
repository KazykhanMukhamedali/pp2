import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
x, y = 320, 240

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: # клавиша нажата, активатор события с клавиатуры
            
            if event.key == pygame.K_LEFT:
                x -= 20
            elif event.key == pygame.K_RIGHT:
                x += 20
            elif event.key == pygame.K_UP:
                y -= 20
            elif event.key == pygame.K_DOWN:
                y += 20

    screen.fill((255, 255, 255))  # заполнить экран белым
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)  # рисую круг

    pygame.display.flip()  # флип
