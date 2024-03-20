def counter():
    occurrences = {}
    fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "apple",
        "kiwi",
        "banana",
        "melon",
        "orange",
        "strawberry",
    ]

    # ここにコードを書いてください
    #各果物の出現回数をカウントしてoccurrencesに格納する
    for fruit in fruits:
        if fruit not in occurrences:
            occurrences[fruit] = 1
        else:
            occurrences[fruit] += 1
    
    #カウント結果を出力する
    for fruit, count in occurrences.items():
        print(f"{fruit}: {count}")
    return occurrences

print(counter())
