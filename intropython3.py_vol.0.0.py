#User input and while loops
greet = input("What's your name? ")
print("Hello " + greet.title() + " it's nice to meet you!")
message = input("Tell me something and I will repeat it back to you.")
print(message)

number = input("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are a Adult.")
elif age <= 18 and age == 13:
    print("You are a Teen.")
else:
    print("You are a Kid.")

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd like to visit {city.title()}.")

unconfirmed_players = ['ren', 'jerome', 'leo']
confirmed_players = []

while unconfirmed_players:
    current_user = unconfirmed_players.pop()

    print(f"Verifying players: {current_user.title()}")
    confirmed_players.append(current_user)

print("\nYou have confirmed following players:")
for player in confirmed_players:
    print(player.title())

#Functions
def greet_user(username):
    print(f"Hello and welcome {username.title()}!")
greet_user('ren')

def describe_pet(pet_name, animal_type='penguin'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name.title()}.")
describe_pet('linux')

def describe_bro(sibling_name, my_sibling='brother', bro_age=6):
    print(f"\nI have a {my_sibling}.")
    print(f"My {my_sibling} name is {sibling_name.title()}.")
    print(f"He is {bro_age} years old.")
describe_bro(sibling_name='kevin')

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at anytime to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    last_name = input("Last name: ")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, last_name)
    print(f"Hello {formatted_name.title()}.")

def greet_user(names):
    for name in names:
        message = (f"Hello {name.title()}!")
        print(message)
    usernames = ['levi', 'zeke', 'eren']
    greet_user(usernames)

def make_cofee(menus):
    for menu in menus:
        print("Welcome to our Coffe shop, what can i do for you?")
        print(f"- {menu}")
    make_cofee('americano', 'spanish latte', 'capuccino')

#Classes
class Penguin:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print(f"The {self.name} is saying that he's name is Linux.")
        
    def walk(self):
        print(f"The {self.name} is now walking away.")
        
class Penguin:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
my_penguin = Penguin('Linux', 67)
print(f"My penguin's name is {my_penguin.name}.")
print(f"My penguin's age is {my_penguin.age}.")
my_penguin.walk()


class Car:
    pass


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    my_new_car = Car('subaru', '9', 2018)
    print(f"My new car is {my_new_car.get_descriptive_name()}")





