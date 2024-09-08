from get_tokenize import txt_loader, split_txt, get_vocab, generate_vocab, index_token
from google_bleu import corpus_bleu
from rouge import Rouge

from collections import Counter


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


def main_process(file_raw, file_new):
    tx_raw, tx_new = txt_loader(file_raw, file_new)
    token_raw = split_txt(tx_raw)
    token_new = split_txt(tx_new)
    vo = Counter()
    vo = get_vocab(token_raw, vo)
    vo = get_vocab(token_new, vo)
    vocab_index = generate_vocab(vo)
    t_index_raw = index_token(token_raw, vocab_index)
    t_index_new = index_token(token_new, vocab_index)
    t_dict_raw = {0:t_index_raw}
    t_dict_new = {0:t_index_new}
    bleu, rouge_l = eval_accuracies(t_dict_raw, t_dict_new)
    print(bleu, rouge_l)


if __name__ == '__main__':
    a = {0:['我 like English well . How do you ?']}
    b = {0:['我 like English well . How do me ?']}
    a = {0: ['一位真正的作家永远只为内心写作']}
    b = {0: ['1位真正的作家永远只为内心写作。']}
    bleu, rouge_l = eval_accuracies(a, b)
    print(bleu, rouge_l)