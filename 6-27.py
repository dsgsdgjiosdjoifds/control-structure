number = 9
column = 0
while number > 0:
    line = ""
    while column < 3:
        line += str(number - 2 + column * 2) + ' '
        column += 1
        number -= 1
    print(line)
    column = 0