import os

from PIL import Image as Im
from process import process, CannotCompleteError


def test():
    """
    not an actual test, but just runs every image with every algorithm
    """

    image = None
    algorithms = ["breadth first search", "depth first search", "left hand turn"]

    files = [f for f in os.listdir("img") if os.path.isfile(os.path.join("img", f))]

    for file in files:
        path = os.path.join("img", file)
        for algo in algorithms:
            try:
                image = Im.open(path).convert("L")
                process(image, algo)
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
    test()
