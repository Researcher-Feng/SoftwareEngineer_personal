import numpy as np


# 最长公共子序列算法
def my_lcs(string, sub):
    # 如果字符串长度小于子字符串长度，则将字符串和子字符串进行交换
    if len(string) < len(sub):
        sub, string = string, sub

    # 创建一个二维列表，用于存储lcs的长度，列表的每一行表示一个字符串的不同位置，列表的每一列表示该位置上的不同字符
    lengths = [[0] * (len(sub) + 1) for _ in range(len(string) + 1)]
    # 遍历字符串和子字符串，计算lcs的长度
    for j in range(1, len(sub) + 1):
        for i in range(1, len(string) + 1):
            # 如果当前字符相同，lcs长度加1，否则取两个字符串中较长的那一个
            if string[i - 1] == sub[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])
    # 返回lcs的长度
    return lengths[len(string)][len(sub)]


class Rouge:
    """
    Class for computing ROUGE-L score for a set of candidate sentences for the MS COCO test set
    """

    def __init__(self):
        self.beta = 1.2

    # 计算两个文本的相似度，其中 candidate 是待检索文本，refs 是参考文本列表
    def calc_score(self, candidate, refs):
        # 首先，我们需要确保输入的 candidate 和 refs 都是单个文本的列表，而不是单个文本的字符串
        assert (len(candidate) == 1)
        assert (len(refs) > 0)
        # 定义两个列表，用于存储精准度和召回率
        prec = []
        rec = []

        # split into tokens
        token_c = candidate[0].split(" ")

        # 遍历参考文本列表，计算每个参考文本的精准度和召回率
        for reference in refs:
            # split into tokens
            token_r = reference.split(" ")
            # compute the longest common subsequence
            lcs = my_lcs(token_r, token_c)
            prec.append(lcs / float(len(token_c)))
            rec.append(lcs / float(len(token_r)))

        # 计算精准度和召回率的最大值
        prec_max = max(prec)
        rec_max = max(rec)

        # 如果精准度和召回率的最大值不为0，则计算相似度
        if prec_max != 0 and rec_max != 0:
            score = ((1 + self.beta ** 2) * prec_max * rec_max) / float(rec_max + self.beta ** 2 * prec_max)
        else:
            score = 0.0
        return score

    # 计算评估结果的得分
    def compute_score(self, gts, res):
        # 首先，我们需要确保输入的结果和标准答案是有序的，如果不然就会出错
        assert (sorted(gts.keys()) == sorted(res.keys()))
        # 然后，我们需要获取所有的图片ID
        imgIds = list(gts.keys())

        # 接下来，我们开始遍历所有的图片，并计算它们的得分
        score = dict()
        for id_i in imgIds:
            # 首先，我们从结果中获取当前图片的预测结果
            hypo = res[id_i]
            # 然后，我们从标准答案中获取当前图片的真实答案
            ref = gts[id_i]

            # Sanity check.
            # 首先，我们需要进行一个基本的sanity check，确保预测结果和标准答案的类型是正确的
            assert (type(hypo) is list)
            assert (len(hypo) == 1)
            assert (type(ref) is list)
            # 然后，我们需要确保预测结果和标准答案的长度是相同的
            assert (len(ref) > 0)

            # 接下来，我们需要定义一个计算函数，它接受预测结果和标准答案，并返回得分
            score[id_i] = self.calc_score(hypo, ref)

        # 接下来，我们定义一个计算平均得分的函数
        average_score = np.mean(np.array(list(score.values())))
        # 最后，我们返回平均得分和评估结果
        return average_score, score

    @staticmethod
    def method():
        return "Rouge"
