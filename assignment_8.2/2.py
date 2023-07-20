import random
def random_word(word_list):
    if not word_list:
        raise ValueError("empty.")

    return random.choice(word_list)

words = ["hp", "asus", "acer", "lenovo", "dell"]
guessed_word = random_word(words)
for i in range(5):
    guessed_input = input("Guess the word: ")

    if guessed_word == guessed_input:
        print("You guessed the correct word.")
        print("The correct word was:", guessed_word)
        break
    else:
        print("Your guess is wrong.")

