# FILE NAME - inchesToFeet
# NAME - Md Wara
# DATE - 02-08-2023
# DISCRIPTION - converts inches to feet

def main():
    convert()

def convert():
    inches = int (input("Enter the number of inches:"))
    Feet = int(inches/12)
    Remainderinches= int (inches % 12)
    print(inches, "inches is", Feet, "feet, and", Remainderinches, "inches.")

main()    