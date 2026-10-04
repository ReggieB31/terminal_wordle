import random


words = [
    "apple",
    "brain",
    "chair",
    "dance",
    "eager",
    "flame",
    "grape",
    "honey",
    "ivory",
    "jolly",
    "knack",
    "lemon",
    "mango",
    "noble",
    "ocean",
    "pearl",
    "quake",
    "raven",
    "solar",
    "tiger",
    "ultra",
    "vivid",
    "waltz",
    "xeric",
    "youth",
    "zebra",
    "amber",
    "cabin",
    "daisy",
    "ember",
    "fable"
]

guess_number = 1
all_results = {}
#Selects a random word from the list
word_choice = random.choice(words)
print(word_choice)

#Gathers the users first guess
guess = input("Guess a 5 letter word: ")[:5]
print("-" * 40)
print()

#Runs the game while user has guesses left and has not guessed the answer.
while guess != word_choice and guess_number < 6:
    result = ""

    print(f" {" ".join(guess)}")

    #Returns the standard responses depending on guess accuracy.
    for i in range(len(word_choice)):
        if guess[i] == word_choice[i]:
            result += "🟩"
        elif guess[i] in word_choice:
            result += "🟨"
        else:
            result += "⬜"

    #Appends the most recent result to allow displaying of all guess results.
    all_results[f"result{guess_number}"] = result

    #Prints each result on a new line
    print("\n".join(all_results.values()))

    guess_number += 1
    guess = input("\nGuess again: ")[:5]

#End of game handling
if guess == word_choice:
    print("You guessed it!")
else:
    print("Out of guesses, you lose!")