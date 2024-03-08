def compute_factorial():
    # ここにコードを書いてください
    # number変数を編集し、ユーザー入力として正の整数を受け取ります。整数に変換することを忘れないでください
    number = int(input('正の整数を入力して下さい'))
    
    if number == 0:
        return 1
    
    # while loop
    # count = number    
    #        
    #while( count > 0):
    ##    if count ==1 :
    #       break
        
    #    number  = number * (count-1)
    #    count = count-1 """
    # for loop
    # range(5)      => 0, 1, 2, 3, 4
    # range(1,5)    => 1, 2, 3, 4
    # 1st step : oneNumber =1
    for oneNumber in range(1, number):
        number = number*oneNumber

    # result変数を編集し、最終的な計算結果を保存します
    result = number
    return result


compute_factorial()
