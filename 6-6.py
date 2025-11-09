duration = int(input("Enter the number of hours of parking: "))

fee = 0
if duration >= 1 and duration <= 2:
    fee = 5
elif duration >= 3 and duration <= 6:
    fee = 15
elif duration > 6:
    fee = 20

print(f"Parking fee: {fee} PLN")