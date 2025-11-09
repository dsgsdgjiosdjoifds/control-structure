# Write a program that calculates a dog's age in dog's years.
# For the first two years, a dog's life is equal to 10.5 human years.
# After that, each dog year is equal to 4 human years.
# Sample result:
#Enter the dog's age in human years: 15
#The dog's age in dog's years is 73 years.

age = int(input("Enter the dog's age in human years: "))

in_dog_years = 0
for i in range(1, age+1):
    if i <= 2:
        print("a")
        in_dog_years += 10.5
    else:
        print("b")
        in_dog_years += 4

print(f"The dog's age in dog's years is {in_dog_years:.0f} years.")