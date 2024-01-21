import pygame

# Load images (assuming they are in the same directory)
try:
    WHITE_PAWN_IMAGE = pygame.image.load("images_for_pieces/white_pawn.png")
    BLACK_PAWN_IMAGE = pygame.image.load("images_for_pieces/black_pawn.png")
except pygame.error as e:
    print(f"Error loading image: {e}")
    raise

class Pawn:
    def __init__(self, color, position):
        self.color = color 
        self.position = position
        self.image = WHITE_PAWN_IMAGE if color == 'white' else BLACK_PAWN_IMAGE

    def get_possible_moves(self, board):
        """Calculates the possible moves for this pawn based on its current position and the board's state.
        :param board: A 2D list representing the current state of the chess board.
        :return: A list of tuples representing possible new positions (row, column).
        """
        moves = []
        direction = 1 if self.color == 'white' else -1
        start_row = 1 if self.color == 'white' else 6

        # Forward move
        forward_row = self.position[0] + direction
        if 0 <= forward_row < 8 and board[forward_row][self.position[1]] is None:
            moves.append((forward_row, self.position[1]))

            # Double move from start position
            if self.position[0] == start_row and board[forward_row][self.position[1]] is None:
                double_forward_row = self.position[0] + 2 * direction
                if board[double_forward_row][self.position[1]] is None:
                    moves.append((double_forward_row, self.position[1]))

        # Capturing moves
        for dx in [-1, 1]:
            capture_col = self.position[1] + dx
            if 0 <= capture_col < 8:
                if 0 <= forward_row < 8 and board[forward_row][capture_col] is not None:
                    if board[forward_row][capture_col].color != self.color:
                        moves.append((forward_row, capture_col))

        return moves

    def draw(self, screen, square_size):
        row, col = self.position
        x = col * square_size
        y = row * square_size
        pawn_image = pygame.transform.scale(self.image, (square_size, square_size))
        screen.blit(pawn_image, (x, y))
