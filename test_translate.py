# coding=utf-8
from unittest import TestCase
import unittest
import BaiduTranslator


class TestTranslate(TestCase):
    def test_translate(self):
        self.assertRaises(Exception, BaiduTranslator.translate ,u'今天是个好日子')


if __name__ == '__main__':
    unittest.main()