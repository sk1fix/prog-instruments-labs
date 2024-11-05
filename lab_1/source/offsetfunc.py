# Simple function to add a 0.5 to both members of a coordinate tuple.
def off_set_to_center(coordinate):
    coordinate = (float(coordinate[0]) + 0.5, float(coordinate[1]) + 0.5)
    return coordinate
