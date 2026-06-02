def sum_odd_numbers(range_size):
    if range_size <= 0:
        print("Invalid range")
        return

    total = 0

    for i in range(range_size):
        if i % 2 == 0:
            continue

        total += i

    print(f"Sum of Odd Numbers: {total}")

sum_odd_numbers(10)