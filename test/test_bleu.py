import numpy as np
from src.google_bleu import corpus_bleu, compute_bleu

def test_corpus_bleu():
    hypothesis = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    references = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
    assert bleu == 1.0
    assert avg_score == 1.0
    assert ind_score == {'id1': 1.0, 'id2': 1.0}

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
    assert bleu == 1.0
    assert avg_score == 1.0
    assert ind_score == {'id1': 1.0, 'id2': 1.0}

    hypothesis = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    references = {
        'id3': ['This is a test.'],
        'id4': ['This is another test.']
    }
    bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
    assert bleu == 0.0
    assert avg_score == 0.0
    assert ind_score == {'id1': 0.0, 'id2': 0.0}

    hypothesis = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    references = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
    assert bleu == 1.0
    assert avg_score == 1.0
    assert ind_score == {'id1': 1.0, 'id2': 1.0}

    hypothesis = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    references = {
        'id1': ['This is a test.'],
        'id3': ['This is another test.']
    }
    bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
    assert bleu == 0.5
    assert avg_score == 0.5
    assert ind_score == {'id1': 1.0, 'id2': 0.5}

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
    bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
    assert bleu == 0.6666666666666666
    assert avg_score == 0.6666666666666666
    assert ind_score == {'id1': 1.0, 'id2': 0.8333333333333334}

    hypothesis = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    references = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    hyp_list = [hypothesis['id1'], hypothesis['id2']]
    ref_list = [references['id1'], references['id2']]
    bleu, avg_score, ind_score = corpus_bleu(hyp_list, ref_list)
    assert bleu == 1.0
    assert avg_score == 1.0
    assert ind_score == {'id1': 1.0, 'id2': 1.0}

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
    bleu, avg_score, ind_score = corpus_bleu(hyp_list, ref_list)
    assert bleu == 0.5
    assert avg_score == 0.5
    assert ind_score == {'id1': 1.0, 'id2': 0.5}

    hypothesis = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    references = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.'],
        'id3': ['This is a different test.']
    }
    hyp_list = [hypothesis['id1'], hypothesis['id2']]
    ref_list = [references['id1'], references['id2'], references['id3']]
    bleu, avg_score, ind_score = corpus_bleu(hyp_list, ref_list)
    assert bleu == 0.6666666666666666
    assert avg_score == 0.6666666666666666
    assert ind_score == {'id1': 1.0, 'id2': 0.8333333333333334}

    # Test with empty hypothesis and reference
    hypothesis = {}
    references = {}
    bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
    assert bleu == 0.0
    assert avg_score == 0.0
    assert ind_score == {}

    # Test with different lengths of hypothesis and reference
    hypothesis = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    references = {
        'id1': ['This is a test.']
    }
    bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
    assert bleu == 0.0
    assert avg_score == 0.0
    assert ind_score == {'id1': 0.0, 'id2': 0.0}

    # Test with different ID orders in hypothesis and reference
    hypothesis = {
        'id2': ['This is another test.'],
        'id1': ['This is a test.']
    }
    references = {
        'id1': ['This is a test.'],
        'id2': ['This is another test.']
    }
    bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
    assert bleu == 1.0
    assert avg_score == 1.0
    assert ind_score == {'id1': 1.0, 'id2': 1.0}

    # Test with multiple IDs with the same values in hypothesis and reference
    hypothesis = {
        'id1': ['This is a test.'],
        'id2': ['This is a test.']
    }
    references = {
        'id1': ['This is a test.'],
        'id2': ['This is a test.']
    }
    bleu, avg_score, ind_score = corpus_bleu(hypothesis, references)
    assert bleu == 1.0