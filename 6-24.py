# Write a program that creates the following pattern.

TOP = 5

i = 1
rev = False
while True:
    if i <= 0:
        break
    print("*" * i)
    if i >= TOP:
        rev = True
    i += (1 if not rev else -1)