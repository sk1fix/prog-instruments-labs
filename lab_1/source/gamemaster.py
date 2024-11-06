import random

import turtle as t

from Settings import Settings
from Renderer import Renderer
from PlayField import PlayField
from Player import Player
from constants import GAMESTATE_AWAIT, MOVESTATE_SUCCESS, MOVESTATE_OUTOFBOUNDS, MOVESTATE_TILEOCCUPIED


win = t.Screen()
canvas = win.getcanvas()
root = canvas.winfo_toplevel()
root.resizable(False, False)
window_size = canvas.winfo_screenheight() - 210
win.setup(window_size, window_size + 90)
t.colormode(255)
bgcolor = (128, 128, 128)
win.bgcolor(bgcolor)

font_size_factor = 40
game_font = ('Arial', int(window_size / font_size_factor), 'normal')


def recreate_screen():
    """
    Clears and reinitializes the game screen.
    """
    t.Screen().clear()
    t.colormode(255)
    win.bgcolor(bgcolor)


def reset_state():
    """
    Resets the game state and variables to their default values.
    """
    GameMaster.settings = None
    GameMaster.playing_field = None

    GameMaster.current_game_state = 1
    GameMaster.lenght_of_travel = 0
    GameMaster.players = []
    GameMaster.player_choice = 0
    GameMaster.piece_choice = 0
    GameMaster.roll = 0
    GameMaster.at_tempt = 0
    GameMaster.in_menu = True
    GameMaster.state_text = ""


class GameMaster:
    """
    Main class for managing the game.

    Attributes:
    ----------
    settings : Settings
        Game settings, including the number of players, pieces, and additional tiles.
    playing_field : PlayField
        The game board object.
    current_game_state : int
        The current status of the game.
    lenght_of_travel : int
        Length of the path for pieces on the game board.
    players : list[Player]
        List of players in the game.
    player_choice : int
        Index of the current player.
    piece_choice : int
        Index of the selected piece.
    roll : int
        Current roll value.
    at_tempt : int
        Counter for attempt tracking.
    in_menu : bool
        Indicates if the game is currently in the menu.
    state_text : str
        Text to display the current game state.
    """
    settings = None
    playing_field = None

    current_game_state = 1

    lenght_of_travel = 0
    players = []
    player_choice = 0
    piece_choice = 0
    roll = 0
    at_tempt = 0
    in_menu = True

    state_text = ""

    def __init__(self, player_amount, piece_amount, extra_tiles):
        """
        Initializes the GameMaster class, sets up the game field, and prepares players.

        Parameters:
        ----------
        player_amount : int
            The number of players in the game.
        piece_amount : int
            The number of pieces each player has.
        extra_tiles : int
            Additional tiles on the game board.
        """
        t.tracer(False)
        self.settings = Settings(player_amount, piece_amount, extra_tiles)
        self.playing_field = PlayField()

        self.playing_field.generate_field(
            self.settings.extra_tiles, window_size)
        self.lenght_of_travel = len(self.playing_field.field_tiles)
        win.setworldcoordinates(
            0, 0, self.playing_field.canvas_size[1], self.playing_field.canvas_size[0])

        for i in range(len(self.playing_field.decoration)):
            Renderer().render((102, 102, 102),
                              self.playing_field.decoration[i], self.playing_field.dot_size, "plus")

        for i in range(self.settings.player_amount):
            player = Player(self.settings.piece_colors[i],
                            self.settings.house_colors[i],
                            self.settings.start_tile_colors[i],
                            self.settings.piece_amount, self.playing_field.dot_size)

            self.players.append(player)

        for i in range(len(self.playing_field.field_tiles)):
            Renderer().render(self.playing_field.color,
                              self.playing_field.field_tiles[i].tile_coords,
                              self.playing_field.dot_size, "star")

        for x in range(self.settings.player_amount):
            Renderer().render(self.players[x].start_tile_color,
                              self.playing_field.field_tiles[self.playing_field.start_tile_ids[x]].tile_coords,
                              self.playing_field.dot_size, "star")
            for i in range(self.settings.piece_amount):
                Renderer().render(self.players[x].house_color,
                                  self.playing_field.end_houses[x][i].tile_coords,
                                  self.playing_field.dot_size, "questionmark")

                Renderer().render(self.players[x].house_color,
                                  self.playing_field.start_houses[x][i].tile_coords,
                                  self.playing_field.dot_size, "questionmark")

        for i in range(self.settings.player_amount):
            for x in range(self.settings.piece_amount):
                self.players[i].player_pieces[x].place_piece(
                    self.playing_field.start_houses[i][x].tile_coords)

        Renderer().inithighlight(self.playing_field.dot_size)

        Renderer().refresh_ui(self.playing_field.canvas_size[1], self.settings.player_names[self.player_choice], self.piece_choice, self.roll, int(window_size / font_size_factor), Settings.player_names,
                              self.state_text)
        position = self.players[self.player_choice].player_pieces[self.piece_choice].position
        Renderer().highlight((position[0] + 0.5, position[1] + 0.5))

        t.tracer(True)

    # Debug method for randomly placing pieces on the field
    def shuffle_pieces(self):
        """
        Randomly places pieces on the game field for debugging purposes.
        """
        for i in range(self.settings.player_amount):
            for x in range(self.settings.piece_amount):
                if x != 0:
                    piece_to_shuffle = self.players[i].player_pieces[x]
                    placement = random.randrange(
                        0, len(self.playing_field.field_tiles))

                    if self.playing_field.field_tiles[placement].tile_standing_player is None:
                        piece_to_shuffle.move_piece(
                            self.playing_field.field_tiles[placement].tile_coords)
                        self.playing_field.field_tiles[placement].tile_standing_player = i
                        self.playing_field.field_tiles[placement].tile_standing_piece = x

    # Method for kicking pieces from the playing field back into starter houses
    def kick_piece(self, team_to_kick, piece_to_kick):
        """
        Sends a piece back to its starting position on the board.

        Parameters:
        ----------
        team_to_kick : int
            The index of the team whose piece is to be moved.
        piece_to_kick : int
            The index of the piece to be moved.
        """
        self.players[team_to_kick].player_pieces[piece_to_kick].move_piece(
            self.playing_field.start_houses[team_to_kick][piece_to_kick].tile_coords)
        self.players[team_to_kick].player_pieces[piece_to_kick].position_in_playing_field = None
        self.players[team_to_kick].player_pieces[piece_to_kick].tiles_moved = 0

    # Method for placing piece on the field from the start house
    def initiate_piece(self):
        """
        Places a piece on the field from the start house.

        Returns:
        -------
        bool
            True if the piece was successfully placed; False otherwise.
        """
        self.current_game_state = GAMESTATE_AWAIT
        piece = self.players[self.player_choice].player_pieces[self.piece_choice]

        starting_tile = self.playing_field.field_tiles[self.playing_field.start_tile_ids[self.player_choice]]

        if starting_tile.tile_standing_player is self.player_choice:
            return False

        piece.position_in_playing_field = self.playing_field.start_tile_ids[self.player_choice]
        piece.tiles_moved = 1
        piece.move_piece(
            self.playing_field.field_tiles[self.playing_field.start_tile_ids[self.player_choice]].tile_coords)
        if starting_tile.tile_standing_player is not None:
            self.kick_piece(starting_tile.tile_standing_player,
                            starting_tile.tile_standing_piece)
        self.playing_field.field_tiles[
            self.playing_field.start_tile_ids[self.player_choice]].tile_standing_player = self.player_choice
        self.playing_field.field_tiles[
            self.playing_field.start_tile_ids[self.player_choice]].tile_standing_piece = self.piece_choice

        return True

    # Method for moving pieces on the playing field
    def iterate_trough_field(self, looprange):
        """
        Moves a piece across the board tiles.

        Parameters:
        ----------
        looprange : int
            The number of steps to move the piece.
        """
        piece = self.players[self.player_choice].player_pieces[self.piece_choice]

        for i in range(looprange):
            piece.tiles_moved += 1
            piece.position_in_playing_field += 1
            piece.move_piece(
                self.playing_field.field_tiles[piece.position_in_playing_field].tile_coords)

    # Method for moving pieces inside end houses
    def iterate_trough_house(self, looprange):
        """
        Moves a piece within the end houses.

        Parameters:
        ----------
        looprange : int
            The number of steps to move within the house.
        """
        piece = self.players[self.player_choice].player_pieces[self.piece_choice]

        for i in range(looprange):
            piece.position_in_house += 1
            piece.move_piece(
                self.playing_field.end_houses[self.player_choice][piece.position_in_house].tile_coords)

    def notify_tile_of_peice(self):
        """
        Notifies the game field tile of the piece's presence on it.
        """
        piece = self.players[self.player_choice].player_pieces[self.piece_choice]

        self.playing_field.field_tiles[piece.position_in_playing_field].tile_standing_player = self.player_choice
        self.playing_field.field_tiles[piece.position_in_playing_field].tile_standing_piece = self.piece_choice

    def remove_piece_from_tile(self):
        """
        Removes the piece's presence from the current tile on the field.
        """
        piece = self.players[self.player_choice].player_pieces[self.piece_choice]

        self.playing_field.field_tiles[piece.position_in_playing_field].tile_standing_player = None
        self.playing_field.field_tiles[piece.position_in_playing_field].tile_standing_piece = None

    def notify_house_of_piece(self):
        """
        Notifies the end house of the piece's presence on it.
        """
        piece = self.players[self.player_choice].player_pieces[self.piece_choice]

        self.playing_field.end_houses[self.player_choice][piece.position_in_house].tile_standing_piece = self.piece_choice

    def remove_piece_from_house(self):
        """
        Removes the piece's presence from its current position within the end house.
        """
        piece = self.players[self.player_choice].player_pieces[self.piece_choice]

        self.playing_field.end_houses[self.player_choice][piece.position_in_house].tile_standing_piece = None

    # Method with logic and rules for moving pieces.
    def perform_movement(self, roll):
        """
        Executes the logic for moving a piece based on the roll.

        Parameters:
        ----------
        roll : int
            The number of steps to move the piece.

        Returns:
        -------
        int
            Status code representing the result of the move (e.g., success, out of bounds, tile occupied).
        """
        self.current_game_state = GAMESTATE_AWAIT

        piece = self.players[self.player_choice].player_pieces[self.piece_choice]

        # If the move results in a piece going outside the playing field or end house, the move gets skipped
        if piece.tiles_moved + roll + piece.position_in_house > self.lenght_of_travel - 1 + self.settings.piece_amount:
            return MOVESTATE_OUTOFBOUNDS

        # If the move results in the piece exceeding the lenght of travel needed to get into a house
        if piece.tiles_moved + roll > self.lenght_of_travel:
            currenttiles_moved = piece.tiles_moved
            house_difference = self.lenght_of_travel - piece.tiles_moved
            if piece.is_in_house is True:
                current_position = self.playing_field.end_houses[
                    self.player_choice][piece.position_in_house]
            else:
                current_position = self.playing_field.field_tiles[piece.position_in_playing_field]

            future_position = self.playing_field.end_houses[self.player_choice][piece.position_in_house + (
                roll - house_difference)]

            # if the tile inside the house is already occupied, the move gets skipped
            if future_position.tile_standing_piece is not None:
                self.iterate_trough_field(house_difference)
                self.iterate_trough_house(roll - house_difference)
                piece.tiles_moved = currenttiles_moved
                if piece.is_in_house is False:
                    piece.position_in_playing_field = current_position.tile_ID
                    piece.position_in_house = -1
                    piece.move_piece(current_position.tile_coords)
                else:
                    piece.position_in_house = current_position.tile_ID
                    piece.move_piece(current_position.tile_coords)

                return MOVESTATE_TILEOCCUPIED

            self.remove_piece_from_house()
            self.iterate_trough_field(house_difference)
            self.iterate_trough_house(roll - house_difference)
            self.notify_house_of_piece()
            if piece.is_in_house is False:
                self.playing_field.field_tiles[piece.position_in_playing_field].tile_standing_player = None
            piece.is_in_house = True
            return MOVESTATE_SUCCESS

        self.remove_piece_from_tile()
        difference = (piece.position_in_playing_field + roll) - \
            (self.lenght_of_travel - 1)
        difference = max(0, difference)
        currenttiles_moved = piece.tiles_moved
        current_position = self.playing_field.field_tiles[piece.position_in_playing_field]

        if difference > 0:
            future_position = self.playing_field.field_tiles[difference - 1]

        else:
            future_position = self.playing_field.field_tiles[piece.position_in_playing_field + roll]

        # if the tile inside the playing field is occupied by a piece of the same player, the move gets skipped

        self.iterate_trough_field(roll - difference)
        if difference > 0:
            piece.position_in_playing_field = -1
            self.iterate_trough_field(difference)

        if future_position.tile_standing_player == self.player_choice:
            piece.tiles_moved = currenttiles_moved
            piece.position_in_playing_field = current_position.tile_ID
            piece.move_piece(current_position.tile_coords)
            self.notify_tile_of_peice()
            return MOVESTATE_TILEOCCUPIED

        # if the tile inside the playing field is occupied by a piece of another player, the peice gets kicked out
        elif future_position.tile_standing_player != self.player_choice:
            if future_position.tile_standing_player is None:
                self.notify_tile_of_peice()
                return MOVESTATE_SUCCESS

            if future_position.tile_ID == self.playing_field.start_tile_ids[future_position.tile_standing_player]:
                piece.move_piece(current_position.tile_coords)
                piece.position_in_playing_field = current_position.tile_ID
                self.notify_tile_of_peice()
                return MOVESTATE_TILEOCCUPIED

            self.kick_piece(future_position.tile_standing_player,
                            future_position.tile_standing_piece)
            self.notify_tile_of_peice()
            return MOVESTATE_SUCCESS

        self.notify_tile_of_peice()
        return MOVESTATE_SUCCESS

    def refresh_ui(self):
        """
        Refreshes the game UI to display the current state and player details.
        """
        Renderer().refresh_ui(self.playing_field.canvas_size[1], self.settings.player_names[self.player_choice],
                              self.piece_choice, self.roll, game_font[1], self.settings.player_names, self.state_text)
