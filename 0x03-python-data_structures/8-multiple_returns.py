#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sent_len = len(sentence)
    else:
        sent_len = 0
    return (sent_len, sentence if not sentence else sentence[:1])
