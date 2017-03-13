# -*- coding: utf-8 -*-
from rouge import *

def pythonrouge(peer_sentences, model_sentences, ROUGE_path=None, data_path=None):
    return rouge.rouge(peer_sentences, model_sentences)

