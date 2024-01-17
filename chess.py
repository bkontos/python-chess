# Simple 2 player game of chess using pygame to practice Object Oriented Programming in Python
import pygame
from board import Board


pygame.init()
size = 800
screen = pygame.display.set_mode((size, size))
chessboard = Board(size)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    chessboard.draw(screen)

    pygame.display.flip()

    clock.tick(60)
pygame.quit()
