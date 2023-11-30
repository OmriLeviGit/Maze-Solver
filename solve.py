import numpy as np
from PIL import Image as Im
import bfs
from Maze import Maze


def solve(image):
    maze = Maze(image)

    path, is_completed = bfs.solve(maze)

    if not is_completed:
        return -1

    large_image = enlarge_image(draw(image, path))
    large_image.show()



def draw(image, path):
    image_array = np.array(image.convert('RGB')).astype(np.uint8)

    prev = path[0]
    for node in path:
        y, x = node
        y_prev, x_prev = prev

        min_y, max_y = min(y, y_prev), max(y, y_prev)
        min_x, max_x = min(x, x_prev), max(x, x_prev)

        # the slicing operation will result in an empty array if  either min_y == max_y or min_x == max_x
        if min_y == max_y:
            image_array[min_y, min_x:max_x] = [0, 255, 0]
        elif min_x == max_x:
            image_array[min_y:max_y, min_x] = [0, 255, 0]
        image_array[y, x] = [0, 255, 0]

        prev = node

    return Im.fromarray(image_array)




def enlarge_image(image):
    original_width, original_height = image.size
    max_size = 800

    scale_factor = int(max_size / min(original_width, original_height))
    enlarged_image = Im.new('RGB', (original_width * scale_factor, original_height * scale_factor))

    for x in range(original_width):
        for y in range(original_height):
            original_pixel = image.getpixel((x, y))
            for i in range(int(scale_factor)):
                for j in range(int(scale_factor)):
                    enlarged_image.putpixel((int(x * scale_factor) + i, int(y * scale_factor) + j), original_pixel)
    return enlarged_image
