#lists are ordered collections of items
#they can contain any type of data, including other lists, allow duplicates, and can be nested
#lists are mutable, meaning they can be changed after creation
#lists are defined using square brackets[]

#changing, accessing and printing items in a list
fruits = ['apple', 'banana', 'cherry']
print(fruits)  # Output the list of fruits

print(fruits(0))  # Accessing the first item in the list

fruits[2] = 'orange'  # Changing the third item in the list
print(fruits)  # Output the modified list

#removing, adding and printing items from a list
fruits.append('kiwi')  # Adding a new item to the end of the list
print(fruits)  # Output the list after adding kiwi

fruits.insert(1, 'mango')  # Inserting a new item at index 1 (positioning)
print(fruits)  # Output the list after inserting mango


fruits.pop()  # Removing the last item from the list
print(fruits)  # Output the list after popping the last item

fruits.remove('banana')  # Removing an item by value and it removed the first out of most value it gets.
print(fruits)  # Output the list after removing banana

fruits.sort()  # Sorting the list in ascending order
print(fruits)  # Output the sorted list

fruits.sort(reverse=True)  # Sorting the list in descending order
print(fruits)  # Output the list sorted in descending order
