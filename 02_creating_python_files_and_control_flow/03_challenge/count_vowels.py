# ここにコードを書いてください
usrinput = input("好きな英文を入力してください：")
vowels = "aiueo"
x = 0
for char in usrinput.lower():
    if char in vowels:
        x += 1
print("Number of vowels:"+ str(x))