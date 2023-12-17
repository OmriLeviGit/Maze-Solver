from CONST import WHITE, BLACK, THRESHOLD

from PIL import Image
import numpy as np

from utils import trim_white_borders


def process_and_enhance_image(image):
    thresholded_image = image.convert("L").point(lambda pixel: WHITE if pixel > THRESHOLD else BLACK, "L")
    image_array = np.array(thresholded_image)

    # if there is only one white cell in the first row, it is a generated maze and the image was not processed
    if np.sum(image_array[0] == WHITE) == 1:
        return image, False

    processed_array = trim_white_borders(clean_up_correction(apply_smoothing(clean_up_array_duplicates(image_array))))

    return Image.fromarray(processed_array), True


def clean_up_array_duplicates(array):
    """
    Remove duplicate rows and columns from a 2D NumPy array.

    Parameters:
    - array (numpy.ndarray): The input 2D array.

    Returns:
    - numpy.ndarray: The array with duplicate rows and columns removed.
    """

    # Clean up rows
    prev_row = 0
    temp_array = np.empty((0, array.shape[1]))  # Initialize as an empty array with the original number of columns

    # Iterate through rows
    for i in range(1, array.shape[0]):

        # Check if the previous row is equal to the next row
        if not np.array_equal(array[prev_row], array[i]):
            # If not equal, add the previous row to the new array
            temp_array = np.vstack((temp_array, array[prev_row]))
            prev_row = i  # Update the previous row index

    # Add the last row to the new array
    temp_array = np.vstack((temp_array, array[prev_row]))

    # Clean up columns on the new array
    prev_col = 0
    no_duplicates = np.empty((temp_array.shape[0], 0))  # Initialize as an empty array with the new number of rows

    # Add the first column to the new array
    no_duplicates = np.hstack((no_duplicates, temp_array[:, prev_col][:, None]))

    # Iterate through columns
    for i in range(1, temp_array.shape[1]):

        # Check if the previous column is equal to the next column
        if not np.array_equal(temp_array[:, prev_col], temp_array[:, i]):
            # If not equal, add the previous column to the new array
            no_duplicates = np.hstack((no_duplicates, temp_array[:, i][:, None]))
            prev_col = i  # Update the previous column index

    # Reshape to 2D
    no_duplicates = no_duplicates.reshape((temp_array.shape[0], -1))

    return no_duplicates


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


def clean_up_correction(array):
    """
    Perform correction after smoothing and duplicate removal to avoid shifting walls in the maze.

    The process involves scanning rows and columns, checking for alternating black and white patterns,
    and reconstructing a corrected array to mitigate potential shifts caused by smoothing and removal of duplicates.

    Parameters:
    - array (numpy.ndarray): The 2D array representing the maze.

    Returns:
    - numpy.ndarray: The corrected array after the cleanup process.
    """
    # Scan Rows
    num_rows, num_cols = array.shape
    temp_array = np.array([array[0]])

    backward_steps = 0  # Tracks the number of rows to skip when comparing rows for copying into the new array

    # Check for alternating black and white patterns in adjacent rows
    for i in range(num_rows - 2):
        row_is_added = False

        for j in range(num_cols):
            # If alternating pattern found, add the current row to the temp array
            last_added = temp_array[i - backward_steps][j]
            alternating_pattern = last_added == array[i + 2][j] != array[i + 1][j]

            if alternating_pattern:
                temp_array = np.vstack((temp_array, array[i + 1, :]))
                row_is_added = True
                break

        if not row_is_added:
            backward_steps += 1

    temp_array = np.vstack((temp_array, array[-1]))     # Add last row

    # Scan Columns
    num_rows, num_cols = temp_array.shape
    new_array = np.array([temp_array[:, 0]])
    new_array = new_array.T

    backward_steps = 0  # Tracks the number of rows to skip when comparing rows for copying into the new array

    # Check for alternating black and white patterns in adjacent columns
    for i in range(num_cols - 2):
        col_is_added = False
        for j in range(num_rows):
            # If alternating pattern found, add the current column to the new array
            last_added = new_array[j][i - backward_steps]
            alternating_pattern = last_added == temp_array[j][i + 2] != temp_array[j][i + 1]

            if alternating_pattern:
                new_array = np.hstack((new_array, temp_array[:, i + 1][:, None]))
                col_is_added = True
                break

        if not col_is_added:
            backward_steps += 1

    new_array = np.hstack((new_array, temp_array[:, -1][:, None]))     # Add last column

    return new_array
