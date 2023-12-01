import timeit

import numpy as np
from PIL import Image as Im
from Maze import Maze
from algo_factory import create_solver


def process(image):
    maze_time = timeit.default_timer()

    maze = Maze(image)

    print(f"Maze building time: {timeit.default_timer() - maze_time} seconds")

    solver = create_solver("lht")

    solver1 = create_solver("bfs")      # delete

    solver_time = timeit.default_timer()

    path, is_completed = solver(maze)
    path1, is_completed1 = solver1(maze)      # delete

    print(f"Solving time: {timeit.default_timer() - solver_time} seconds")

    if not is_completed:
        return -1

    enlarge_time = timeit.default_timer()

    large_image = enlarge_image(draw(image, path))
    large_image1 = enlarge_image(draw(image, path1))      # delete

    print(f"Enlarging: {timeit.default_timer() - enlarge_time} seconds")

    print(f"Overall: {timeit.default_timer() - maze_time} seconds")

    large_image.show()
    large_image1.show()      # delete


# works for left hand turn but not the rest
# def draw(image, path):
#     image_array = np.array(image.convert('RGB')).astype(np.uint8)
#
#     # define colors for solution and backtracking
#     solution_color = [0, 255, 0]
#     backtracking_color = [0, 64, 0]
#
#     # flag to track the first occurrence of a duplicated node
#     duplicate_flag = False
#
#     for i, node in enumerate(path):
#         y, x = node
#
#         is_duplicate = path.count(node) > 1
#         color = backtracking_color if is_duplicate else solution_color
#
#         # if the current node is part of a duplicate substring, and it's the first occurrence, color as if not duplicate
#         if is_duplicate and not duplicate_flag:
#             image_array[y, x] = solution_color
#             duplicate_flag = True
#
#         # if the current node is part of a duplicate substring, find the range of indices for this substring
#         if is_duplicate:
#             start_index = path.index(node)
#             reversed_path = path[::-1]
#             first_occurrence_index = reversed_path.index(node)
#             end_index = len(path) - 1 - first_occurrence_index
#
#             # color everything between the first and last occurrence of the node
#             for j in range(start_index + 1, end_index):
#                 y_sub, x_sub = path[j]
#                 image_array[y_sub, x_sub] = color
#         else:
#             # if the current node is not part of a duplicate substring, color it with the determined color
#             image_array[y, x] = color
#             duplicate_flag = False
#
#     return Im.fromarray(image_array)


def draw(image, path):
    image_array = np.array(image.convert('RGB')).astype(np.uint8)
    print(path)

    prev = path[0]
    for node in path:
        solution_color = [0, 255, 0]
        backtracking_color = [0, 64, 0]

        y, x = node
        y_prev, x_prev = prev

        min_y, max_y = min(y, y_prev), max(y, y_prev)
        min_x, max_x = min(x, x_prev), max(x, x_prev)

        is_duplicate = path.count(node) > 1
        color = backtracking_color if is_duplicate else solution_color

        # the slicing operation will result in an empty array if  either min_y == max_y or min_x == max_x
        if min_y == max_y:
            image_array[min_y, min_x:max_x] = color
        elif min_x == max_x:
            image_array[min_y:max_y, min_x] = color
        image_array[y, x] = color

        prev = node

    return Im.fromarray(image_array)




def enlarge_image(image):
    original_width, original_height = image.size
    max_size = 800

    scale_factor = int(max_size / min(original_width, original_height))
    enlarged_image = Im.new('RGB', (original_width * scale_factor, original_height * scale_factor))

    for x in range(original_width):
        for y in range(original_height):
            original_pixel = image.getpixel((x, y))
            for i in range(int(scale_factor)):
                for j in range(int(scale_factor)):
                    enlarged_image.putpixel((int(x * scale_factor) + i, int(y * scale_factor) + j), original_pixel)
    return enlarged_image
