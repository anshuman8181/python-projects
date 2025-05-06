import random
playing = True
number = str(random.randint(10,20))


print("I will generate a number free 10 to 20 and you have to guess the number")
print("the game ends when you get it right")
while playing:
    guess = input("Give me your best guess")
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break

    else:
        print("your guess is not quite right please try again.\n")