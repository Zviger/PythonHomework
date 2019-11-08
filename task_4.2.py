from collections import Counter


def most_common_words(file_path, number_of_words=1):
    with open(file_path, "r") as f:
        text = f.read().lower().translate({".": None, ",": None})
    words = text.split()
    return [word for word, _ in Counter(words).most_common(number_of_words)]


if __name__ == "__main__":
    print(most_common_words("data/lorem_ipsum.txt", 3))
