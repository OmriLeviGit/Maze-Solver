import numpy as np
from PIL import Image as Im
import timeit
import bfs
from Maze import Maze

"""
execute solution:
get output like from bfs

1:
check if completed

2:
if performance is good:
    convert to rgb -> draw path -> enlarge
    # wont look at good, but A LOT easier

else: 
    enlarge image -> convert to rgb dtype int16 -> draw path

3:
return image
"""


def organize(image):
    maze = Maze(image)

    path, is_completed = bfs.solve(maze)

    if not is_completed:
        return -1


    large_image = enlarge_image(draw(image, path))
    large_image.show()





def draw(image, path):
    image_array = np.array(image.convert('RGB'))

    for node in path:
        y, x = node
        image_array[y, x] = [0, 255, 0]

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
