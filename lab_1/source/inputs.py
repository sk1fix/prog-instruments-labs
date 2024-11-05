from tkinter import *

from gamemaster import *


class InputSystem:
    """
    Class for handling user input and managing game actions.

    Attributes:
    ----------
    roll_btn : Button
        Button for rolling the dice.
    move_btn : Button
        Button for moving a piece.
    result_screen : any
        Screen to display the game result.
    master : GameMaster
        Main game controller object.
    """
    roll_btn = None
    move_btn = None
    result_screen = None

    master = None
    # master = GameMaster(4, 4, 3)
    # master.in_menu = False

    def __init__(self, result_screen):
        """
        Initializes the InputSystem class, sets up buttons, and binds key events.

        Parameters:
        ----------
        result_screen : any
            Screen object to display the results.
        """
        win.onkey(lambda key="Return": self.input_handler(key), "Return")
        win.onkey(lambda key="Space": self.input_handler(key), "space")
        win.onkey(lambda key="Left": self.input_handler(key), "Left")
        win.onkey(lambda key="Right": self.input_handler(key), "Right")
        self.roll_btn = Button(
            canvas.master, text="Hoď", command=lambda key="Space": self.input_handler(key), font=game_font)
        self.move_btn = Button(canvas.master, text="Choď",
                               command=lambda key="Return": self.input_handler(key), font=game_font)
        self.roll_btn.place(relx=0.7, rely=0.05, anchor=CENTER)
        self.move_btn.place(relx=0.3, rely=0.05, anchor=CENTER)
        self.result_screen = result_screen

        win.onclick(self.mouse_select_piece)

        win.listen()

    def input_handler(self, key):
        """
        Handles key input actions and triggers corresponding game actions.

        Parameters:
        ----------
        key : str
            Key pressed by the user.
        """
        if self.master.in_menu is False and self.master.current_game_state != GAMESTATE_AWAIT:
            match key:
                case "Left":
                    self.cycle_pieces_left()
                case "Right":
                    self.cycle_pieces_right()
                case "Return":
                    if self.master.roll == 0:
                        return

                    self.move_attempt(
                        self.master.players[self.master.player_choice].player_pieces[self.master.piece_choice])
                case "Space":
                    self.roll()
                    if self.master.current_game_state == GAMESTATE_GETPIECEOUT:
                        self.move_attempt(
                            self.master.players[self.master.player_choice].player_pieces[self.master.piece_choice])

        self.master.refresh_ui()

    def mouse_select_piece(self, x, y):
        """
        Selects a piece based on mouse click position.

        Parameters:
        ----------
        x : int
            X-coordinate of the click.
        y : int
            Y-coordinate of the click.
        """
        position = (int(x), int(y))

        piecelist = self.master.players[self.master.player_choice].player_pieces
        for pi in range(len(piecelist)):
            if position == piecelist[pi].position:
                self.master.piece_choice = pi
                Renderer().highlight((position[0] + 0.5, position[1] + 0.5))
                self.master.refresh_ui()
                return

    def cycle_pieces_right(self):
        """
        Cycles the selection to the next piece on the right.
        """
        if self.master.piece_choice + 1 > self.master.settings.piece_amount - 1:
            self.master.piece_choice = 0
        else:
            self.master.piece_choice += 1

        pos = self.master.players[self.master.player_choice].player_pieces[self.master.piece_choice].position
        Renderer().highlight((pos[0] + 0.5, pos[1] + 0.5))
        print(self.master.piece_choice)

    def cycle_pieces_left(self):
        """
        Cycles the selection to the previous piece on the left.
        """
        if self.master.piece_choice - 1 < 0:
            self.master.piece_choice = self.master.settings.piece_amount - 1
        else:
            self.master.piece_choice -= 1

        pos = self.master.players[self.master.player_choice].player_pieces[self.master.piece_choice].position
        Renderer().highlight((pos[0] + 0.5, pos[1] + 0.5))
        print(self.master.piece_choice)

    def roll(self):
        """
        Rolls the dice and updates the game state.
        """
        if self.master.current_game_state != GAMESTATE_MOVE:
            self.master.roll = random.randrange(1, 7)
            self.master.refresh_ui()

        if self.master.current_game_state != GAMESTATE_GETPIECEOUT:
            self.master.current_game_state = GAMESTATE_MOVE

    def debug_roll(self, roll):
        """
        Sets a predefined dice roll value for debugging purposes.

        Parameters:
        ----------
        roll : int
            Value to set for the dice roll.
        """
        if self.master.current_game_state != GAMESTATE_MOVE:
            self.master.roll = roll
            self.master.refresh_ui()

        if self.master.current_game_state != GAMESTATE_GETPIECEOUT:
            self.master.current_game_state = GAMESTATE_MOVE

    def goto_result_screen(self, victor):
        """
        Navigates to the result screen and resets the game state.

        Parameters:
        ----------
        victor : str
            Name of the winning player.
        """
        recreate_screen()
        reset_state()
        self.move_btn.place_forget()
        self.roll_btn.place_forget()
        self.result_screen.victor = victor
        self.result_screen.show_result_screen()

    def cycle_players(self):
        """
        Switches to the next player and updates the game state.
        """
        has_winner = True
        player = self.master.players[self.master.player_choice]
        for i in player.player_pieces:
            if i.is_in_house is False:
                has_winner = False
                break

        if has_winner is True:
            print(
                f' {self.master.settings.player_names[self.master.player_choice]} won!')
            self.goto_result_screen(
                self.master.settings.player_names[self.master.player_choice])

        if self.master.player_choice + 1 > self.master.settings.player_amount - 1:
            self.master.player_choice = 0
        else:
            self.master.player_choice += 1

        if self.is_piece_on_board():
            self.master.current_game_state = GAMESTATE_ROLL
        else:
            self.master.current_game_state = GAMESTATE_GETPIECEOUT

        self.master.roll = 0
        self.master.at_tempt = 0

        pos = self.master.players[self.master.player_choice].player_pieces[self.master.piece_choice].position
        Renderer().highlight((pos[0] + 0.5, pos[1] + 0.5))

    def is_piece_on_board(self):
        """
        Checks if any of the current player's pieces are on the board.

        Returns:
        -------
        bool
            True if any piece is on the board; False otherwise.
        """
        for i in range(len(self.master.players[self.master.player_choice].player_pieces)):
            if self.master.players[self.master.player_choice].player_pieces[i].position_in_playing_field is not None:
                return True

        return False

    def can_piece_move(self, roll, piece):
        """
        Determines if a specific piece can move based on the roll.

        Parameters:
        ----------
        roll : int
            Dice roll value.
        piece : Piece
            The piece to evaluate.

        Returns:
        -------
        bool
            True if the piece can move; False otherwise.
        """
        if piece.position_in_playing_field is None:
            return False
        if self.master.lenght_of_travel - piece.tiles_moved > roll and piece.position_in_house == -1:
            print(
                f'PIECE CAN STILL TRAVEL ON FIELD {self.master.lenght_of_travel - piece.tiles_moved} GREATER THAN {roll}')
            return True
        if piece.position_in_house + roll < self.master.settings.piece_amount:
            print(
                f'PIECE CAN STILL TRAVEL IN HOUSES {piece.position_in_house + roll} LESS THAN {self.master.settings.piece_amount}')
            return True
        if piece.tiles_moved + roll + piece.position_in_house <= self.master.lenght_of_travel - 1 + self.master.settings.piece_amount:
            return True

        return False

    def can_any_piece_move(self, roll):
        """
        Checks if any piece of the current player can move.

        Parameters:
        ----------
        roll : int
            Dice roll value.

        Returns:
        -------
        int
            Number of available moves.
        """
        available_moves = 0

        for i in range(len(self.master.players[self.master.player_choice].player_pieces)):
            piece = self.master.players[self.master.player_choice].player_pieces[i]

            if piece.position_in_playing_field is None and roll == 6 or self.can_piece_move(roll, piece):
                available_moves += 1

        return available_moves

    def move_attempt(self, piece):
        """
        Attempts to move a piece and applies the game rules.

        Parameters:
        ----------
        piece : Piece
            The piece to move.
        """
        if self.master.current_game_state == GAMESTATE_GETPIECEOUT:
            if self.master.roll == 6:
                self.master.initiate_piece()
                self.cycle_players()
                self.master.state_text = ""

            elif self.master.attempt + 1 > 2:
                self.cycle_players()
                self.master.state_text = "Došli ti pokusi"
            else:
                self.master.attempt += 1
                self.master.state_text = "Máš dalšlí pokus"
            return

        elif piece.position_in_playing_field is None and self.master.current_game_state == GAMESTATE_MOVE:
            if self.master.roll == 6:
                if self.master.initiate_piece():
                    self.cycle_players()
                    self.master.state_text = ""
                    return
                self.master.current_game_state = GAMESTATE_MOVE
                return

        available_moves = self.can_any_piece_move(self.master.roll)
        print(f'Available moves is {available_moves}')

        if available_moves <= 0:
            self.cycle_players()
            self.master.state_text = "0 možných pohybov"
            return

        if not self.can_piece_move(self.master.roll, piece):
            self.master.state_text = "Neplatný pohyb"
            return

        result = self.master.perform_movement(self.master.roll)
        print(f'Result of move is {result}')

        match result:
            case 0:  # MOVESTATE_SUCCESS
                self.master.state_text = ""
                self.cycle_players()
            case 1:  # MOVESTATE_OUTOFBOUNDS
                if available_moves <= 1:
                    self.master.state_text = "Neplatný pohyb, 0 možných pohybov"
                    self.cycle_players()
                    return
                self.master.state_text = "Neplatný pohyb"
                self.master.current_game_state = GAMESTATE_MOVE
            case 2:  # MOVESTATE_TILEOCCUPIED
                if available_moves <= 1:
                    self.master.state_text = "Neplatný pohyb, 0 možných pohybov"
                    self.cycle_players()
                    return
                self.master.current_game_state = GAMESTATE_MOVE
                self.master.state_text = "Neplatný pohyb"


input_system = InputSystem()
win.mainloop()
