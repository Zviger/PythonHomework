import functools


def func(start_list: list):
    full_product = functools.reduce(lambda a, b: a*b, start_list)
    return [full_product // i for i in start_list]


if __name__ == "__main__":
    print(func([1, 2, 3, 4, 5]))
