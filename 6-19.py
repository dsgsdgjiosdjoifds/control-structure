print("SURVEY")
interested = input("Are you interested in computer science? (y/n): ")
interested = True if interested == 'y' else False

games = input("Do you like playing computer games? (y/n): ")
games = True if games == 'y' else False

instagram = input("Do you have an Instagram account? (y/n): ")
instagram = True if instagram == 'y' else False

print("SURVEY RESULTS")
print(f"Interested in computer science: {"Yes" if interested else "No"}")
print(f"Playing computer games: {"Yes" if games else "No"}")
print(f"Has an Instagram account: {"Yes" if instagram else "No"}")