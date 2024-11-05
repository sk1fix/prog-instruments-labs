from Piece import *


class Player:
    player_pieces = []
    piece_color = None
    house_color = None
    start_tile_color = None

    def __init__(self, piece_color, house_color, start_tile_color, piece_amount, piece_size):
        self.player_pieces = []
        self.piece_color = piece_color
        self.house_color = house_color
        self.start_tile_color = start_tile_color
        for this_piece in range(piece_amount):
            piece = Piece(self.piece_color, piece_size, this_piece)
            self.player_pieces.append(piece)
