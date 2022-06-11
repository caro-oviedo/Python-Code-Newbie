from random import randint


print("The computer has picked a random number for you")
print("Clue: it is between 1 and 15 (both inclusive)")
print("can you guess within 3 attempts? Make a try")

computer_number = randint(1,15)
no_attempt = 0
guess = False
user_guess = 0

while no_attempt < 3:
    user_guess = int(input("Enter a number: "))
    no_attempt += 1

    if user_guess == computer_number:
        guess = True
        break
    elif user_guess > computer_number:
        print("It is high. Try again!")
    else:
        print("It is low. Try again")


if guess:
    print("Excellent you have guessed it right")
    print(f"You've taken {no_attempt} attempt(s)")
else:
    print(f"The computer picked the number: {computer_number}")
    print("You have lost the game now")
