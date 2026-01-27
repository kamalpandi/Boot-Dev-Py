def list_files(parent_directory: dict, current_filepath=""):
    if parent_directory == {}:
        return []
    path_list = []
    new_path: str = ""
    for sub_dir in parent_directory:
        new_path = current_filepath + "/" + sub_dir
        value = parent_directory[sub_dir]
        if value is None:
            path_list.append(new_path)
            print("new_path", new_path)
        else:
            path_list.extend(list_files(value, new_path))
    return path_list
