import os


def word_counts(file_path, word):
    if not os.path.exists(file_path):
        return -1

    try:
        f = open(file_path)
        c = f.read().count(word)

        return c

    finally:
        f.close()


print(word_counts('./sample.txt', 'Python'))  # 存在するファイル => 1
print(word_counts('./not_found.txt', 'Java'))  # 存在しないファイル => -1
print(word_counts('./sample.txt', None))  # 存在するファイル => TypeError
