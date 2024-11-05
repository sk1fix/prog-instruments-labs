# Simple function to add a 0.5 to both members of a coordinate tuple.
def off_set_to_center(coordinate):
    """
    Offsets a coordinate by 0.5 units in both the x and y directions to center it.

    Parameters:
    ----------
    coordinate : tuple
        A tuple representing the (x, y) coordinate to be centered.

    Returns:
    -------
    tuple
        The adjusted (x, y) coordinate, centered by adding 0.5 to each component.
    """
    coordinate = (float(coordinate[0]) + 0.5, float(coordinate[1]) + 0.5)
    return coordinate
