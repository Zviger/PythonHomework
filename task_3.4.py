def combine_dicts(*args: dict):
    result_dict = {}
    for _dict in args:
        for k, v in _dict.items():
            result_dict[k] = result_dict.get(k, 0) + v
    return result_dict


if __name__ == "__main__":
    dict_1 = {"a": 100, "b": 200}
    dict_2 = {"a": 200, "c": 300}
    dict_3 = {"a": 300, "d": 100}

    print(combine_dicts(dict_1, dict_2, dict_3))
