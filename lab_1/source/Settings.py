class Settings:
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
        self.player_amount = player_amount
        self.piece_amount = piece_amount
        # 16 is minimum, increment size is 8
        self.extra_tiles = extra_tiles
