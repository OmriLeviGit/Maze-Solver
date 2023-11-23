import numpy as np
from PIL import Image as im
from aenum import Enum, auto


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


class Border(Enum):
    TOP = 0
    RIGHT = auto()
    BOTTOM = auto()
    LEFT = auto()


class Color(Enum):
    White = 0
    Black = 255


def main():
    # open image, convert to black and white and into a nd.array
    path = "img/square-maze-game-for-kids-free-vector.jpg"
    img_original = im.open(path)
    img = img_original.convert("L")  # convert to black and white to speed up calculations
    img_array = np.array(img)

    borders = borders_location(img_array)
    start, end = find_openings(img_array, borders)
    thickness = border_thickness(img_array, borders)

    # draw borders
    img_array[borders[0]] = [0]
    img_array[:, borders[1]] = [0]
    img_array[borders[2]] = [0]
    img_array[:, borders[3]] = [0]

    new_img = im.fromarray(img_array)
    new_img.show()

    """
    img_array[325] = [1]
    new_img = Image.fromarray(img_array)
    new_img.show()

    print(img_array)
    """
    img_original.close()


def find_openings(img_array, borders):
    start = borders[Border.LEFT]
    end = borders[Border.Right]

    i = 0
    entrance = 1
    entrance_length = 0
    for i in range(start, end):
        pixel_color = img_array[borders[Border.TOP], start + i]

        if entrance_length != 0 and pixel_color == Color.Black:
            break

        if pixel_color == Color.White:
            entrance_length += 1

    maze_start = 1
    maze_end = 1
    return maze_start, maze_end


def borders_location(img_array):
    width, height = img_array.shape

    vertical_mid_point = int(width / 2)
    horizontal_mid_point = int(height / 2)

    top_border_y = 0
    for i in range(height):
        current_pixel_color = img_array[i][horizontal_mid_point]
        if current_pixel_color < Color.Black:
            top_border_y = i
            break

    right_border_x = 0
    for i in range(width - 1, 0, -1):
        current_pixel_color = img_array[vertical_mid_point][i]
        if current_pixel_color < Color.Black:
            right_border_x = i
            break

    bot_border_y = 0
    for i in range(height - 1, 0, -1):
        current_pixel_color = img_array[i][horizontal_mid_point]
        if current_pixel_color < Color.Black:
            bot_border_y = i
            break

    left_border_x = 0
    for i in range(width):
        current_pixel_color = img_array[vertical_mid_point][i]
        if current_pixel_color < Color.Black:
            left_border_x = i
            break

    return top_border_y, right_border_x, bot_border_y, left_border_x


def border_thickness(array, borders):
    avg = int((borders[Border.RIGHT] + borders[Border.LEFT]) / 2)
    thickness = 0
    while array[borders[Border.TOP] + thickness, avg] != 0:
        thickness += 1
    return thickness


if __name__ == '__main__':
    main()
