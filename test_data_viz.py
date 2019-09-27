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
    def test_boxplot_filename_type(self):
        self.assertRaises(TypeError, dv.boxplot,[1,2,3],123)
        self.assertRaises(TypeError, dv.boxplot,[1,2,3],['text','text','text'])
    def test_boxplot_output_file_type(self):
        self.assertRaises(ValueError,dv.boxplot,[1,2,3],'output.txt')
        
class TetHistogram(unittest.TestCase):
    def test_histogram_empty_input(self):
        self.assertRaises(TypeError, dv.histogram,None)
    def test_histogram_wrong_input_type(self):
        self.assertRaises(TypeError,dv.histogram,1)
        self.assertRaises(TypeError,dv.histogram,1.5)
        self.assertRaises(TypeError,dv.histogram,'text')
    def test_histogram_bad_input_in_list(self):
        self.assertRaises(TypeError, dv.histogram,['text','text'])
        self.assertRaises(TypeError, dv.histogram,[[1,2],[1,2]])
    def test_histogram_filename_type(self):
        self.assertRaises(TypeError, dv.histogram,[1,2,3],123)
        self.assertRaises(TypeError, dv.histogram,[1,2,3],['text','text','text'])
    def test_histogram_output_file_type(self):
        self.assertRaises(ValueError,dv.histogram,[1,2,3],'output.txt')
        