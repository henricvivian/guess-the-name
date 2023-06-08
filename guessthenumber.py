import random

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = None
        self.attempts = 0

    def start(self):
        print("Welcome to Guess the Number!")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        while True:
            self.attempts += 1
            self.make_guess()

            if self.is_guess_correct():
                self.print_congratulations()
                break

            if self.is_max_attempts_reached():
                self.print_attempts_limit_reached()
                break

    def make_guess(self):
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < self.secret_number:
            print("Too low!")
        elif guess > self.secret_number:
            print("Too high!")

    def is_guess_correct(self):
        return self.secret_number == guess

    def print_congratulations(self):
        print(f"Congratulations! You guessed the number in {self.attempts} attempts!")

    def is_max_attempts_reached(self):
        return self.attempts >= 5

    def print_attempts_limit_reached(self):
        print("Sorry, you have run out of attempts.")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start()
