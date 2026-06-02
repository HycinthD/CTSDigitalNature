def first_even(range_size):
    if range_size <= 0:
        print("Invalid range size")
        return

    for i in range(range_size):
        if i % 2 == 0:
            print(f"First Even Number: {i}")
            break

first_even(10)