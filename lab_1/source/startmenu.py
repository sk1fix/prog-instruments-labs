import sys

from tkinter import Button, Label, CENTER

from inputs import InputSystem
from inputs import window_size, win
from gamemaster import font_size_factor


menu_font = ('Arial', int(window_size / font_size_factor), 'normal')
title_font = ('Comic Sans MS', int(
    window_size / (font_size_factor * 0.5)), 'normal')


def rgb_to_hex(rgb):
    """
    Converts an RGB color tuple to a hexadecimal color string.

    Parameters:
    ----------
    rgb : tuple
        RGB color values as a tuple (R, G, B).

    Returns:
    -------
    str
        Hexadecimal color string.
    """
    return "#%02x%02x%02x" % rgb


def exit_game():
    """
    Exits the game by terminating the program.
    """
    sys.exit(0)


class Mainmenu:
    """
    Class representing the main menu of the game, including buttons for starting, exiting, and viewing the guide.

    Attributes:
    ----------
    start : Button
        Button to start the game.
    leave : Button
        Button to exit the game.
    game_guide : Button
        Button to show the game guide.
    game_name : Label
        Label displaying the game's title.
    """
    start = None
    leave = None
    game_guide = None
    game_name = None

    def __init__(self):
        """
        Initializes the Mainmenu with buttons and the game title.
        """
        self.start = Button(canvas.master, text="Hrať", width=int(window_size / 50),
                            command=lambda: self.start_btn(), font=menu_font)
        self.leave = Button(canvas.master, text="Koniec", width=int(window_size / 50),
                            command=lambda: exit_game(), font=menu_font)
        self.game_guide = Button(canvas.master, text="Ako hrať", width=int(window_size / 50),
                                 command=lambda: self.game_guidebtn(), font=menu_font)
        self.game_name = Label(text="Cloveče Nehnevaj Sa!",
                               font=title_font, bg=rgb_to_hex(bgcolor))

    def show_main_menu(self):
        """
        Displays the main menu buttons and title.
        """
        self.start.place(relx=0.5, rely=0.42, anchor=CENTER)
        self.leave.place(relx=0.5, rely=0.58, anchor=CENTER)
        self.game_guide.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.game_name.place(relx=0.5, rely=0.3, anchor=CENTER)

    def hide_main_menu(self):
        """
        Hides the main menu buttons and title.
        """
        self.start.place_forget()
        self.leave.place_forget()
        self.game_guide.place_forget()
        self.game_name.place_forget()

    def start_btn(self):
        """
        Hides the main menu and shows game options.
        """
        self.hide_main_menu()
        options.show_game_options()

    def game_guidebtn(self):
        """
        Hides the main menu and shows the game guide.
        """
        self.hide_main_menu()
        guide.show_game_guide()


class GameOptions:
    """
    Class for configuring game options, such as player count, piece count, and board size.

    Attributes:
    ----------
    player_amount : int
        Number of players.
    piece_amount : int
        Number of pieces per player.
    tile_amount : int
        Size of the game board in tiles.
    Various UI elements for displaying and adjusting game settings.
    """
    player_amount = 4
    piece_amount = 4
    tile_amount = 3

    top_text = None
    player_amount_label = None
    player_amount_higher = None
    player_amount_number = None
    player_amount_lower = None

    piece_amount_label = None
    piece_amount_higher = None
    piece_amount_number = None
    piece_amount_lower = None

    tile_amount_label = None
    tile_amount_higher = None
    tile_amount_number = None
    tile_amount_lower = None
    back = None

    names_btn = None
    names = ["Modrý", "Žltý", "Zelený", "Červený"]
    entry_fields = []

    start_game = None

    input_system = None

    def __init__(self):
        """
        Initializes the GameOptions menu with widgets for adjusting game settings.
        """
        self.top_text = Label(
            canvas.master, text="Zvol nastavenia hry", font=menu_font, bg=rgb_to_hex(bgcolor))

        # Player amount widgets
        self.player_amount_label = Label(
            canvas.master, text="Počet hráčov:", font=menu_font, bg=rgb_to_hex(bgcolor))
        self.player_amount_higher = Button(canvas.master, text=">",
                                           command=lambda: self.increase_player_amount(), font=menu_font)

        self.player_amount_number = Label(canvas.master, text=str(
            self.player_amount), font=menu_font, bg=rgb_to_hex(bgcolor))
        self.player_amount_lower = Button(canvas.master, text="<",
                                          command=lambda: self.decrease_player_amount(), font=menu_font)

        # Piece amount widgets
        self.piece_amount_label = Label(
            canvas.master, text="Počet figúrok:", font=menu_font, bg=rgb_to_hex(bgcolor))
        self.piece_amount_higher = Button(canvas.master, text=">",
                                          command=lambda: self.increase_piece_amount(), font=menu_font)

        self.piece_amount_number = Label(canvas.master, text=str(
            self.piece_amount), font=menu_font, bg=rgb_to_hex(bgcolor))
        self.piece_amount_lower = Button(canvas.master, text="<",
                                         command=lambda: self.decrease_piece_amount(), font=menu_font)

        # Tile amount widgets
        self.tile_amount_label = Label(
            canvas.master, text="Veľkosť hernej plochy:", font=menu_font, bg=rgb_to_hex(bgcolor))
        self.tile_amount_higher = Button(canvas.master, text=">",
                                         command=lambda: self.increase_tile_amount(), font=menu_font)

        self.tile_amount_number = Label(canvas.master, text=str(
            self.tile_amount), font=menu_font, bg=rgb_to_hex(bgcolor))
        self.tile_amount_lower = Button(canvas.master, text="<",
                                        command=lambda: self.decrease_tile_amount(), font=menu_font)

        self.back = Button(canvas.master, text="Späť",
                           command=lambda: self.back_btn(), font=menu_font)
        self.names_btn = Button(canvas.master, text="Zvoľ mená",
                                command=lambda: self.name_window(), font=menu_font)
        self.start_game = Button(
            canvas.master, text="Hrať", command=lambda: self.start_btn(), font=menu_font)

    def show_game_options(self):
        """
        Displays the game options menu.
        """
        self.top_text.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.player_amount_label.place(relx=0.5, rely=0.36, anchor=CENTER)
        self.player_amount_higher.place(relx=0.6, rely=0.42, anchor=CENTER)
        self.player_amount_number.place(relx=0.5, rely=0.42, anchor=CENTER)
        self.player_amount_lower.place(relx=0.4, rely=0.42, anchor=CENTER)

        self.piece_amount_label.place(relx=0.5, rely=0.48, anchor=CENTER)
        self.piece_amount_higher.place(relx=0.6, rely=0.54, anchor=CENTER)
        self.piece_amount_number.place(relx=0.5, rely=0.54, anchor=CENTER)
        self.piece_amount_lower.place(relx=0.4, rely=0.54, anchor=CENTER)

        self.tile_amount_label.place(relx=0.5, rely=0.60, anchor=CENTER)
        self.tile_amount_higher.place(relx=0.6, rely=0.66, anchor=CENTER)
        self.tile_amount_number.place(relx=0.5, rely=0.66, anchor=CENTER)
        self.tile_amount_lower.place(relx=0.4, rely=0.66, anchor=CENTER)

        self.back.place(relx=0.3, rely=0.8, anchor=CENTER)
        self.names_btn.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.start_game.place(relx=0.7, rely=0.8, anchor=CENTER)

    def hide_game_options(self):
        """
        Hides the game options menu.
        """
        self.top_text.place_forget()

        self.player_amount_label.place_forget()
        self.player_amount_higher.place_forget()
        self.player_amount_number.place_forget()
        self.player_amount_lower.place_forget()

        self.piece_amount_label.place_forget()
        self.piece_amount_higher.place_forget()
        self.piece_amount_number.place_forget()
        self.piece_amount_lower.place_forget()

        self.tile_amount_label.place_forget()
        self.tile_amount_higher.place_forget()
        self.tile_amount_number.place_forget()
        self.tile_amount_lower.place_forget()

        self.back.place_forget()
        self.names_btn.place_forget()
        self.start_game.place_forget()

    def increase_player_amount(self):
        """
        Increases the player count, up to a maximum of 4.
        """
        if self.player_amount + 1 <= 4:
            self.player_amount += 1
            self.player_amount_number.config(text=str(self.player_amount))

    def decrease_player_amount(self):
        """
        Decreases the player count, down to a minimum of 2.
        """
        if self.player_amount - 1 >= 2:
            self.player_amount -= 1
            self.player_amount_number.config(text=str(self.player_amount))

    def increase_piece_amount(self):
        """
        Increases the piece count, up to a maximum of 11, limited by board size.
        """
        if self.piece_amount + 1 <= 11 and self.piece_amount + 1 <= self.tile_amount + 1:
            self.piece_amount += 1
            self.piece_amount_number.config(text=str(self.piece_amount))

    def decrease_piece_amount(self):
        """
        Decreases the piece count, down to a minimum of 1.
        """
        if self.piece_amount - 1 >= 1:
            self.piece_amount -= 1
            self.piece_amount_number.config(text=str(self.piece_amount))

    def increase_tile_amount(self):
        """
        Increases the board size, up to a maximum of 10 tiles.
        """
        if self.tile_amount + 1 <= 10:
            self.tile_amount += 1
            self.tile_amount_number.config(text=str(self.tile_amount))

    def decrease_tile_amount(self):
        """
        Decreases the board size, adjusting piece count if necessary.
        """
        if self.tile_amount - 1 >= 0:
            self.tile_amount -= 1
            self.tile_amount_number.config(text=str(self.tile_amount))
            if self.tile_amount < self.piece_amount - 1:
                self.piece_amount -= 1
                self.piece_amount_number.config(text=str(self.piece_amount))

    def back_btn(self):
        """
        Returns to the main menu from game options.
        """
        self.hide_game_options()
        main.show_main_menu()

    def name_window(self):
        """
        Opens a window for entering player names.
        """
        name_window = Toplevel(canvas)
        name_window.title("Zvoľ mená")
        name_window_size = str(int(window_size / 3)) + \
            "x" + str(int(window_size / 3))
        name_window.geometry(str(name_window_size))
        self.entry_fields = []

        def close_name_window():
            for player_names in range(self.player_amount):
                self.names[player_names] = self.entry_fields[player_names].get()
            name_window.destroy()

        Label(name_window, text="Zvoľ mená hráčov", font=menu_font).pack()
        for players in range(self.player_amount):
            entry_field = Entry(name_window, font=menu_font)
            entry_field.insert(0, self.names[players])
            self.entry_fields.append(entry_field)
            self.entry_fields[players].pack()

        Button(name_window, text="Potvrdiť",
               command=lambda: close_name_window(), font=menu_font).pack()

    def start_btn(self):
        """
        Starts the game with the chosen settings.
        """
        Settings.player_names = ["", "", "", ""]
        for player_names in range(self.player_amount):
            Settings.player_names[player_names] = self.names[player_names]

        self.hide_game_options()
        self.input_system = input_system(ResultScreen())
        self.input_system.master = GameMaster(
            self.player_amount, self.piece_amount, self.tile_amount)
        GameMaster.in_menu = False


class game_guide:
    """
    Class for displaying the game guide screen with a back button.

    Attributes:
    ----------
    back : Button
        Button to return to the main menu.
    """
    back = None

    def __init__(self):
        """
        Initializes the game guide with a back button.
        """
        self.back = Button(canvas.master, text="Späť",
                           command=lambda: self.back_btn(), font=menu_font)

    def show_game_guide(self):
        """
        Displays the game guide screen.
        """
        self.back.place(relx=0.3, rely=0.8, anchor=CENTER)

    def hide_game_guide(self):
        """
        Hides the game guide screen.
        """
        self.back.place_forget()

    def back_btn(self):
        """
        Returns to the main menu from the game guide.
        """
        self.hide_game_guide()
        main.show_main_menu()


class ResultScreen:
    """
    Class for displaying the result screen after a game ends, showing the winner.

    Attributes:
    ----------
    title : Label
        Label displaying the winner's name.
    back : Button
        Button to return to the main menu.
    victor : str
        Name of the winning player.
    """
    title = None
    back = None
    victor = None

    def __init__(self):
        """
        Initializes the result screen with title and back button.
        """
        self.title = Label(text="X vyhral!", font=title_font,
                           bg=rgb_to_hex(bgcolor))
        self.back = Button(canvas.master, text="Späť do hlavného menu",
                           command=lambda: self.back_btn(), font=menu_font)

    def show_result_screen(self):
        """
        Displays the result screen with the winner's name.
        """
        self.title.config(text=f'{self.victor} vyhral!')
        self.title.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.back.place(relx=0.5, rely=0.8, anchor=CENTER)

    def hide_result_screen(self):
        """
        Hides the result screen.
        """
        self.title.place_forget()
        self.back.place_forget()

    def back_btn(self):
        """
        Returns to the main menu from the result screen.
        """
        self.hide_result_screen()
        main.show_main_menu()


main = Mainmenu()
options = GameOptions()
guide = game_guide()
result = ResultScreen()

Mainmenu().show_main_menu()
win.mainloop()
