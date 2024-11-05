import turtle as t

from offsetfunc import *


class Piece:
    position = None
    unique_turt = None
    piece_number = None
    position_in_playing_field = None
    position_in_house = -1
    tiles_moved = 0
    is_in_house = False

    def __init__(self, piece_color, piece_size, piece_number):
        self.unique_turt = t.Turtle()
        self.piece_number = piece_number
        self.unique_turt.shape("circle")
        self.unique_turt.color(piece_color)
        self.unique_turt.penup()
        self.unique_turt.turtlesize(piece_size / 25)

        # self.unique_turt.onclick(self.getpieceid)

    def place_piece(self, position):
        self.unique_turt.speed(0)
        self.unique_turt.setpos(off_set_to_center(position))
        self.unique_turt.speed(3)
        self.position = position

    # Moves the piece to the input coordinate tuple.
    def move_piece(self, coords):
        self.unique_turt.setpos(off_set_to_center(coords))
        self.position = coords

    # def getpieceid(self, dummy, dummy2):
    #     print(self.piecenumber, self.position)
    #     return self.position
