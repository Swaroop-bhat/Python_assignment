import random
def random_word(words):
    if not words:
        raise ValueError("empty.")

    return random.choice(words)

def clue_word(word, guessed_letters):
    clue = ""
    for letter in word:
        if letter in guessed_letters:
            clue += letter
        else:
            clue += "_"
    return clue

words = ["hp", "asus", "acer", "lenovo", "dell"]
guessed_word = random_word(words)
guessed_letters = set()
print("Clue: " + clue_word(guessed_word, guessed_letters))

attempts = 6
while attempts > 0:
    guessed_letter = input("Guess a letter: ").lower()

    if len(guessed_letter) != 1 or not guessed_letter.isalpha():
        print("Please enter a single letter.")
        continue

    if guessed_letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guessed_letter)

    if guessed_letter in guessed_word:
            print("Correct guess")
    else:
        attempts -= 1
        print("Incorrect guess. {} attempts remaining.".format(attempts))

    clue = clue_word(guessed_word, guessed_letters)
    print("Clue: " + clue)

    if "_" not in clue:
        print("You guessed the word:", guessed_word)
        break

if attempts == 0:
    print("0 attempts. The word was:", guessed_word)

