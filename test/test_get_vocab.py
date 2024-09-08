import unittest
from src.get_tokenize import get_vocab

# 测试
class TestGetVocab(unittest.TestCase):

    # 测试空的token_list参数
    def test_empty_token_list(self):
        token_list = []
        vocab = {}
        result_vocab, result_token_list = get_vocab(token_list, vocab)
        self.assertEqual(vocab, result_vocab)
        self.assertEqual(token_list, result_token_list)

    # 测试非空的token_list参数
    def test_non_empty_token_list(self):
        token_list = ["hello", "world"]
        vocab = {"hello": 1, "world": 2}
        result_vocab, result_token_list = get_vocab(token_list, vocab)
        self.assertEqual(vocab, result_vocab)
        self.assertEqual(token_list, result_token_list)

    # 测试空的vocab参数
    def test_empty_vocab(self):
        token_list = ["hello", "world"]
        vocab = {}
        result_vocab, result_token_list = get_vocab(token_list, vocab)
        expected_vocab = {"hello": 1, "world": 2}
        self.assertEqual(expected_vocab, result_vocab)
        self.assertEqual(token_list, result_token_list)

    # 其他测试用例略
    def test_non_empty_vocab(self):
        token_list = ["hello", "world"]
        vocab = {"hello": 1}
        result_vocab, result_token_list = get_vocab(token_list, vocab)
        expected_vocab = {"hello": 1, "world": 2}
        self.assertEqual(expected_vocab, result_vocab)
        self.assertEqual(token_list, result_token_list)

    def test_token_not_in_vocab(self):
        token_list = ["hello", "world"]
        vocab = {"hello": 1}
        result_vocab, result_token_list = get_vocab(token_list, vocab)
        expected_vocab = {"hello": 1, "world": 2}
        self.assertEqual(expected_vocab, result_vocab)
        self.assertEqual(token_list, result_token_list)

    def test_token_in_vocab(self):
        token_list = ["hello", "world"]
        vocab = {"hello": 1}
        result_vocab, result_token_list = get_vocab(token_list, vocab)
        expected_vocab = {"hello": 1}
        self.assertEqual(expected_vocab, result_vocab)
        self.assertEqual(token_list, result_token_list)