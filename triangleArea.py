# FILE NAME - triangleArea.py
# NAME - Md Wara
# DATE - 02-08-2023
# DISCRIPTION - Find area of a triangle

def main():
    findArea()

def findArea():
    height = float(input("Enter the height: "))
    base = float(input ("Enter the base: "))
    Area = float(1/2 * height * base)
    print("The area of the triangle is", Area)

main()


