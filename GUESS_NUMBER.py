# week06 -> guess_number.py

def main():
    correct_answer = 13
    guess = None
    num_guesses = 0

    print("Welcome to the Guess the Number Game!")
    print("Guess the number between 1 and 20.")

    while guess != correct_answer:
        user_input = input("Enter your guess: ")
        
        if not user_input.isdigit():
            print("Invalid entry. Please enter a number between 1 and 20.")
            continue

        guess = int(user_input)
        num_guesses += 1

        if guess < 1 or guess > 20:
            print("Invalid entry. Please enter a number between 1 and 20.")
        elif guess < correct_answer:
            print("The correct answer is higher.")
        elif guess > correct_answer:
            print("The correct answer is lower.")

    print(f"Congratulations! You guessed the correct number {correct_answer} in {num_guesses} attempts.")

if __name__ == "__main__":
    main()
