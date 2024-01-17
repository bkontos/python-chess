import pygame

class Board:
    def __init__(self, size = 800):
        self.size = size
        self.board = self.create_board()
        self.square_size = self.size // 8

    def create_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        return board
    
    def draw(self,screen):
        colors = [pygame.Color(40,102,40), pygame.Color(220, 235, 220)]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                pygame.draw.rect(screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))
