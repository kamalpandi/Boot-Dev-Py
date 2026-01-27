def sum_nested_list(lst:list):
    if lst is None:
        return 0
    total_size =0 
    for element in lst:
        if isinstance(element, list):
            total_size+=sum_nested_list(element)
        else:
            total_size+=element
    return total_size
