import unittest
import get_data as gd

class TestGetData(unittest.TestCase):
    def test_read_stdin_col_no_input(self):
        # Test if there is input passed to the function
        self.assertRaises(TypeError,gd.read_stdin_col,None)
        