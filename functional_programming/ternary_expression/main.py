def choose_parser(file_extension):

    val = "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"
    return val