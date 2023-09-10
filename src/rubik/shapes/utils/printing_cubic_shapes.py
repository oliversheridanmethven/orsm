#!/usr/bin/env python3
"""
Some useful utilities for printing "perfect" cubic structures
of the form NxNxN.

         top
          |
          |
          V

         ____ ____
       /____/____/|
     /____/____/| |
    |    |    | |/|   <-- right
    |    |    |/| |
     ---- ----  | |
    |    |    | |/
    |    |    |/
     ---- ----

        _.
        /|
       /
      /
    front

    The faces come in the order
    [front, back, right, left, top, bottom] and the orientation is:

              ----------
             |  top   4 |
     --------------------------------------
    | left 3 | front  0 | right 2 | back 1 |
     --------------------------------------
             | bottom 5 |
              ----------

    where the upper left of each face is the (0,0) entry.
"""


def to_string(*args, faces, colours, **kwargs):
    """Try to show the cube in a very pictorial way."""
    'front 0  back 1  right 2  left 3  top 4  bottom 5'
    top = faces[4]
    front = faces[0]
    right = faces[2]
    left = faces[3]
    back = faces[1]
    bottom = faces[5]
    s = "\n\n"
    indent = 1 + 2 * len(top)
    indenting = indent + 1 + len(top)
    for row in top:
        s += ' ' * indenting
        for tile in row:
            s += f"{colours(tile).colour(tile)} "
        s += '\n'
        indenting -= 1
    bars = '-' * len(row) * 2
    s += ' ' * indent + '/' + bars + '/'
    for left_row, front_row, right_row, back_row in zip(left, front, right, back):
        s += "\n"
        for tile in left_row:
            s += f"{colours(tile).colour(tile)} "
        s += ': '
        for tile in front_row:
            s += f"{colours(tile).colour(tile)} "
        s += ': '
        for tile in right_row:
            s += f"{colours(tile).colour(tile)} "
        s += ': '
        for tile in back_row:
            s += f"{colours(tile).colour(tile)} "
    s += "\n" + ' ' * indent + "\\" + bars + "\\"
    for row in bottom:
        s += '\n'
        indenting += 1
        s += ' ' * indenting
        for tile in row:
            s += f"{colours(tile).colour(tile)} "
    s += "\n\n"
    return s


if __name__ == "__main__":
    pass
