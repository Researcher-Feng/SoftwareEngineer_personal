from src.get_tokenize import generate_string
import unittest

# 测试
class TestGetVocab(unittest.TestCase):
    def test_generate_string_on_empty_list(self):
        # 定义一个空列表
        input_list = []
        # 定义预期输出
        expected_output = ""
        # 调用 generate_string 函数，并将实际输出赋值给 actual_output
        actual_output = generate_string(input_list)
        # 断言 actual_output 等于预期输出
        self.assertEqual(actual_output, expected_output)

    def test_generate_string_on_single_element_list(self):
        # 定义一个包含一个元素的列表
        input_list = [1]
        # 定义预期输出
        expected_output = "1"
        # 调用 generate_string 函数，并将实际输出赋值给 actual_output
        actual_output = generate_string(input_list)
        # 断言 actual_output 等于预期输出
        self.assertEqual(actual_output, expected_output)

    def test_generate_string_on_error_type(self):
        input_1 = 1
        self.assertRaises(TypeError, generate_string, input_1)

    def test_generate_string_on_multi_element_list(self):
        # 定义一个包含多个元素的列表
        input_list = [1, 2, 3]
        # 定义预期输出
        expected_output = "1 2 3"
        # 调用 generate_string 函数，并将实际输出赋值给 actual_output
        actual_output = generate_string(input_list)
        # 断言 actual_output 等于预期输出
        self.assertEqual(actual_output, expected_output)