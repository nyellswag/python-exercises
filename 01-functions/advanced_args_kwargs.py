# The sum with *args

def smart_sum(*numbers):
    sum = 0
    
    for element in numbers:
        try:
            sum += element
        except:
            print("You must provide only numbers!")
            return None
    return sum

print(smart_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, "hello"))

# Message with **kwargs

def bulid_message(greeting, name, **kwargs):
    print(f"{greeting} дорогая {name}.")
    for key, value in kwargs.items():
        print(f"{key}:{value}")
bulid_message("Привет", "Мария", age=25, city="СПб", hobby="рисование")
