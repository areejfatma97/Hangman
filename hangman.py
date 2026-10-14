import random


class Hangman:
    WORDS = ["python", "hangman", "computer", "garden", "planet"]
    MAX_WRONG = 6

    def __init__(self):
        self.word = random.choice(self.WORDS)
        self.guessed = []
        self.wrong = 0

    def reveal(self):
        return " ".join(letter if letter in self.guessed else "_" for letter in self.word)

    def get_guess(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter one letter.")
            elif guess in self.guessed:
                print("You already guessed that letter.")
            else:
                return guess

    def play(self):
        print("Welcome to Hangman!")

        while self.wrong < self.MAX_WRONG:
            print(f"\nWord: {self.reveal()}")
            print(f"Wrong guesses left: {self.MAX_WRONG - self.wrong}")
            if self.guessed:
                print(f"Guessed letters: {', '.join(self.guessed)}")

            guess = self.get_guess()
            self.guessed.append(guess)

            if guess in self.word:
                print("Correct!")
                if all(letter in self.guessed for letter in self.word):
                    print(f"You won! The word was '{self.word}'.")
                    return
            else:
                self.wrong += 1
                print("That letter is not in the word.")

        print(f"You ran out of guesses. The word was '{self.word}'.")


if __name__ == "__main__":
    Hangman().play()