# Q1: Create an empty Dictionary
inventory = {}

# Q2: Prompt the user to enter details for at least 3 products
for _ in range(3):
    product_id = int(input("Enter Product ID (integer): "))
    product_name = input("Enter Product Name (string): ")
    
    # Q3: Populate the dictionary with the entered product id and name
    inventory[product_id] = product_name

# Q4: Display the final Dictionary containing all product id and name
print("\nFinal Inventory:")
for product_id, product_name in inventory.items():
    print(f"Product ID: {product_id}, Product Name: {product_name}")
