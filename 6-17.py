normal_format = input("Enter time (24-hour format): ")
splitted = normal_format.split(':')

hours = int(splitted[0])
minutes = int(splitted[1])
smth = "am"

if hours >= 12 and hours <= 23:
    hours -= 11
    smth = "pm"
elif hours == 0:
    hours = 12

print(f"Time in 12-hour format: {hours}:{minutes}{smth}")
