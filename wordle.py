import random

def game_instruction():
    print("Welcome to Wordle!\n"
          "You have limited attempts to get the hidden word right\n"
          "Game guide:\n"
          "🔴 indicates that the letter isn't in the hidden word\n"
          "🟢 indicates that the letter was guessed correctly at the correct position\n"
          "🟡 indicates that the letter was guessed correctly but at the wrong position\n")


def get_random_word():
    try:
        with open(r"C:\Users\minh\PycharmProjects\wordle\words.txt", 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
            return random.choice(words).lower()
    except FileNotFoundError:
        print("Error: words.txt file not found")
        return "test"
    except Exception as e:
        print(f"Error reading file: {e}")
        return "test"


def check_word():
    keyword = get_random_word()
    print(f"The keyword have {len(keyword)} characters")
    attempts = len(keyword) + 3
    score = attempts
    url = "https://dictionary.cambridge.org/dictionary/english-vietnamese/{}".format(keyword)
    while attempts > 0:
        guess = input("Guess the word: ").strip()

        if guess == "x":
            print("Thanks for playing! Game exited.")
            return
        x
        if len(guess) != len(keyword):
            print(f"Please enter a {len(keyword)}-letter word!")
            continue

        if guess == keyword:
            print(f"Correct! Your score is {score}\n"
                  f"Vietnamese Meaning: {url}")
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
            print(f"The word was: {keyword}\n"
                  f"Vietnamese Meaning: {url}")


if __name__ == "__main__":
    game_instruction()
    check_word()