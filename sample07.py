import os


def word_counts(file_path: str, word: str) -> int:
    """
    ファイル内の単語の出現数をカウントする。

    Args:
        file_path (str): ファイルパス
        word (str): カウントする単語

    Returns:
        int: ファイル内での単語の出現数。ファイルが存在しない場合は -1 を返す。
    """
    if not os.path.exists(file_path):
        return -1

    with open(file_path) as f:
        return f.read().count(word)


if __name__ == '__main__':
    print(word_counts('./sample.txt', 'Python'))
    print(word_counts('./not_found.txt', 'Java'))  # 存在しないファイル
    print(word_counts('./sample.txt', None))  # 存在するファイル => TypeError
