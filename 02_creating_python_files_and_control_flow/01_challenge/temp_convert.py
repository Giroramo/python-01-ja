def convert():
    temp = float(input("温度を入力してください: "))
    unit = input("温度の単位を入力してください（摂氏の場合はc、華氏の場合はf）: ")

    if unit.lower() == 'c':
        temp = (temp * 9/5) + 32
    elif unit.lower() == 'f':
        temp = (temp - 32) * 5/9

    return temp

convert()