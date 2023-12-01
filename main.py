from PIL import Image as Im
from process import process


# TODO fix the draw function to work on both lht and bfs

def main():
    path = "img/small_perfect.bmp"
    image = None

    try:
        image = Im.open(path).convert("L")
        process(image)
    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if image is not None:
            image.close()


if __name__ == '__main__':
    main()
