"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Yifei Xiao.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------
    del_x = rectangle.get_width() / 2
    del_y = (rectangle.corner_1.y - rectangle.corner_2.y)

    start_corner_1 = rectangle.corner_1
    start_corner_2 = rectangle.corner_2

    corner_1 = rectangle.corner_1
    corner_2 = rectangle.corner_2

    for k in range(n):
        for j in range(k + 1):
            new_rectangle = rg.Rectangle(corner_1, corner_2)
            new_rectangle.attach_to(window)
            window.render()

            corner_1.x += del_x * 2
            corner_2.x += del_x * 2

        corner_1 = rg.Point(start_corner_1.x - (k + 3) * del_x, corner_1.y + del_y)
        corner_2 = rg.Point(start_corner_2.x - (k + 3) * del_x, corner_2.y + del_y)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
