import unittest
import numpy as np

from image_processing import apply_smoothing, crop_maze


class TestImageProcessing(unittest.TestCase):
    def test_apply_smoothing(self):
        input_array = np.array([
            [255, 255, 255, 255, 255],
            [255, 255, 0, 255, 255],
            [255, 0, 0, 0, 255],
            [255, 0, 0, 255, 255],
            [255, 255, 255, 255, 255]], dtype=np.uint8)

        expected_output = np.array([
            [255, 255, 255, 255, 255],
            [255, 255, 255, 255, 255],
            [255, 0, 0, 255, 255],
            [255, 0, 0, 255, 255],
            [255, 255, 255, 255, 255]
        ], dtype=np.uint8)

        result = apply_smoothing(input_array)
        np.testing.assert_array_equal(result, expected_output)

    def test_crop_maze(self):
        input_array = np.array([
            [255, 255, 255, 255, 255, 255, 255],
            [255, 255, 0, 255, 0, 255, 255],
            [255, 255, 0, 0, 0, 255, 255],
            [255, 255, 0, 0, 0, 255, 255],
            [255, 255, 255, 255, 255, 255, 255],
            [255, 255, 255, 255, 255, 255, 255],
            [255, 255, 255, 255, 255, 255, 255]
        ], dtype=np.uint8)

        expected_output = np.array([
            [0, 0, 0],
            [0, 0, 0]
        ], dtype=np.uint8)

        result = crop_maze(input_array)
        print(result)
        np.testing.assert_array_equal(result, expected_output)


if __name__ == '__main__':
    unittest.main()
