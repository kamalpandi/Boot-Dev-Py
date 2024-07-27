def filter_messages(messages):
    count_list = []
    count=0
    words = []
    # print(messages)
    # count_list.append(0)
    for i in messages:
        splitted_words = i.split()
        for splitted_word in splitted_words:
            if splitted_word == "dang":
                count+=1
                splitted_words.remove(splitted_word)
        count_list.append(count)
        count-=count
        words.append(" ".join(splitted_words))
    return words, count_list