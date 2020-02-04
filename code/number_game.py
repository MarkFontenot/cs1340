import random


round = 0
while round < 10:
    print("Round:" + str(round))
    target = random.randint(1, 100)
    while True:
        guess = int(input("Give me a number")) # "10"

        if guess > target:
            print("lower")
        elif guess < target:
            print("higher")
        else:
            print("congratulations!")
            break
    round += 1