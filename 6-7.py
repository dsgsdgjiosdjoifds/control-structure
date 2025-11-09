age = int(input("Enter your age in years: "))

group = "Child"
if age >= 13 and age <= 19:
    group = "Teen"
elif age >= 20 and age <= 64:
    group = "Adult"
elif age >= 65:
    group = "Senior"

print(f"You belong to a/an {group} group")