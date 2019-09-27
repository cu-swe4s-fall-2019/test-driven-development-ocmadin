import unittest
import math_lib as ml


class TestListMean(unittest.TestCase):
    def test_list_mean_no_input(self):
        # test if no input is passed to the function
        self.assertRaises(TypeError, ml.list_mean, None)
    
    def test_list_mean_type(self):
        # test if the input is the wrong type
        self.assertRaises(TypeError, ml.list_mean, 1)
        self.assertRaises(TypeError, ml.list_mean,1.05)
        self.assertRaises(TypeError, ml.list_mean,{})
        self.assertRaises(TypeError, ml.list_mean,True)
        self.assertRaises(TypeError, ml.list_mean,'Text')
        
    def test_list_mean_empty(self):
        # test if the list is empty
        self.assertRaises(IndexError,ml.list_mean,[])