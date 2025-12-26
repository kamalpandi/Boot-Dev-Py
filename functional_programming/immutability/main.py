def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    new_document = (documents) + (new_doc,)
    return new_document
