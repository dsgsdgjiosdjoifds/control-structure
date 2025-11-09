CORRECT_PIN = "0805"
MAX_TRIES = 3
tries = 0
while True:
    pin = input("Enter the PIN code: ")
    if pin != CORRECT_PIN:
        tries += 1
        print("Incorrect...")
    else:
        print("Correct PIN entered!")
        break
    if tries >= MAX_TRIES:
        print("Sorry, your payment card has been blocked.")
        break
