from unittest import TestCase
from main import translate_path
import unittest

class TestTranslate_path(TestCase):
    def test_multiple_process(self):
        self.assertRaises(Exception, translate_path,'./testfiles')
if __name__ == '__main__':
    unittest.main()
