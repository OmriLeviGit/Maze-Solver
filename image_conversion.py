from maze_solver import enlarge_image

from PIL import Image
import numpy as np


def process_image(image):
    image = Image.open("img/maze2jpg").convert("L")
    threshold = 127
    image = image.point(lambda pixel: 0 if pixel < threshold else 255, "L")

    array = np.array(image)
    array = remove_duplicate_rows_and_columns(array)  # speed up the smoothing function

    smooth(array)
    array = trio_scan(array)

    array = remove_duplicate_rows_and_columns(array)  # smoothing may create duplicates

    new_image = Image.fromarray(array).convert("RGB")
    large = enlarge_image(new_image)
    large.show()
    large.save("output/test2.jpg", format="JPEG")


if __name__ == '__main__':
    process_image()


def remove_duplicate_rows_and_columns(array):
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

def smooth(array):
    def pixel_is_valid(array, num_rows, num_cols):
        white = 255

        top_left = array[num_rows - 1][num_cols - 1] == white
        top = array[num_rows - 1][num_cols] == white
        top_right = array[num_rows - 1][num_cols + 1] == white
        right = array[num_rows][num_cols + 1] == white
        bot_right = array[num_rows + 1][num_cols + 1] == white
        bot = array[num_rows + 1][num_cols] == white
        bot_left = array[num_rows + 1][num_cols - 1] == white
        left = array[num_rows][num_cols - 1] == white

        if top and top_right and right and (not top_left or not bot_right):
            return False

        if right and bot_right and bot and (not top_right or not bot_left):
            return False

        if bot and bot_left and left and (not bot_right or not top_left):
            return False

        if left and top_left and top and (not bot_left or not top_right):
            return False

        return True

    num_rows, num_cols = array.shape
    changes_made = True

    # Smooth until no change is made, since vertical smoothing may interfere with horizontal smoothing and vice versa
    while changes_made:
        changes_made = False

        # Process rows
        for i in range(1, num_rows - 1):
            for j in range(1, num_cols - 1):
                while array[i][j] == 0:
                    if pixel_is_valid(array, i, j):
                        break

                    array[i][j] = 255
                    j -= 1      # move back to the previous column
                    changes_made = True

                j += 1          # move to the next column

        # Process columns
        for j in range(1, num_cols - 1):
            i = 1               # initialize i for each column
            backward_steps = 0  # track backward steps

            while i < num_rows - 1:
                while array[i][j] == 0:
                    if pixel_is_valid(array, i, j):
                        break

                    array[i][j] = 255
                    i -= 1      # move back to the previous row
                    backward_steps += 1
                    changes_made = True

                i += 1 + backward_steps     # move to the next row
                backward_steps = 0          # reset backward steps




def trio_scan(array):
    # Scan Rows
    num_rows, num_cols = array.shape
    temp_array = np.array([array[0]])

    step_back = 0  # Tracks the number of rows to skip when comparing rows for copying into the new array

    # Check for alternating black and white patterns in adjacent rows
    for i in range(num_rows - 2):
        row_is_added = False

        for j in range(num_cols):
            # If alternating pattern found, add the current row to the temp array
            curr_row = temp_array[i - step_back][j]
            if curr_row == array[i + 2][j] and curr_row != array[i + 1][j]:
                temp_array = np.vstack((temp_array, array[i + 1, :]))
                row_is_added = True
                break

        if not row_is_added:
            step_back += 1

    temp_array = np.vstack((temp_array, array[-1]))     # Add last row

    # Scan Columns
    temp_array = temp_array
    num_rows, num_cols = temp_array.shape
    new_array = np.array([temp_array[:, 0]])
    new_array = new_array.T

    step_back = 0  # Tracks the number of rows to skip when comparing rows for copying into the new array

    # Check for alternating black and white patterns in adjacent columns
    for i in range(num_cols - 2):
        col_is_added = False

        for j in range(num_rows):
            # If alternating pattern found, add the current column to the new array
            curr_row = new_array[j][i - step_back]
            if curr_row == temp_array[j][i + 2] and curr_row != temp_array[j][i + 1]:
                new_array = np.hstack((new_array, temp_array[:, i + 1][:, None]))
                col_is_added = True
                break

        if not col_is_added:
            step_back += 1

    new_array = np.hstack((new_array, temp_array[:, -1][:, None]))     # Add last column

    return new_array
