def display_coordinates(coords):
    if len(coords) != 2:
        print("Invalid coordinates")
        return

    x, y = coords
    print(f"Coordinates: ({x}, {y})")

coordinates = (10, 20)

display_coordinates(coordinates)