import numpy as np


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
