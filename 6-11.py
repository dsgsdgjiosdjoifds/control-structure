# A computer program analyses the price of a product in an online store.
# If the product price decreases by at least 10%, the program prints a purchase recommendation:
#Buy the product!!
#Product price reduced by 17%

current_price = 140.0
previous_price = 200.0

diff = ((current_price - previous_price) / previous_price) * 100
if diff < 0:
    print("Buy the product!!")
    print(f"Product price reduced by {abs(diff):.0f}%")