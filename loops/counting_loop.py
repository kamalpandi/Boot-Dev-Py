def count_enemies(enemy_names):
    i = 0
    j = 0
    count=0
    enemies_dict ={}
    unique_name = list(set(enemy_names))
    for enemy_name in enemy_names:
        if enemy_names[i] == enemy_names[j]:
            count+=1
            j+=1
            enemies_dict[enemy_name]=count
        else:
            enemies_dict[enemy_name]=count
            j+=1
    return enemies_dict