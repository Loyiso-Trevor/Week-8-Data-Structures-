#tuples are ordered and immutable sequences of objects, meaning they are unchangeable after creation
#tuples can contain any type of data, including other tuples, and allow duplicates
#tuples are defined using parentheses ()

my_tuple = (1, 2, 3, 4, 5)  # Creating a tuple with five elements
print(my_tuple)  # Output the tuple

print(my_tuple[0])  # Accessing the first item in the tuple
print(my_tuple[1:3])  # Accessing a slice of the tuple (items at index 1 and 2)

my_tuple = my_tuple + (6, 7)  # Adding new items to the tuple by concatenation
print(my_tuple)  # Output the modified tuple

my_tuple2 = (8, 9)  # Creating another tuple
my_tuple += my_tuple2  # Concatenating another tuple to the existing one
print(my_tuple)  # Output the tuple after concatenation

rep_tuple = my_tuple * 2  # Repeating the tuple twice *2
print(rep_tuple)  # Output the repeated tuple

