secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations! You won.")
        break
else:
    print("Sorry, you failed!")

# Inspired by this, I made another web based game. See https://github.com/ahnafalnafis/guessing-game
