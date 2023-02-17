# FILE NAME - feetToMiles.py

# NAME - Md Wara
#DATE - 02-02-2023
#DISCRIPTION - Convert feet to miles


def main():
    feetToMiles()

def feetToMiles():
    feet = int( input("How many feet are there?"))

    miles = int(feet / 5280)
    remainderfeet = feet % 5280

    print("There are miles", miles, "with", remainderfeet, "Feet left over.")

main()
