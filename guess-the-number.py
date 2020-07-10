# Guess the number game
import random
print("Hello. What is your name?")
user_name = input()

secret_number = random.randint(1, 20)
print("Well, " + user_name + ", I am thinking of a number between 1 and 20")

# Ask player to guess 6 times
for guesses_used in range(1, 7):
    print("Take a wild guess")
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break

if guess == secret_number:
    print("Good job, " + user_name + "! You guessed my number in " + str(guesses_used) + " guesses!")

print("You took " + str(guesses_used) + " guesses.")