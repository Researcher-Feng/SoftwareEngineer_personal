from src.get_tokenize import *
from src.google_bleu import corpus_bleu
from src.rouge import Rouge
import Levenshtein
from collections import Counter
import argparse


def eval_accuracies(hypotheses, references):
    # 断言：输入的两个字典（hypotheses和references）的键值对是有序的
    assert (sorted(references.keys()) == sorted(hypotheses.keys()))
    # Compute BLEU scores
    _, bleu, ind_bleu = corpus_bleu(hypotheses, references)
    # Compute ROUGE scores
    rouge_calculator = Rouge()
    rouge_l, ind_rouge = rouge_calculator.compute_score(references, hypotheses)
    # result
    return bleu * 100, rouge_l * 100


# 这是一个计算两个字符串的levenshtein相似度的函数，函数名为levenshtein_similarity。下面是加上注释后的代码：
def levenshtein_similarity(str1, str2):
    try:
        # 导入levenshtein库
        distance = Levenshtein.distance(str1, str2)
        # 计算相似度，使用公式计算：相似度 = 1 - (距离 / 最大长度)
        similarity = 1 - (distance / max(len(str1), len(str2)))
        # 返回相似度
        return similarity
    except ZeroDivisionError:
        # 处理除数为 0 的情况，返回相似度为 1.0（完全相同）或 0.0（默认值）
        print("字符串长度为 0，返回相似度为 -1")
        return -1  # 或者返回 1.0 取决于业务逻辑



def main_process(file_raw, file_new):
    # 加载原始文本和新文本
    tx_raw, tx_new = txt_loader(file_raw, file_new)
    l_similarity = levenshtein_similarity(tx_raw, tx_new)
    print(f'编辑距离相似度：{l_similarity}')

    if l_similarity < 0.5:
        # 分词
        token_raw = split_txt(tx_raw)
        token_new = split_txt(tx_new)

        # 获得词汇表
        vo = Counter()
        vo, token_raw_list = get_vocab(token_raw, vo)
        vo, token_new_list = get_vocab(token_new, vo)

        # 生成词汇表
        vocab_index = generate_vocab(vo)
        vocab_len = len(vocab_index)

        # 打印词汇表大小
        print('词汇表大小: ', vocab_len)

        # 索引化
        t_index_raw = index_token(token_raw_list, vocab_index)
        t_index_new = index_token(token_new_list, vocab_index)

        # 生成字符串
        string_raw = generate_string(t_index_raw)
        string_new = generate_string(t_index_new)

        # 如果词汇表大小大于1000，则采用编辑距离计算相似度
        if vocab_len > 1000:
            print('文本较长，采用编辑距离计算相似度')
            l_similarity = levenshtein_similarity(string_raw, string_new)
            print(f'相似度：{l_similarity}')
        # 否则，采用BLEU和ROUGE-L方法计算相似度
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