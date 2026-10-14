
rooms = {}

rooms["A"] = input("Enter status of Room A (Clean/Dirty): ").capitalize()
rooms["B"] = input("Enter status of Room B (Clean/Dirty): ").capitalize()

position = input("Enter vacuum position (A/B): ").upper()

while "Dirty" in rooms.values():
    print("\nVacuum is in Room", position)

    if rooms[position] == "Dirty":
        rooms[position] = "Clean"
        print("Room", position, "cleaned")
    else:
        position = "B" if position == "A" else "A"
        print("Moving to Room", position)

print("\nAll rooms are clean!")
