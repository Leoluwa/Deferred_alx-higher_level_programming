#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first_ch = sentence[0]

    if length == 0:
        first_ch = None
        return (length, first_ch)
    else:
        return (length, first_ch)
