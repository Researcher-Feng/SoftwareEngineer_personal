import jieba
UNK = -1


def txt_loader(file_raw, file_new):
    with open(file_raw, 'r') as f1:
        txt1 = f1.readlines()
    with open(file_new, 'r') as f2:
        txt2 = f2.readlines()
    return txt1, txt2


def split_txt(text):
    seg_list = jieba.cut(text, cut_all=False)
    return seg_list


def get_vocab(token_list, vo):
    vo.update(list(token_list))
    return vo


def generate_vocab(vocab_current):
    vocab_index = {'UNK':-1}
    for i, item in enumerate(vocab_current):
        vocab_index[item[0]] = i
    return vocab_index


def index_token(token_list, vocab_index):
    new_token_list = []
    for i, item in enumerate(token_list):
        new_token_list.append(vocab_index.get(item, UNK))
    return new_token_list



