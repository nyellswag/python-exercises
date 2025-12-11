# Interactive translator

import random

dictionary = {
    "hello": "привет",
    "cat": "кот",
    "dog": "собака",
    "book": "книга",
    "water": "вода",
    "sun": "солнце",
    "python": "питон",
    "goodbye": "пока",
    "yes": "да",
    "no": "нет"
}

todays_words = {}
learned_today = 0

def translator():
    print("Hello, welcome to translator!")
    word_count = 0

    while True:
        my_word = input("What word do you want to translate?: ")
        if my_word in dictionary:
            print(f"Your word translate as '{dictionary[my_word]}' in russian")
            word_count += 1
            todays_words[my_word] = dictionary[my_word]
        else:
            new_word = input("There's no such word in our dictionary, please add translation of it: ")
            dictionary[my_word] = new_word
            todays_words[my_word] = new_word
            word_count += 1
            print(f"Here's updated dictionary: \n{dictionary}")

        continue_choice =  input("Do you want to continue?: ")
        if continue_choice == 'no':
            print(f"Okay, see you later, here how much word you searched today: {word_count}")
            print(f"And here're the words that we searched today: {todays_words}")
            break

translator()
