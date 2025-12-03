# Temperature in Fahrenheit → return in Celsius

def fahrenheit_to_celsius(temp):
    c_temp = (temp - 32) * (5/9)
    return c_temp

temp_f = int(input("Enter the temperature in Fahrenheit: "))
print(f"In celsius: {round(fahrenheit_to_celsius(temp_f), 2)}")

# Polindrome text check

my_text = input("Enter the text for polindrome check here: ")

def polindrim_text(text):
    for i in range(len(text)):
        if (text[len(text)-1-i] != text[i] or text[len(text)-1-i].lower() != text[i].lower() or text[len(text)-1-i].upper() != text[i].upper()):
            return False
    return True

if polindrim_text(my_text) == True:
    print("Your text is polindrom")
else:
    print("Your text is not polindrom")

# To Power 'n'

my_number = int(input("Set value of number: "))
my_power = int(input("Set value of power: "))

def to_power_n(number, power):
    return number**power

print(f"Your result is: {to_power_n(my_number, my_power)}")

# Letters counter

my_text = input("Please enter text for counting: ")

def count_element(text):
    count = 0
    cleared_text = ''.join(text.split())
    for element in cleared_text:
        count += 1
    return count

if count_element(my_text) == 1:
    print("There is only 1 letter in your text")
elif count_element(my_text) == 0:
    print("You didn't enter any text, please try again!")
else:
    print(f"There are {count_element(my_text)} letters in your text")

# Words counter

my_text = input("Please enter text for counting: ")

def word_counter(text):
    count = 0
    word_list = text.split()
    for word in word_list:
        count += 1
    # Or we can just return the length of list
    return count

if word_counter(my_text) == 1:
    print("There is only 1 word in your text")
elif word_counter(my_text) == 0:
    print("You didn't enter any text, please try again!")
else:
    print(f"There are {word_counter(my_text)} words in your text")


# Greeting in different languages

language_set = input("1. 'ru' \n 2. 'eng' \n 3. 'es' \n")

if language_set == 'eng':
    my_name = input("What is your name?: ")
    print(f"Hello, {my_name}, it's nice to meet you!")
elif language_set == 'ru':
    my_name = input("Как тебя зовут?: ")
    print(f"Здравствуй {my_name}, приятно с тобой познакомиться!")
elif language_set == 'es':
    my_name = input("¿Cómo te llamas?")
    print(f"Hola, {my_name}, ¡es un placer conocerte!")
else:
    print("Error! Try again")
