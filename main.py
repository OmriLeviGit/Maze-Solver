from PIL import Image as Im
from solve import solve
from timeit import timeit


# TODO make a factory

def main():
    path = "img/very_large_perfect.bmp"
    image = None

    try:
        image = Im.open(path).convert("L")
        print(timeit(lambda: solve(image), number=1))
    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if image is not None:
            image.close()


if __name__ == '__main__':
    main()
