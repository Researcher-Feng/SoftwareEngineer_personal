import collections
import math


# 获取给定句子的n-gram统计信息
def _get_ngrams(segment, max_order):
    # 定义一个字典，用于存储n-gram及其出现频率
    ngram_counts = collections.Counter()
    # 遍历给定的句子，从order=1到order=max_order
    for order in range(1, max_order + 1):
        # 遍历句子的长度为i的n-gram
        for i in range(0, len(segment) - order + 1):
            # 取出n-gram
            ngram = tuple(segment[i:i + order])
            # 计算n-gram的频率
            ngram_counts[ngram] += 1
        # 返回n-gram统计信息
    return ngram_counts


# 计算 BLEU
def compute_bleu(reference_corpus, translation_corpus, max_order=4,
                 smooth=False):
    # matches_by_order 是一个列表，用于存储不同 n 阶的匹配数量
    matches_by_order = [0] * max_order
    # possible_matches_by_order 是一个列表，用于存储不同 n 阶的可能匹配数量
    possible_matches_by_order = [0] * max_order
    # reference_length 是一个变量，用于存储参考文献的总长度
    reference_length = 0
    # translation_length 是一个变量，用于存储翻译文献的总长度
    translation_length = 0
    # 遍历两个文献序列，并计算 BLEU 评估指标
    for (references, translation) in zip(reference_corpus,
                                         translation_corpus):
        # 更新参考文献和翻译文献的总长度
        reference_length += min(len(r) for r in references)
        translation_length += len(translation)

        # merged_ref_ngram_counts 是一个字典，用于存储合并后的参考 n 元语法的计数
        merged_ref_ngram_counts = collections.Counter()
        # 遍历参考文献，并将其 n 元语法添加到合并后的字典中
        for reference in references:
            merged_ref_ngram_counts |= _get_ngrams(reference, max_order)
        # translation_ngram_counts 是一个字典，用于存储翻译文献的 n 元语法的计数
        translation_ngram_counts = _get_ngrams(translation, max_order)
        # overlap 是一个字典，用于存储两个字典的交集
        overlap = translation_ngram_counts & merged_ref_ngram_counts
        # 遍历交集中的 n 元语法，并更新匹配数量
        for ngram in overlap:
            matches_by_order[len(ngram) - 1] += overlap[ngram]
        # 遍历不同 n 阶的可能匹配数量
        for order in range(1, max_order + 1):
            # 计算第 i 阶的可能匹配数量
            possible_matches = len(translation) - order + 1
            # 如果可能匹配数量大于 0，则更新可能匹配数量
            if possible_matches > 0:
                possible_matches_by_order[order - 1] += possible_matches

    # 计算不同 n 阶的精度
    precisions = [0] * max_order
    for i in range(0, max_order):
        # 如果需要平滑，则使用平滑的精度
        if smooth:
            precisions[i] = ((matches_by_order[i] + 1.) /
                             (possible_matches_by_order[i] + 1.))
        # 如果不需要平滑，则使用非平滑的精度
        else:
            if possible_matches_by_order[i] > 0:
                precisions[i] = (float(matches_by_order[i]) /
                                 possible_matches_by_order[i])
            else:
                precisions[i] = 0.0

    # 如果精度中最小的精度大于 0，则计算 geometric mean（几何平均值）和比率
    if min(precisions) > 0:
        p_log_sum = sum((1. / max_order) * math.log(p) for p in precisions)
        geo_mean = math.exp(p_log_sum)
    else:
        geo_mean = 0

    ratio = float(translation_length) / reference_length

    # 如果比率大于 1，则将 bp 设置为 1
    if ratio > 1.0:
        bp = 1.
    # 如果比率小于 1，则计算反比例因子
    else:
        bp = math.exp(1 - 1. / ratio)

    # 计算 n 元语法
    bleu = geo_mean * bp

    return bleu, precisions, bp, ratio, translation_length, reference_length


# 计算一个语料库（corpus）的 BLEU 得分
def corpus_bleu(hypotheses, references):
    try:
        assert (sorted(hypotheses.keys()) == sorted(references.keys())), '输入数据不对齐'

        # 定义一个空列表，用于存储参考文献（references）
        refs = []
        # 定义一个空列表，用于存储假设文献（hypotheses）
        hyps = []
        # 定义一个计数器，用于统计计算的句子数量
        count = 0
        # 遍历所有句子的 ID，并将它们添加到列表中
        total_score = 0.0


        Ids = list(hypotheses.keys())
        # 遍历所有句子
        ind_score = dict()

        for id_i in Ids:
            # 将句子的假设文献和参考文献添加到列表中
            hyp = hypotheses[id_i][0].split()
            ref = [r.split() for r in references[id_i]]
            hyps.append(hyp)
            refs.append(ref)

            # 计算每个句子的 BLEU 得分
            score = compute_bleu([ref], [hyp], smooth=True)[0]
            # 累加所有句子的得分
            total_score += score
            # 增加句子数量
            count += 1
            ind_score[id_i] = score

        # 计算语料库的平均 BLEU 得分和每个句子的得分
        avg_score = total_score / count
        re_corpus_bleu = compute_bleu(refs, hyps, smooth=True)[0]
        return re_corpus_bleu, avg_score, ind_score
    except AttributeError:
        print("请输入字典类型的数据")
        raise AttributeError
    except ZeroDivisionError:
        print("输入不能为空")
        raise ZeroDivisionError
    except AssertionError:
        print('请输入对齐的数据')
        raise AssertionError
