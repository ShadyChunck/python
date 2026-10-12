# List
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

print("--------Tuples----------")
# Tuples
# It's a data structure that is unmutable (it's value cannot change after it's creation.)
# It saves a collection of elements. Unlike lists, the contents of a tuple are enclosed within parentheses ( ).

tuple = (1, 2, 3, 4, 5)
print("Tuple:", tuple)
print(tuple[0])
print(tuple[1])

# Tuple Methods

# .count(element) | Returns the number of times a certain element apears en the tuple.
# .index(element) | Returns the index of the first appearance of an element in the tuple.
# .len(tuple) | Returns the length of the tuple.
print(len(tuple))
print(len("Hola"))
print("Index of a tuple:", tuple.index(4))

# Exercises
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