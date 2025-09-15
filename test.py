import random

number = random.randint(1, 100)
print("猜一个 1 到 100 之间的数字：")

while True:
    guess = input("请输入你的猜测：")
    try:
        guess = int(guess)
    except ValueError:
        print("请输入有效的数字！")
        continue

    if guess < number:
        print("太小了！")
    elif guess > number:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")
        break