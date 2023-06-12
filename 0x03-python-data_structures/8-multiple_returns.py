#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == "":
        return(0, None)
    else:
        return(len(sentence), sentence[0])
