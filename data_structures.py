# List
print("Lists")
# It's a mutable data structure that can hold a collection of items in order.
# By mutable it means the list can be modified after it's creation.
# It's important to remember that a list can have different data types and it's contents are closed within square brackets [ ].

# Example of a list
#Creation of a list
fruits = ["apple", "banana", "orange"]
print(fruits)
print(fruits[0]) # Within the square brackets it should be a number that represents the order of the value in the list starting from zero (0).
print(fruits[-1]) # Negative numbers starting from minus one represents the last values of a list. -1 is the last one, -2 is the penultimate and so on.
print(fruits[-2]) # It prints "banana"

# List Methods
# .append(element) | Adds an element to the list and inserts it to the last position of the list.
# .insert(index, element) | Inserts an element to a specific position of the list. Position starts at 0.
fruits.insert(1, "grape")
print("After .insert and before .pop")
print(fruits)
# .remove(element) | Removes the first occurrence of the specified element from a list.
# .pop(index) | Eliminate and returns the element of the specific position of the list.
pop_value = fruits.pop() # By default, .pop() eliminates and gets the value of the last element of the list unless it specifies the position.
print("After .pop")
print(fruits)
print(pop_value) # The value that .pop() eliminates can also be saved into a variable.
# .sort() | Sort the values ​​in the list in ascending order.
fruits.sort()
print(fruits)
# .reverse() | Reverses the order of the elements in the list.
fruits.reverse()
print(fruits)

# Comprehension Lists
# Is a concise way to create new lists based off an existing sequence.
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers if x % 2 == 0]
print(squared)
booleans = [x % 2 == 0 for x in [1, 2, 3]]
print(booleans)

# Lists Exercises
# Exercise 1.
print("Lists Exercises")
print("Exercise 1.")
inventory = ["Notebook", "Pencil", "Eraser"]
print(inventory[0])
print(inventory[-1])

# Exercise 2.
print("Exercise 2.")
employees = ["Ana", "Carlos", "Beatriz", "David"]
employees.remove("Carlos")
employees.append("Elena")
print(employees)

# Exersice 3.
print("Exercise 3.")
grades = [45, 12, 88, 55, 92]
grades.sort()
lowest_grade = grades.pop(0)
print(lowest_grade)
print(grades)

# Exercise 4.
print("Exercise 4.")
prices = [15, 45, 80, 120, 30, 55, 9]
premium_prices = [x for x in prices if x >= 50]
print(premium_prices)

# Exercise 5.
print("Exercise 5.")
chores = ["Barrer", "Trapear", "Barrer", "Lavar", "Barrer"]
new_chores = [chore for chore in chores if chore != "Barrer"]
new_chores.insert(0, "Limpiar ventanas")
print(new_chores)

print("--------Tuples----------")
# Tuples
# It's a data structure that is unmutable (it's value cannot change after it's creation.)
# It saves a collection of elements. Unlike lists, the contents of a tuple are enclosed within parentheses ( ).

tuple = (1, 2, 3, 4, 5)
print("Tuple:", tuple)
print(tuple[0])
print(tuple[1])

# Tuple Methods

# .count(element) | Returns the number of times a certain element appears en the tuple.
# .index(element) | Returns the index of the first appearance of an element in the tuple.
# .len(tuple) | Returns the length of the tuple.
print(len(tuple))
print(len("Hola"))
print("Index of a tuple:", tuple.index(4))

# Tuple Exercises.
# Exercise 1.
# Situación: Estás desarrollando un GPS y necesitas almacenar las coordenadas exactas de un destino.
# Tu tarea:
# Crea una tupla llamada destination que contenga los números 40.7128 y -74.0060.
# Imprime en consola el primer número usando índices positivos.
# Imprime en consola el segundo número usando índices negativos.
print("Exercise 1.")
destination = (40.7128, -74.0060)
print(f"{destination[0]}, {destination[1]}")

# Exercise 2.
# Situación: Una base de datos te devuelve un registro de un empleado en formato de tupla. Necesitas separar esa información para trabajar con ella.
# Tu tarea: Dada la tupla employee_record = (105, "Sarah Connor", "IT")
# En una sola línea de código, "desempaqueta" esta tupla en tres variables con nombres descriptivos en inglés.
# Imprime únicamente la variable que contiene el departamento ("IT").
print("Exercise 2.")
employee_record = (105, "Sarah Connor", "IT")
id, name, department = employee_record
print(department)

# Exercise 3.
# Situación: Tienes los resultados de una encuesta rápida de satisfacción del 1 al 5.
# Tu tarea: Dada la tupla survey_results = (5, 4, 3, 5, 2, 5, 4, 1, 5)
# Utiliza un método de las tuplas para averiguar cuántas veces los usuarios calificaron con un 5 y guarda ese valor en una variable.
# Utiliza otro método para encontrar en qué índice (posición) aparece el primer 1.
# Imprime ambos resultados.
print("Exercise 3.")
survey_results = (5, 4, 3, 5, 2, 5, 4, 1, 5)
survey_five_counts = survey_results.count(5)
survey_first_one = survey_results.index(1)
print(f"The number 5 appeared {survey_five_counts} times and the first number 1 of the tuple has the index number {survey_first_one}")

# Exercise 4.
# Situación: Tienes un registro de temperaturas tomadas cada hora. Sabes que hubo una caída a 15 grados, pero quieres ignorar las primeras 4 horas del día en tu búsqueda.
# Tu tarea: Dada la tupla temperatures = (18, 16, 15, 19, 20, 15, 21, 15, 22)
# Utiliza el método .index() para encontrar el número 15, pero configura el método para que comience a buscar a partir del índice 4 en adelante.
# Imprime la posición encontrada.
print("Exercise 4.")
temperatures = (18, 16, 15, 19, 20, 15, 21, 15, 22)
print(f"The temperature fall of 15 degrees happened at the {temperatures.index(15, 4) + 1}th hour, being in the index {temperatures.index(15, 4)}")

# Exercise 5.
# Situación: Estás trabajando con una API que te devuelve información de un servidor en forma de "tuplas anidadas" (una tupla dentro de otra tupla).
# Tu tarea: Dada la siguiente estructura:
# server_data = ("SVR-01", "Active", ("192.168.0.1", "10.0.0.5"))
print("Exercise 5.")
server_data = ("SVR-01", "Active", ("192.168.0.1", "10.0.0.5"))
print(f"The server IP is {server_data[2][1]}")
# The first square bracket [2] indicates the principal index order of the array.
#    0          1                   2 (Considered one because both of the ip's are in the same parenthesis)
# "SVR-01", "Active", ("192.168.0.1", "10.0.0.5")
# The second square bracket [1] represents the index of the child tuple that is inside of the father tuple
#        0           1
# "192.168.0.1", "10.0.0.5"

# Dictionaries
print("---------Dictionaries----------")
# Is a mutable data structure that saves a collection of key-value information in order (It doesn't have an order before Python 3.7).
# Each element in a dictionary has it's own unique key with their value.
# Dictionaries uses curly braces {} and the key-values are seperated by comas.
# An examole of a dictionary:

person = {"name": "Sam", "age": 25, "city": "Madrid"}

# To access the values of a dictionary, you need yo use the key word between brackets.

print(person["name"])
print(person["age"])
print(person["city"])
print(person.get("name")) # The function get() obtains the value of the inserted key word.
# Unlike "person[keyword]", this function returns None as a value if the keyword inserted was not found.

# Dictionary Methods.
# keys() | Returns a view of all the keys of a dictionary.
print(person.keys())
# values() | Returns a view of all the values of a dictionary.
print(person.values())
# items() | Returns a view of all the key-value elements of a dictionary.
print(person.items())
# update(other_dictionary) | Updates the dictionary with the key-value elements of another dictionary.
person.update({"language": "Python"})
print(person)

# With dictionaries you can also add individual key-values.
car = {"brand": "Toyota", "year": 2020}
print(car)
# If the key doesn't exist, it creates it and adds it to the last part of the dictionary.
car["color"] = "Red"
print(car)
# If the key does exist, it overwrite it's value
car["year"] = 2022
print(car)
# It can also use some lists/tuple methods
print(car.pop("year"))
# It eliminates it directly from the memory
del car["color"]

# There can also be dictionaries inside of dictionaries
user = {
    "username": "coder_99",
    "social_media": { # Dictionary called "social_media"
        "twitter": "@coder99",
        "github": "coder99-dev"
    },
    "languages": ["Python", "JavaScript"]
}

print(user["social_media"]["github"]) # Prints coder99-dev
print(user["languages"][0])    # Prints Python

# To access nested dictionaries, you must chain the bracket notations sequentially.

# Dictionary Exercises
print("----Dictionary Exercises----")
# Exercise 1
print("Exercise 1")
# You need to create a simple contact entry for a user.
# Create a dictionary named contact with the following key-value pairs:
# "name": "Alice"
# "phone": "555-1234"
# "city": "New York"

# Print the value associated with the "phone" key.
contact = {"name": "Alice", "phone": "555-1234", "city": "New York"}
print(contact["phone"])

# Exercise 2
print("Exercise 2")
# A user's profile needs to be updated with new information.
# Given the dictionary user_profile = {"username": "coder99", "level": 10}
# Add a new key "email" with the value "coder99@email.com".
# Update the value of the "level" key to 11.

# Print the updated user_profile dictionary.
user_profile = {"username": "coder99", "level": 10}
print(f"Before: {user_profile}")
user_profile.update({"email": "coder99@email.com", "level": 11})
print(f"After {user_profile}")

# Exercise 3
print("Exercise 3")
# You are fetching configuration settings for an application, but some settings might be missing.
# Given the dictionary app_config = {"theme": "dark", "language": "en"}
# Use the appropriate dictionary method to retrieve the value of the key "volume".
# Ensure that if "volume" does not exist, the method returns the integer 50 instead of raising an error or returning None.
# Store the result in a variable named current_volume and print it.
app_config = {"theme": "dark", "language": "en"}
print(f"Current app_config: {app_config}")
current_volume = app_config.get("volume", 50)
print(f"\"Updated\" config: {app_config}.\nCurrent volume: {current_volume}")

# Exercise 4
print("Exercise 4")
# You have a dictionary containing the scores of students in a class. You need to print out a specific format for the report card.
# Given the dictionary scores = {"Math": 85, "Science": 92, "History": 78}
# Use a for loop to iterate through the dictionary.
# In each iteration, print a string formatted exactly like this: "Subject: [key], Score: [value]". (Hint: You will need to access both keys and values simultaneously).
scores = {"Math": 85, "Science": 92, "History": 78}
for key, value in scores.items():
    print(f"Subject: {key}, Score: {value}")

# Exercise 5
print("Exercise 5")
# You are simulating a shopping cart. The cart contains items, but the user decided to remove one item.
# Given the dictionary shopping_cart = {"laptop": 1200, "mouse": 25, "keyboard": 75}
# Remove the "mouse" key-value pair from the dictionary using a method that also returns its value.
# Store the returned value (the price of the mouse) in a variable called removed_item_price.
# Print the removed_item_price.
# Print the final shopping_cart dictionary to confirm the item is gone.
shopping_cart = {"laptop": 1200, "mouse": 25, "keyboard": 75}
print(f"Before: {shopping_cart}")
removed_item_price = shopping_cart.pop("mouse")
print(f"Removed item: {removed_item_price}\nFinal Shopping Cart: {shopping_cart}")

# Sets
print("----Set Lessons----")
