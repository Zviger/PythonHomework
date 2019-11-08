def generate_squares(num: int):
    return {i: i ** 2 for i in range(1, num+1, 1)}


if __name__ == "__main__":
    print(generate_squares(5))
