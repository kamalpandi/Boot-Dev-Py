def restore_documents(originals: tuple, backups: tuple):
    return set({x.upper() for x in originals + backups if type(x) is str and not x.isdigit()})