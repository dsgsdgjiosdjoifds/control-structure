total_amount = int(input("Enter the amount in PLN: "))
amount = total_amount

pln5 = amount // 5
amount -= pln5 * 5

pln2 = amount // 2
amount -= pln2 * 2

pln1 = amount // 1
amount -= pln1 * 1

print(f"The amount of PLN {total_amount} in coins:")
print(f"5 PLN coins: {pln5}")
print(f"2 PLN coins: {pln2}")
print(f"1 PLN coins: {pln1}")