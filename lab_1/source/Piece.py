import turtle as t

from offsetfunc import off_set_to_center


class Piece:
    """
    Class representing a game piece with movement and positioning capabilities.

    Attributes:
    ----------
    position : tuple or None
        Current position of the piece on the game board.
    unique_turt : Turtle
        Turtle object representing the piece's visual appearance.
    piece_number : int
        Identifier number for the piece.
    position_in_playing_field : int or None
        Index of the piece's position on the main playing field.
    position_in_house : int
        Position of the piece within the end house (-1 if not in house).
    tiles_moved : int
        Total number of tiles moved by the piece.
    is_in_house : bool
        Indicates whether the piece is within the end house.
    """
    position = None
    unique_turt = None
    piece_number = None
    position_in_playing_field = None
    position_in_house = -1
    tiles_moved = 0
    is_in_house = False

    def __init__(self, piece_color, piece_size, piece_number):
        """
        Initializes the Piece object with its color, size, and identifier.

        Parameters:
        ----------
        piece_color : str
            The color of the piece.
        piece_size : int
            The visual size of the piece.
        piece_number : int
            Unique identifier for the piece.
        """
        self.unique_turt = t.Turtle()
        self.piece_number = piece_number
        self.unique_turt.shape("circle")
        self.unique_turt.color(piece_color)
        self.unique_turt.penup()
        self.unique_turt.turtlesize(piece_size / 25)

        # self.unique_turt.onclick(self.getpieceid)

    def place_piece(self, position):
        """
        Places the piece at a specific position on the board.

        Parameters:
        ----------
        position : tuple
            The (x, y) coordinates for placing the piece.
        """
        self.unique_turt.speed(0)
        self.unique_turt.setpos(off_set_to_center(position))
        self.unique_turt.speed(3)
        self.position = position

    # Moves the piece to the input coordinate tuple.
    def move_piece(self, coords):
        """
        Moves the piece to a new set of coordinates on the board.

        Parameters:
        ----------
        coords : tuple
            The (x, y) coordinates to move the piece to.
        """
        self.unique_turt.setpos(off_set_to_center(coords))
        self.position = coords

    # def getpieceid(self, dummy, dummy2):
    #     print(self.piecenumber, self.position)
    #     return self.position
