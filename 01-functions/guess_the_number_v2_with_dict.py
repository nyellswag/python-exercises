import random

# Setting Language of game
set_lang = input("1. 'eng' \n2. 'ru'\nSet language: ")
while (set_lang != "ru" and set_lang != "eng"):
    print("Please set correct value!")
    set_lang = input("1. 'eng' \n2. 'ru'\nSet language: ")

texts ={
    "eng": {
        "first_attempt": "Try to guess number, what's your guess?: ",
        "lower": "You're close, try lower",
        "higher": "You're close try higher",
        "next_guess": "What is your next guess?: ",
        "right_guess": "You guessed the right number! The number of tries is ",
        "play_again": "Do you want to play one more game?: \n1.Yes\n2.No\n",
        "goodbye": "This was good game, see later"

    },
    "ru": {
        "first_attempt": "Попробуйте угадать загаданное число: ",
        "lower": "Ты блико, попробуй значение меньше",
        "higher": "Ты близко, попробуй значение больше",
        "next_guess": "Какое будет твое следующее значение?: ",
        "right_guess": "Ты угадал загаданное число! Число твоих попыток равна ",
        "play_again": "Хочешь ли ты сыграть еще один раз: \n1. Да\n2. Нет\n",
        "goodbye": "Это была отличная игра, увидимся еще!"
    }
}

# The Logic of game
def number_guesser(lang):
    number = random.randint(1, 100)
    num_guess = int(input(texts[lang]["first_attempt"]))
    my_tries = 1
            
    while num_guess != number:
        if num_guess > number:
            print(texts[lang]["lower"])
        else:
            print(texts[lang]["higher"])

        my_tries += 1
        num_guess = int(input(texts[lang]["next_guess"]))
    return my_tries

# Future Logic of "Record"
tries = number_guesser(set_lang)

print(f"{texts[set_lang]['right_guess']} {tries}")

# Checking if person want to play again

play_again = input(texts[set_lang]["play_again"])

while play_again in ('Yes', 'yes', 'Да', "да"):
    print(number_guesser(set_lang))
    play_again = input(texts[set_lang]["play_again"])
else:
    print(texts[set_lang]["goodbye"])
