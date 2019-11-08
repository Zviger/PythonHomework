def count_letters(s: str):
    result_dict = {}
    for c in s:
        result_dict[c] = result_dict.get(c, 0) + 1
    return result_dict


if __name__ == "__main__":
    print(count_letters("stringsample"))
