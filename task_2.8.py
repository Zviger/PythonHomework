def get_pairs(start_list: list):
    list_1 = start_list[1:]
    list_2 = start_list[:-1]
    result = list(zip(list_2, list_1))
    if len(result) == 0:
        result = None
    return result


if __name__ == "__main__":
    print(get_pairs([1, 2, 3, 4, 5]))
