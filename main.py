import os
import sys

from PIL import Image as Im

from process import process, CannotCompleteError


def main():
    image = None
    solved_maze = None
    algorithms = ["breadth first search", "depth first search", "left hand turn"]

    # default
    image_path = "input/101x101, Medium.bmp"
    chosen_algo = algorithms[2]

    if len(sys.argv) > 0 and len(sys.argv) == 3:
        image_path = sys.argv[1]                    # First command-line argument
        chosen_algo = sys.argv[2]                   # Second command-line argument
    else:
        print(f"Using the default maze \"{image_path}\" and algorithm \"{chosen_algo}\".")

    image_name, _ = os.path.splitext(os.path.basename(image_path))

    try:
        image = Im.open(image_path).convert("L")
        solved_maze = process(image, chosen_algo)
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
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

        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        solved_maze.save(f"output/{image_name} - {chosen_algo}.jpg", format="JPEG")


if __name__ == '__main__':
    main()
