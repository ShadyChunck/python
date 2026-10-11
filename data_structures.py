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
# .append(element) | Adds an element to the list.
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
