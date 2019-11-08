def split_by_index(s, indexes):
    len_s = len(s)
    new_indexes = []
    for index in indexes[1:]:
        current_index = index
        if current_index < 1:
            continue
        if len_s - 1 < current_index:
            break
        if len(new_indexes) == 0:
            new_indexes.append(current_index)
        if current_index > new_indexes[-1]:
            new_indexes.append(current_index)
    return [s[c: n] for (c, n) in zip([0] + new_indexes, new_indexes + [len(s)])]


print(split_by_index("pythoniscool,isn'tit?", [-5, 6, 6, 8, 12, 13, 18, 18, 21]))
