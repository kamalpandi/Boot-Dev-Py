def file_type_getter(file_extension_tuples):
    map_file_ext = {}
    for doc_type, file_exts in file_extension_tuples:
        for file_ext in file_exts:
            map_file_ext[file_ext] = doc_type
    return lambda s: map_file_ext.get(s, "Unknown")
