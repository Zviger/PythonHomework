def get_digits(num: int):
    return tuple(int(c) for c in str(num))


if __name__ == "__main__":
    print(get_digits(12454))
