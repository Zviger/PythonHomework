def is_palindrome(s: str):
    s = s.replace(" ", "").lower()
    str_len = len(s)
    for index, char in enumerate(s, start=1):
        if char != s[str_len - index]:
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome("А роза упала на лапу Азора"))
