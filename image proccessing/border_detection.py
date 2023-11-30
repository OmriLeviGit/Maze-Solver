from enum import Enum
from ordered_enum import OrderedEnum

from Line import Line
from Point import Point


class Border(OrderedEnum):
    TOP = 0
    RIGHT = 1
    BOT = 2
    LEFT = 3


class Color(Enum):
    BLACK = 0
    WHITE = 255
    THRESH = 127





"""
def main():
    # THIS IS USING CV2 AND IMAGE PROCESSING
    path = "img/square-maze-game-for-kids-free-vector.jpg"

    img = cv2.imread(path)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    threshold = 127
    lower = np.array([0, 0, 0])
    higher = np.array([250, 250, 250])

    mask = cv2.inRange(img, lower, higher)

    cont, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cont_img = cv2.drawContours(img, cont, -1, 255, 3)

    c = max(cont, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)

    plt.imshow(img)
    plt.show()
"""
"""
    # open image, binarize, and convert it into a nd.array for easier and faster processing
path = "img/square-maze-game-for-kids-free-vector.jpg"
image_original = Im.open(path)
image_grayscale = image_original.convert("L")

threshold = 128
image = image_grayscale.point(lambda pixel: Color.WHITE.value if pixel > threshold else Color.BLACK.value)
image_array = np.array(image)

thickness = get_border_thickness(image_array)
borders = get_borders_info(image_array, thickness)
tunnel_width = get_tunnel_width(image_array, borders, thickness)

start_point, end_point = find_openings(image_array, borders)
# draw start and end points
image_array[start_point.get_y()][start_point.get_x()] = False
image_array[end_point.get_y()][end_point.get_x()] = False

new_img = Im.fromarray(image_array)
new_img.show()

"""


def find_openings(img_array, borders):
    entrances = []

    # horizontal entrances
    horizontal_borders = [borders[Border.TOP.value], borders[Border.BOT.value]]
    for border_y in horizontal_borders:
        entrance_start = None
        entrance_end = None

        for i in range(borders[Border.LEFT.value], borders[Border.RIGHT.value]):
            pixel_color = img_array[border_y, i]

            if pixel_color == Color.WHITE.value and entrance_start is None:
                entrance_start = i

            if pixel_color == Color.BLACK.value and entrance_start is not None:
                entrance_end = i
                break

        if entrance_start is not None and entrance_end is not None:
            start_point = Point(entrance_start, border_y)
            end_point = Point(entrance_end, border_y)

            entrance_mid_point = Line(start_point, end_point).middle_point()
            entrances.append(entrance_mid_point)

    # vertical entrances
    vertical_borders = [borders[Border.LEFT.value], borders[Border.RIGHT.value]]
    for border_x in vertical_borders:
        entrance_start = None
        entrance_end = None

        for i in range(borders[Border.TOP.value], borders[Border.BOT.value]):
            pixel_color = img_array[i, border_x]

            if pixel_color == Color.WHITE.value and entrance_start is None:
                entrance_start = i

            if pixel_color == Color.BLACK.value and entrance_start is not None:
                entrance_end = i
                break

        if entrance_start is not None and entrance_end is not None:
            start_point = Point(border_x, entrance_start)
            end_point = Point(border_x, entrance_end)

            entrance_mid_point = Line(start_point, end_point).middle_point()
            entrances.append(entrance_mid_point)

    return entrances[0], entrances[1]


def get_border_thickness(img_array):
    _, height = img_array.shape
    horizontal_mid_point = int(height / 2)

    thickness = 0
    for i in range(height):
        current_pixel_color = img_array[i][horizontal_mid_point]
        if current_pixel_color == Color.BLACK.value:
            thickness += 1

        if current_pixel_color == Color.WHITE.value and thickness > 0:
            break

    return thickness


def get_tunnel_width(img_array, borders, thickness):
    top_border = int(borders[Border.TOP.value] + thickness / 2)
    width, height = img_array.shape
    vertical_mid_point = int(width / 2)

    tunnel_width = 0
    while img_array[top_border + tunnel_width][vertical_mid_point] == Color.WHITE.value:
        tunnel_width += 1

    return tunnel_width


def get_borders_info(img_array, thickness):
    width, height = img_array.shape
    half_thickness = int(thickness / 2)
    vertical_mid_point = int(width / 2)
    horizontal_mid_point = int(height / 2)

    top_border_y = None
    for i in range(height):
        current_pixel_color = img_array[i][horizontal_mid_point]
        if current_pixel_color == Color.BLACK.value:
            top_border_y = i + half_thickness
            break

    right_border_x = None
    for i in range(width - 1, 0, -1):
        current_pixel_color = img_array[vertical_mid_point][i]
        if current_pixel_color == Color.BLACK.value:
            right_border_x = i - half_thickness
            break

    bot_border_y = None
    for i in range(height - 1, 0, -1):
        current_pixel_color = img_array[i][horizontal_mid_point]
        if current_pixel_color == Color.BLACK.value:
            bot_border_y = i - half_thickness
            break

    left_border_x = None
    for i in range(width):
        current_pixel_color = img_array[vertical_mid_point][i]
        if current_pixel_color == Color.BLACK.value:
            left_border_x = i + half_thickness
            break

    return top_border_y, right_border_x, bot_border_y, left_border_x
