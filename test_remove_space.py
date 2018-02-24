# coding=utf-8
from unittest import TestCase
import unittest

import docx
from docx import Document

import Filehandler
# coding=utf8


class TestRemove_space(TestCase):
    def test_remove_txt_space(self):
        self.assertEqual(u'删除全角空格', Filehandler.remove_txt_space(u'删除　全角　空格'))
        self.assertEqual(u'删除全角空格', Filehandler.remove_txt_space('删除　全角　空格'))


if __name__ == '__main__':
    unittest.main()

