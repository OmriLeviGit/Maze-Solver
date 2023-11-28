from PIL import Image as Im

from Maze import Maze


"""
workflow:
1. convert the array to only black white and red
2. draw a line from the middle to find the closest black line
3. circle the maze to find both the entrance and the exit:
    go to the right, if there is no right go to the bottom, if there is no bottom continue, while counting all 
    white pixels  until black or hit end of the screen.
4. the size of the entrance determine a block size, divide the maze into square grids
5. the middle of each grid is where each step is taken, and the size of each step is the size of the grid.
6. execute the algorithm
"""


def main():
    path = "img/small_perfect.bmp"
    image = Im.open(path).convert("L")
    maze = Maze(image)

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
