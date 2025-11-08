number = int(input("Enter the number: "))

if number < 0:
    print(f"Number {number} is negative")
elif number > 0:
    print(f"Number {number} is positive")
else:
    print(f"Number {number} is 0")