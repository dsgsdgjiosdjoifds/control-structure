# Write a program that converts a decimal number into a binary number.

decimal = int(input("Enter decimal number: "))
binary = ""

while True:
    if decimal == 0:
        break

    binary = str(decimal % 2) + binary
    decimal //= 2

print(f"{decimal}(10) = {binary}(2)")