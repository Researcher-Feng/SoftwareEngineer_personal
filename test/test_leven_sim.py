import unittest
from difflib import SequenceMatcher
from Levenshtein import distance
from main import levenshtein_similarity

# test
class TestLevenshteinSimilarity(unittest.TestCase):
    # 测试两个空字符串的相似度
    def test_similarity_when_both_strings_are_empty(self):
        self.assertEqual(levenshtein_similarity("", ""), 1)

    # 测试一个空字符串和一个有字符的字符串的相似度
    def test_similarity_when_one_string_is_empty(self):
        self.assertEqual(levenshtein_similarity("", "a"), 0)
        self.assertEqual(levenshtein_similarity("a", ""), 0)

    # 测试两个有字符的字符串的相似度
    def test_similarity_when_both_strings_have_one_character(self):
        self.assertEqual(levenshtein_similarity("a", "a"), 1)

    # 测试不同长度的字符串的相似度
    def test_similarity_when_one_string_has_one_character(self):
        self.assertEqual(levenshtein_similarity("a", "b"), 0)

    # 这是一个名为levenshtein_similarity的函数，它计算两个字符串的Levenshtein相似度
    def test_similarity_when_strings_have_different_lengths(self):
        self.assertEqual(levenshtein_similarity("a", "ab"), 0)