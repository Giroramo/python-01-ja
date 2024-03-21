import random

def rps():
    #手の種類定義
    kind_of_hands = ["rock", "paper", "scissors"]
    hands_dict = {"0":"rock", "2":"scissors", "5":"paper"}

    #コンピューターの手をランダムに生成
    com_hand = random.choice(kind_of_hands)

    #プレーヤーの手の入力選択
    player_input = input("手を選んでください、グーは0、チョキは2、パーは5を入力してください:")
    player_hand = hands_dict.get(player_input)

    #プレーヤーの手の開示
    print(f"コンピューターの手： {com_hand}")
    print(f"あなたの手： {player_hand}")

    #判定
    if com_hand == player_hand:
        print("あいこです")
    elif (com_hand == "rock" and player_hand == "scissors") or \
         (com_hand == "scissors" and player_hand == "paper") or \
         (com_hand == "paper" and player_hand == "rock") :
        print("あなたの負けです")
    else :
        print("あなたの勝ちです！")

    
rps()