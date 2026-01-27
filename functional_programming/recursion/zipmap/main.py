def zipmap(keys: list, values: list, result_dict=None) -> dict:
    if result_dict is None:
        result_dict = {}
    if not keys or not values:
        return result_dict

    key = keys[0]
    value = values[0]
    result_dict[key] = value

    return zipmap(keys[1:], values[1:], result_dict)
