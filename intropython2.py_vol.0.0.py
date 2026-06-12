print("This is intro in Python programming")
message = ("Welcome to Python 101\nLet's learn Python basics!")
print(message)

name = ("fatima rozu torres")
print(name.title())
print(name.upper())
print(name.lower())

first_name = "fatima"
middle_name = "rozu"
last_name = "torres"
full_name = (f"{first_name} {middle_name} {last_name}")
greet = (f"Hello,{full_name.title()}")
print(greet)

print("Programming language: \nPython\nC/C++\nSQL\nJavaScript")

#Integers operation
add = 9+6
sub = 6-3
multi = 9*3
div = 81/9
expo = 5**9
print(add, sub, multi, div, expo)

#Float operations
add1 = 0.9+3.6
sub1 = 9.6-5.3
multi1 = 3.10*9.1
div1 = 4.5/8.15
expo1 = 5.1**3.9
print(add1, sub1, multi1, div1, expo1)

#Integers & Float
add2 = 5+6.3
sub2 = 2-1.5
multi2 = 3.5*9
div2 = 5.9/3
expo2 = 6.1**3
print(add2, sub2, multi2, div2, expo2)

#Lists & Range
science = ['Physics', 'Chemistry', 'Biology']
print(science)
science.append('Astronomy')
print(science)
print(f"{science[0]} is my favorite science")

prog_lang = []
prog_lang.append('Python')
prog_lang.append('C/C++')
prog_lang.append('SQL')
prog_lang.append('JavaScript')
print(prog_lang)
prog_lang.insert(2, 'Rust')
print(prog_lang)
del prog_lang[3]
print(prog_lang)

companies = ['Meta', 'Anthropic', 'Nvidia', 'Google', 'OpenAI']
companies.sort()
print(companies)
companies.sort(reverse=True)
print(companies)
print("Here is the original list:")
print(companies)
print("\nHere is the sorted list:")
print(sorted(companies))
print(companies[0:3])

scientist = ['Albert Einstein', 'Isaac Newton', 'Marie Curie']
for genius in scientist:
    print(f"{genius.title()}, was a great scientist!")
print("They changed the world of science")

nationality = ['Filipino', 'Spanish', 'Japanese', 'German', 'Itallian']
print(nationality[1:4])
print(nationality[:3])
print(nationality[3:])

for value in range(10):
    print(value)

for value in range(1, 5):
    print(value)

dimensions = (300, 900)
for dimension in dimensions:
    print(dimension)

#Conditions
movies = ['starwars', 'whiplash', 'the godfather']
for movie in movies:
    if movie == 'whiplash':
        print(movie.upper())
    else:
        print(movie.title())

food = "chicken"
if food =="chicken":
    print("lets go to McDonald!")
else:
    print("what would you like to eat?")

age = 17
if age >= 18:
    print("Adult")
elif age <= 17:
    print("Teenager")
else:
    print("Child")

money = 50
if money == 50:
    print("Here's your Burger")
elif money > 100:
    print("Here's your Steak")
elif money > 30 :
    print("Here's your Fries")
else:
    print("Here's your Juice")

requested_food = ['steak','bbq', 'fried chicken', 'spaghetti']
for food in requested_food:
    if food == 'steak':
        print("preparing your dish")
    else:
        print("what other food would you like to eat?")

#Dictionaries
barney = {'species': 'dinosaur', 'color' : 'purple'}
print(barney['species'])
print(barney['color'])

barney = {}
barney['color'] = 'purple'
barney['species'] = 'dinosaur'
print(barney)
print(f"Barney is a {barney['species']} from my imagination.")
print(f"He is a {barney['color']} {barney['species']} from my imagination.")

fav_show = {
    'benny' : 'breaking bad',
    'johann' : 'money heist',
    'francis' : 'You',
    'raven' : 'end of the f world'
}

for name in sorted(fav_show.keys()):
    print(f"{name.title()}'s favorite show is {fav_show[name]}")
print("Thank you for taking the poll!")

