import time

import numpy as np
from PIL import Image as Im
from Maze import Maze
from factory import create_solver


class CannotCompleteError(Exception):
    """A custom exception class."""
    pass


def maze_solver(image, algo):
    start_time = time.time()
    maze = Maze(image)
    maze_time = time.time() - start_time
    print(f"Initializing the maze: {maze_time} seconds.")

    solver = create_solver(algo)

    start_time = time.time()
    path, is_completed = solver(maze)
    solving_time = time.time() - start_time
    print(f"Solving the maze: {solving_time} seconds.")

    if not is_completed:
        raise CannotCompleteError(algo, path)

    start_time = time.time()
    large_image = enlarge_image(draw(image, path))
    enlarging_time = time.time() - start_time
    print(f"Drawing the solution & Enlarging the image: {enlarging_time} seconds.\n")

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
    Identify backtracking occurrences in a path, considering dead-ends as backtracking, but the first
    (and last) cell is not considered backtracking.

    Parameters:
    - path (list): The path to analyze for backtracking.

    Returns:
    - tuple: A tuple containing two lists:
    - List of unique cells on the main path.
    - List of cells where backtracking occurred.

    Example:
    path = [(0, 0), (1, 0), (2, 0), (1, 0), (0, 0)]
    unique_cells, backtracking_cells = find_backtracking(path)

    unique_cells == [(0, 0)]
    backtracking_cells == [(1, 0), (2, 0)]
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
    Manually enlarge an image without interpolation, suitable for BMP images to maintain pixel integrity.

    Note:
    Since Pillow interpolates to fill the gaps and stretches existing pixels,
    it is not suitable for enlarging BMP images to a proper size.
    This manual enlargement preserves pixel integrity without interpolation.
    """

    original_width, original_height = image.size
    size = 600  # if one of the dimensions is smaller than size, enlarge the image for better viewing experience

    scale_factor = int(max(size / min(original_width, original_height), 1))

    if scale_factor == 1:  # image larger than size, no need to enlarge
        return image

    enlarged_image = Im.new('RGB', (original_width * scale_factor, original_height * scale_factor))

    for x in range(original_width):
        for y in range(original_height):
            original_pixel = image.getpixel((x, y))

            for i in range(int(scale_factor)):
                for j in range(int(scale_factor)):
                    enlarged_image.putpixel((int(x * scale_factor) + i, int(y * scale_factor) + j), original_pixel)

    return enlarged_image
