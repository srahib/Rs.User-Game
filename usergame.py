import random
print("Guess the number between 1 and 100!")
#generate random number

number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number:"))
    if guess < number:
        print("To low number!")
    elif guess > number:
        print("To high number!")
    else:
        
        print("congratulations you got a right number")
        break

