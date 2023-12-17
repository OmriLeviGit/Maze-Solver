import os
import sys

from PIL import Image as Im

from maze_solver import maze_solver, CannotCompleteMazeError
from image_conversion import process_and_enhance_image

# todo remove comment return from image_conversion


def solve_maze(image_path, chosen_algo):
    image = None

    try:
        image = Im.open(image_path).convert("L")
        processed_image = process_and_enhance_image(image)

        return maze_solver(processed_image, chosen_algo)
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
    except CannotCompleteMazeError as e:
        print(f"Error: The maze could not be completed using the \"{e.args[0]}\" algorithm.")
        print(f"Path: {e.args[1]}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if image is not None:
            image.close()

    return None


def main():
    # list of available algorithms
    algorithms = ["breadth first search", "depth first search", "left hand turn", "dijkstra", "a star"]

    # default values
    image_path = "input/101x101, Medium.bmp"
    chosen_algo = algorithms[0]
    solving_message = f"Solving the default maze \"{image_path}\" using the algorithm \"{chosen_algo}\":"

    # check for command-line arguments
    if len(sys.argv) == 3:
        image_path = sys.argv[1]  # First command-line argument
        chosen_algo = sys.argv[2]  # Second command-line argument
        solving_message = f"Solving the maze \"{image_path}\" using the algorithm \"{chosen_algo}\":"

    print(solving_message, "\n")
    image_name, _ = os.path.splitext(os.path.basename(image_path))

    # call solve_maze function to handle maze solving and potential errors
    solved_maze = solve_maze(image_path, chosen_algo)

    # check if the maze was successfully solved
    if solved_maze:
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_path = os.path.join(output_folder, f"{image_name.title()} - {chosen_algo.title()}.jpg")

        solved_maze.save(output_path, format="JPEG")
        print(f"Solution saved to {output_path}.")

    solved_maze.show()


if __name__ == '__main__':
    main()
