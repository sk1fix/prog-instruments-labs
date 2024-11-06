from Piece import Piece


class Player:
    """
    Class representing a player in the game, containing pieces and their attributes.

    Attributes:
    ----------
    player_pieces : list[Piece]
        List of the player's pieces.
    piece_color : str
        Color of the player's pieces.
    house_color : str
        Color of the player's end house.
    start_tile_color : str
        Color of the starting tile for the player's pieces.
    """
    player_pieces = []
    piece_color = None
    house_color = None
    start_tile_color = None

    def __init__(self, piece_color, house_color, start_tile_color, piece_amount, piece_size):
        """
        Initializes the Player object, creating pieces and setting colors.

        Parameters:
        ----------
        piece_color : str
            Color assigned to the player's pieces.
        house_color : str
            Color of the player's end house.
        start_tile_color : str
            Color of the player's starting tile.
        piece_amount : int
            Number of pieces assigned to the player.
        piece_size : int
            Size of each piece.
        """
        self.player_pieces = []
        self.piece_color = piece_color
        self.house_color = house_color
        self.start_tile_color = start_tile_color
        for this_piece in range(piece_amount):
            piece = Piece(self.piece_color, piece_size, this_piece)
            self.player_pieces.append(piece)
