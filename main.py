import os

from PIL import Image as Im
from process import process, CannotCompleteError


# TODO fix the draw function to work on both lht and bfs

def main():
    path = "img/very_large_perfect.bmp"
    image = None
    algorithms = ["breadth first search", "depth first search", "left hand turn"]

    try:
        image = Im.open(path).convert("L")
        process(image, algorithms[2])
    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
    except CannotCompleteError as e:
        print(f"Error: The maze could not be completed using the \"{e.args[0]}\" algorithm.")
        print(f"Path: {e.args[1]}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if image is not None:
            image.close()


if __name__ == '__main__':
    main()
