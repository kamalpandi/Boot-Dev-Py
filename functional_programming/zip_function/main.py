valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
    pairs = list(zip(doc_names, doc_formats))
    filterd_pair = list(filter(filter_pairs, pairs))
    return filterd_pair


def filter_pairs(pairs):
    for pair in pairs:
        if pair in valid_formats:
            return pairs
