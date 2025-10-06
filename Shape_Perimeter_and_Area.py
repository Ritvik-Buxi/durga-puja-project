shape = str(input("Which shape do you want to calculate the perimeter and area of?\n(answer must be one word):"))
if str(shape.upper()) == "TRIANGLE":
    a = float(input("Enter first side of the triangle: "))
    b = float(input("Enter second side of the triangle: "))
    c = float(input("Enter third side of the triangle: "))

    print("The perimiter of your triangle is ",(a+b+c))

    s=(a+b+c)/2
    x = s-a
    y = s-b
    z = s-c

    area = (s*x*y*z)**0.5
    print("The area of your triangle is ",area)

elif str(shape.upper()) == "SQUARE":
    a = float(input("Enter one of the sides of your square: "))
    print("The perimeter of your square is ",4*a)
    print("The area of your square is", a*a)

elif str(shape.upper()) == "RECTANGLE":
    a = float(input("Enter one of the opposite side length of your rectangle: "))
    b = float(input("Enter the other opposite side length of your rectangle: "))
    print("The perimeter of your rectangle is ",(2*(a+b)))
    print("The area of your rectangle is ",a*b)

elif str(shape.upper()) == "CIRCLE":
    r = float(input("Enter the radius of your circle: "))
    print("The perimeter of your circle is ",(2*3.14*r))
    print("The area of your circle is ",(3.14*r*r))

else:
    print("The shape you entered was not recognised.\n Please run the program again")