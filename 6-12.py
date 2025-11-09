# In one of the online stores, a 25% discount is charged for each product purchased over two.
# Write a program that calculates the amount to be paid.
# Read the number of purchased products and the product price from the keyboard.

product_count = int(input("Number of products purchased: "))
product_price = int(input("Product price: "))

total = 0
for i in range(1, product_count+1):
    price = product_price if i <= 2 else product_price * 0.75
    total += price

print(f"Amount to pay: {total}")