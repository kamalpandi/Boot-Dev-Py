def change_bullet_style(document):
    
    
    mapped_val = map(convert_line, document.split('\n'))
    mapped_list = list(mapped_val)
    return "\n".join(mapped_list)
    
    


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
