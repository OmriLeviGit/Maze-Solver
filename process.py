import time

import numpy as np
from PIL import Image as Im
from Maze import Maze
from algo_factory import create_solver


class CannotCompleteError(Exception):
    """A custom exception class."""
    pass


def process(image, algo):
    start_time = time.time()
    maze = Maze(image)
    maze_time = time.time() - start_time

    solver = create_solver(algo)

    start_time = time.time()
    path, is_completed = solver(maze)
    solving_time = time.time() - start_time

    if not is_completed:
        raise CannotCompleteError(algo, path)

    start_time = time.time()
    large_image = enlarge_image(draw(image, path))
    enlarging_time = time.time() - start_time

    print(f"Building the maze: {maze_time} seconds\n"
          f"Solving the maze: {solving_time} seconds\n"
          f"Drawing the solution & enlarging the image: {enlarging_time} seconds")
    return large_image


def draw(image, path):
    image_array = np.array(image.convert('RGB')).astype(np.uint8)

    solution_color = [0, 255, 0]
    backtracking_color = [0, 64, 0]

    unique, backtracking = find_backtracking(path)

    prev = path[0]
    for position in path:
        y, x = position
        y_prev, x_prev = prev

        min_y, max_y = min(y, y_prev), max(y, y_prev)
        min_x, max_x = min(x, x_prev), max(x, x_prev)

        color = None

        if position in unique:
            if prev not in backtracking:
                color = solution_color
        else:
            color = backtracking_color

        if color is not None:
            image_array[min_y:max_y + 1, min_x:max_x + 1] = color

        prev = position

    return Im.fromarray(image_array)


def find_backtracking(path):
    """
    Finds which parts of the path are appearing twice, therefore backtracking occurred there.
    This is different from simply checking for duplicates, since the main path should be counted as 'unique' for
    coloring, and dead-ends also need to be counted as backtracking.
    Each sublist begins and ends with backtracked cells, not including the entrance to the sublist on the main path
    """

    unique = []
    backtracking = []

    for i, position in enumerate(path):
        # start index of sub-lists of duplicates, where everything between the start and the end is a backtracked path
        sublist_start = None
        sublist_end = None

        if (position in unique) and (position not in backtracking):
            unique.remove(position)
            backtracking.append(position)
        else:
            # move the first position in each backtracking sub-list to unique because it's a part of the main path
            if path[i - 1] in backtracking:
                sublist_start = path.index(path[i - 1]) + 1
                sublist_end = i - 1

                backtracking.remove(path[i - 1])
                unique.append(path[i - 1])
            unique.append(position)


        # if sublist detected, every position inside it is defined as a backtracked cell
        if sublist_start is not None:
            for j in range(sublist_start, sublist_end):
                curr = path[j]
                if curr in unique:
                    unique.remove(curr)
                    backtracking.append(curr)

    return unique, backtracking


def enlarge_image(image):
    """
    A manual enlarging function. Since Pillow interpolates to fill the gaps and stretches existing pixels,
    therefore not suitable for enlarging bmp to a proper size.
    """

    original_width, original_height = image.size
    size = 800      # if the image would be smaller than 800 x 800, enlarge it for better viewing experience

    scale_factor = int(max(size / min(original_width, original_height), 1))
    enlarged_image = Im.new('RGB', (original_width * scale_factor, original_height * scale_factor))

    for x in range(original_width):
        for y in range(original_height):
            original_pixel = image.getpixel((x, y))
            for i in range(int(scale_factor)):
                for j in range(int(scale_factor)):
                    enlarged_image.putpixel((int(x * scale_factor) + i, int(y * scale_factor) + j), original_pixel)

    return enlarged_image
