a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

a,b,c=b,c,a

print("Your numbers have switched their pointers to the next number. i.e. \n \
first number is the second number, second number is the third number, and \n \
the third number is the first number")

print(f"Here is the first number, second number and third number respectively\n \
{a}, {b} and {c}")