def apply_transforms(numbers, transformers):
    if numbers ==[]:
        return []
        
    if transformers == []:
        return numbers
    result = []
    for num in numbers:
        current_num =num
        for func in transformers:
            current_num = func(current_num)
        result.append(current_num)
    
    return result

