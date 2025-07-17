#dictionaries are mutable, unordered collections of items.
#they consist of key-value pairs, where each key is unique and maps to a value
#dictionaries are defined using curly braces {}

my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}  # Creating a dictionary with three key-value pairs
print(my_dict)  # Output the dictionary

print(my_dict['apple'])  # Accessing the value associated with the key 'apple'
print(my_dict.get('banana'))  # Accessing the value associated with the key 'banana

my_dict['orange'] = 4  # Adding a new key-value pair to the dictionary
print(my_dict)  # Output the dictionary after adding orange

my_dict['banana'] = 5  # Changing the value associated with the key 'banana'
print(my_dict)  # Output the dictionary after changing the value of banana