class Settings:
    """
    Class representing game settings, including player configuration and visual properties.

    Attributes:
    ----------
    player_amount : int
        Number of players in the game.
    piece_amount : int
        Number of pieces each player has.
    extra_tiles : int
        Additional tiles on the game board beyond the minimum.
    piece_colors : list[tuple]
        List of RGB color tuples representing each player's piece color.
    house_colors : list[tuple]
        List of RGB color tuples representing each player's house color.
    start_tile_colors : list[tuple]
        List of RGB color tuples representing the color of each player's start tile.
    player_names : list[str]
        List of player names, initially empty.
    """
    player_amount = None
    piece_amount = None
    extra_tiles = None
    piece_colors = [(68, 85, 242), (235, 235, 52),
                    (40, 237, 47), (240, 38, 38)]
    house_colors = [(43, 55, 166), (153, 153, 35),
                    (22, 130, 26), (148, 24, 24)]
    start_tile_colors = [(103, 114, 219), (214, 214, 103),
                         (106, 189, 109), (186, 95, 95)]

    player_names = ["", "", "", ""]

    def __init__(self, player_amount, piece_amount, extra_tiles):
        """
        Initializes the Settings object with player and tile configurations.

        Parameters:
        ----------
        player_amount : int
            Number of players in the game.
        piece_amount : int
            Number of pieces each player has.
        extra_tiles : int
            Number of additional tiles added to the board, with a minimum of 16 and an increment of 8.
        """
        self.player_amount = player_amount
        self.piece_amount = piece_amount
        # 16 is minimum, increment size is 8
        self.extra_tiles = extra_tiles
