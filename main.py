from PIL import Image as Im

import bfs
from Maze import Maze


def main():
    path = "img/small_perfect.bmp"
    image = Im.open(path).convert("L")
    maze = Maze(image)

    bfs.solve(maze)



    array = maze.array
    nodes = maze.nodes

    for node in nodes:
        x, y = node.coordinate
        array[x, y] = 127

    # Get the original width and height
    original_width, original_height = image.size

    # Double the size
    new_width = original_width * 100
    new_height = original_height * 100

    new_image = Im.fromarray(array)

    # Resize the image
    resized_image = new_image.resize((new_width, new_height))
    resized_image.show()


if __name__ == '__main__':
    main()
