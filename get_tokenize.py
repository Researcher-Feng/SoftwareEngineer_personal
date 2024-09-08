import jieba
UNK = -1


def txt_loader(file_raw, file_new):
    full_text1 = read_full_txt(file_raw)
    full_text2 = read_full_txt(file_new)
    return full_text1, full_text2


def read_full_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f1:
        txt1 = f1.readlines()
    full_text = ''
    for i in txt1:
        full_text = full_text + i
    return full_text


def split_txt(text):
    seg_list = jieba.cut(text, cut_all=True)
    return seg_list


def get_vocab(token_list, vo):
    t_list = list(token_list)
    vo.update(t_list)
    return vo, t_list


def generate_vocab(vocab_current):
    vocab_index = {'UNK':-1}
    for i, item in enumerate(vocab_current.most_common()):
        vocab_index[item[0]] = i
    return vocab_index


def index_token(token_list, vocab_index):
    new_token_list = []
    for i, item in enumerate(token_list):
        new_token_list.append(vocab_index.get(item, UNK))
    return new_token_list


def generate_string(token_list):
    return ' '.join([str(i) for i in token_list])



