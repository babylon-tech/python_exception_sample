import os


def word_counts(file_path, word):
    if not os.path.exists(file_path):
        return -1

    with open(file_path) as f:
        return f.read().count(word)


print(word_counts('./sample.txt', 'Python'))
print(word_counts('./not_found.txt', 'Java'))  # 存在しないファイル
print(word_counts('./sample.txt', None))  # 存在するファイル => TypeError
