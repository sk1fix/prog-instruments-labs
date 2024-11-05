import turtle as t

from offsetfunc import *


class Renderer:
    """
    Class responsible for rendering game visuals, including pieces, highlights, and UI elements.

    Attributes:
    ----------
    rendering_turtle : Turtle
        Turtle used for drawing game pieces.
    writing_turtle : Turtle
        Turtle used for displaying text on the screen.
    click_select_turtle : Turtle
        Turtle used for highlighting selected pieces.
    """
    rendering_turtle = t.Turtle()
    writing_turtle = t.Turtle()
    click_select_turtle = t.Turtle()

    rendering_turtle.hideturtle()
    writing_turtle.hideturtle()
    click_select_turtle.hideturtle()

    # Draws a dot on the given coordinate with the given color offset by 0.5 on both axis
    # this resutls in the dot being drawn at the center of the coordinate.
    def render(self, color, input_tuple, dot_size, symbol):
        """
        Draws a dot or symbol at a specified coordinate with a given color and size.

        Parameters:
        ----------
        color : str or tuple
            Color to fill the symbol.
        input_tuple : tuple
            (x, y) coordinates where the symbol will be drawn.
        dot_size : int
            Size of the dot.
        symbol : str
            Type of symbol to draw ("plus", "star", or "questionmark").
        """
        self.rendering_turtle.penup()
        self.rendering_turtle.hideturtle()
        self.rendering_turtle.speed(6)
        self.rendering_turtle.setpos(off_set_to_center(input_tuple))
        self.rendering_turtle.width(dot_size / 12)

        if symbol == "plus":
            self.rendering_turtle.width(dot_size / 12)
            self.rendering_turtle.color(color)
            self.rendering_turtle.pendown()
            for i in range(4):
                self.rendering_turtle.forward(0.2)
                self.rendering_turtle.backward(0.2)
                self.rendering_turtle.right(90)
            self.rendering_turtle.penup()
            return

        self.rendering_turtle.color("black")
        self.rendering_turtle.dot(dot_size + (dot_size / 6))
        self.rendering_turtle.color(color)
        self.rendering_turtle.dot(dot_size)

        if symbol == "star":
            self.rendering_turtle.color("black")
            self.rendering_turtle.pendown()
            for i in range(6):
                self.rendering_turtle.forward(0.2)
                self.rendering_turtle.backward(0.2)
                self.rendering_turtle.right(60)
            self.rendering_turtle.penup()

        if symbol == "questionmark":
            self.rendering_turtle.color("black")
            self.rendering_turtle.right(-90)
            self.rendering_turtle.backward(0.22)
            self.rendering_turtle.dot(dot_size / 10)
            self.rendering_turtle.forward(0.1)
            self.rendering_turtle.pendown()
            self.rendering_turtle.forward(0.1)
            self.rendering_turtle.right(45)
            self.rendering_turtle.forward(0.1)
            self.rendering_turtle.right(-22.5)
            self.rendering_turtle.forward(0.1)
            self.rendering_turtle.right(-45)
            self.rendering_turtle.forward(0.1)
            self.rendering_turtle.right(-45)
            self.rendering_turtle.forward(0.1)
            self.rendering_turtle.right(-45)
            self.rendering_turtle.forward(0.1)
            self.rendering_turtle.right(-45)
            self.rendering_turtle.forward(0.1)
            self.rendering_turtle.setheading(0)
            self.rendering_turtle.penup()

    def init_highlight(self, dot_size):
        """
        Initializes the highlight cursor for selecting pieces.

        Parameters:
        ----------
        dot_size : int
            Size of the highlight indicator.
        """
        self.click_select_turtle.shape("circle")
        self.click_select_turtle.color("orange")
        self.click_select_turtle.hideturtle()
        self.click_select_turtle.penup()
        self.click_select_turtle.turtlesize(dot_size / 17)

    def highlight(self, position):
        """
        Shows the highlight cursor at the given position.

        Parameters:
        ----------
        position : tuple
            (x, y) coordinates to move the highlight cursor to.
        """
        t.tracer(False)
        self.click_select_turtle.showturtle()
        self.click_select_turtle.goto(position)
        t.tracer(True)

    def hide_highlight(self):
        """
        Hides the highlight cursor.
        """
        self.click_select_turtle.hideturtle()

    def refresh_ui(self, canvas_size, player_name, piece_chosen, roll, font_size, name_list, state_text):
        """
        Refreshes and updates the user interface with the latest game information.

        Parameters:
        ----------
        canvas_size : int
            Size of the canvas.
        player_name : str
            Name of the current player.
        piece_chosen : int
            Index of the selected piece.
        roll : int
            The result of the latest dice roll.
        font_size : int
            Font size for text.
        name_list : list[str]
            List of player names.
        state_text : str
            Text representing the current game state.
        """
        t.tracer(False)
        font = ('Arial', font_size, 'normal')
        name_font = ('Arial', font_size, 'bold')

        self.writing_turtle.clear()
        self.writing_turtle.hideturtle()
        self.writing_turtle.up()

        self.writing_turtle.goto(
            canvas_size - 1 - 0.37, canvas_size - 1 + 0.25)
        self.writing_turtle.color("black")
        self.writing_turtle.write(name_list[0], False, "right", name_font)
        self.writing_turtle.goto(1 + 0.37, 0 + 0.25)
        self.writing_turtle.write(name_list[1], False, "left", name_font)
        self.writing_turtle.goto(canvas_size - 1 - 0.37, 0 + 0.25)
        self.writing_turtle.write(name_list[2], False, "right", name_font)
        self.writing_turtle.goto(1 + 0.37, canvas_size - 1 + 0.25)
        self.writing_turtle.write(name_list[3], False, "left", name_font)

        self.writing_turtle.goto(canvas_size / 2, 0.25)
        self.writing_turtle.write(state_text, False, "center", font)

        self.writing_turtle.goto(0, canvas_size)
        self.writing_turtle.write(f"  Hrá {player_name}", False, "left", font)

        self.writing_turtle.goto(canvas_size / 2, canvas_size)
        self.writing_turtle.write(
            f"Figúrka {piece_chosen + 1} zvolená", False, "center", font)
        self.writing_turtle.goto(canvas_size, canvas_size)
        self.writing_turtle.write(f"Hodil si: {roll}  ", False, "right", font)
        t.tracer(True)
