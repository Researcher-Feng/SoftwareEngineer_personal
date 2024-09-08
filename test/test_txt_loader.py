import os
import tempfile
import shutil
import unittest
from src.get_tokenize import txt_loader

# 这是一个名为 TestTxtLoader 的单元测试类，包含了一些测试用例，用于测试名为 txt_loader 的函数。下面是加上中文注释后的代码：
class TestTxtLoader(unittest.TestCase):
    # 测试当原始文件和新文件不存在时，函数返回空字符串
    def test_txt_loader_files_not_exist(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_raw = os.path.join(tmp_dir, 'raw.txt')
            file_new = os.path.join(tmp_dir, 'new.txt')
            full_text1, full_text2 = txt_loader(file_raw, file_new)
            self.assertEqual(full_text1, '')
            self.assertEqual(full_text2, '')

    # 测试当原始文件存在，新文件不存在时，函数返回原始文件内容和空字符串
    def test_txt_loader_file_raw_exist_file_new_not_exist(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_raw = os.path.join(tmp_dir, 'raw.txt')
            with open(file_raw, 'w', encoding='utf-8') as f1:
                f1.write('This is a test file.')
            file_new = os.path.join(tmp_dir, 'new.txt')
            full_text1, full_text2 = txt_loader(file_raw, file_new)
            self.assertEqual(full_text1, 'This is a test file.\n')
            self.assertEqual(full_text2, '')

    # 测试当原始文件存在，新文件存在时，函数返回原始文件内容和新文件内容
    def test_txt_loader_file_raw_exist_file_new_exist(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_raw = os.path.join(tmp_dir, 'raw.txt')
            with open(file_raw, 'w', encoding='utf-8') as f1:
                f1.write('This is a test file.')
            file_new = os.path.join(tmp_dir, 'new.txt')
            with open(file_new, 'w', encoding='utf-8') as f2:
                f2.write('This is another test file.')
            full_text1, full_text2 = txt_loader(file_raw, file_new)
            self.assertEqual(full_text1, 'This is a test file.\n')
            self.assertEqual(full_text2, 'This is another test file.')

    # 测试当原始文件不存在，新文件存在时，函数会抛出 FileNotFoundError 异常
    def test_txt_loader_file_raw_not_exist_file_new_exist(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_raw = os.path.join(tmp_dir, 'raw.txt')
            file_new = os.path.join(tmp_dir, 'new.txt')
            with open(file_new, 'w', encoding='utf-8') as f2:
                f2.write('This is another test file.')
            with self.assertRaises(FileNotFoundError):
                txt_loader(file_raw, file_new)