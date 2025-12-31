def remove_invalid_lines(document: str):
    lines = document.split("\n")
    clean_line = list(filter(lambda line: not line.startswith("-"), lines))
    return("\n").join(clean_line)
