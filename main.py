import os

import argcomplete
import argparse
from PIL import Image as Im

from process import process, CannotCompleteError


def main():
    image = None
    solved_maze = None
    algorithms = ["breadth first search", "depth first search", "left hand turn"]

    default_algo = algorithms[2]
    default_image = "101x101, Medium.bmp"

    default_algo = algorithms[0]
    default_image = "1001x1001, Huge.bmp"

    parser = argparse.ArgumentParser()
    parser.add_argument("image_name",
                        help="Image name without path", nargs="?", default=default_image)
    parser.add_argument("algorithm",
                        help="Algorithm to use", choices=algorithms, nargs="?", default=default_algo)
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    image_name = args.image_name
    chosen_algo = args.algorithm

    try:
        image_path = os.path.join("input", image_name)

        image = Im.open(image_path).convert("L")
        image_name, _ = os.path.splitext(os.path.basename(image_path))
        solved_maze = process(image, chosen_algo)
    except FileNotFoundError:
        print(f"Error: The file {image_name} was not found.")
    except CannotCompleteError as e:
        print(f"Error: The maze could not be completed using the \"{e.args[0]}\" algorithm.")
        print(f"Path: {e.args[1]}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if image is not None:
            image.close()

    if solved_maze:
        solved_maze.show()
        solved_maze.save(f"output/{image_name} - {chosen_algo}.jpg", format="JPEG")


if __name__ == '__main__':
    main()
