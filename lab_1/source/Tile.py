class Tile:
    """
    Class representing a tile on the game board, which may hold a player piece.

    Attributes:
    ----------
    tile_coords : tuple
        Coordinates of the tile on the board.
    tile_standing_player : int or None
        ID of the player whose piece is currently on the tile, if any.
    tile_standing_piece : int or None
        ID of the piece currently on the tile, if any.
    tile_ID : int
        Unique identifier for the tile.
    is_house : bool
        Indicates whether the tile is part of a player's house.
    """
    tile_coords = ()
    tile_standing_player = None
    tile_standing_piece = None
    tile_ID = None

    def __init__(self, tile_ID, cords, is_house):
        """
        Initializes a Tile object with coordinates, ID, and house status.

        Parameters:
        ----------
        tile_ID : int
            Unique identifier for the tile.
        cords : tuple
            (x, y) coordinates of the tile on the board.
        is_house : bool
            True if the tile is part of a player's house, False otherwise.
        """
        self.tile_coords = cords
        self.tile_ID = tile_ID
        self.is_house = is_house
