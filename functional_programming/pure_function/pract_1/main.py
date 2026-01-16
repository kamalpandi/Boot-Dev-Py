default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    commands_cpy = commands.copy()
    commands_cpy[new_command] = function
    return commands_cpy


def add_format(formats, format):
    formats_cpy=formats.copy()
    formats_cpy.append(format)
    return formats_cpy


def save_document(docs, file_name, doc):
    print(type(docs))
    docs_cpy= docs.copy()
    docs_cpy[file_name] = doc
    
    return docs_cpy


def add_line_break(line):
    return line + "\n\n"
