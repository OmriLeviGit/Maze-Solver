import numpy as np
from PIL import Image as Im
from enum import Enum
from ordered_enum import OrderedEnum

from Line import Line
from Point import Point

"""
workflow:
1. convert the array to only black white and red
2. draw a line from the middle to find the closest black line
3. circle the maze to find both the entrance and the exit:
    go to the right, if there is no right go to the bottom, if there is no bottom continue, while counting all 
    white pixels  until black or hit end of the screen.
4. the size of the entrance determine a block size, divide the maze into square grids
5. the middle of each grid is where each step is taken, and the size of each step is the size of the grid.
6. execute the algorithm
"""


class Border(OrderedEnum):
    TOP = 0
    RIGHT = 1
    BOT = 2
    LEFT = 3


class Color(Enum):
    BLACK = False
    WHITE = True


def main():
    # open image, convert to black and white and into a nd.array
    path = "img/square-maze-game-for-kids-free-vector.jpg"
    img_original = Im.open(path)
    img = img_original.convert("1")  # convert to black and white to speed up calculations
    img_array = np.array(img)

    thickness = get_border_thickness(img_array)
    borders = get_borders_info(img_array, thickness)
    tunnel_width = get_tunnel_width(img_array, borders, thickness)

    start_point, end_point = find_openings(img_array, borders)


    """
    # draw borders
    img_array[borders[0]] = [0]
    img_array[:, borders[1]] = [0]
    img_array[borders[2]] = [0]
    img_array[:, borders[3]] = [0]

    # draw start and end points
    img_array[start.get_y()][start.get_x()] = False
    img_array[end.get_y()][end.get_x()] = False
    
    new_img = Im.fromarray(img_array)
    new_img.show()
    """
    img_original.close()


def find_openings(img_array, borders):
    entrances = []

    # horizontal entrances
    horizontal_borders = [borders[Border.TOP.value], borders[Border.BOT.value]]
    for border_y in horizontal_borders:
        entrance_start = None
        entrance_end = None

        for i in range(borders[Border.LEFT.value], borders[Border.RIGHT.value]):
            pixel_color = img_array[border_y, i]

            if pixel_color == Color.WHITE.value and entrance_start is None:
                entrance_start = i

            if pixel_color == Color.BLACK.value and entrance_start is not None:
                entrance_end = i
                break

        if entrance_start is not None and entrance_end is not None:
            start_point = Point(entrance_start, border_y)
            end_point = Point(entrance_end, border_y)

            entrance_mid_point = Line(start_point, end_point).middle_point()
            entrances.append(entrance_mid_point)

    # vertical entrances
    vertical_borders = [borders[Border.LEFT.value], borders[Border.RIGHT.value]]
    for border_x in vertical_borders:
        entrance_start = None
        entrance_end = None

        for i in range(borders[Border.TOP.value], borders[Border.BOT.value]):
            pixel_color = img_array[i, border_x]

            if pixel_color == Color.WHITE.value and entrance_start is None:
                entrance_start = i

            if pixel_color == Color.BLACK.value and entrance_start is not None:
                entrance_end = i
                break

        if entrance_start is not None and entrance_end is not None:
            start_point = Point(border_x, entrance_start)
            end_point = Point(border_x, entrance_end)

            entrance_mid_point = Line(start_point, end_point).middle_point()
            entrances.append(entrance_mid_point)

    return entrances[0], entrances[1]


def get_border_thickness(img_array):
    _, height = img_array.shape
    horizontal_mid_point = int(height / 2)

    thickness = 0
    for i in range(height):
        current_pixel_color = img_array[i][horizontal_mid_point]
        if current_pixel_color == Color.BLACK.value:
            thickness += 1

        if current_pixel_color == Color.WHITE.value and thickness > 0:
            break

    return thickness


def get_tunnel_width(img_array, borders, thickness):
    top_border = int(borders[Border.TOP.value] + thickness / 2)
    width, height = img_array.shape
    vertical_mid_point = int(width / 2)

    tunnel_width = 0
    while img_array[top_border + tunnel_width][vertical_mid_point] == Color.WHITE.value:
        tunnel_width += 1


    return tunnel_width


def get_borders_info(img_array, thickness):
    width, height = img_array.shape
    half_thickness = int(thickness / 2)
    vertical_mid_point = int(width / 2)
    horizontal_mid_point = int(height / 2)

    top_border_y = None
    for i in range(height):
        current_pixel_color = img_array[i][horizontal_mid_point]
        if current_pixel_color == Color.BLACK.value:
            top_border_y = i + half_thickness
            break

    right_border_x = None
    for i in range(width - 1, 0, -1):
        current_pixel_color = img_array[vertical_mid_point][i]
        if current_pixel_color == Color.BLACK.value:
            right_border_x = i - half_thickness
            break

    bot_border_y = None
    for i in range(height - 1, 0, -1):
        current_pixel_color = img_array[i][horizontal_mid_point]
        if current_pixel_color == Color.BLACK.value:
            bot_border_y = i - half_thickness
            break

    left_border_x = None
    for i in range(width):
        current_pixel_color = img_array[vertical_mid_point][i]
        if current_pixel_color == Color.BLACK.value:
            left_border_x = i + half_thickness
            break

    return top_border_y, right_border_x, bot_border_y, left_border_x


if __name__ == '__main__':
    main()
