def get_most_common_enemy(enemies_dict):
    val=[]
    for key in enemies_dict:
        value = enemies_dict[key]
        val.append(value)
    if not val==[]:
        max = val[0]
    else:
        return None
    for i in val:
        if i>max:
            max=i
    for key, value in enemies_dict.items():
        if value == max:
            return key
        