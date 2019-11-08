def swaper(s: str):
    new_s = ""
    for char in s:
        if char == "\"":
            new_s += "'"
        elif char == "'":
            new_s += "\""
        else:
            new_s += char
    return new_s


if __name__ == "__main__":
    print(swaper(input()))
