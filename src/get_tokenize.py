import jieba
UNK = -1


# 加载两个文本文件的内容
def txt_loader(file_raw, file_new):
    # 定义一个名为 read_full_txt 的函数，用于读取文本文件
    def read_full_txt(file_path):
        with open(file_path, 'r', encoding='utf-8') as f1:
            txt1 = f1.readlines()
        full_text = ''
        # 遍历文件，将文件内容合并为一个字符串
        for i in txt1:
            full_text = full_text + i
        return full_text
    full_text1 = read_full_txt(file_raw)
    full_text2 = read_full_txt(file_new)
    return full_text1, full_text2


# 分词
def split_txt(text):
    # 使用 jieba 库进行分词，使用 cut_all 参数进行全模式分词
    seg_list = jieba.cut(text, cut_all=True)
    # 返回分词后的列表
    return seg_list


# 构建词典
def get_vocab(token_list, vo):
    # 遍历列表中的每个词，将其添加到词典中
    t_list = list(token_list)
    vo.update(t_list)
    return vo, t_list


# 生成词表（vocabulary）
def generate_vocab(vocab_current):
    try:
        # 创建一个空的词索引（vocabulary index）字典
        vocab_index = {'UNK':-1}
        # 遍历现有的词频最高的列表，并将每个词添加到词索引字典中
        for i, item in enumerate(vocab_current.most_common()):
            vocab_index[item[0]] = i
        # 返回生成的词索引字典
        return vocab_index
    except AttributeError:
        print("请输入正确的数据类型")
        raise AttributeError


# 将文本序列中的词转换为数字序列
def index_token(token_list, vocab_index):
    new_token_list = []
    for i, item in enumerate(token_list):
        new_token_list.append(vocab_index.get(item, UNK))
    return new_token_list


# 这是一个生成字符串的函数，其输入是一个列表（token_list）。下面是加上注释后的代码：
def generate_string(token_list):
    try:
        # 使用 join 函数将列表中的元素连接成一个字符串，并返回
        return ' '.join([str(i) for i in token_list])
    except TypeError:
        print("请输入列表类型的数据")
        raise TypeError



