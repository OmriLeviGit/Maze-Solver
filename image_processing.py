from CONST import WHITE, BLACK, THRESHOLD

from PIL import Image
import numpy as np


def process_and_enhance_image(image):
    thresholded_image = image.convert("L").point(lambda pixel: WHITE if pixel > THRESHOLD else BLACK, "L")
    image_array = np.array(thresholded_image)
    is_processed = True

    # if there is only one white cell in the first row, it is a generated maze and the image was not processed
    if np.sum(image_array[0] == WHITE) == 1:
        return thresholded_image, not is_processed

    smoothed_array = apply_smoothing(image_array)
    cropped_array = crop_maze(smoothed_array)

    return Image.fromarray(cropped_array), is_processed


def apply_smoothing(array):
    """
    Apply a smoothing operation to a 2D NumPy array.

    The function iteratively performs a smoothing operation on the input array until no more changes are made.
    Smoothing is applied to eliminate black pixels that are sticking out by checking their surrounding pixels.

    The smoothing operation is performed in both rows and columns.

    Parameters:
    - array (numpy.ndarray): The input 2D array representing an image.

    Returns:
    - numpy.ndarray: The smoothed array with black pixels eliminated
     """

    new_array = array.copy()

    def pixel_is_valid(y_val, x_val):
        """
        Checks if a black pixel is invalid, and needs to be smoothed out.

        An invalid pixel is defined as a black pixel surrounded by 3 white pixels, creating a 2x2 square,
        but cannot create a 3x3 isosceles triangle where the pixel itself is in the middle of the base.
        """

        top_left = new_array[y_val - 1][x_val - 1] == WHITE
        top = new_array[y_val - 1][x_val] == WHITE
        top_right = new_array[y_val - 1][x_val + 1] == WHITE
        right = new_array[y_val][x_val + 1] == WHITE
        bot_right = new_array[y_val + 1][x_val + 1] == WHITE
        bot = new_array[y_val + 1][x_val] == WHITE
        bot_left = new_array[y_val + 1][x_val - 1] == WHITE
        left = new_array[y_val][x_val - 1] == WHITE

        if top and top_right and right and (not top_left or not bot_right):
            return False

        if right and bot_right and bot and (not top_right or not bot_left):
            return False

        if bot and bot_left and left and (not bot_right or not top_left):
            return False

        if left and top_left and top and (not bot_left or not top_right):
            return False

        return True

    num_rows, num_cols = new_array.shape
    changes_made = True

    # Smooth until no change is made, since vertical smoothing may interfere with horizontal smoothing and vice versa
    while changes_made:
        changes_made = False

        # Process rows
        for i in range(1, num_rows - 1):
            for j in range(1, num_cols - 1):
                while new_array[i][j] == 0:
                    if pixel_is_valid(i, j):
                        break

                    new_array[i][j] = WHITE
                    j -= 1      # move back to the previous column
                    changes_made = True

                j += 1          # move to the next column

        # Process columns
        for j in range(1, num_cols - 1):
            i = 1               # initialize i for each column
            backward_steps = 0  # track backward steps

            while i < num_rows - 1:
                while new_array[i][j] == 0:
                    if pixel_is_valid(i, j):
                        break

                    new_array[i][j] = WHITE
                    i -= 1      # move back to the previous row
                    backward_steps += 1
                    changes_made = True

                i += 1 + backward_steps     # move to the next row
                backward_steps = 0          # reset backward steps

    return new_array


def crop_maze(array):
    top = 0
    while np.all(array[top] == WHITE):
        top += 1

    right = array.shape[1] - 1
    while np.all(array[:, right] == WHITE):
        right -= 1

    bot = array.shape[0] - 1
    while np.all(array[bot] == WHITE):
        bot -= 1

    left = 0
    while np.all(array[:, left] == WHITE):
        left += 1

    # Uneven top row
    while True:
        color_change_count = 0
        for i in range(left, right - 1):
            if (array[top, i] == WHITE and array[top, i + 1] == BLACK
                    or array[top, i] == BLACK and array[top, i + 1] == WHITE):
                color_change_count += 1

        if color_change_count == 1:
            top += 1
        else:
            break

    # Uneven right col
    while True:
        color_change_count = 0
        for i in range(top, bot - 1):
            if (array[i, right] == WHITE and array[i + 1, right] == BLACK
                    or array[i, right] == BLACK and array[i + 1, right] == WHITE):
                color_change_count += 1

        if color_change_count == 1:
            right -= 1
        else:
            break

    # Uneven bot row
    while True:
        color_change_count = 0
        for i in range(left, right - 1):
            if (array[bot, i] == WHITE and array[bot, i + 1] == BLACK
                    or array[bot, i] == BLACK and array[bot, i + 1] == WHITE):
                color_change_count += 1

        if color_change_count == 1:
            bot -= 1
        else:
            break

    # Uneven left col
    while True:
        color_change_count = 0
        for i in range(top, bot - 1):
            if (array[i, left] == WHITE and array[i + 1, left] == BLACK
                    or array[i, left] == BLACK and array[i + 1, left] == WHITE):
                color_change_count += 1

        if color_change_count == 1:
            left += 1
        else:
            break

    return array[top:bot, left:right]
