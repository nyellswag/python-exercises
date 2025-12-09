prices = {"apple": 5, "coconut": 10, "orange": 7}
print(prices)

# User greeting with additional info

user = {}
work_stage = input("Add new memeber here:\n1. Yes\n2. No\n")
while (work_stage != "Yes" and work_stage != "No"):
    print("You must set correct value!")
    work_stage = input("Do you want to add new memeber here:\n1. Yes\n2. No\n")

def greeting_dict(work_status):

    while work_status == "Yes":
        user_name = input("What is persons' name?: ")
        user_age = int(input("How old person is?: "))
        user[user_name] = user_age
        work_status = input("Do you want to add new member?: ")

        print(f"The information was added.")
        print(user)
        

greeting_dict(work_stage)

# Letter Counting

my_word = input("Hello, enter anything you want to count elements here: ")
my_dict = {}

def count_letters(text):
    for element in text.lower():
        my_dict[element] = text.lower().count(element)
    return my_dict

print(f"I hope, I could help you properly, here are your results:\n")
print(count_letters(my_word))

# Exercise with given values

student = {"name": "Маша", "scores": [4, 5, 5, 3, 4]}

average_grade = sum(student["scores"]) / len(student["scores"])
print(average_grade)

# Mergin two dicts

dict1 = {"Name": "Ali", "age": 21, "Job": "Programmer"}
dict2 = {"Surname": "Maharramli", "age": 23, "Favorite Actor": "Johny Depp"}

def merge_dicts(dict1, dict2):
    new_dict = {}

    for key, value in dict2.items():
        new_dict[key] = value
    
    for key, value in dict1.items():
        new_dict[key] = value
    
    return new_dict
        
print(merge_dicts(dict1, dict2))

# Тут есть более рабочие варианты (часто используемые), буду иметь ввиду

# def merge_dicts(d1, d2):
#     result = d2.copy()      # или result = dict(d2)
#     result.update(d1)       # d1 перезаписывает d2
#     return result

# merged = dict2 | dict1          # если Python ≥ 3.9
# # или
# merged = {**dict2, **dict1}
