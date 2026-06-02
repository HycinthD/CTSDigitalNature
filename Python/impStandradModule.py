import math

def calculate_circle_area(radius):
    if radius <= 0:
        print("Invalid radius")
        return

    area = math.pi * radius * radius
    print(f"Area of Circle: {area:.2f}")

calculate_circle_area(5)