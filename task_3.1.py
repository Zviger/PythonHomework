import string


def func_1(*ss: str):
    sets_of_chars = [set(s) for s in ss]
    result_chars = (sets_of_chars[0])
    for set_of_chars in sets_of_chars[1:]:
        result_chars = result_chars.intersection(set_of_chars)
    return result_chars


def func_2(*ss: str):
    all_chars = []
    for s in ss:
        for c in list(s):
            all_chars.append(c)
    return set(all_chars)


def func_3(*ss: str):
    result_chars = []
    for c, n in zip(ss, (ss[-1],) + ss):
        result_chars += (func_1(c, n))
    return set(result_chars)


def func_4(*ss: str):
    alphabet = set(string.ascii_lowercase)
    return alphabet.difference(func_2(*ss))


if __name__ == "__main__":
    test_strings = ["hello", "world", "python"]
    print(func_4(*test_strings))
    print(func_3(*test_strings))
    print(func_2(*test_strings))
    print(func_1(*test_strings))
