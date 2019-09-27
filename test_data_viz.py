import unittest
import data_viz as dv

class TestBoxplot(unittest.TestCase):
    def test_boxplot_empty_input(self):
        self.assertRaises(TypeError, dv.boxplot,None)