import statistics

def analyze_sales():
    try:
        with open("sales.txt", "r") as file:
            sales = [float(line.strip()) for line in file]

        if not sales:
            print("No sales data found")
            return

        mean_sales = statistics.mean(sales)
        median_sales = statistics.median(sales)

        print("Sales Statistics")
        print(f"Mean: {mean_sales:.2f}")
        print(f"Median: {median_sales:.2f}")

    except FileNotFoundError:
        print("sales.txt not found")

    except ValueError:
        print("Invalid data in file")

analyze_sales()