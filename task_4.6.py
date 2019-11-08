def call_once(func):
    is_called = False

    def inner(*args, **kwargs):
        nonlocal is_called
        if is_called:
            return
        else:
            is_called = True
            return func(*args, **kwargs)
    return inner


@call_once
def sum_of_numbers(a, b):
    return a + b


if __name__ == "__main__":
    print(sum_of_numbers(5, 6))
    print(sum_of_numbers(5, 6))
    print(sum_of_numbers(5, 6))
