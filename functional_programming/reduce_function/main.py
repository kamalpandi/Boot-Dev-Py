import functools


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    list_of_sentences = sentences[:n]
    print("list_of_sentences---", list_of_sentences)
    full_sentence = functools.reduce(join, list_of_sentences)
    print("full_sentence---", full_sentence + ".")
    return full_sentence + "."
