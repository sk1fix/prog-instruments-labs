class Tile:
    tile_coords = ()
    tile_standing_player = None
    tile_standing_piece = None
    tile_ID = None

    def __init__(self, tile_ID, cords, is_house):
        self.tile_coords = cords
        self.tile_ID = tile_ID
        self.is_house = is_house
