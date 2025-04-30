import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print("sorry, guess again. Too low.")
        elif guess > random_number:
            print("sorry, guess again. Too high.")
        else:
            print(f"yay, congrats. You have guessed the number {random_number} correctly.")

guess(10)

# google collab link of this
# https://colab.research.google.com/drive/1Fs41TXgjf19tpvINoZkcWF5gExJm9iO_?usp=sharing