import unittest
from collections import Counter
from src.get_tokenize import generate_vocab

# 单元测试
class TestGenerateVocab(unittest.TestCase):

    # 测试空Vocabulary的生成
    def test_empty_vocab(self):
        # 定义一个空的Vocabulary列表
        vocab_current = []
        vo1 = Counter(vocab_current)
        # 定义预期的结果，即一个包含UNK键的空字典
        expected = {'UNK': -1}
        # 调用generate_vocab函数生成实际结果
        actual = generate_vocab(vo1)
        # 使用assertDictEqual断言两个字典是否相等
        self.assertDictEqual(actual, expected)

    # 测试非空Vocabulary的生成
    def test_non_empty_vocab(self):
        # 定义一个包含重复元素的Vocabulary列表
        vocab_current = ['hello', 'world', 'hello', 'world']
        vo1 = Counter(vocab_current)
        # 定义预期的结果，即一个包含三个键（hello，world和UNK）和相应值的字典
        expected = {'UNK': -1, 'hello': 0, 'world': 1}
        # 调用generate_vocab函数生成实际结果
        actual = generate_vocab(vo1)
        # 使用assertDictEqual断言两个字典是否相等
        self.assertDictEqual(actual, expected)

    # 测试非空Vocabulary的生成
    def test_error_type(self):
        # 定义一个包含重复元素的Vocabulary列表
        vocab_current = 'hello'
        # 使用assertDictEqual断言两个字典是否相等
        self.assertRaises(AttributeError, generate_vocab, vocab_current)