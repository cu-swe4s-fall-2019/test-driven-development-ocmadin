import unittest
import data_viz as dv

class TestBoxplot(unittest.TestCase):
    def test_boxplot_empty_input(self):
        self.assertRaises(TypeError, dv.boxplot,None)
    def test_boxplot_wrong_input_type(self):
        self.assertRaises(TypeError,dv.boxplot,1)
        self.assertRaises(TypeError,dv.boxplot,1.5)
        self.assertRaises(TypeError,dv.boxplot,'text')
    def test_boxplot_bad_input_in_list(self):
        self.assertRaises(TypeError, dv.boxplot,['text','text'])
        self.assertRaises(TypeError, dv.boxplot,[[1,2],[1,2]])