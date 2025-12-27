def file_to_prompt(file, to_string):
    res = to_string(file)
    return "```\n" + res + "\n```"
