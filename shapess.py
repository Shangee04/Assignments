class Calculate:
    """creating class"""

    def rectangle(self):

        length = int(input("enter the length value:"))
        breadth = int(input("enter the breadth value:"))
        rect_area = length * breadth
        rect_perimeter = 2 * (length + breadth)
        print(f"enter the area of rectangle{rect_area}")
        print(f"enter the perimeter of rectangle{rect_perimeter}")


    def Circle(self):
        radius = int(input("enter the radius value:"))
        pi = 3.14
        circle_area = pi * radius * radius
        circle_perimeter = 2 * pi * radius
        print(f"enter the area of rectangle{circle_area}")
        print(f"enter the perimeter of rectangle{circle_perimeter}")


    def Square(self):
        side = int(input("enter the side value:"))
        sqt_area = side * side
        sqt_perimeter = 4 * side
        print(f"enter the area of rectangle{sqt_area}")
        print(f"enter the perimeter of rectangle{sqt_perimeter}")


    def Rhombus(self):
        diagonal_1 = int(input("enter the diagonal_1 value:"))
        diagonal_2 = int(input("enter the diagonal_2 value:"))
        rhombus_area = 1 / 2 * (diagonal_1 * diagonal_1)
        rhombus_perimeter = 4 * diagonal_1
        print(f"enter the area of rectangle{rhombus_area}")
        print(f"enter the perimeter of rectangle{rhombus_perimeter}")


    def Triangle(self):
        side_1 = int(input("enter the side_1 value:"))
        side_2 = int(input("enter the side_2 value:"))
        side_3 = int(input("enter the side_3 value:"))
        triangle_area = 1 / 2 * side_1 * side_2
        triangle_perimeter = side_1 + side_2 + side_3
        print(f"enter the area of rectangle{triangle_area}")
        print(f"enter the perimeter of rectangle{triangle_perimeter}")


calculate_shape = Calculate()
print("1:Rectangle")
print("2:Circle")
print("3:Square")
print("4:Rhombus")
print("5:Triangle")
print("calculate:")
while True:
    ch = int(input("enter the choice to find the area and perimeter of shape:"))
    if ch == 1:
        calculate_shape.rectangle()
    elif ch == 2:
        calculate_shape.Circle()
    elif ch == 3:
        calculate_shape.Square()
    elif ch == 4:
        calculate_shape.Rhombus()
    elif ch == 5:
        calculate_shape.Triangle()
    else:
        print("invalid shape")
