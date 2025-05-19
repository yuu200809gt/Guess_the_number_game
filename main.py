import random


#ゲームチュートリアル
print("数字当てゲーム")
print("1から100までのランダムの数字を当ててください。")

target = random.randint(1,100) #1から100までのランダムの数字
max_tries = 5 #試行回数

#ゲームスタート
for i in range(1,max_tries + 1):
    try:
        guess = int(input(f"[{i}回目] 数字を入力してください (1~100) : "))
        if guess < 1 or guess > 100:
            print("範囲外です！1〜100の数字を入力してください。\n")
            continue
        if guess == target:
            print(f"正解！{i}回目で当てました！おめでとう！")
            break
        elif guess < target:
            print("小さすぎます。\n")
        else:
            print("大きすぎます。")
    except ValueError:
        print("数字を入力してください。\n")
else:
    print(f"ゲームオーバー！正解は {target} でした。")

