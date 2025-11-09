n = int(input("N: "))

print("Prime numbers: ", end="")
for i in range(2, n+1):
    is_prime = True
    for j in range(2, i+1):
        if i % j == 0 and j != i:
            is_prime = False
    if is_prime:
        print(i, end=" ")