def get_longest_word(s: str):
    words = s.split()
    lens_words = [len(word) for word in words]
    max_len = max(lens_words)
    index = 0
    for i, len_word in enumerate(lens_words):
        if len_word == max_len:
            index = i
            break
    return words[index]


if __name__ == "__main__":
    print(get_longest_word("dsadas asd as dasd               asdasasdasdsadd\n\t asdasdadjkbfakf"))