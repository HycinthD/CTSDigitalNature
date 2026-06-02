def display_coordinates(coords):
    if not isinstance(coords, tuple) or len(coords) != 2:
        print("Invalid coordinates")
        return

    x, y = coords  # Multiple assignment
    print(f"Coordinates: ({x}, {y})")

coordinates = (10, 20)
display_coordinates(coordinates)