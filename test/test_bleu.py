import unittest
import sys
sys.path.append('..')
from src.google_bleu import corpus_bleu, compute_bleu

class TestGetVocab(unittest.TestCase):
    def test_corpus_bleu_empty(self):
        """
            空
        """
        hypothesis = {}
        references = {}
        self.assertRaises(ZeroDivisionError, corpus_bleu, hypothesis, references)

    def test_corpus_bleu_right(self):
        """
            正例
        """
        hypothesis = {
            'id1': ['This is a test.'],
            'id2': ['This is another test.']
        }
        references = {
            'id1': ['This is a test.'],
            'id2': ['This is another test.']
        }
        bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
        self.assertEqual(bleu, 1.0)
        self.assertEqual(avg_score, 1.0)
        self.assertEqual(ind_score, {'id1': 1.0, 'id2': 1.0})

    def test_corpus_bleu_ID_order(self):
        """
            hypothesis 和 reference 的 ID 顺序不同
        """
        hypothesis = {
            'id1': ['This is a test.'],
            'id2': ['This is another test.']
        }
        references = {
            'id2': ['This is another test.'],
            'id1': ['This is a test.']
        }
        bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
        self.assertEqual(bleu, 1.0)
        self.assertEqual(avg_score, 1.0)
        self.assertEqual(ind_score, {'id1': 1.0, 'id2': 1.0})

    def test_corpus_bleu_ID_incorrect(self):
        """
            数据类型错误
        """
        hypothesis = {
            'id1': 'This is a test.',
            'id2': ['This is another test.']
        }
        references = {
            'id3': ['This is a test.'],
            'id4': ['This is another test.']
        }
        self.assertRaises(AssertionError, corpus_bleu, hypothesis, references)

    def test_corpus_bleu_ID_incorrect2(self):
        """
            存在多个 hypothesis 和 reference 的 ID 相同
        """
        hypothesis = {
            'id1': ['This is a test.'],
            'id2': ['This is another test.']
        }
        references = {
            'id1': ['This is a test.'],
            'id2': ['This is another test.'],
            'id3': ['This is a different test.']
        }
        self.assertRaises(AssertionError, corpus_bleu, hypothesis, references)

    def test_corpus_bleu_hyp_list_incorrect(self):
        """
            hypothesis 和 reference 的 数量不匹配
        """
        hypothesis = {
            'id1': ['This is a test.'],
            'id2': ['This is another test.']
        }
        references = {
            'id1': ['This is a test.'],
            'id2': ['This is another test.']
        }
        hyp_list = [hypothesis['id1']]
        ref_list = [references['id1'], references['id2']]
        self.assertRaises(AttributeError, corpus_bleu, hyp_list, ref_list)



