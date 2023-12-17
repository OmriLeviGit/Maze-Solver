import time

from Maze import Maze
from factory import create_solver
from image_processing import process_and_enhance_image
from utils import enlarge_image, draw


class CannotCompleteMazeError(Exception):
    """A custom exception class."""
    pass


def maze_solver(image, algo):
    processed_image = process_and_time(image, process_and_enhance_image, f"Processing the image")
    maze = process_and_time(processed_image, Maze, f"Initializing the maze")
    solver = create_solver(algo)
    path, is_completed = process_and_time(maze, solver, "Solving the maze")

    if not is_completed:
        raise CannotCompleteMazeError(algo, path)

    enlarged_image = process_and_time((processed_image, path, algo),
                                      lambda args: enlarge_image(draw(*args)),
                                      "Drawing the solution & Enlarging the image")
    return enlarged_image


def process_and_time(data, func, message):
    start_time = time.time()
    result = func(data)
    elapsed_time = time.time() - start_time
    print(f"{message}: {elapsed_time} seconds.")
    return result
