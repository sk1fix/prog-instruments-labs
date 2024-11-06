from Tile import Tile


class PlayField:
    """
    Class representing the game board, including field tiles, start and end houses, and decorations.

    Attributes:
    ----------
    field_tiles : list[Tile]
        List of tiles on the playing field.
    canvas_size : tuple
        Size of the canvas in terms of tiles (width, height).
    dot_size : int
        Size of each tile in pixels.
    field_in_crement : int
        Increment used for field configuration.
    field_min_size : int
        Minimum size of the playing field.
    canvas_min_size : int
        Minimum size of the canvas.
    border : int
        Border size for the playing field.
    color : str
        Color of the playing field.
    start_houses : list[list[Tile]]
        Lists of tiles representing each player's starting houses.
    end_houses : list[list[Tile]]
        Lists of tiles representing each player's end houses.
    start_tile_ids : list[int]
        IDs of starting tiles on the board.
    decoration : list[tuple]
        List of coordinates for decorative elements.
    """
    field_tiles = []
    canvas_size = (5, 5)
    dot_size = 70
    field_in_crement = 8
    field_min_size = 16
    canvas_min_size = 5
    border = 2
    color = "white"

    start_houses = [[], [], [], []]
    end_houses = [[], [], [], []]
    start_tile_ids = []
    decoration = []

    def generate_field(self, extra_tiles, screen_size):
        """
        Generates the playing field, start and end houses, and decorations.

        Parameters:
        ----------
        extra_tiles : int
            Additional tiles to add around the basic field size.
        screen_size : int
            Screen size in pixels, used to calculate tile sizes.
        """
        canvas_size = self.canvas_min_size + (extra_tiles * 2) + self.border
        self.dot_size = (screen_size / canvas_size) - \
            ((screen_size / canvas_size) / 7)
        self.canvas_size = (canvas_size + 1, canvas_size)
        center = (canvas_size / 2) - 0.5
        right_list = []
        left_list = []

        for x in range(canvas_size):
            for y in range(canvas_size):
                self.decoration.append((x, y))

        # generate playing field in the right order and write down the tiles into a list
        for x in range(2 + extra_tiles):
            right_list.append((center + 1, center + 2 + extra_tiles - x))
            left_list.append((center - 1, center - 2 - extra_tiles + x))

        for x in range(1 + extra_tiles):
            right_list.append((center + 2 + x, center + 1))
            left_list.append((center - 2 - x, center - 1))

        right_list.append((center + 2 + extra_tiles, center))
        left_list.append((center - 2 - extra_tiles, center))

        for x in range(2 + extra_tiles):
            right_list.append((center + 2 + extra_tiles - x, center - 1))
            left_list.append((center - 2 - extra_tiles + x, center + 1))

        for x in range(1 + extra_tiles):
            right_list.append((center + 1, center - 2 - x))
            left_list.append((center - 1, center + 2 + x))

        right_list.append((center, center - 2 - extra_tiles))
        left_list.append((center, center + 2 + extra_tiles))

        full_list = right_list + left_list
        for i in range(len(full_list)):
            tile = Tile(i, full_list[i], False)
            self.field_tiles.append(tile)

        # create tiles for end houses and put them in a list
        for i in range(extra_tiles + 1):
            end_house_tuples1 = (center, center + extra_tiles + 1 - i)
            end_house_tuples2 = (center, center - extra_tiles - 1 + i)
            end_house_tuples3 = (center + extra_tiles + 1 - i, center)
            end_house_tuples4 = (center - extra_tiles - 1 + i, center)

            tile1 = Tile(i, end_house_tuples1, True)
            tile2 = Tile(i, end_house_tuples2, True)
            tile3 = Tile(i, end_house_tuples3, True)
            tile4 = Tile(i, end_house_tuples4, True)

            self.end_houses[0].append(tile1)
            self.end_houses[1].append(tile2)
            self.end_houses[2].append(tile3)
            self.end_houses[3].append(tile4)

        # create tiles for starting houes in a grid and put them in a list
        for y in range(1 + int(((extra_tiles / 2) + 0.5))):
            for x in range(1 + int(((extra_tiles / 2) + 0.5))):
                start_houses1 = (canvas_size - 2 - y, canvas_size - 2 - x)
                start_houses2 = (1 + y, 1 + x)
                start_houses3 = (canvas_size - 2 - y, 1 + x)
                start_houses4 = (1 + y, canvas_size - 2 - x)

                tile1 = Tile(1, start_houses1, True)
                tile2 = Tile(1, start_houses2, True)
                tile3 = Tile(1, start_houses3, True)
                tile4 = Tile(1, start_houses4, True)

                self.start_houses[0].append(tile1)
                self.start_houses[1].append(tile2)
                self.start_houses[2].append(tile3)
                self.start_houses[3].append(tile4)

        # put the IDs of starting tiles into a list
        starting_tiles_division = int(len(self.field_tiles) / 4)
        for i in range(len(self.field_tiles)):
            self.start_tile_ids.append(self.field_tiles[i].tile_ID)
            self.start_tile_ids.append(
                self.field_tiles[starting_tiles_division * 2].tile_ID)
            self.start_tile_ids.append(
                self.field_tiles[starting_tiles_division * 1].tile_ID)
            self.start_tile_ids.append(
                self.field_tiles[starting_tiles_division * 3].tile_ID)
