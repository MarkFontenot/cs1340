import random

round = 0

while round < 10:
    print("Round " + str(round))
    target = random.randint(1, 100)
    while True:
        num = int(input("give me a number"))
        if num > target:
            print("lower")
        elif num < target:
            print("higher")
        else:
            print("Congratulations!")
            break
    round += 1


