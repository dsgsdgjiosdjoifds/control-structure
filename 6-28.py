previous = 0 # F_0
current = 1 # F_1
print(f"{previous} {current} ", end="")

for i in range(0, 21):
    _sum = previous + current
    previous = current
    current = _sum
    print(f"{_sum} ", end="")