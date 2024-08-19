def count_enemies(enemy_names):
    enemies_dict={}
    names = list(set(enemy_names))
    value = []
    for name in names:
        count = 0
        for enemy_name in enemy_names:
            if name == enemy_name:
                count+=1
        value.append(count)
    print(names)
    print(value)
    enemies_dict={names[i]: value[i] for i in range(len(names))}
    return enemies_dict