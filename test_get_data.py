import unittest
import get_data as gd

class TestGetData(unittest.TestCase):
    def test_read_stdin_col_no_input(self):
        # Test if there is input passed to the function
        self.assertRaises(TypeError,gd.read_stdin_col,None)
    def test_read_stdin_col_type(self):
        # test to see if the correct type is passed to the function
        self.assertRaises(TypeError,gd.read_stdin_col,'text')
        self.assertRaises(TypeError,gd.read_stdin_col,1.23)
        self.assertRaises(TypeError,gd.read_stdin_col,[1,2,3])
        self.assertRaises(TypeError,gd.read_stdin_col,{})        