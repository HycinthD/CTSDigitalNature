from tabulate import tabulate

class Converter:
    def celsius(self, c):
        return [
            ["Fahrenheit", (c * 9/5) + 32],
            ["Kelvin", c + 273.15]
        ]

c = float(input("Enter Celsius: "))

results = Converter().celsius(c)

print(
    tabulate(
        results,
        headers=["Scale", "Value"],
        floatfmt=".2f"
    )
)