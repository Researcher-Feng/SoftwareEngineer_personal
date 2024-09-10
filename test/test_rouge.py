import numpy as np
from src.rouge import Rouge
import unittest

# 测试一些常见的情况
class TestRouge(unittest.TestCase):
    def setUp(self):
        self.rouge = Rouge()

    def test_empty_gts(self):
        # 定义一个空的 ground truths（gts）字典
        gts = dict()
        # 定义一个空的结果（res）字典
        res = dict()
        # 断言得分为 -1
        self.assertEqual(self.rouge.compute_score(gts, res), -1)

    def test_empty_res(self):
        # 定义一个包含一个键为 a、值为一个列表，列表中只有一个元素“a sentence”的gts字典
        gts = dict(a=[["a sentence"]])
        # 定义一个空的 res 字典
        res = dict()
        # 断言得分为 -1
        self.assertEqual(self.rouge.compute_score(gts, res), -1)

    def test_diff_key_order(self):
        # 定义一个包含一个键为 a、值为一个列表，列表中只有一个元素“a sentence”的 gts 字典
        gts = dict(a=[["a sentence"]])
        # 定义一个包含一个键为 b、值为一个列表，列表中只有一个元素“a sentence”的 res 字典
        res = dict(b=[["a sentence"]])
        # 断言得分为 -1
        self.assertEqual(self.rouge.compute_score(gts, res), -1)

    def test_non_list_hypo(self):
        # 定义一个包含一个键为 a、值为一个非列表类型的 res 字典
        gts = dict(a=[["a sentence"]])
        res = dict(a=123)
        # 使用 rouge 计算得分，期望出现异常
        self.assertEqual(self.rouge.compute_score(gts, res), -1)

    def test_non_list_ref(self):
        # 定义一个包含一个键为 a、值为非列表类型的gts字典
        gts = dict(a=123)
        # 定义一个包含一个键为 a、值为一个列表类型的 res 字典
        res = dict(a=[["a sentence"]])
        # 使用 rouge 计算得分，期望出现异常
        self.assertEqual(self.rouge.compute_score(gts, res), -1)

    def test_diff_len_list(self):
        # 定义一个包含一个键为 a、值为一个列表，列表中有两个元素“a sentence”和“another sentence”的gts字典
        gts = dict(a=[["a sentence"]])
        # 定义一个包含一个键为 a、值为一个列表，列表中只有一个元素“a sentence”的 res 字典
        res = dict(a=["a sentence", "another sentence"])
        # 使用 rouge 计算得分，期望出现异常
        self.assertEqual(self.rouge.compute_score(gts, res), -1)