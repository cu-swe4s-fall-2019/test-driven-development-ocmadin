import unittest
import math_lib as ml


class TestListMean(unittest.TestCase):
    def test_list_mean_no_input(self):
        # test if no input is passed to the function
        self.assertRaises(TypeError, ml.list_mean, None)
