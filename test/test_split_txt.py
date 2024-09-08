import unittest
import jieba
from src.get_tokenize import split_txt


# 测试
class TestSplitTxt(unittest.TestCase):
    def test_split_txt(self):
        # 测试 split_txt 函数的空值和空字符串的情况
        self.assertEqual(split_txt(None), [])
        self.assertEqual(split_txt(""), [])
        # 测试 split_txt 函数的基本功能
        self.assertEqual(split_txt("hello world!"), ["hello", "world", "!",])
        self.assertEqual(split_txt("你好，世界！"), ["你好", "，", "世界", "！"])
        self.assertEqual(split_txt("1234567890"), ["1234567890"])
        # 测试 split_txt 函数的字母和数字的情况
        self.assertEqual(split_txt("a b c d e f g h i j k l m n o p q r s t u v w x y z"), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])