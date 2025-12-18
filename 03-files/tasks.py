with open("diary.txt", 'w') as diary_file:
    diary_file.write("Hello, its my diary!")

with open("diary.txt", 'a') as diary_file:
    diary_file.write("\nN1: Do codding")
    diary_file.write("\nN2: Make some food")

with open("diary.txt") as my_file:
   for line in my_file:               # ← напрямую по объекту файла
        print(line.strip())            # strip() убирает \n и пробелы

        # content = my_file.read()      # ← или если хочешь всё сразу:
        # print(content)

# Message log
def message_log():
    my_input = input("What do you want to add to file: ")

    with open("log.txt", "a") as my_file:
        my_file.write("\n" + my_input)

    while True:
        asking_to_play = input("Do you want to add something more?: ")

        if asking_to_play in ['no', 'No', 'NO']:
            break

        my_input = input("What do you want to add to file: ")
        with open("log.txt", "a") as my_file:
            my_file.write("\n" + my_input)

message_log()

# Read Logs
def read_logs(my_file):
    with open(my_file) as file_to_read:
       print(file_to_read.read())
