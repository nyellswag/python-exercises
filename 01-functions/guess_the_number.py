import random
# Setting Language of game
set_lang = input("1. 'eng' \n2. 'ru'\nSet language: ")
while (set_lang != "ru" and set_lang != "eng"):
    print("Please set correct value!")
    set_lang = input("1. 'eng' \n2. 'ru'\nSet language: ")
# The Logic of game
def number_guesser(lang):
    if lang == "eng":
        def numebr_guesser_eng():
            number = random.randint(1, 100)
            num_guess = int(input("Try to guess number, what's your guess?: "))
            my_tries = 1
            
            while num_guess != number:
                if num_guess > number:
                    print("You're close, try lower")
                else:
                    print("You're close try upper")

                my_tries += 1
                num_guess = int(input("What is your next guess?: "))
            return my_tries
        return numebr_guesser_eng()
    else:
        def numebr_guesser_ru():
            number = random.randint(1, 100)
            num_guess = int(input("Попробуйте угадать загаданное число: "))
            my_tries = 1
            
            while num_guess != number:
                if num_guess > number:
                    print("Ты блико, попробуй значение меньше")
                else:
                    print("Ты близко, попробуй значение больше")

                my_tries += 1
                num_guess = int(input("Какое будет твое следующее значение?: "))
            
            return my_tries
        return numebr_guesser_ru() 

# Future Logic of "Record"
tries = number_guesser(set_lang)

if set_lang == "eng":
    print(f"You guessed the right number! The number of tries is {tries}")
else:
    print(f"ты угадал загаданное число! Число твоих попыток равна {tries}")

# Checking if person want to play again

play_again = input("Do you want to play one more game?: \n1.Yes\n2.No\n")

while play_again == "Yes":
    print(number_guesser(set_lang))
    play_again = input("Do you want to play one more game?: \n1.Yes\n2.No\n")
else:
    print("This was good game, see later")
