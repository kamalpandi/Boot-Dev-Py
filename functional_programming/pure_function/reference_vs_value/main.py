def add_format(default_formats, new_format):
    added_format = default_formats.copy()
    added_format[new_format] = True
    return added_format


def remove_format(default_formats, old_format):
    removed_format = default_formats.copy()
    removed_format[old_format] = False
    return removed_format
