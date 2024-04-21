def word_counts(file_path, word):
    f = open(file_path)
    c = f.read().count(word)
    f.close()

    return c


print(word_counts('./sample.txt', 'Python'))  # 存在するファイル => 1
print(word_counts('./not_found.txt', 'Java'))  # 存在しないファイル => FileNotFoundError
