import random
import os


def game_instruction():
    print("Welcome to Wordle!\n"
          "You have 5 attempts to get the hidden word right\n"
          "Progress guide:\n"
          "🔴 indicates that the letter isn't in the hidden word\n"
          "🟢 indicates that the letter was guessed correctly at the correct position\n"
          "🟡 indicates that the letter was guessed correctly but at the wrong position\n")


def get_random_word():
    try:
        with open(r"C:\Users\minh\PycharmProjects\wordle\words.txt", 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
            return random.choice(words)
    except FileNotFoundError:
        print("Error: words.txt file not found")
        return "test"  # fallback word
    except Exception as e:
        print(f"Error reading file: {e}")
        return "test"


def check_word():
    keyword = get_random_word()
    attempts = 5
    score = 5

    while attempts > 0:
        guess = input("Guess the word: ").strip()  # Remove whitespace

        if len(guess) != len(keyword):
            print(f"Please enter a {len(keyword)}-letter word!")
            continue

        if guess == keyword:
            print("Correct! Your score is {}.".format(score))
            break
        else:
            attempts -= 1
            score -= 1
            print("Sorry, the word wasn't correct, you have {} attempts left.".format(attempts))

        # Check each letter
        for key_letter, guess_letter in zip(keyword, guess):
            if guess_letter == key_letter:
                print(guess_letter + "🟢")
            elif guess_letter in keyword:
                print(guess_letter + "🟡")
            else:
                print(guess_letter + "🔴")

        if attempts == 0:
            print("GAME OVER")
            print(f"The word was: {keyword}")


if __name__ == "__main__":
    game_instruction()
    check_word()