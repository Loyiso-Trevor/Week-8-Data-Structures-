#building a shopping cart system that will continually ask the user for input until they choose to exit ('quit'-'q')
#the user should input the item and the price ofn the item
#the program should then display the current items in the cart and the total price

print(input("Welcome to the shopping cart system! Type 'quit' or 'q' to exit.\n"))
cart = {}  # Initialize an empty shopping cart
while True:
    item = input("Enter the item name (or 'quit'/'q' to exit): ").strip()
    if item.lower() in ['quit', 'q']:
        break  # Exit the loop if the user types 'quit' or 'q'
    
    try:
        price = float(input(f"Enter the price for {item}: "))  # Get the price of the item
    except ValueError:
        print("Invalid price. Please enter a numeric value.")
        continue  # Skip to the next iteration if the price is invalid
    
    cart[item] = price  # Add the item and its price to the cart
    print(f"Current items in your cart: {cart}")  # Display current items in the cart
    total_price = sum(cart.values())  # Calculate total price of items in the cart
    print(f"Total price: R{total_price:.2f}")  # Display total price formatted to two decimal places
    
for item, price in cart.items():
    print(f"{item}: R{price:.2f}")  # Print each item and its price in the cart
print(f"Final total price: R{total_price:.2f}")  # Display final total price when exiting
print("Thank you for using the shopping cart system!")  # Thank the user for using the system
print("Goodbye!")  # Farewell message