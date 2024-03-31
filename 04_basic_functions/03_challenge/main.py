def unique_substrings(input_string):
    substrings = set()  # 重複を防ぐために set を使用
    n = len(input_string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(input_string[i:j])
    return sorted(list(substrings))  # リストに変換してソートして返す

# テスト
input_string = "banana"
print(unique_substrings(input_string))  # ['a', 'an', 'ana', 'anan', 'anana', 'b', 'ba', 'ban', 'bana', 'banan', 'banana', 'n', 'na', 'nan', 'nana']
