import random
number=random.randint(1,9)
chances=0
print("guess a number between 1 and 9")
while chances<5:
    guess=int(input("enter your guess"))
    if guess==number:
        print("Congratulations YOU WON!!!")
        break
    elif guess <number:
        print("Guess a bigger number")
    else:
        print("Guess a smaller number")
    chances+=1
if not chances<5:
    print("You lose,!The number is",number)
        
        