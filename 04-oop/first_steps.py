# First Tasks

# Dog with bark method
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} bark!")

doberman = Dog('Mark', 2)
doberman.bark()

# Bank Account
class BankAccount():
    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner
    
    def deposit(self, amount):
        self.balance += amount
        print(f'You deposited {amount} dollars to your account. Your balance is {self.balance}')
    
    def withdraw(self, amount ):
        self.balance -= amount
        print(f'You withdrawed {amount} dollars to your account. Your balance is {self.balance}')

my_account = BankAccount('Ali', 1000)
my_account.deposit(500)
my_account.withdraw(236)

# Book info
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def info(self):
        print(f"The '{self.title}' was written by {self.author}, and has {self.pages} pages.")


dostoyevkiy_book = Book("Crime and Punishment", "Fyodor Mikhailovich Dostoevsky", 527)
dostoyevkiy_book.info()
