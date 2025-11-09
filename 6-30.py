COLUMNS = 7
MAX_NUMBER = 49

number = 1
while number <= MAX_NUMBER / COLUMNS:
    for column in range(0, COLUMNS):
        print(number + 7 * column, end = " ")
    number += 1
    print()