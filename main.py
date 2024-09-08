from get_tokenize import *
from google_bleu import corpus_bleu
from rouge import Rouge
import Levenshtein
from collections import Counter
import argparse


def eval_accuracies(hypotheses, references):
    """An unofficial evalutation helper.
     Arguments:
        hypotheses: A mapping from instance id to predicted sequences.
        references: A mapping from instance id to ground truth sequences.
        copy_info: Map of id --> copy information.
        sources: Map of id --> input text sequence.
        filename:
        print_copy_info:
    """
    assert (sorted(references.keys()) == sorted(hypotheses.keys()))
    # Compute BLEU scores
    _, bleu, ind_bleu = corpus_bleu(hypotheses, references)
    # Compute ROUGE scores
    rouge_calculator = Rouge()
    rouge_l, ind_rouge = rouge_calculator.compute_score(references, hypotheses)
    # result
    return bleu * 100, rouge_l * 100


def levenshtein_similarity(str1, str2):
    distance = Levenshtein.distance(str1, str2)
    similarity = 1 - (distance / max(len(str1), len(str2)))
    return similarity


def main_process(file_raw, file_new):
    tx_raw, tx_new = txt_loader(file_raw, file_new)
    token_raw = split_txt(tx_raw)
    token_new = split_txt(tx_new)
    vo = Counter()
    vo, token_raw_list = get_vocab(token_raw, vo)
    vo, token_new_list = get_vocab(token_new, vo)
    vocab_index = generate_vocab(vo)
    vocab_len = len(vocab_index)
    print('词汇表大小: ', vocab_len)
    t_index_raw = index_token(token_raw_list, vocab_index)
    t_index_new = index_token(token_new_list, vocab_index)
    string_raw = generate_string(t_index_raw)
    string_new = generate_string(t_index_new)
    if vocab_len > 1000:
        print('文本较长，采用编辑距离计算相似度')
        l_similarity = levenshtein_similarity(string_raw, string_new)
        print(f'相似度：{l_similarity}')
    else:
        print('文本较短，采用bleu和rouge_l方法计算相似度')
        t_dict_raw = {0:[string_raw]}
        t_dict_new = {0:[string_new]}
        bleu, rouge_l = eval_accuracies(t_dict_raw, t_dict_new)
        print(f'bleu相似度：{bleu}, rouge_l相似度：{rouge_l}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('--raw_file', type=str, default=r'D:\我的文档\Desktop\学校\软件工程\作业\2\orig.txt')
    # parser.add_argument('--compare_file', type=str, default=r'D:\我的文档\Desktop\学校\软件工程\作业\2\orig_0.8_add.txt')
    parser.add_argument('--raw_file', type=str, default=r'D:\我的文档\Desktop\学校\软件工程\作业\2\test\demo_orig.txt')
    parser.add_argument('--compare_file', type=str, default=r'D:\我的文档\Desktop\学校\软件工程\作业\2\test\demo_orig_0.8.txt')
    args = parser.parse_args()
    main_process(args.raw_file, args.compare_file)