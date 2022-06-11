from random import Random, randint

print("The computer has picked a random number for you")
print("Clue: it is between 1 and 15 (both inclusive)")
print("can you guess within 3 attempts? Make a try")



for i in range (0,3):
    computer_number = randint(1,15)
    user_guess = int(input("Enter a number: "))
    if user_guess == computer_number:
        print("Excellent you have guessed it right")
        break
    elif user_guess > computer_number:
        print("It is high. Try again")
    else:
        print("It is low. Try again")

print(f"The computer picked the number: {computer_number}")
print("You have lost the game now")

           
