#sets are unordered collections of unique elements
#they do not allow duplicates and are mutable, meaning they can be changed after creation
#sets are defined using curly braces {}

my_set = {1, 2, 3, 4, 5}  # Creating a set with five elements
print(my_set)  # Output the set

my_set.add(6)  # Adding a new item to the set
print(my_set)  # Output the set after adding 6  

my_set.remove(2)  # Removing an item from the set by value
print(my_set)  # Output the set after removing 2

#operations on sets
my_set2 = {4, 5, 6, 7, 8}  # Creating another set
union_set = my_set.union(my_set2)  # Union of two sets, combining all unique elements
print(union_set)  # Output the union of the two sets, which includes all unique elements from both sets(removed 4, 5)

inter_set = my_set.intersection(my_set2)  # Intersection of two sets, common elements(4, 5 )
print(inter_set)  # Output the intersection of the two sets, which includes only elements present

def_set = my_set.difference(my_set2)  # Difference of two sets, elements in my_set not in my_set2
print(def_set)  # Output the difference of the two sets, which includes elements in my_set but not in my_set2 (1, 3)