import random

def guess_the_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("I have generated a random number between 1 and 100.")
    print("Can you guess what it is?")

    while not guessed_correctly:
        try:
            # Prompt the user to input their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare the guess to the generated number and provide feedback
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number correctly in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    guess_the_number()
