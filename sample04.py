import os


def word_counts(file_path, word):
    if not os.path.exists(file_path):
        return -1

    f = open(file_path)
    c = f.read().count(word)
    # close()の前でエラーが発生すると・・・
    f.close()

    return c


print(word_counts('./sample.txt', 'Python'))  # 存在するファイル => 1
print(word_counts('./not_found.txt', 'Java'))  # 存在しないファイル => -1
# print(word_counts('./sample.txt', None))  # 存在するファイル => TypeError
